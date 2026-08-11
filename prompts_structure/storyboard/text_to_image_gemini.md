## Description
Use this architecture when generating a storyboard — a single 16:9 composite image containing 4–8 sequential frames that show narrative progression. This is the visual script: key moments arranged in reading order to communicate a scene's flow before video production.

**⚠️ Storyboards are BLACK AND WHITE LINE ART.** They serve as structural reference only: camera position, character blocking, scene layout, and composition. Color is deliberately avoided to prevent polluting the final video model's color/style decisions — those come from separate Frame references (see `frame/` skills).

**Subtype variants** (load for specialized scene types):
- `action.md` — fight choreography, fast cuts, impact frames
- `dialogue.md` — reaction shots, eye-line continuity, emotional beats
- `vfx.md` — particle effects, energy trails, transformation sequences

If the scene type isn't specified, use this general file as fallback.

## Layout Grid

```
┌──────────────┬──────────────┬──────────────┐
│              │              │              │
│   FRAME 1    │   FRAME 2    │   FRAME 3    │
│   (Setup)    │   (Action)   │  (Reaction)  │
│              │              │              │
├──────────────┼──────────────┼──────────────┤
│              │              │              │
│   FRAME 4    │   FRAME 5    │   FRAME 6    │
│   (Turning)  │   (Climax)   │  (Aftermath)  │
│              │              │              │
└──────────────┴──────────────┴──────────────┘
```

- Default: 6 frames (3×2). Short scenes: 4 frames (2×2). Complex scenes: 8 frames (4×2).
- Frames read left→right, top→bottom like a comic/manga page.
- Each frame labeled: `FRAME N (SHOT TYPE — BEAT NAME)`
- Thin black borders between frames. Clean white background.

## Prompt Composition

```
[Layout: 16:9 storyboard, N×M grid, N frames, labeled, thin black borders, clean white background] +
[Scene context: scene number, location, time, emotional arc (tension→action→resolution)] +
[Character anchor: "<Name>, <outfit>, <build> — consistent across ALL frames"] +

Frame 1: (SHOT TYPE — BEAT) <subject> + <action> + <key detail>. Camera: <focal length>, <angle>, <distance>.
Frame 2: (SHOT TYPE — BEAT) <subject> + <action> + <key detail>. Camera: <focal length>, <angle>, <distance>.
Frame 3: (SHOT TYPE — BEAT) <subject> + <action> + <key detail>. Camera: <focal length>, <angle>, <distance>.
...
Frame N: (SHOT TYPE — BEAT) <subject> + <action> + <key detail>. Camera: <focal length>, <angle>, <distance>.

[Style suffix]
```

### Frame Micro-Format
```
FRAME N (SHOT TYPE — BEAT NAME):
<Subject> + <Action/moment — visual evidence only, no interpretation> + <Key visual detail>.
Camera: <focal length>, <angle>, <distance>. Light: <key light source position, shadow quality>.
```
2–3 sentences per frame max. Every word must describe something visible on screen.
**No**: internal thoughts, emotional interpretations, narrative significance, what the moment "means."
**Yes**: facial muscle positions, object placements, light angles, shadow edges, what's in frame.

### Story Beat Pattern
Every scene follows a 4-act pulse: **Setup → Action → Reaction → Shift**. Even in a 6-frame grid, these four beats must be present. A scene that's all action or all reaction doesn't read as a story.

## Camera & Lens Narrative

Every framing decision communicates emotion. These are storytelling tools, not aesthetics.

### Angle → Attitude

| Angle | Story Effect | Use When |
|-------|-------------|----------|
| Low angle | Power, authority, threat | Villain intro, dominance, intimidation |
| High angle | Vulnerability, weakness, isolation | Defeat, loneliness, being watched |
| Dutch angle | Psychological instability, disorientation | Mental breakdown, chaos, vertigo |
| Eye level | Objectivity, neutrality, intimacy | Dialogue, connection, audience POV |

### Focal Length → Psychological Distance

