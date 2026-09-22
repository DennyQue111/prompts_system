# Character Concept Design Sheet - Flux Video Layout

## Purpose

A simplified **2-panel front/back character sheet** for Flux and similar open-source image models when the goal is downstream video consistency, not a dense production design document.

This layout trades panel count for panel clarity. Flux is less reliable than GPT/Gemini at preserving multiple dense subviews inside one sheet, so the safest layout is fewer panels with larger bodies and explicit panel order.

## Important limitation

This layout is a **production concept sheet**, not the strongest possible face anchor for video on its own. When downstream video identity precision matters, pair this sheet with a separate **single-character identity anchor** image.

## Layout Grid (16:9)

```
┌────────────────────────────┬────────────────────────────┐
│                            │                            │
│        FRONT VIEW          │         BACK VIEW          │
│        ~1/2 width          │         ~1/2 width         │
│        full height         │         full height        │
│                            │                            │
│   full body, head to toe   │   full body, head to toe   │
│   neutral standing pose    │   rear-facing neutral pose │
│   clear face and hairline  │   back of head and outfit  │
│   outfit front visible     │   outfit back visible      │
│   shoes fully visible      │   shoes fully visible      │
│                            │                            │
└────────────────────────────┴────────────────────────────┘
```

## Panel Definitions

- **LEFT - FRONT VIEW**, 1/2 width x full height. Full body, head-to-toe, front-facing, neutral standing pose. The face must be clearly visible, centered, and large enough to read identity. Show hairline, facial structure, body proportions, outfit front, accessories, hands, trouser shape, and shoes.

- **RIGHT - BACK VIEW**, 1/2 width x full height. Full body, head-to-toe, rear-facing, neutral standing pose mirroring the front panel. Show the back of the head, hairstyle from behind, collar/back seams, belts, apron ties, accessories from the back, trouser back shape, and shoes/heels/soles as visible.

## Background and dividers

Both panels share a clean white or neutral light-gray background. Use one thin dark divider line between the two panels. No scenery, props, labels, or floating wardrobe pieces.

## Full prompt composition

```
[Layout instruction: 16:9, 2 equal vertical columns, clean light background, one thin dark divider] +
[Character identity: name + age + role] +
[LEFT PANEL - FRONT VIEW: full body head-to-toe, neutral standing pose, clear visible face, front hair, outfit front, accessories front, shoes visible] +
[RIGHT PANEL - BACK VIEW: full body head-to-toe, rear-facing neutral pose, back of head, hairstyle rear, outfit back, accessories back, shoes visible] +
[Style suffix]
```

## Key rules

1. **Two panels only.** Do not silently add a facial close-up, expression row, props row, or side view.
2. **Both panels are full body.** Do not crop at the knees, thighs, or waist.
3. **Front view keeps the face.** This layout is intentionally not headless.
4. **Back view keeps the head and feet.** Rear hairstyle and footwear are both required.
5. **Neutral reference pose only.** No action pose, no dramatic camera angle, no cinematic scene lighting.
6. **Panel order is fixed.** Front on the left, back on the right.

## When to use

| Scenario | Use |
|----------|-----|
| Flux character concept sheet for downstream video reference | **flux_video_layout** |
| Need the cleanest possible facial signal for video sampling | Use this layout plus a separate single-character identity anchor |
| Full production sheet with expressions and wardrobe | **general_layout_instruction.md** |
| GPT/Gemini/Jimeng default three-panel video sheet | **simple_layout_instruction.md** |
