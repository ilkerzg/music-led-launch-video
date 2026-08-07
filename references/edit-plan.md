# Edit-plan format

Use this optional JSON format when a project benefits from a machine-checkable beat map. It describes decisions without prescribing a layout or creative style.

```json
{
  "duration": 30,
  "fps": 30,
  "sync_tolerance": 0.07,
  "beats": [0, 0.5, 1.0],
  "transients": [0.25, 0.75],
  "events": [
    {
      "id": "opening",
      "at": 0,
      "kind": "cut",
      "layout": "full",
      "sources": ["opening-a.mp4"]
    },
    {
      "id": "accent",
      "at": 0.5,
      "kind": "cut",
      "layout": "custom",
      "sources": ["angle-b.mp4", "detail-c.mp4"]
    }
  ]
}
```

## Fields

- `duration`: final video duration in seconds.
- `fps`: delivery frame rate.
- `sync_tolerance`: maximum distance in seconds from a beat or transient before the validator warns.
- `beats`: detected or manually verified main beats.
- `transients`: additional musical accents.
- `events`: ordered edit events.
- `events[].id`: unique human-readable identifier.
- `events[].at`: event time in seconds.
- `events[].kind`: `cut`, `layout`, `title`, or another descriptive value.
- `events[].layout`: descriptive layout name; no fixed vocabulary is required.
- `events[].sources`: one or more source paths visible after the event.
- `events[].sync`: optional `beat`, `transient`, `offbeat`, or `free`. `offbeat` and `free` suppress alignment warnings.

The validator checks structure and likely mistakes. It does not decide whether a cut is creatively correct.
