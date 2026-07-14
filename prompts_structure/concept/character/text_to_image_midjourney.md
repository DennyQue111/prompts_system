## Description
Use this architecture when generating a **single-image character design prompt for Midjourney**. Unlike `general.md` (which produces multi-panel 16:9 concept sheets for Gemini/GPT), this file produces one cinematic still that captures the character's visual identity in a single frame — optimized for Midjourney's strengths in atmosphere, texture, and lighting.

The key difference: `general.md` defines *what panels are needed*. This file defines *how to design the character from story and world-view DNA* so the single image carries maximum identity.

## Core Principles

1. **Design from world-view, not from description.** Every visual choice must be traceable back to the project's world DNA. If the world is "cold blue light, rain never stops, mirror surfaces everywhere," the character's clothing materials, skin sheen, and eye reflections must be saturated with that logic.
2. **Story context shapes the body.** Who they were before entering the game, how they died, what they lost — these narrative facts should produce visible marks on the character (a wedding ring tan line, scar tissue from their death wound, clothing adapted from their last living outfit).
3. **Personality-to-Visual is the anchor.** In a single image with no expression panels, body language, hand state, and a signature gesture are the ONLY tools to show personality. Use them ruthlessly.
4. **One shot, one story.** The single image must feel like a film still — not a reference sheet, not a studio portrait. It should look like a freeze-frame from a movie that already exists.

## Prompt Content Formula

```
[Character subject: name + age + role + pre-death identity] +
[World-view injection: light, atmosphere, material from world DNA] +
[Face + hair + build: shaped by their story] +
[Personality-to-Visual: body language + hand state + signature gesture] +
[Outfit: prototype garment → combat adaptation, with world materials] +
[Accessories & story marks: scars, jewelry, death wound] +
[Environment grounding: where they stand in the world] +
[Camera & composition: lens, angle, framing] +
[MJ style parameters]
```

### Content Components

| Component | Description | How to Design from Story & World-View |
|-----------|-------------|--------------------------------------|
| **Character subject** | Name, age, role, pre-death identity | The gap between "who they were" and "who they are now" IS the character. A 32-year-old programmer who died debugging at 3 AM reads very differently as a death-game survivor than a 28-year-old soldier. |
| **World-view injection** | Light temperature, atmosphere, material logic from world DNA | Directly pull from the project's world-view document: "冷蓝光线清洗过的一切," "雨永远在下," "镜面永远在反射" → the character's skin should be washed in cold blue, their clothing should glisten with rain, their eyes should reflect like mirrors. |
| **Face + hair + build** | Physical appearance shaped by story | Build contrast = memorability. A gentle office-worker face on a massive frame, or vice versa. Hair maintenance level reflects their mental state — character who's given up stops cutting their hair. |
| **Personality-to-Visual** | Body language, hand state, signature gesture, contrast shot | This is where the translation table in `general.md` pays off. EVERY personality trait becomes a visible cue. A loyal character's body angles slightly forward like a shield. A gentle giant's fingers are half-curled and relaxed. |
| **Outfit** | Prototype garment → death-game adaptation | The "prototype rule": what garment did they die in? A wedding tuxedo adapted for combat with torn sleeves and tactical straps. A hospital gown with armor plates bolted on. The original garment must be VISIBLE beneath the adaptation. |
| **Accessories & story marks** | Scars, jewelry, death wound, tattoos | Every mark tells a piece of their story. The death wound is especially important — it should be visible somewhere on the body as a permanent reminder. A ring tan line on a ring-less finger suggests a marriage that ended before death. |
| **Environment grounding** | Where they stand, what surrounds them | Don't float the character in void. Place them in a specific location from the world — a rain-slicked rooftop, a mirror-maze corridor, a white awakening chamber. The environment contextualizes the outfit and lighting. |
| **Camera & composition** | Lens, angle, framing, camera movement | From `reference.md` Section 5. Default: 50mm for natural presence or 85mm for intimate character shot. Full-body for outfit read, 3/4 for personality focus. Slightly low angle for quiet strength, eye-level for vulnerability. |
| **MJ style parameters** | Midjourney-specific flags | See Parameters section below. |

