## Description
Use this architecture when generating an image of a humanoid character — a multi-panel concept design sheet (16:9) presenting full visual range as a video production reference.

**Not for**: non-humanoid sentient entities → use `entity`.

## Core Principle: Show, Don't Tell

AI models don't understand abstract personality words. "He is loyal" produces nothing. "He unconsciously positions his body half a step in front of his teammates" produces an image. **Every personality trait must be translated into a visible physical cue before it enters the prompt.**

### Personality-to-Visual Translation

Translate inner traits into 4 visible dimensions:

| Dimension | What to Describe |
|-----------|-----------------|
| **Body language** | How they stand/sit/walk — weight distribution, shoulder angle, head tilt, reaction speed |
| **Hand state** | Calluses, scars, dirt under nails, grip style, resting position — hands tell the history |
| **Signature micro-gesture** | One recurring unconscious action: rubbing a ring-less finger, tilting head when confused, cracking knuckles |
| **Contrast shot** | One visual contradiction that reveals hidden depth: giant hand holding something tiny, scarred face breaking into a childlike smile |

Translation examples:

| Inner Trait | Visual Translation |
|-------------|-------------------|
| Loyal / protective | Stands slightly in front of teammates, body angled toward them |
| Stubborn | Direct unwavering gaze, no unnecessary micro-expressions, moves deliberately |
| Brutally strong | Thick neck and shoulders, large callused hands, unconsciously clenches fists |
| Gentle / soft-hearted | Fingers relaxed and half-curled, touches objects with careful fingertips, shoulders rounded inward |
| Battle-hardened | Old scars on knuckles, dirt under fingernails, holds objects with the side of the grip |
| Stoic / cold | Weight planted evenly, shoulders squared but not tense, jaw set, no wasted movement |

## Panel Content

| Panel | Content | What to Describe |
|-------|---------|-----------------|
| **Main Visual** (~1/3 width, ~4/5 height) | Full-body, default outfit, neutral expression | Face → Hair → Build → Body language (personality-to-visual) → Outfit (outer→inner→bottom→shoes) → Accessories & body marks → Posture |
| **View Variations** (upper-right half) | 2–3 angles (front, back, side) | ~1 sentence each. Only describe what's NEW from that angle: back → hair rear, jacket back, shoulder width; side → profile, build thickness, clothing drape |
| **Expressions** (lower-right half, 2×2 grid) | Joy / Anger / Sorrow / Happiness, shoulder-up or face-only | Each: emotion label + brow position + eye shape + mouth + any wrinkles/tension. Match expression to personality — a stoic's anger is cold and tight, not explosive |
| **Bottom Row** (full width, ~1/5 height) | All clothing, accessories, scars, birthmarks — each in its own panel, one horizontal row | Clothing laid flat. Marks as cropped body close-ups. Panel width adjusts to item count. More items → smaller panels |

## Prompt Formula

```
[Subject: name + age + role] +
[Face + Hair + Build — highlight face/body contrast if notable] +
[Personality-to-Visual: body language + hand state + signature gesture + contrast shot] +
[Outfit: outer → inner → bottom → shoes. Use prototype rule: "combat-adapted [original garment]" beats "black tactical [garment]"] +
[Accessories & body marks: visibility rules, locations] +
[Posture — enriched by personality cues]
```

## Key Rules

1. **Personality first**: Translate inner traits into visible cues before writing any physical description.
2. **Prototype rule**: "Combat suit adapted from a wedding tuxedo" is always more memorable than "black tactical suit." What did they wear when they died?
3. **Expression contrast**: Joy (eyes crinkle + smile) vs Anger (brows down + jaw tight) vs Sorrow (inner brows up + unfocused eyes) vs Happiness (wide relaxed smile + bright eyes). Don't use "same face, slightly different mouth."
4. **Scan for hidden items**: Rings, scars, birthmarks, tattoos mentioned anywhere in the user's description must appear in the bottom row.
5. **Layout reference**: For exact grid positions and full prompt composition, see `concept-sheet/character-sheet/general.md`.
