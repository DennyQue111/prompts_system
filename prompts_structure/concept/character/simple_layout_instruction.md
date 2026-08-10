# Character Concept Design Sheet — Simple Layout Instruction

## Purpose

A simplified 3-panel horizontal layout optimized for **video generation reference images**. Unlike the general layout (which packs expressions, view variations, item inventory into a dense sheet), this layout maximizes per-panel resolution for video model sampling — especially facial detail.

### The Headless Front View Principle

In a standard 3-column reference, the full-body front view contains a small, low-resolution face. Even though the left panel provides a high-res facial close-up, the video model can still cross-attend to the low-res face in the middle panel, creating two competing facial signal sources. Minor rendering differences between the two (inevitable at different scales) become noise — the model blends two inconsistent facial references, reducing precision.

**The solution**: Crop the head off the front full-body view at the neck. Now there is exactly ONE source of facial data in the entire reference image — the left close-up panel. The model has no choice but to query the highest-quality facial data, eliminating the low-res interference entirely.

This is a community-validated best practice observed in advanced Seedance / Kling / Jimeng pipelines.

## Layout Grid (16:9)

```
┌──────────────────┬──────────────────┬──────────────────┐
│                  │                  │                  │
│   FACE CLOSE-UP  │   FRONT VIEW     │   BACK VIEW      │
│   ~1/3 width     │   ~1/3 width     │   ~1/3 width     │
│   full height    │   full height    │   full height    │
│                  │                  │                  │
│  Upper body /    │  Full body       │  Full body       │
│  shoulder-up     │  front-facing    │  rear-facing     │
│  HIGH-RES FACE   │  ⚠️ HEAD CROPPED │  neck-up only    │
│  (sole facial    │  AT NECK —       │  back of head +  │
│   data source)   │  no face visible │  hairstyle rear  │
│                  │  body + outfit   │  outfit back     │
│                  │  only, from      │  full body       │
│                  │  neck down       │                  │
└──────────────────┴──────────────────┴──────────────────┘

         ↑                                    ↑
    ONLY source of                    Only source of
    facial data for                   back-of-head data
    the video model                   for the video model
```

## Panel Definitions

- **LEFT — FACE CLOSE-UP**, 1/3 width × full height. Upper body or shoulder-up shot, head fully visible including hairline to chin. This is the **sole facial data source** in the entire reference image — no other panel contains any face pixels. Facial features, skin tone, eye shape, hairline, expression, and any facial markings must be rendered with maximum clarity. The face should fill most of this panel's height. Lighting should be even and neutral (no harsh shadows across the face) to give the video model the cleanest possible facial reference.

- **MIDDLE — FRONT VIEW (HEADLESS)**, 1/3 width × full height. Full body from the **neck down**, front-facing, neutral standing pose. The head is intentionally cropped out — the frame cuts cleanly at the neckline. This panel provides body type, proportions, posture, outfit front, and accessories. By removing the face, it eliminates the low-resolution facial signal that would otherwise compete with the dedicated close-up panel. Pose should be relaxed and natural (arms at sides or slightly relaxed), not an action pose.

- **RIGHT — BACK VIEW**, 1/3 width × full height. Full body, rear-facing. Shows back of head and hairstyle from behind (the only source of rear head data), back of outfit, back of accessories, any markings on the back. The head is NOT cropped here — the back of the head provides unique information (hairstyle rear, back profile) not available in the face close-up panel. Pose mirrors the front view for consistency.

## Background & Dividers

All three panels share a unified clean white or near-white background. Thin dark vertical divider lines separate the three columns. No labels needed — the visual distinction between close-up / headless front / back is self-evident.

## Full Prompt Composition

```
[Layout instruction: 16:9, 3 equal vertical columns, white background, thin dark dividers] +
[Character identity: name + age + role] +
[Panel 1: FACE CLOSE-UP — upper body / shoulder-up, highest fidelity, neutral expression, even lighting, face fills most of panel height. THIS IS THE ONLY FACIAL DATA IN THE ENTIRE IMAGE.] +
[Panel 2: FRONT VIEW (HEADLESS) — full body from neck down only, head intentionally cropped out, front-facing, neutral standing pose, full outfit visible, relaxed posture. NO FACE, NO HEAD, neck cut is clean and obvious.] +
[Panel 3: BACK VIEW — full body including back of head, rear-facing, back of hairstyle, back of outfit, any back markings] +
[Style suffix]
```

## Key Rules

1. **Face close-up is the ONLY facial data source**: The middle panel must have zero face pixels. Neck cut must be clean and unambiguous.
2. **Even lighting on face**: No dramatic chiaroscuro, no half-shadow — the video model needs clean geometry.
3. **Neutral expression**: This is a reference sheet, not a performance. Save emotions for shot-level prompts.
4. **Front and back body should match**: Same pose energy, same lighting, same rendering quality. The model cross-references them.
5. **Back view keeps the head**: The back of the head provides unique data (hairstyle rear, back profile) not duplicated in the close-up — no conflict, so no need to crop.
6. **No items/clothing laid flat**: This is body-focused. Wardrobe inventory belongs in the general layout.
7. **Three equal columns**: The visual weight should feel balanced. Don't let the close-up panel dominate or shrink.
8. **Prompt must explicitly state the crop**: "head intentionally cropped out / no face / no head" — this prevents the image generator from accidentally including a tiny face in the body panel.

## Why This Works Better Than a Standard 3-View

| Approach | Facial signal sources | Risk |
|----------|----------------------|------|
| Standard 3-view (face in both left + middle) | 2 competing sources (high-res + low-res) | Model blends inconsistent signals → identity drift |
| **Headless front view** | 1 exclusive source (high-res only) | No competing signal → clean, stable facial anchor |

The back view keeps the head because rear head data (hair from behind, back profile) has no competing source — it's uniquely informative without creating signal conflict.

## When to Use

| Scenario | Use |
|----------|-----|
| Generating a reference image for video generation (Seedance / Kling / Jimeng / etc.) | **simple_layout** |
| Full production character design sheet with expressions + wardrobe | **general_layout** |
