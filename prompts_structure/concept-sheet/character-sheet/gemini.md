## Description
Use this architecture when generating a character concept design sheet — a single 16:9 composite with full-body main visual, viewing angles, expressions, and wardrobe inventory in a structured multi-panel layout. This is the production reference format.

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

- **Main Visual** — top-left. Full-body in default outfit, neutral expression, name label included.
- **View Variations** — upper-right. 2–3 angles (front, back, side) revealing silhouette and drape.
- **Expressions** — lower-right. Joy / Anger / Sorrow / Happiness, 2×2 grid, shoulder-up. Match personality: stoic anger = cold and tight, not explosive.
- **Bottom Row** — full width, one horizontal row. Each clothing item, accessory, scar, birthmark displayed individually. More items → smaller panels.

All panels on a clean white background with thin dark dividers. Labels in small clean typography.

## Full Prompt Composition

```
[Layout instruction: 16:9 character concept design sheet, panel positions, background] +
[Character identity: name + age + role] +
[Panel 1: MAIN VISUAL — full body, richest description, follow general.md formula] +
[Panel 2: VIEW VARIATIONS — 2–3 angles, ~1 sentence each, highlight what's new per angle] +
[Panel 3: EXPRESSIONS — joy/anger/sorrow/happiness, 2×2 grid, shoulder-up, match personality] +
[Panel 4: BOTTOM ROW — all clothing, accessories, body marks as individual panels, one row] +
[Style suffix]
```

## Style Suffix

Derive from the project's visual direction. Concept sheets should use lighter rendering specs than final cinematic shots — no camera brand names, no film stock.

| Direction | Suffix |
|-----------|--------|
| Photorealistic | `cinematic character concept sheet, photorealistic 8K, game production character design reference` |
| CG Anime / Dark Sci-Fi | `3D CG anime cinematic render, GANTZ:O style, cel-shaded characters on detailed 3D models, dark sci-fi character concept sheet, game production reference` |
| General / Neutral | `clean character concept sheet, professional game production art, character design reference` |

## Usage Notes

- **Layout first**: Open the prompt with the grid instruction. Macro (zones) → micro (panel contents).
- **Main visual is the anchor**: The richest paragraph. Every visual signal lives here.
- **View variations = what's new**: Don't repeat the main description. If the back view shows nothing new, it's wasted space.
- **Expressions must differ**: Clear brow/eye/mouth changes per emotion. Match the character's personality.
- **Bottom row = inventory**: For 4 items it's spacious; for 8 items it's compact. Let the AI auto-scale.

## Example

**Input**: "Xiao Wu, 28, office worker in death game. Honest wide face, short black hair, Ma Dong-seok build, combat-adapted charcoal wedding suit, silver ring that glimmers briefly."

**Output** (abbreviated — agent fills in full descriptions from general.md):

```
16:9 character concept design sheet. Clean white background with subtle paper texture and thin dark panel dividers.

TOP-LEFT — MAIN VISUAL, one-third width and four-fifths height. Full-body shot of XIAO WU, 28, office worker turned death-game survivor. [Full description from general.md formula: face → hair → build → body language → outfit → accessories → posture. Use prototype rule for the combat-adapted wedding suit.]

UPPER-RIGHT — VIEW VARIATIONS. FRONT / BACK / SIDE. [~1 sentence per angle, highlight what's new.]

LOWER-RIGHT — EXPRESSIONS, 2×2 grid, shoulder-up. JOY / ANGER / SORROW / HAPPINESS. [4 expressions with clear brow/eye/mouth changes, matched to personality.]

BOTTOM ROW — full width, ~1/5 height. JACKET / SHIRT / TROUSERS / BOOTS / RING. [Each item in its own panel. Clothing laid flat. Ring as translucent glimmer.]

3D CG anime cinematic render, GANTZ:O style meets Demon Slayer aesthetic, cel-shaded characters on detailed 3D models, dark sci-fi character concept sheet, game production reference.
```
