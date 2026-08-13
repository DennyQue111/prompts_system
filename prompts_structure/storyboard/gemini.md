## Description
Use this architecture when generating a storyboard — a single 16:9 composite image containing 4–12 sequential frames that show narrative progression. This is the visual script: key moments arranged in reading order to communicate a scene's flow before video production.

**⚠️ Storyboards are BLACK AND WHITE LINE ART.** They serve as structural reference only: camera position, character blocking, scene layout, and composition. Color is deliberately avoided to prevent polluting the final video model's color/style decisions — those come from separate Frame references (see `frame/` skills).

**Scene-type specializations are inline below** — when the scene contains action, dialogue, VFX, or a mix, jump to the relevant section under [Scene-Type Specializations](#scene-type-specializations). If the scene type isn't specified, use the general architecture as fallback.

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

- Default: 6 frames (3×2). Short scenes: 4 frames (2×2). Complex scenes: 8 frames (4×2). Extended action choreography: up to 12 frames (4×3).
- Frames read left→right, top→bottom like a comic/manga page.
- Each frame labeled: `FRAME N (SHOT TYPE — BEAT NAME)`
- Thin black borders between frames. Clean white background.

### Frame Count vs Video Duration

When the user specifies a target video duration, choose the frame count accordingly:

| Video Duration | Frame Count | Grid Layout | Rationale |
|----------------|-------------|-------------|-----------|
| 5s | 3–4 frames | 3×1 or 2×2 | Minimal: setup → action → reaction |
| 10s | 5–6 frames | 3×2 | Standard: full 4-act pulse with breathing room |
| 15s | 6–8 frames | 3×2 or 4×2 | Extended: room for secondary beats and transitions |
| 20s | 8–10 frames | 4×2 or 5×2 | Complex: multiple scene-type transitions |
| 30s | 10–12 frames | 4×3 or 5×3 | Full sequence: multiple scenes or extended choreography |

- If the user doesn't specify duration, default to 6 frames (10s baseline).
- Action scenes need more frames per second (shorter shots, faster cuts). Dialogue scenes need fewer frames per second (longer holds, reaction beats).
- Never force a frame count that doesn't serve the story. A 10s dialogue scene might only need 4 frames; a 10s action scene might need 8.

## Reference Image Declaration

When the user provides reference images (character concept sheets, location concept sheets, keyframes, etc.), declare them at the top of the prompt so the image model knows what each reference is for:

```
[Reference images:
@image character_ref.png — Character: <name>, <brief 1-sentence description>.
  Use as character design reference across all frames. Maintain consistent outfit, hair, build, and prosthetic/cybernetic details.
@image location_ref.png — Location: <brief 1-sentence description>.
  Use as environment reference across all frames. Maintain consistent architecture, lighting, and atmosphere.]
```

- One line per reference image, with `@image filename — <role>: <description>.` format.
- State clearly what the reference is for (character design / environment / lighting / mood) and what to maintain from it.
- If no reference images are provided, skip this section entirely — describe characters and environment from the prompt's scene context.

## Prompt Composition

```
[Reference images — if provided, declare here. See Reference Image Declaration above.]

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

---

## Style Suffix

**Default (B&W line art — use this 99% of the time):**

`black and white line art storyboard, clean ink drawing style, manga storyboard panel layout, no grayscale shading — pure high-contrast linework, no color of any kind, solid white background, professional film production storyboard`

**Rare alternative — colored reference storyboard (only if explicitly requested):**

`cinematic anime storyboard, GANTZ:O style, cel-shaded consistent character design, dark sci-fi aesthetic, film production storyboard`

---

## Scene-Type Specializations

When the scene contains action, dialogue, VFX, or a mix, apply the relevant section(s) below. These are **not mutually exclusive** — a single storyboard can use action rules for frames 1–4 and dialogue rules for frames 5–8. See [Mixed Scenes](#mixed-scenes) for combination guidance.

---

### Action Scenes

Fight choreography, chase sequences, stunts, explosions, and any scene driven by physical conflict. Every frame communicates movement, impact, or consequence. Speed is the primary emotional dimension.

#### Anti-Cold-Open Rule

**Start directly from action.** Do not begin with a calm stance, preparation shot, or slow introduction. Frame 1 must show the character already in motion — mid-strike, mid-leap, mid-impact. The storyboard's first panel sets the energy baseline; a static opening panel drains momentum from the entire sequence.

```
✅ Frame 1: "Character A mid-air, flying diagonal kick already in progress — leg extended, body at 30° tilt, hair trailing upward."
❌ Frame 1: "Character A stands in fighting stance, calm and ready."
```

#### Shot Type Defaults

| Purpose | Shot | Rationale |
|---------|------|-----------|
| Establish arena | Wide + Dutch angle | Signal that order is broken |
| Who's winning | Wide + Low angle | Power dominance in this moment |
| Impact moment | Telephoto + CU | Fist contact, debris, foot landing |
| Losing side | Wide + High angle | Aftermath of a blow |
| Arsenal detail | Macro | Weapons, wounds, object in motion |

#### Frame Rhythm

Action beats are faster: **2 short frames → 1 wide frame for recovery → repeat.** Wide frame re-establishes spatial awareness. No more than 2 action frames before a reaction/wide frame. Climax impact gets a standalone frame — the frozen moment of contact.

#### Camera & Movement

| When | Camera Decision |
|------|----------------|
| Default state | Dutch angle — chaos is the baseline |
| Aggression incoming | Forward push (dolly in) |
| Pursuit / speed | Side pan, whip pan |
| After a flurry of CUs | Static wide — the "breather" frame |
| Intensity spike | Handheld shake (1–2 frames max) |

##### Camera Movement Energy Vocabulary

Beyond static framing (focal length + angle), action storyboards benefit from describing the **movement energy** of each shot — the feel of the camera in motion, not just its position. Use these energy terms in frame descriptions:

| Energy Term | What It Communicates | Example Frame |
|-------------|---------------------|---------------|
| Handheld energy | Chaos, urgency, visceral immersion | CU of impact, shake on contact |
| Fast panning feel | Speed pursuit, horizontal tracking | Character sprinting across frame |
| Orbital camera movement | Showcase, spectacle, 360° awareness | Character spinning attack, camera circles |
| Overhead shot | Spatial clarity, god's-eye geometry | Two fighters' positions on ground |
| Side profile | Clean silhouette, form readability | Kick extension, body line at peak |
| Aggressive close-up | Intimacy of violence, detail of impact | Fist connecting, sweat flying |
| Telephoto compression | Flattened depth, layered chaos | Multiple fighters in tight frame |
| Extreme low angle | Power, scale, domination | Character stomping down toward camera |
| Wide negative space | Isolation, scale, environment as pressure | Solo fighter in vast arena |
| Strong parallax | Depth perception, speed through layers | Character running past foreground columns |

> These are NOT video generation camera movements — they are storyboard-level **energy descriptors** that communicate the feel of the shot to whoever reads the storyboard. In frame descriptions, pair them with focal length: e.g., "Camera: 85mm, aggressive close-up, handheld energy."

#### Lighting

- High contrast, strong shadows. Action lives in chiaroscuro.
- Color temperature shifts DRAMATICALLY at climax (cold → warm or vice versa).
- Practical lights (flickering bulbs, muzzle flashes, neon) add chaos.
- Silhouette fights are valid — shape over detail in wide frames.

#### Action Key Rules

1. **One action per frame.** Two things happening = split into two frames.
2. **Every panel must contain visible motion and strong body momentum.** No static poses. The character should feel like they are caught mid-movement in every frame — limbs in transit, weight shifting, hair/cloth trailing. Even "recovery" frames show the body settling from momentum, not standing still. Static poses kill storyboard energy.
3. **Reaction pair applies even here.** Every impact frame needs the receiver's reaction within 1–2 panels — the reaction IS the impact.
4. **Spatial anchor.** After 2–3 close-up action frames, insert one wide frame to re-establish positions.
5. **Motion blur is style data.** Write "motion blur on impact" or "speed lines on swing" in the frame description.
6. **Arena lighting is set in Frame 1.** Don't re-describe the environment — only note lighting changes.
7. **Action escalation across panels.** Choreography should build: early panels establish movement vocabulary → mid panels escalate intensity and complexity → late panels reach peak impact → final panel is the climax pose with maximum body distortion and environmental effect. Don't peak in frame 3 and then deflate.

#### Action Example (Abbreviated)

```
FRAME 1 (WIDE + DUTCH — ARENA): Rain-slick rooftop, character A in fighting stance,
character B lunging forward. Cold blue neon from billboard floods the scene.
Camera: 24mm, Dutch 15°.

FRAME 2 (CU + TELEPHOTO — IMPACT): Character B's fist connects with A's jaw.
Water droplets freeze mid-air. Motion blur on fist. Camera: 135mm, static.

FRAME 3 (CU — REACTION): Character A staggers, eyes unfocused, blood at lip.
Camera: 85mm, slight handheld shake.

FRAME 4 (WIDE + LOW ANGLE — RECOVERY): Both characters reset distance.
Character B advances, backlit by neon. Camera: 35mm, low angle.
```

#### Action Exclusion List

```
No static poses. No frozen standoffs. No timestamps. No dialogue text.
No extra characters. No logos. No watermarks. No color. No 3D rendering.
```

---

### Dialogue Scenes

Conversation scenes, interrogations, emotional confrontations, character moments. Performance carries the story — face, hands, and the space between people. Action is internal.

#### Shot Type Defaults

| Purpose | Shot | Rationale |
|---------|------|-----------|
| Relationship in one frame | 50mm, eye-level two-shot | Distance between bodies = emotional distance |
| Speaker | 85mm, OTS over listener's shoulder | Immersion in their perspective |
| Listener (more important) | 85-135mm, CU | Eyes act. This frame often matters more than the speaker's. |
| Subtext carriers | Macro | Hands, ring, glass, cigarette — a hand action IS a dialogue line |

#### Frame Rhythm

**Wide two-shot → OTS A → OTS B → CU A → CU B → Wide two-shot.** Cyclical, mirroring conversation. Reaction frame always follows the speaking frame within 1 panel. A static wide frame can carry an entire line before cutting in.

#### Camera & Movement

| When | Camera Decision |
|------|----------------|
| Default | Eye level — neutral, intimate, human |
| Emotional intensity rising | Slow push-in over 1–2 frames (barely perceptible) |
| Emotional withdrawal | Slow pull-out after something said |
| Attention shift between characters | Rack focus (foreground blur → background sharp across frames) |
| Formality, tension, coldness | Static, no movement entire scene |
| Conversation destabilizing | Dutch angle (rare — save for the breaking point) |

#### Lighting

- **Consistent.** Dialogue values continuity over spectacle.
- Warm = intimacy. Cold = distance. Side light = conflict.
- One light source change = one narrative beat. Don't shift casually.
- Eyes lit is the default. Eyes in shadow = deliberate choice (hiding truth, danger).

#### Dialogue Key Rules

1. **Eyeline match is non-negotiable.** If character A looks frame-right, B must look frame-left. Missing this = viewer loses spatial coherence instantly.
2. **Hands are half the performance.** At least one hand-specific frame per scene.
3. **The listener's face is the story.** Reaction frames carry more emotional weight than the speaker's. The audience watches the listener to know how to feel.
4. **Background contextualizes emotion.** Crowded café ≠ empty room. Include one frame that shows the environment reacting (or not reacting) to the conversation.
5. **Foreground = emotional distance.** An object in the foreground between two characters = barrier. Remove it for intimacy frames.

#### Dialogue Example (Abbreviated)

```
FRAME 1 (MEDIUM TWO-SHOT — SETUP): Two characters at a café table, rain on window.
Character A (left) leans forward, Character B (right) looks down at cup.
Camera: 50mm, eye level. Warm amber café light.

FRAME 2 (OTS — SPEAKER): Over B's shoulder, A speaking, slight tension in jaw.
Camera: 85mm, eye level.

FRAME 3 (CU — REACTION): B's hands tighten around coffee cup. Eyes don't lift.
The reaction IS the response. Camera: 135mm, static.

FRAME 4 (MACRO — SUBTEXT): B's thumb tracing the rim of the cup.
Slow, deliberate — a decision forming. Camera: macro, shallow focus.
```

#### Dialogue Exclusion List

```
No action VFX. No dramatic camera angles. No timestamps. No extra characters.
No logos. No watermarks. No color. No 3D rendering.
```

---

### VFX Scenes

Scenes driven by visual effects: magic, energy manipulation, transformation, particle systems, holograms, environmental VFX. The VFX IS the narrative event — not decoration, not background ambiance.

#### Shot Type Defaults

| Purpose | Shot | Rationale |
|---------|------|-----------|
| VFX in context | Wide + clean composition | Show scale, environment, light interaction |
| Character illuminated | CU + light from VFX | VFX light on face — color, intensity, falloff |
| VFX detail | Macro | Smoke billow, spark cluster, data stream, energy tendril |
| World interaction | Medium | VFX affecting the environment (shadows, reflections, debris) |
| Reality destabilized | Dutch + chaos VFX | When the effect breaks physics |

#### Frame Rhythm

**Wide establish → Character reaction → VFX detail → Consequence → Aftermath.** This is the VFX beat structure. VFX-heavy frames need "breathing room" before and after — don't chain 3 complex VFX frames back to back. The transformation frame (VFX peak) gets a standalone frame.

#### Camera & Movement

| When | Camera Decision |
|------|----------------|
| VFX is the subject | Static camera — let the VFX speak |
| Buildup | Slow push-in |
| Energy transfer between frames | Whip pan transition to reaction frame |
| VFX destabilizes reality | Dutch angle |

#### Lighting

- **Light source IS the VFX.** Describe color, intensity, falloff, and what it illuminates.
- **Practical light interaction required.** VFX must cast shadows, create reflections, light faces.
- **Color temperature shifts are VFX-driven:** blue energy → cold face light; fire VFX → warm.
- Lens flare, bloom, glow, light streaks — these ARE the VFX vocabulary. Use them in frame descriptions.

#### VFX Key Rules

1. **VFX must interact with the environment.** Sparks cast light. Smoke creates occlusion. Holograms reflect off wet surfaces. Never describe a VFX in isolation from its world.
2. **Pair every VFX frame with a character reaction.** The effect means nothing without the human response in the next 1–2 panels.
3. **Specify the effect precisely.** Never write "magic energy" — write "tendrils of cyan energy, arcing upward, casting cold light." Color + shape + direction + light interaction. All four.
4. **One VFX type per scene.** Fire + ice + lightning + hologram in one scene = noise. Pick one visual language.
5. **VFX must have a source.** Character's hand, device, sky, ground — ground it in the physical world.
6. **VFX must escalate across panels.** Effects should build progressively throughout the storyboard — not appear at full intensity from frame 1.

##### VFX Progression System

| Storyboard Phase | VFX Intensity | What to Show |
|-----------------|---------------|--------------|
| **Early panels** (Frames 1–3) | Subtle, barely visible | Wind hints, dust motes, pressure lines, faint aura shimmer — the effect is nascent |
| **Mid panels** (Frames 4–6) | Building, environmental interaction | Debris lifting, ground ripples, air shockwaves, visible energy trails — the effect is growing |
| **Late panels** (Frames 7–9) | Controlled, shaped | Flame trails, energy spirals, directed beams, shaped shockwaves — the effect is weaponized |
| **Final panel** (Last frame) | Maximum combined surge | All elements converging, peak intensity, environmental destruction at climax — the effect at full power |

**Progression rules:**
- Never start at peak intensity. Frame 1's VFX should feel like the calm before the storm.
- Each phase's VFX builds on the previous — mid panels don't abandon early panel effects, they amplify them.
- The final panel is the only frame where multiple VFX elements combine at maximum intensity.
- If the storyboard has fewer than 6 frames, compress to 3 phases: subtle → building → peak.

**VFX quality tone:** Effects should feel spiritual, ritualistic, and cinematic — not superheroic. Avoid comic-book energy blasts. Prefer atmospheric pressure, heat distortion, elemental residue, and gravitational warping.

#### VFX Example (Abbreviated)

```
FRAME 1 (WIDE — ESTABLISH): Dark laboratory. Character stands at center,
arms raised. A device on their chest begins to glow — faint cyan pulse,
reflecting off wet floor. Camera: 35mm, static.

FRAME 2 (CU — REACTION): Character's face illuminated from below by cyan light.
Eyes wide, sweat on brow. The glow intensifies. Camera: 85mm, static.

FRAME 3 (MACRO — VFX DETAIL): The chest device erupts — branching tendrils of
cyan energy arc outward, trailing light particles. Cold blue glow casts hard shadows.
Camera: macro, static.

FRAME 4 (WIDE — CONSEQUENCE): Energy tendrils fill the room, wrapping around
equipment, shattering glass. Character suspended at center, backlit by their own light.
Camera: 24mm, Dutch angle 10°.
```

#### VFX Exclusion List

```
No photorealistic effects. No particle noise. No timestamps. No dialogue text.
No extra characters. No logos. No watermarks. No color. No 3D rendering.
```

---

### Mixed Scenes

When a single storyboard contains multiple scene types — e.g., action leading into dialogue, or dialogue interrupted by VFX.

#### Combination Rules

1. **Per-frame type classification.** Classify each frame individually, not the entire storyboard. Frame 1–3 might be action, frame 4–5 dialogue, frame 6–8 VFX.
2. **Apply the relevant section's rules per frame.** Action frames follow action rules (anti-cold-open, motion requirement, energy vocabulary). Dialogue frames follow dialogue rules (eyeline match, hand performance, listener focus). VFX frames follow VFX rules (progression, environment interaction, precise specification).
3. **Transitions between types need a bridge frame.** Don't jump from an action CU directly to a dialogue two-shot. Insert a wide frame that re-establishes space and signals the tonal shift.
4. **Exclusion list: take the union of all involved types.** If action + VFX, combine both exclusion lists.
5. **Frame rhythm: follow the dominant type.** If 8 of 12 frames are action, use action rhythm (2 short → 1 wide) as the backbone, with dialogue/VFX frames as "breather" beats within that rhythm.
6. **Style suffix: pick one.** Don't switch between "clean ink" and "rough pencil" mid-storyboard. If action dominates, use rough pencil throughout — dialogue frames will still read fine in rough style.

---

## Key Rules (General — Apply to All Scene Types)

1. **NO COLOR. Storyboards are B&W line art.** Color in a storyboard pollutes the video model's color decisions. Color/style/lighting reference comes from Frame generation (separate skill). Use ink lines only — hatch marks and line weight for shading, never grayscale fills.
2. **VISUAL ONLY — NO NARRATIVE COMMENTARY.** Describe what the camera sees — not what it "means." The AI draws pixels, not subtext. "Eyes wide, pupils dilated, mouth open" renders. "The moment between seeing and impact, stretched into stillness" does not. If a sentence requires the model to *understand* the story to draw it, delete it. Save director's commentary for the script and shot breakdown.
3. **Character consistency is the #1 problem.** Describe the same character IDENTICALLY in every frame (same outfit, hair, build). Add "consistent character design across all frames" to the style suffix. Use outfit and hair as visual anchors that don't change.
4. **Frame 1 sets the baseline.** Spend the most care here — it establishes the composition language and spatial logic. All subsequent frames match this reference.
5. **Vary shot types.** No two adjacent frames at the same distance. Pattern: Wide → Medium → Close → Wide → Medium → Close. The emotional beat dictates the shot — close-ups for internal moments, wides for scale and isolation.
6. **Pair action with reaction.** Every action frame needs a reaction frame within the next 1–2 panels. Action → reaction is how stories breathe.
7. **Light is described by direction and shadow, not color.** "Light from frame left, hard shadows across face" — not "cold blue light."
8. **2–3 sentences per frame.** Enough to render, not so much the model forgets what it just drew. If a frame needs more explanation, split it into two frames.
9. **Environment minimalization.** Keep backgrounds minimal and atmospheric — a few key environmental anchors (pillars, hanging cloth, light beams, ground texture) are enough. Don't overcrowd the frame with environmental detail. The character and action are the focus; environment exists to contextualize, not to compete. List 4–6 environmental elements maximum per scene and reuse them across frames.
10. **Per-storyboard exclusion list.** End each storyboard prompt with an explicit exclusion list of what must NOT appear — e.g., "No timestamps. No dialogue. No extra characters. No logos. No watermarks." Customize per scene type (see each scene-type section for specific exclusion lists). This is especially important for GPT models that tend to add unwanted text and elements.
11. **No dialogue text on panels.** Never write spoken lines as text on storyboard panels. Dialogue is conveyed through facial expression, body language, and lip movement only. Text on panels pollutes downstream video model generation. Black text is limited to panel labels and 2–3 word action notes.

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

---

## Usage

1. **Determine the model** — Gemini or GPT. If GPT, also load `gpt.md` for model-specific overlay.
2. **Determine the scene type(s)** — action, dialogue, VFX, or mixed.
3. **Build the prompt** using the Prompt Composition structure above.
4. **Apply scene-type rules** from the relevant section(s) to each frame.
5. **Append style suffix** — default B&W line art, or rough pencil for action choreography preview (GPT only).
6. **Append exclusion list** — customize per scene type.
7. **Check against Key Rules** before output.
