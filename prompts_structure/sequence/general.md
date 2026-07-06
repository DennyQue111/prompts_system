## Description
Use this architecture when generating a **multi-shot sequence prompt for Gemini/GPT image models** — a timed sequence of frames designed to feed directly into a video generation model (e.g., Seedance). Each shot includes not just the visual frame but timing, camera movement, and transition instructions.

Unlike `storyboard/general.md` (key moments only), a sequence covers every shot of a scene with precise timing — this is the pre-visualization blueprint for video production.

## Core Principles

1. **Every shot has a duration.** A sequence is a timeline, not just a series of images. Each shot's length determines pacing — shorter shots = tension/action, longer shots = contemplation/emotion.
2. **Camera movement is the video dimension.** Static frames describe composition; sequences describe how the camera MOVES through that composition (pan, dolly, rack focus, handheld).
3. **Transitions connect shots.** How one shot flows into the next (cut, dissolve, match cut, smash cut) is as important as the shots themselves.
4. **Seedance compatibility.** Keep shot durations realistic (2–8 seconds), avoid impossible camera moves, and ensure visual continuity between consecutive shots.

## Sequence Structure

```
┌─────────────────────────────────────────────────────────┐
│  SCENE HEADER                                           │
│  [Scene #] — [Location] — [Time of Day] — [Duration]   │
├─────────────────────────────────────────────────────────┤
│  SHOT 1  │  SHOT 2  │  SHOT 3  │  SHOT 4  │  SHOT 5   │
│  00:00   │  00:03   │  00:06   │  00:10   │  00:14    │
│  → 3s    │  → 3s    │  → 4s    │  → 4s    │  → 4s     │
│  [type]  │  [type]  │  [type]  │  [type]  │  [type]   │
├──────────┴──────────┴──────────┴──────────┴───────────┤
│  TOTAL DURATION: 18s                                    │
└─────────────────────────────────────────────────────────┘
```

Standard sequence: 10–30 seconds total, 3–8 shots. This is the sweet spot for Seedance — long enough for narrative, short enough for consistency.

## Prompt Content Formula

```
[Scene header: number, location, time, total duration] +
[Character consistency note] +

[SHOT 1: duration + shot type + visual + camera movement + transition to next] +
[SHOT 2: duration + shot type + visual + camera movement + transition to next] +
[SHOT 3: duration + shot type + visual + camera movement + transition to next] +
[...repeat for all shots...] +

[Style suffix + video generation notes]
```

### Content Components

| Component | Description | Key Info |
|-----------|-------------|----------|
| **Scene header** | Scene number, location, time, duration | `SCENE 01 — Rooftop Awakening — Night/Rain — 18s total` |
| **Character consistency** | Who's in the scene, their outfit, any state changes | "Protagonist wears black tactical suit (adapted from wedding tuxedo), rain-soaked throughout" |
| **Shot duration** | How long the shot lasts (seconds) | Action: 2–3s. Dialogue/reaction: 3–5s. Establishing: 5–8s. Climax: 2–4s quick cuts |
| **Shot type** | Wide/medium/close-up + camera movement | "WIDE, slow dolly forward" or "MCU, handheld slight shake" |
| **Visual description** | What the camera sees during this shot | Include light source, key visual element, any character action |
| **Camera movement** | How the camera moves during the shot | Static, push in, pull out, dolly L→R, pan up, handheld, rack focus |
| **Transition** | How this shot connects to the next | Cut (default), dissolve (time passage), match cut (visual connection), smash cut (sudden contrast) |
| **Style suffix** | Video-oriented rendering | `cinematic video sequence, consistent character across shots, film production pre-visualization` |

## Shot Duration Guide

| Shot Purpose | Recommended Duration | Rationale |
|-------------|---------------------|-----------|
| Establishing shot | 5–8s | Viewer needs time to read the environment |
| Character introduction | 4–6s | First impression of a character |
| Dialogue / reaction | 3–5s | Natural conversation rhythm |
| Action beat | 2–3s | Quick cuts create tension |
| Climax / reveal | 3–5s | Let the moment land |
| Aftermath / stillness | 5–8s | Emotional processing time |
| Quick cut sequence | 1–2s each | Rapid-fire tension (max 4 in a row) |

## Camera Movement Reference

