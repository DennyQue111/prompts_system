## Description
Use this architecture when generating a **single cinematic frame for Midjourney** — a standalone shot that functions like a storyboard cell rendered at full quality. This is the atomic unit of visual storytelling: one composition, one moment, one emotional beat.

A frame is NOT a concept sheet. It's a single image that should feel like a freeze-frame from a finished film.

## Core Principles

1. **One frame = one emotion.** Every compositional choice (angle, focal length, depth, lighting) should serve a single emotional intent. A high-angle wide shot of a lone figure in rain is loneliness. A tight 85mm of hands trembling over a weapon is tension.
2. **Camera tells the story.** The lens choice IS the storytelling. Wide angle = isolation, immersion. Telephoto = intimacy, compression, pressure. Dutch angle = unease. Eye-level = humanity.
3. **Light is emotion.** Cold blue = clinical, lonely, dead. Warm amber = memory, safety, the past. Hard single-source = interrogation, truth. Soft diffused = dream, memory, afterlife.
4. **Depth creates cinema.** Every frame needs at least three depth planes: foreground element → subject → background. Flat images read as amateur.

## Prompt Content Formula

```
[Shot type + emotional intent] +
[Subject: who/what is in the frame, their action/moment] +
[Lighting: source, temperature, quality, emotional function] +
[Depth layers: foreground element → midground subject → background] +
[Environment: location context from world DNA] +
[Camera: lens focal length, angle, distance, any movement implication] +
[Composition: framing rule, subject placement, negative space] +
[Atmosphere: weather, particles, haze, time of day] +
[Style Palette: film stock + format + color palette + camera language] +
[MJ style parameters]
```

### Content Components

| Component | Description | Key Decisions |
|-----------|-------------|---------------|
| **Shot type + emotional intent** | What kind of shot + what it should make the viewer feel | Wide establishing (awe, isolation), medium (presence, conversation), close-up (intimacy, tension), extreme close-up (obsession, detail), over-the-shoulder (witness, voyeurism) |
| **Subject** | Who/what is in frame, their action/moment | A character's specific micro-action (raising a weapon, touching a ring, looking up at rain), not a generic pose |
| **Lighting** | Source, temperature, quality | Hard single-source (dramatic shadows, interrogation), soft diffused (dream, memory), rim/backlight (silhouette, mystery), practical lights in-frame (world authenticity) |
| **Depth layers** | Foreground → midground → background | Foreground: out-of-focus element near camera (rain on glass, shoulder, debris). Midground: the subject. Background: depth vanishing point |
| **Environment** | Location context from world DNA | Pull from the project's location designs. If the world has "mirror surfaces," the frame's environment should contain them |
| **Camera** | Lens, angle, distance | See `reference.md` Section 5 for focal length guide. High angle = small/vulnerable. Low angle = powerful/threatening. Dutch = unease. Eye-level = human connection |
| **Composition** | Framing rule, subject placement | Rule of thirds (default), center-frame (confrontation, symmetry), negative space left/right (looking room, movement room), leading lines to subject |
| **Atmosphere** | Weather, particles, haze, time of day | Rain (melancholy, cleansing), fog (mystery, isolation), dust motes in light (stillness, memory), smoke/haze (danger, aftermath) |

## Shot Type Quick Reference

| Shot | Focal Length | Subject Framing | Emotional Function |
|------|-------------|-----------------|-------------------|
| Extreme Wide (EWS) | 18–24mm | Figure tiny in landscape | Isolation, scale, awe |
| Wide (WS) | 24–35mm | Full body + environment | Place, context, arrival |
| Medium Wide (MWS) | 35–50mm | Full body, environment recedes | Character in context |
| Medium (MS) | 50mm | Waist-up | Conversation, presence |
| Medium Close-up (MCU) | 65–85mm | Chest-up | Emotion, reaction |
| Close-up (CU) | 85–100mm | Face filling frame | Intense emotion, realization |
| Extreme Close-up (ECU) | 100mm+ | Eye, hand, object detail | Obsession, detail, trigger |
| Over-the-Shoulder (OTS) | 50–85mm | Back of one character, face of another | Witness, relationship, power dynamic |

## Lens + Emotion Mapping

| Emotional Intent | Lens | Angle | Lighting |
|-----------------|------|-------|----------|
| Loneliness / isolation | 24mm wide | High angle | Single cold source, long shadows |
| Intimacy / connection | 85mm | Eye-level | Soft warm, shallow DOF |
| Tension / danger | 50mm | Dutch 3–5° tilt | Hard single-source, deep blacks |
| Power / threat | 35mm | Low angle | Backlight silhouette or hard top-light |
| Memory / flashback | 50mm | Eye-level | Soft diffused, warm amber, slight haze |
| Revelation / truth | 85mm | Eye-level → slight push | Light source revealed in frame |
| Despair / loss | 24–35mm | High angle | Cold blue, rain or fog, desaturated |
| Hope / safety | 50mm | Eye-level | Warm practical lights, golden hour |

## Style Palette

> **See `style_reference.md`** for the complete palette library (film stock templates, CG anime templates, color palettes, camera language options). Choose one that matches your project's visual direction, then append it as the final content block before MJ parameters.
>
> Do not default to any palette — always consult `style_reference.md` and verify against the project's confirmed visual style first.

---

## MJ-Specific Parameters

Default: `--ar 16:9 --style raw --s 150 --q 2 --v 6.1`

- High action/tension: `--s 100` (more literal, less artistic drift)
- Atmospheric/mood: `--s 200–300` (embraces MJ's atmospheric strengths)
- CG anime projects: use `--s 200–300` (anime needs more stylization than photorealism) + anime palette from `style_reference.md`

## Usage Notes
- **Start with emotional intent.** Before any technical description, decide: what should the viewer FEEL? Every choice flows from that.
- **The shot type table is a compass, not a prison.** If a 35mm at eye-level with hard light conveys the right emotion, use it regardless of what the table says.
- **Depth is non-negotiable.** Foreground → subject → background. Always three planes.
- **One frame, one subject, one emotion.** Don't try to fit multiple story beats in a single frame. That's what sequences and storyboards are for.
- **Movement implication:** MJ can't render motion blur perfectly, but descriptive language like "mid-stride," "hair caught in wind," "rain frozen mid-fall" implies motion in a still frame.
