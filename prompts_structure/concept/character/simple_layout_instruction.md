# Character Concept Design Sheet — Simple Layout Instruction

## Purpose

A simplified 3-panel horizontal layout optimized for **video generation reference images**. Unlike the general layout (which packs expressions, view variations, item inventory into a dense sheet), this layout maximizes per-panel resolution for video model sampling — especially facial detail.

**Core insight**: In a full-body shot, the face occupies ~5-10% of the canvas. Video models sampling from low-res facial regions suffer identity drift and blurring over time. A dedicated high-res face close-up panel gives the model a crisp facial anchor, dramatically improving temporal face stability.

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
│  facial detail   │  neutral pose    │  outfit back +   │
│  anchor for      │  full outfit     │  hair from       │
│  video sampling  │  visible         │  behind          │
│                  │                  │                  │
└──────────────────┴──────────────────┴──────────────────┘
```

## Panel Definitions

- **LEFT — FACE CLOSE-UP**, 1/3 width × full height. Upper body or shoulder-up shot. This is the **highest-fidelity panel** — facial features, skin tone, eye shape, hairline, expression, and any facial markings must be rendered with maximum clarity. The face should fill most of this panel's height. Lighting should be even and neutral (no harsh shadows across the face) to give the video model the cleanest possible facial reference. This panel exists specifically to provide a high-resolution facial anchor that video models can sample from to prevent identity drift during motion.

- **MIDDLE — FRONT VIEW**, 1/3 width × full height. Full body, front-facing, neutral standing pose. Full outfit, accessories, proportions, and posture all visible. This is the primary body reference — the video model reads silhouette, build, and clothing structure from this panel. Pose should be relaxed and natural (arms at sides or slightly relaxed), not an action pose, to serve as a neutral body template.

- **RIGHT — BACK VIEW**, 1/3 width × full height. Full body, rear-facing. Shows back of outfit, hair from behind, back of accessories, any markings on the back. This prevents the video model from hallucinating back details when the character turns around. Pose mirrors the front view for consistency.

## Background & Dividers

All three panels share a unified clean white or near-white background. Thin dark vertical divider lines separate the three columns. No labels needed — the visual distinction between close-up / front / back is self-evident.

## Full Prompt Composition

```
[Layout instruction: 16:9, 3 equal vertical columns, white background, thin dark dividers] +
[Character identity: name + age + role] +
[Panel 1: FACE CLOSE-UP — upper body / shoulder-up, highest fidelity, neutral expression, even lighting, face fills most of panel height] +
[Panel 2: FRONT VIEW — full body, front-facing, neutral standing pose, full outfit visible, relaxed posture] +
[Panel 3: BACK VIEW — full body, rear-facing, back of outfit, hair from behind, any back markings] +
[Style suffix]
```

## Key Rules

1. **Face close-up is the priority panel**: Give it the most descriptive detail. Every facial feature matters for video sampling.
2. **Even lighting on face**: No dramatic chiaroscuro, no half-shadow — the video model needs clean geometry.
3. **Neutral expression**: This is a reference sheet, not a performance. Save emotions for shot-level prompts.
4. **Front and back should match**: Same pose energy, same lighting, same rendering quality. The model cross-references them.
5. **No items/clothing laid flat**: This is body-focused. Wardrobe inventory belongs in the general layout.
6. **Three equal columns**: The visual weight should feel balanced. Don't let the close-up panel dominate or shrink.

## When to Use

| Scenario | Use |
|----------|-----|
| Generating a reference image for video generation (Seedance / Kling / Jimeng / etc.) | **simple_layout** |
| Full production character design sheet with expressions + wardrobe | **general_layout** |
