## Description
Use this architecture when generating a location concept design sheet — a single 16:9 composite with establishing shots, alternative angles, top-down spatial overview, mid-distance structure shots, architectural detail close-ups, and a color palette reference. This is the production reference format.

## Layout Grid (16:9)

```
┌────────────────┬────────────────────┬──────────────────┐
│                │  ALTERNATE ANGLE   │   TOP-DOWN VIEW   │
│  MAIN VISUAL   │  (alt perspective  │   (bird's eye     │
│  ~1/3 × ~4/5   │   broad shot)      │    overview)      │
│                ├────────────────────┴───────────────────┤
│                │       MID-DISTANCE SHOTS               │
│                │       2-4 key structures               │
│                │       AI flexible grid                 │
├────────────────┴───┬──────────┬──────────┬─────────────┤
│  Detail A │Detail B │ Detail C    │ Color Palette       │
│  ~1/5 height, one horizontal row                        │
└─────────────────────────────────────────────────────────┘
```

- **Main Visual** — top-left, 1/3×4/5. Primary establishing shot: wide panoramic view capturing the entire location's geography and atmosphere.
- **Alternate Angle** — right-upper-left. Second broad establishing shot from a drastically different perspective (higher/lower elevation, opposite side). Shows depth and layering invisible from the main angle.
- **Top-Down View** — right-upper-right. Bird's-eye overview of spatial organization: district layout, path flow, key structure footprints. Can retain atmospheric lighting.
- **Mid-Distance Shots** — right-lower. 2–4 medium-range views of the most important individual structures or zones. AI arranges flexibly: 2→side by side, 3→2+1, 4→2×2.
- **Bottom Row** — full width, ~1/5 height. 2–4 detail close-up panels (architectural ornament, materials, signage, structural joints) + a fixed-width color palette with 4–6 swatches with material-context labels.

All panels on a unified white background with thin dark dividers. Small clean labels on each panel.

## Full Prompt Composition

```
[Layout instruction: 16:9 location concept design sheet, panel positions, background] +
[Location identity: name + type + function tag] +
[Panel 1: MAIN VISUAL — primary establishing shot, richest description, follow general.md formula] +
[Panel 2: ALTERNATE ANGLE — second broad perspective, ~2-3 sentences, highlight what's new] +
[Panel 3: TOP-DOWN VIEW — bird's-eye spatial overview, footprint shapes, path flows] +
[Panel 4: MID-DISTANCE SHOTS — 2-4 key structures, ~1-2 sentences each] +
[Panel 5: DETAIL CLOSE-UPS — architectural language + signage + materials] +
[Panel 6: COLOR PALETTE — 4-6 swatches with material-context labels] +
[Style suffix]
```

## Style Suffix

Concept sheets use lighter rendering specs than final cinematic shots — no camera brand names, no film stock.

| Direction | Suffix |
|-----------|--------|
| Photorealistic | `cinematic location concept sheet, photorealistic 8K, game environment design reference` |
| CG Anime / Dark Sci-Fi | `3D CG anime cinematic render, GANTZ:O style, cel-shaded environments on detailed 3D models, dramatic rim lighting, dark sci-fi location concept sheet, game environment reference` |
| General / Neutral | `clean location concept sheet, professional game environment art, environment design reference` |

## Key Rules

1. **Layout first**: Grid instruction opens the prompt. Macro (zones) → micro (panel contents).
2. **Main visual anchors everything**: Lighting, time of day, and atmosphere carry through all panels for cohesion.
3. **Alternate angle must earn its space**: If it shows nothing new, cut it. Pick a perspective that reveals depth, elevation, or the back side of structures.
4. **Top-down = spatial logic**: Its job is to explain layout. Can be atmospheric, but clarity of organization comes first.
5. **Mid-distance = hero buildings**: Each panel highlights one key structure or zone. Don't repeat the same building.
6. **Detail panels = world-building proof**: Signs, materials, joints — the difference between a generic place and a lived-in world.
7. **Color palette is a production tool**: Swatch labels must include material context. "Dark teal" → "Dark teal — oxidized copper dome."

## Example

**Input**: "a vertical cyberpunk megacity called The Spire, 300 floors of stacked neon districts"

**Output** (abbreviated):
```
16:9 location concept design sheet. Clean white background with subtle paper texture and thin dark panel dividers.

TOP-LEFT — MAIN VISUAL. Primary establishing shot of THE SPIRE — Vertical Megacity, 300 floors. [Full description: monolithic tower-city rising from smog-choked base through neon mid-section to gleaming corporate crown piercing cloud cover. Thousands of structures piled onto a central superstructure. Holographic billboards in pink and cyan bleeding through perpetual rain. Bottom = dark industrial orange, middle = neon dense vertical labyrinth, top = cold white-blue geometric. Atmosphere: overwhelming scale, beautiful decay.]

UPPER-RIGHT LEFT — ALTERNATE ANGLE. Worm's-eye view from street level looking straight up through the central vertical atrium. [Thousands of balconies, catwalks, and hanging platforms receding upward into a distant rectangle of sky.]

UPPER-RIGHT RIGHT — TOP-DOWN VIEW. Hexagonal footprint with hollow central atrium. [Industrial rings at base, dense mid-level districts, compact geometric crown with landing pad.]

LOWER-RIGHT — MID-DISTANCE SHOTS, 3 panels. Panel 1 — INDUSTRIAL BASE: furnace stacks, gantry cranes, hazard-suited workers on orange-lit catwalks. Panel 2 — MARKET SPINE: vertical market canyon spanning floors 120-180, suspended bridges and escalators, layered neon shopfronts. Panel 3 — CROWN GARDENS: elite upper district, wide plazas with real trees under UV lamps, glass-walled apartments overlooking the clouds.

BOTTOM ROW — full width, ~1/5 height. DETAIL A — weathered neon sign, cracked tubes, condensation on glass. DETAIL B — structural joint showing layered rust and welded plates. DETAIL C — holographic street sign projector with cracked lens. COLOR PALETTE: Neon Pink (signage) / Cyan Blue (holograms) / Industrial Orange (furnace glow) / Smog Gray-Green (ambient fog) / Cold White-Blue (crown) / Rusted Iron (structural metal).

Cinematic location concept sheet, photorealistic 8K, game environment design reference, cyberpunk aesthetic.
```