## World-View to Character Injection Flow

When a project has a world-view document (9 aspects from MOKEAIGC framework), follow this injection flow:

| World-View Aspect | Injects Into Character Component |
|-------------------|----------------------------------|
| World Concept (overall atmosphere) | World-view injection, Environment grounding |
| Inhabitants (how people exist here) | How the character's body language references group behavior |
| Animals / Creatures | (for entity only) |
| Architecture | Environment grounding backdrop |
| Landscape / Terrain | Environment materials underfoot |
| Daily Life (how people live/survive) | Outfit wear-and-tear level, accessory function |
| Travel / Motion (how things move) | Signature gesture dynamics, gait implication in stance |
| Sound / Culture | (visual culture cues: markings, symbols, ritual scars) |
| Power / Authority | Accessory hierarchy markers, body language authority cues |

## Midjourney-Specific Parameters

### Aspect Ratio
```
--ar 16:9    ← standard cinematic (default for this architecture)
--ar 3:2     ← tighter character portrait
--ar 9:16    ← vertical character showcase
```

### Style Control
```
--style raw    ← reduces MJ's "beautification," keeps prompt fidelity
--s 50–250     ← stylization (lower = more literal, higher = more artistic)
--c 0–100      ← chaos (variation between image grid; 0=consistent, 100=wild variation)
```

### Rendering Quality
```
--q 2          ← maximum quality (default for production)
--v 6.1        ← model version
```

### Recommended Defaults
For character design: `--ar 16:9 --style raw --s 150 --q 2 --v 6.1`

## Usage Notes
- **Start from the world-view document.** Before writing a single word about the character, re-read the project's world DNA. The character should look like they were BORN from that world.
- **The death-wound rule:** Every character in a death-game setting should have a visible mark of their death. It's the most powerful visual shorthand for "this person died and was brought back."
- **Prototype garment > generic tactical:** "Combat suit adapted from a blood-stained wedding dress" will always produce a more memorable image than "black tactical bodysuit."
- **Single image means maximum density:** Without expression panels or wardrobe rows, every square inch of the single frame must carry visual information.
- **MJ responds to sensory language:** Words like "rain-slicked," "cold blue," "mirror-bright," "blood-rusted" produce stronger results than "blue light" or "shiny."
- **Avoid photorealistic for Chinese platforms:** If targeting 即梦/豆包, replace photorealism cues with the CG anime style from `reference.md` Section 6 — otherwise the human realism filter will block it.

## Scoring Rubric (for evaluating MJ character prompts)

Score each dimension 0–10.

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **World-view integration** | 1.2 | Does the character visually belong to the world? Are the world's light, materials, and atmosphere visible on the character? |
| **Story context visibility** | 1.0 | Can we see their pre-death identity in their appearance? Is the death wound or a story mark visible? |
| **Personality visualization** | 1.2 | Are inner traits translated into body language, hand state, and a signature gesture? |
| **Outfit storytelling** | 0.8 | Does the outfit have a visible prototype garment? Is it adapted, not just generic? |
| **Composition & camera** | 0.6 | Is the lens, angle, and framing intentional? Does it enhance the character read? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

## Common Issues & Adjustments
- **Character floats outside the world:** The world-view isn't referenced → re-read the world DNA and inject light/materials into the description.
- **Generic "tactical suit":** No prototype garment visible → ask: what did this person wear when they died? Start from there.
- **Personality told, not shown:** "He is loyal" → translate every trait: body angle, hand position, gaze direction, weight distribution.
- **No visual story mark:** No death wound, no ring tan line, no scar → every character needs at least ONE visible mark of their history.
- **Flat MJ output:** Style too weak → add `--style raw`, increase sensory language density, use material-words (slick, rusted, mirrored, torn).

## Image Structure
Unlike `general.md`, this file does NOT produce multi-panel sheets. The output is a single cinematic image. For multi-panel character concept sheets, use `general.md`.

For character sheet layout definitions, see: `concept-sheet/character-sheet/general.md`
