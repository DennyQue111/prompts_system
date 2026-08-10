# Character Concept Design Sheet — Layout Instruction

## Layout Grid (16:9)

```
┌────────────────┬──────────────────────────────────────┐
│                │       VIEW VARIATIONS                 │
│  MAIN VISUAL   │       (upper 1/2 of right area)       │
│  ~1/3 width    ├──────────────────────────────────────┤
│  ~4/5 height   │       EXPRESSIONS                    │
│                │       4 expressions, 2×2 grid         │
│                │       (lower 1/2 of right area)       │
├────────────────┴───┬──────────┬──────────┬───────────┤
│  Item panels — one horizontal row, ~1/5 height         │
│  all clothing + accessories + body marks               │
│  panel width adjusts to item count                     │
└──────────────────────────────────────────────────────┘
```

## Panel Definitions

- **MAIN VISUAL** — top-left, 1/3 width × 4/5 height. Full-body shot in default outfit, neutral expression, name label included. This is the richest rendered area — face, hair, build, body language, outfit, accessories, and posture all live here.

- **VIEW VARIATIONS** — upper-right half. 2–3 angles (front, back, side profile) revealing silhouette, clothing drape, and proportions. Each angle should show something not visible from the main view. If the back view shows nothing new, it is wasted space.

- **EXPRESSIONS** — lower-right half. Joy / Anger / Sorrow / Happiness, 2×2 grid, shoulder-up views. Clear brow/eye/mouth changes per emotion. Match the character's personality: stoic anger = cold and tight, not explosive.

- **BOTTOM ROW** — full width, ~1/5 height. One horizontal row. Each clothing item, accessory, scar, birthmark displayed individually as its own panel. More items → smaller panels. Let the AI auto-scale panel widths.

## Background & Dividers

All panels on a clean white or near-white background with thin dark divider lines. Labels in small clean typography.

## Full Prompt Composition

```
[Layout instruction: 16:9 character concept design sheet, panel positions, background] +
[Character identity: name + age + role] +
[Panel 1: MAIN VISUAL — full body, richest description] +
[Panel 2: VIEW VARIATIONS — 2-3 angles, ~1 sentence each, highlight what's new per angle] +
[Panel 3: EXPRESSIONS — joy/anger/sorrow/happiness, 2×2 grid, shoulder-up, match personality] +
[Panel 4: BOTTOM ROW — all clothing, accessories, body marks as individual panels, one row] +
[Style suffix]
```

## Key Rules

1. **Layout first**: Open the prompt with the grid instruction. Macro (zones) → micro (panel contents).
2. **Main visual is the anchor**: The richest paragraph. Every visual signal lives here.
3. **View variations = what's new**: Don't repeat the main description. Each angle must reveal silhouette or drape invisible from the main view.
4. **Expressions must differ**: Clear brow/eye/mouth changes per emotion. Match the character's personality.
5. **Bottom row = inventory**: For 4 items it's spacious; for 8 items it's compact. Let the AI auto-scale.
6. **No narrative backstory in panel descriptions**: Describe only what is visually present (pose, expression, clothing, marks).