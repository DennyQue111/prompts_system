# Entity Concept Design Sheet — Layout Instruction

## Layout Grid (16:9)

```
┌────────────────┬──────────────────────────────────────┐
│                │                                      │
│                │       VIEW VARIATIONS / 三视图        │
│                │       (upper 1/2 of right area)       │
│                │                                      │
│  MAIN VISUAL   ├──────────────────────────────────────┤
│                │                                      │
│  ~1/3 width    │       DETAIL CLOSE-UPS               │
│  ~4/5 height   │       (lower 1/2 of right area)      │
│                │       AI-determined flexible grid     │
│                │       panel size adapts to count      │
│                │                                      │
├────────────────┴───┬──────────┬──────────┬───────────┤
│  Form Variation A  │ Form B   │ Form C   │ Emotion A │ Emotion B │ Emotion C │ ...
│                    ← forms first →         ← emotions →
│                         ~1/5 height, one horizontal row                       │
└─────────────────────────────────────────────────────┘
```

## Panel Definitions

- **MAIN VISUAL** — top-left, 1/3 width × ~4/5 height. The entity in its default/normal form, full visual presence, with name/label. This is the largest rendered area — form, materials, scale, sentience indicators, behavior, and lighting all live here.

- **VIEW VARIATIONS** — upper half of the right area. The same default form shown from 2–3 different viewing angles (front, side, top-down, 3/4 perspective, etc.), giving a sense of the entity's three-dimensionality. Each angle should reveal structure invisible from the main view.

- **DETAIL CLOSE-UPS** — lower half of the right area. Close-ups of critical visual components. The AI should determine the best grid arrangement based on how many details are provided: fewer details = larger panels, more details = smaller panels. No need to strictly enforce equal sizes.

- **BOTTOM ROW** — full width, ~1/5 height. One continuous horizontal row. **Form variations first** (left side), then **emotion states** (right side). All panels in this row share the same height. The number of panels can vary (typically 2–3 forms + 2–3 emotions = 4–6 total). Six panels is the practical upper limit in 16:9.

## Background & Dividers

All panels sit on a unified clean white or near-white background with thin dark divider lines. Labels appear under each panel in small, clean typography.

## Full Prompt Composition

```
[Layout instruction: 16:9 entity concept design sheet, panel positions, background] +
[Entity identity & name: type/role + one-line function tag] +
[Panel 1: MAIN VISUAL — default form, rich description] +
[Panel 2: VIEW VARIATIONS — 2-3 different angles of the default form] +
[Panel 3: DETAIL CLOSE-UPS — N panels, AI-determined flexible grid] +
[Panel 4: BOTTOM ROW — form variations first (left), then emotion states (right)] +
[Style suffix]
```

## Key Rules

1. **Layout first**: The grid instruction must be the first thing. Go macro (layout zones) → micro (panel contents).
2. **Main visual gets the richest text**: ~4/5 height × 1/3 width is a big render area. This paragraph should be the most detailed.
3. **View variations show angles, not forms**: This is about different camera perspectives of the SAME form. The side view might reveal thickness or radial symmetry invisible from the front.
4. **Detail panel count drives the grid**: Tell the AI explicitly: "arrange the detail panels in a flexible grid — larger panels if fewer details, smaller panels if more."
5. **Bottom row flows left to right**: Forms first (what other shapes can it be) → emotions (in the same default shape, how does the light/energy change).
6. **Emotion panels are about color and energy tempo**: Don't re-describe form. Name the emotion + specify hue shift + arc speed + glow radius.
7. **Unified clean background**: A white or near-white background helps all panels read as one clean composition.