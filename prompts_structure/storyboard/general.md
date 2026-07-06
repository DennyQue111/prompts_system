## Description
Use this architecture when generating a **storyboard for Gemini 2.5 Flash / GPT image models** — a single 16:9 composite image containing multiple sequential frames that show narrative progression. This is the visual script: key story moments arranged in reading order to communicate the scene's flow before video production begins.

Unlike Midjourney `frame` (single shot), a storyboard shows multiple frames in one image. The model must render consistent characters and environments across all frames.

## Core Principles

1. **Narrative progression, not random stills.** Each frame must advance the story — an action, a reaction, a reveal, a cut. The sequence should read like a comic strip of the scene.
2. **Consistency over perfection.** The top priority is that characters, outfits, and environments remain the SAME across all frames. Individual frame quality is secondary to consistency.
3. **Clear reading order.** Frames arranged left→right, top→bottom (comic/manga style) or numbered. The viewer must immediately understand the sequence.
4. **Key moments only.** A storyboard is NOT every shot of the scene. It's 4–8 critical beats that define the emotional arc.

## Layout Grid (16:9)

```
┌──────────────┬──────────────┬──────────────┐
│              │              │              │
│   FRAME 1    │   FRAME 2    │   FRAME 3    │
│   (Setup)    │   (Action)   │  (Reaction)  │
│              │              │              │
├──────────────┼──────────────┼──────────────┤
│              │              │              │
│   FRAME 4    │   FRAME 5    │   FRAME 6    │
│   (Turning)  │   (Climax)   │  (Aftermath) │
│              │              │              │
└──────────────┴──────────────┴──────────────┘
```

- Standard: 6 frames (3×2 grid)
- Short scenes: 4 frames (2×2)
- Complex scenes: 8 frames (4×2)
- Each frame labeled with number and shot type
- Thin borders between frames, consistent background color (dark or clean white)

## Prompt Content Formula

```
[Layout instruction: 16:9 storyboard, grid size, frame count] +
[Scene context: what scene this is, time/location, emotional arc] +
[Character consistency note: same characters in all frames, consistent outfits] +

[FRAME 1: (label) — shot type + what happens + camera] +
[FRAME 2: (label) — shot type + what happens + camera] +
[FRAME 3: (label) — shot type + what happens + camera] +
[FRAME 4: (label) — shot type + what happens + camera] +
[FRAME 5: (label) — shot type + what happens + camera] +
[FRAME 6: (label) — shot type + what happens + camera] +

[Style suffix]
```

### Content Components

| Component | Description | Key Info |
|-----------|-------------|----------|
| **Layout instruction** | Grid spec + frame count | `16:9 storyboard, 3×2 grid, 6 frames with thin borders, dark background, each frame labeled with shot number and type` |
| **Scene context** | What scene, location, time, emotional arc | Scene number, location name, time of day, the 3-act emotional shape (tension → action → resolution) |
| **Character consistency** | List who appears in which frames | "All frames feature the same [character name] in [outfit description]" — this is critical for model consistency |
| **Each frame** | Number + label + shot type + action + camera | Format: `FRAME 1 (WIDE — ESTABLISHING): [description]. Camera: 24mm, high angle.` |
| **Style suffix** | Rendering style | `cinematic storyboard, film production storyboard, consistent character design across frames` |

## Frame Description Format

Each frame follows this micro-format:

```
FRAME [N] ([SHOT TYPE] — [BEAT NAME]):
[Subject] + [Action/moment] + [Key visual detail] +
Camera: [focal length], [angle]. Lighting: [key light description].
```

### Example:

```
FRAME 1 (WIDE — ARRIVAL):
A lone figure stands at the edge of a rain-slicked rooftop, back to camera,
cold blue emergency lights catching the rain on their tactical suit.
Camera: 24mm, eye-level from behind. Lighting: single cold blue source from above-right.

FRAME 2 (MCU — RECOGNITION):
Same figure turns, face half-lit by blue light — a wedding ring glimmers on their
finger for a split second before fading. Expression shifts from blank to pained recognition.
Camera: 85mm, eye-level. Lighting: ring glow adds warm accent to cold blue base.
```

## Usage Notes
- **Character consistency is the hardest problem.** Gemini/GPT image models struggle to keep the same face across frames. Mitigation: (1) describe the character identically in every frame, (2) use consistent outfit/hair as anchor points, (3) add "consistent character design across all frames" to the style suffix.
- **Label every frame.** Numbers + shot types help the model understand sequence logic.
- **2–3 sentences per frame max.** The model needs enough detail to render, but too much text causes drift.
- **Lighting continuity matters.** If the scene starts in cold blue, it should stay in cold blue unless a deliberate lighting change is a story beat.
- **The first frame sets the visual baseline.** Spend extra care on Frame 1 — it establishes the look that all subsequent frames should match.

## Scoring Rubric

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Narrative clarity** | 1.2 | Does the sequence tell a clear story? Can a viewer follow without context? |
| **Character consistency** | 1.5 | Do characters look the same across all frames? (This is weighted highest — it's the hardest) |
| **Shot variety** | 0.8 | Are there different shot types (wide/medium/close) that serve the narrative? |
| **Emotional arc** | 1.0 | Do the frames trace a clear emotional shape (tension → action → release)? |
| **Lighting continuity** | 0.8 | Does light temperature and direction remain consistent across frames? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

## Common Issues
- **Face drift between frames:** Most common failure mode → add more character-anchor detail (hair, outfit, build) and "consistent character design" to style.
- **Static camera:** All frames at same distance → vary shot types intentionally (wide → medium → close-up → wide).
- **Missing emotional beat:** Frames show action but no reaction → always pair an action frame with a reaction frame.
- **Style inconsistency:** Frames look like different movies → unify lighting and color temperature description across all frames.
