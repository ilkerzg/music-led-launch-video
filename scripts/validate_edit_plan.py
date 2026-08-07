#!/usr/bin/env python3
"""Validate a neutral music-led edit plan without prescribing creative structure."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def load(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("plan root must be an object")
    return data


def validate(plan: dict[str, Any]) -> tuple[list[str], list[str], dict[str, Any]]:
    errors: list[str] = []
    warnings: list[str] = []

    duration = plan.get("duration")
    fps = plan.get("fps")
    tolerance = plan.get("sync_tolerance", 0.07)
    beats = plan.get("beats", [])
    transients = plan.get("transients", [])
    events = plan.get("events", [])

    if not number(duration) or duration <= 0:
        errors.append("duration must be a positive finite number")
        duration = 0.0
    if not number(fps) or fps <= 0:
        errors.append("fps must be a positive finite number")
    if not number(tolerance) or tolerance < 0:
        errors.append("sync_tolerance must be a non-negative finite number")
        tolerance = 0.07

    for label, values in (("beats", beats), ("transients", transients)):
        if not isinstance(values, list) or any(not number(value) for value in values):
            errors.append(f"{label} must be an array of finite numbers")
            if label == "beats":
                beats = []
            else:
                transients = []
        elif values != sorted(values):
            errors.append(f"{label} must be sorted")

    if not isinstance(events, list) or not events:
        errors.append("events must be a non-empty array")
        events = []

    ids: list[str] = []
    all_sources: list[str] = []
    previous_at = -1.0
    previous_sources: tuple[str, ...] | None = None
    sync_points = sorted(set(float(value) for value in [*beats, *transients] if number(value)))
    aligned = 0

    for index, event in enumerate(events):
        prefix = f"events[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{prefix} must be an object")
            continue

        event_id = event.get("id")
        at = event.get("at")
        sources = event.get("sources")
        sync = event.get("sync")

        if not isinstance(event_id, str) or not event_id.strip():
            errors.append(f"{prefix}.id must be a non-empty string")
        else:
            ids.append(event_id)

        if not number(at):
            errors.append(f"{prefix}.at must be a finite number")
            continue
        at = float(at)
        if at < 0 or at >= float(duration or 0):
            errors.append(f"{prefix}.at={at:.3f} is outside the timeline")
        if at < previous_at:
            errors.append(f"{prefix}.at is earlier than the previous event")
        previous_at = at

        if not isinstance(sources, list) or not sources or any(not isinstance(source, str) or not source for source in sources):
            errors.append(f"{prefix}.sources must contain one or more non-empty strings")
            sources = []
        elif len(set(sources)) != len(sources):
            errors.append(f"{prefix}.sources contains the same source more than once")

        source_set = tuple(sorted(sources))
        if previous_sources is not None and source_set == previous_sources:
            warnings.append(f"{prefix} repeats the previous event's complete source set")
        previous_sources = source_set
        all_sources.extend(sources)

        if sync not in ("offbeat", "free") and sync_points:
            nearest = min(abs(at - point) for point in sync_points)
            if nearest <= float(tolerance):
                aligned += 1
            else:
                warnings.append(f"{prefix}.at={at:.3f} is {nearest:.3f}s from the nearest beat or transient")

    duplicate_ids = [key for key, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        errors.append("duplicate event ids: " + ", ".join(sorted(duplicate_ids)))

    repeated_sources = [key for key, count in Counter(all_sources).items() if count > 1]
    if repeated_sources:
        warnings.append(f"{len(repeated_sources)} source(s) are reused across events; verify that every reuse is intentional")

    if events and number(events[0].get("at")) and float(events[0]["at"]) > max(1.0 / float(fps or 1), 0.04):
        warnings.append("first edit event does not begin at time zero")

    report = {
        "duration": duration,
        "fps": fps,
        "events": len(events),
        "unique_sources": len(set(all_sources)),
        "aligned_events": aligned,
        "errors": len(errors),
        "warnings": len(warnings),
    }
    return errors, warnings, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="path to edit-plan JSON")
    parser.add_argument("--strict", action="store_true", help="return non-zero when warnings are present")
    args = parser.parse_args()

    try:
        plan = load(args.plan)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors, warnings, report = validate(plan)
    for item in errors:
        print(f"ERROR: {item}", file=sys.stderr)
    for item in warnings:
        print(f"WARNING: {item}", file=sys.stderr)
    print(json.dumps(report, indent=2))
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
