---
name: music-led-launch-video
description: Create, revise, and quality-check short product or model launch videos whose edit rhythm, visual energy, and final reveal are designed around music. Use for launch films, announcement trailers, rhythmic showcases, montage promos, beat-synced edits, multi-shot AI video assemblies, split-screen sequences, title-card endings, or requests to turn generated clips and a music track into a polished final video. Keep every output original and brand-neutral unless the user supplies brand assets.
---

# Music-Led Launch Video

Build a finished launch film, not a pile of generated clips. Let the music define the timing architecture while the brief defines the visual language.

## Non-negotiable principles

1. Start from the current brief. Do not reuse a previous project's scenes, pacing, palette, layout, BPM, duration, prompts, slogans, or title-card design unless the user explicitly asks.
2. Design the music and edit together. Analyze the actual audio waveform, beats, phrases, accents, breaks, and energy changes before locking cut times.
3. Make every selected source clip earn its place. Changing a clip's position is not a new visual; the content itself must change when the edit promises variety.
4. Prefer direct, decisive cuts. Use transitions only when they express a real visual or musical relationship.
5. Treat grids, split screens, triptychs, stacked bands, picture-in-picture, and full-frame footage as optional devices. Never make any one layout the default.
6. Preserve the source image geometry. Do not warp or stretch footage to fill a frame. Crop intentionally or letterbox when necessary.
7. Keep the final reveal concise. Use only the user-approved launch line and supplied brand element; otherwise use a neutral placeholder for review.
8. Deliver a real rendered artifact and verify it visually and technically.

## Creative reset

Before generating assets, propose three genuinely different structural directions in working notes. Vary at least:

- edit density and energy curve;
- dominant shot scale and camera behavior;
- visual worlds and subject families;
- use or non-use of composited layouts;
- ending behavior.

Choose the direction that best serves the brief. Do not combine all three into a generic compromise. The workflow is reusable; the output must not be.

## Workflow

### 1. Extract the real objective

Identify:

- what is launching;
- what the audience should feel;
- target platform, aspect ratio, duration, and delivery resolution;
- required claims, copy, logo, and legal constraints;
- available source assets and whether new generation is authorized;
- whether music, dialogue, diegetic sound, or silence leads the piece.

If the user asks for a finished video, continue through render and QA. Do not stop at a storyboard or preview unless blocked.

### 2. Establish the music

Choose or create the music before final editing whenever rhythm is central. Favor a track with identifiable sections rather than an unchanging loop.

Analyze and record:

- tempo and approximate beat grid;
- phrase boundaries;
- strong transients and fills;
- breakdowns, rests, and drops;
- energy curve;
- the exact frame where the final reveal should land.

Do not cut on every beat by reflex. Build cadence from musical phrases: hold when the track opens up, accelerate into fills, and reserve the densest cutting for a meaningful peak.

### 3. Build an edit map

Write a time-based edit plan before generating a large batch. Give each section a job, such as establish, accelerate, contrast, peak, breathe, or reveal.

Use beat subdivisions as choices, not rules:

- 2–4 beats for confident establishing shots;
- 1 beat for the main rhythmic body;
- 1/2 or 1/4 beat for short peak runs;
- longer holds or silence around a reveal.

Vary the cadence across the film. A sequence of identical cut lengths usually feels mechanical.

For a structured plan, use the optional event format in [references/edit-plan.md](references/edit-plan.md). Review it directly for event order, source duplication, timeline bounds, and beat alignment; do not let the format dictate the creative structure.

### 4. Design shot diversity

Create a shot matrix before generation. Vary subject, environment, scale, lens, camera motion, subject motion, light, texture, and color. Avoid generating many prompts that are only noun swaps.

The first frames should feel credible and immediately readable. Put especially strong, realistic footage in the opening positions; these establish trust.

Generate more usable footage than the timeline requires, then select. Prefer clips with:

- visible motion within the first few frames;
- one clear focal action;
- stable anatomy and geometry;
- enough clean duration around the intended edit point;
- direction of motion that supports adjacent cuts;
- no accidental text, marks, or baked-in branding.

Do not use first/last-frame bridging merely to disguise unrelated shots. If continuity is required, generate a coherent multi-shot sequence or design an intentional match cut.

### 5. Edit to musical events

Place cuts on verified beats, transients, phrase changes, or deliberately chosen syncopations. Judge by playback, not timestamps alone.

Use visual relationships to strengthen the cut:

- action to action;
- matching screen direction;
- scale contrast;
- shape or color match;
- impact to impact;
- calm-to-chaos contrast at a musical change.

Keep the music continuous across visual cuts. Add sound effects only when requested or when a small number of precise accents materially improve the piece.

### 6. Choose layouts deliberately

Default to the layout that makes the footage strongest.

- Use full frame for presence, realism, and clean subject reading.
- Use split screen to compare, echo, or increase density.
- Use grids only when simultaneous variety is the point.
- Use stacked bands or narrow columns only when the crop still preserves the subject.

When multiple panels are visible, treat each panel as an independent edit track. At a content-change beat, replace the actual sources, not merely their coordinates. Avoid showing the same source twice in one layout unless repetition is an intentional rhythmic device.

### 7. Handle motion and transitions

Favor hard cuts, motivated match cuts, and brief spatial moves. Avoid decorative fades, generic glow sweeps, arbitrary borders, and transition packs.

When animation is needed:

- use professional easing with fast intent and controlled settling;
- enable true motion blur based on movement or shutter sampling;
- apply blur only while an object is moving;
- never fake motion blur by bringing an already blurred object into focus;
- preserve sharp resting frames.

### 8. Build the ending

Let the last musical phrase create space for the reveal. Keep the end card minimal: product name, availability statement if approved, and supplied brand asset. Do not invent slogans.

Animate the end card with the same motion language as the edit. A fast, controlled entrance followed by a readable hold usually works better than a long fade.

### 9. Render and verify

Render the requested master format, then create a smaller review copy when useful. Inspect the actual rendered file.

Verify:

- duration, dimensions, frame rate, codec, and audio stream;
- no missing, frozen, duplicated, warped, or incorrectly cropped footage;
- opening quality at full resolution;
- cut accuracy at representative beats and every high-density run;
- layout changes include source changes where intended;
- end-card spelling, safe margins, and hold duration;
- no unrequested branding, internal notes, provider names, keys, endpoints, request IDs, or private assets.

Read [references/quality-gates.md](references/quality-gates.md) for the final review procedure.

## Failure modes to reject

- Concatenating several long generations with no musical edit.
- Reusing the same few clips while claiming visual variety.
- Moving identical videos between grid cells instead of changing content.
- Cutting at a constant interval for the entire film.
- Using a grid because an earlier successful video used one.
- Generating only dark, low-detail imagery that breaks under compression.
- Stretching footage to fit a layout.
- Using blur-in or opacity fades as a substitute for motion blur.
- Adding ornamental labels, numbers, borders, slogans, or sound effects not requested.
- Hard-coding any company, vendor, model family, logo, endpoint, credential, or private workflow detail into a reusable skill.

## Resources

- [references/editing-grammar.md](references/editing-grammar.md): timing, shot, transition, and layout choices.
- [references/edit-plan.md](references/edit-plan.md): optional neutral event-plan format and manual review checklist.
- [references/quality-gates.md](references/quality-gates.md): final technical and visual review.