| Movement | Description | Emotional Function |
|----------|-------------|-------------------|
| Static | Camera doesn't move | Observation, stillness, tension |
| Push in (dolly forward) | Camera moves toward subject | Intensifying emotion, realization |
| Pull out (dolly back) | Camera moves away from subject | Isolation, abandonment, scale reveal |
| Pan left/right | Camera rotates horizontally | Following action, revealing environment |
| Tilt up/down | Camera rotates vertically | Power (up) or vulnerability (down) |
| Handheld | Slight shake, organic movement | Urgency, documentary realism, chaos |
| Rack focus | Focus shifts from foreground to background (or vice versa) | Revelation, connection between subjects |
| Crane up | Camera rises | Transcendence, overview, departure |

## Transition Reference

| Transition | How It Works | When to Use |
|-----------|-------------|-------------|
| Cut | Instant switch to next shot | Default. Most transitions |
| Dissolve | Gradual fade between shots | Time passage, memory, dream |
| Match cut | Visual element from shot A aligns with shot B | Elegant connection, thematic link |
| Smash cut | Abrupt cut to contrasting shot (quiet → loud) | Shock, surprise, tonal shift |
| Fade to black | Gradual fade to black | Ending, death, loss of consciousness |
| Fade in from black | Gradual reveal | Beginning, awakening, rebirth |

## Usage Notes
- **Total duration target: 10–30 seconds.** This is the optimal range for Seedance — enough for a complete narrative beat, short enough for technical stability.
- **Action = shorter shots.** A fight sequence might be 8 shots in 15 seconds. A dialogue scene might be 4 shots in 20 seconds. Duration IS pacing.
- **Camera movement must be possible.** Don't write "camera flies through 10 city blocks in 2 seconds." Seedance can't do extreme speed ramping. Write moves a human camera operator could execute.
- **Transition logic matters.** Don't dissolve between every shot — save dissolves for time passage or emotional shifts. Default to cuts.
- **Lighting continuity IS character continuity.** If Shot 1 has cold blue rain light, Shot 5 should too — unless a deliberate lighting change is a story beat (e.g., "the arena lights shift from blue to red").
- **First and last shots are the most important.** Shot 1 establishes the scene (spend your best description here). The last shot is what lingers in the viewer's mind.

## Example (Abbreviated)

```
SCENE: Rooftop Awakening — Night/Rain — 20s total
Character: Protagonist in black tactical suit (adapted from wedding tuxedo), rain-soaked

SHOT 1 (5s — WIDE, static → slow push in):
Rooftop at night, cold blue emergency lights reflecting in endless rain puddles.
A figure lies motionless on the wet concrete. Camera slowly pushes toward them.
Transition: Cut.

SHOT 2 (4s — MCU, handheld slight shake):
The figure's hand twitches. Rain runs between their fingers. A wedding ring
glows faintly for half a second then fades. Camera: shaky, urgent, 85mm.
Transition: Cut.

SHOT 3 (3s — CU, static):
Eyes snap open. Cold blue light reflected in the iris. Expression: disoriented,
no memory of how they got here. Camera: 100mm, tight on eyes.
Transition: Cut.

SHOT 4 (5s — WIDE, crane up):
The figure pushes themselves up, rain streaming off their tactical suit.
Camera rises slowly, revealing the rooftop and the ruined city beyond.
A massive holographic display flickers to life in the distance.
Transition: Dissolve.

SHOT 5 (3s — MCU, push in):
Protagonist looks at the holographic display, face illuminated by its glow.
Expression shifts from confusion to grim understanding.
Camera pushes in slowly. Transition: Cut to black.
```

## Scoring Rubric

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Pacing** | 1.2 | Do shot durations create the right rhythm for the scene's emotional intent? |
| **Visual continuity** | 1.2 | Do characters, lighting, and environments remain consistent across shots? |
| **Camera movement design** | 0.8 | Are camera movements intentional and emotionally motivated? |
| **Transition logic** | 0.6 | Do transitions serve the narrative (not just random dissolves)? |
| **Seedance viability** | 1.0 | Is the sequence technically feasible for video generation (duration, complexity)? |
| **Narrative completeness** | 1.0 | Does the sequence tell a complete beat with a clear emotional arc? |

## Common Issues
- **All shots same duration:** A sequence where every shot is 3s is mechanically flat → vary durations based on shot purpose.
- **Camera moves too complex:** "360° orbit while tracking subject down stairs" → simplify to one primary movement per shot.
- **No breathing room:** Every shot is action-packed → include a 5–8s establishing or aftermath shot for emotional rhythm.
- **Transition overuse:** Dissolving between every shot → save special transitions for moments that earn them.
