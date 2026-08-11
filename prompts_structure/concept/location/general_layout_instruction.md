# Location Concept Design Sheet — Layout Instruction

## Layout Grid (16:9)

```
┌────────────────┬────────────────────┬──────────────────┐
│                │  REVERSE ANGLE     │   TOP-DOWN VIEW  │
│  MAIN VISUAL   │  (180° opposite    │   (full spatial  │
│  ~1/3 × ~4/5   │   from main cam)   │    overview)     │
│                ├────────────────────┴───────────────────┤
│                │       MID-DISTANCE SHOTS               │
│                │       3 key structures/zones           │
│                │       side by side                     │
├────────────────┴───┬──────────┬──────────┬─────────────┤
│  Detail A │Detail B │ Detail C │ Color Palette         │
│  ~1/5 height, one horizontal row                        │
└─────────────────────────────────────────────────────────┘
```

## Panel Definitions

- **MAIN VISUAL** — top-left, 1/3 width × 4/5 height. Primary establishing shot: wide panoramic aerial view capturing the full location geography, all key landmarks, and overall atmosphere. This panel must show the entire scene at a glance — what exists, where things are, and the dominant art style.

- **REVERSE ANGLE** — upper-right left. Shot from the exact opposite side of the main camera position (180° flip). Shows what the main visual hides — back faces of structures, depth layering from the other direction, and spatial relationships invisible from the primary angle. Together, main + reverse cover the full 360° of the location.

- **TOP-DOWN VIEW** — upper-right right. Full bird's-eye overview of the entire playable/map area. Must include all story-relevant locations marked with approximate positions: fountain plaza, carousel zone, Ferris wheel base, entrance arch, roller coaster track, etc. This is a production tool for placing individual shots later — clarity of spatial organization comes before atmospheric rendering.

- **MID-DISTANCE SHOTS** — right-lower, 3 panels side by side. Medium-range views of the most important individual structures or zones. Each panel highlights one key location feature that tells environmental story. Do not repeat the same building.

- **BOTTOM ROW** — full width, ~1/5 height. 2–4 detail close-up panels (architectural ornament, materials, signage, structural joints, vegetation) + a fixed-width color palette with 4–6 swatches with material-context labels.

## Background & Dividers

All panels on a unified clean white or near-white background with thin dark divider lines. Labels appear under each panel in small, clean typography.

## Full Prompt Composition

```
[Layout instruction: 16:9 location concept design sheet, panel positions, background] +
[Location identity: name + type + function tag] +
[Panel 1: MAIN VISUAL — primary establishing shot, richest description] +
[Panel 2: REVERSE ANGLE — 180° opposite perspective, ~2-3 sentences, highlight what's new] +
[Panel 3: TOP-DOWN VIEW — bird's-eye spatial overview, all story locations marked, footprint shapes, path flows] +
[Panel 4: MID-DISTANCE SHOTS — 3 key structures, ~1-2 sentences each] +
[Panel 5: DETAIL CLOSE-UPS — architectural language + signage + materials] +
[Panel 6: COLOR PALETTE — 4-6 swatches with material-context labels] +
[Style suffix]
```

## Key Rules

1. **Layout first**: Grid instruction opens the prompt. Macro (zones) → micro (panel contents).
2. **Main visual anchors everything**: Lighting, time of day, and atmosphere carry through all panels for cohesion.
3. **Reverse angle must earn its space**: 180° flip from main camera. If it shows nothing new, the main visual was not panoramic enough.
4. **Top-down = shot placement tool**: Its primary job is to show where every story beat happens. Label key zones clearly.
5. **Mid-distance = hero buildings/zones**: Each panel highlights one key structure. Don't repeat the same building.
6. **Detail panels = world-building proof**: Signs, materials, joints — the difference between a generic place and a lived-in world.
7. **Color palette is a production tool**: Swatch labels must include material context. "Dark teal" → "Dark teal — oxidized copper dome."