| Focal Length | Story Effect | Use When |
|-------------|-------------|----------|
| Wide (24–35mm) | Environmental pressure, scale, even comedy | Fight scenes, crowds, establishing |
| Standard (50mm) | Objectivity, human-eye realism | Neutral observation, dialogue base |
| Telephoto (85–200mm) | Isolation, intimacy, voyeurism | Private moments, emotional close-ups |
| Macro | Obsession, detail, fixation | Key props, micro-expressions, hands |

### Light Direction → Mood (B&W)

In B&W storyboards, describe light *direction* and *shadow quality*, not color.

| Light Quality | Story Effect | Use When |
|--------------|-------------|----------|
| Hard single-source (deep shadows) | Drama, interrogation, danger | Conflict, reveal, tension |
| Soft diffused (weak shadows) | Calm, intimacy, safety | Dialogue, quiet moments, hope |
| Rim / backlight (silhouette) | Mystery, anonymity, revelation | Character intro, the unknown |
| Side light (half-lit face) | Duality, internal conflict | Moral ambiguity, hesitation |
| Top light (eye sockets dark) | Oppression, judgment, dread | Power dynamics, threat |
| Low light (reversed shadows) | Unnatural, wrong, uncanny | Horror, distortion, unreality |

### Foreground → Suspense

- **Blocked subject** (bars, windows, leaves framing shot) = voyeurism, trapped, watched
- **Object between characters** = emotional barrier. Remove for intimacy frames.
- **Clean foreground → deep background** = spatial clarity, objectivity

## Style Suffix

**Default (B&W line art — use this 99% of the time):**

`black and white line art storyboard, clean ink drawing style, manga storyboard panel layout, no grayscale shading — pure high-contrast linework, no color of any kind, solid white background, professional film production storyboard`

**Rare alternative — colored reference storyboard (only if explicitly requested):**

`cinematic anime storyboard, GANTZ:O style, cel-shaded consistent character design, dark sci-fi aesthetic, film production storyboard`

## Key Rules

1. **NO COLOR. Storyboards are B&W line art.** Color in a storyboard pollutes the video model's color decisions. Color/style/lighting reference comes from Frame generation (separate skill). Use ink lines only — hatch marks and line weight for shading, never grayscale fills.
2. **VISUAL ONLY — NO NARRATIVE COMMENTARY.** Describe what the camera sees — not what it "means." The AI draws pixels, not subtext. "Eyes wide, pupils dilated, mouth open" renders. "The moment between seeing and impact, stretched into stillness" does not. If a sentence requires the model to *understand* the story to draw it, delete it. Save director's commentary for the script and shot breakdown.
3. **Character consistency is the #1 problem.** Describe the same character IDENTICALLY in every frame (same outfit, hair, build). Add "consistent character design across all frames" to the style suffix. Use outfit and hair as visual anchors that don't change.
4. **Frame 1 sets the baseline.** Spend the most care here — it establishes the composition language and spatial logic. All subsequent frames match this reference.
5. **Vary shot types.** No two adjacent frames at the same distance. Pattern: Wide → Medium → Close → Wide → Medium → Close. The emotional beat dictates the shot — close-ups for internal moments, wides for scale and isolation.
6. **Pair action with reaction.** Every action frame needs a reaction frame within the next 1–2 panels. Action → reaction is how stories breathe.
7. **Light is described by direction and shadow, not color.** "Light from frame left, hard shadows across face" — not "cold blue light."
8. **2–3 sentences per frame.** Enough to render, not so much the model forgets what it just drew. If a frame needs more explanation, split it into two frames.

### Rule 2: Visual-Only — Examples

```
❌ "This is a glance of longing, of 'finally.' He is heading somewhere important."
✅ "Eyes shift downward toward the passenger seat. Smile quiet, eyelids relaxed, brow smooth."

❌ "There is no stopping, no swerving — the light is the threat."
✅ "Truck headlights flood the windshield. Right side of face washed white, left side in deep shadow."

❌ "Seven has come for the ring. Seven has come for Xiao Wu."
✅ "A floating sphere descends from the portal. The ring glints in the wreckage below."
```

**Litmus test:** Can a person who has never read the script draw this frame from the description alone? If the description references emotions, intentions, or narrative significance that aren't visible on screen → rewrite it as visual evidence.
