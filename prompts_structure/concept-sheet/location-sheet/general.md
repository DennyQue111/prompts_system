## Description
Use this architecture when the user wants to generate a **location concept design sheet** — a single 16:9 composite image that presents the full scope of a story setting: establishing shots, alternative angles, top-down spatial overview, mid-distance structure showcases, architectural detail close-ups, and a color palette reference. This is the "world-building" reference format: a one-page design document that gives a video model everything it needs to understand the visual language of a location.

## Layout Grid (16:9)

```
┌────────────────┬────────────────────┬──────────────────┐
│                │  ALTERNATE ANGLE   │   TOP-DOWN VIEW   │
│                │  (alt perspective  │   (bird's eye     │
│  MAIN VISUAL   │   broad shot)      │    overview)      │
│                │                    │                   │
│  ~1/3 × ~4/5   ├────────────────────┴───────────────────┤
│                │                                       │
│                │       MID-DISTANCE SHOTS               │
│                │       (key structures/districts)        │
│                │       AI flexible grid                │
│                │                                       │
├────────────────┴───┬──────────┬──────────┬─────────────┤
│  Detail A │ Detail B │ Detail C    │ Color Palette     │
│  (arch.   │(signage  │(material   │ 4-6 swatches +     │
│   detail) │ text)    │  macro)    │ labels             │
│  ~1/5 height, one horizontal row                       │
└─────────────────────────────────────────────────────────┘
```

- **Main Visual** — top-left, 1/3 width × ~4/5 height. The primary establishing shot: a wide panoramic view that captures the entire location's architecture, geography, and atmosphere in one frame.
- **Right Upper (left half)** — Alternate Angle. A second broad establishing shot from a dramatically different perspective (e.g., 3/4 angle if main is straight-on, or from a higher/lower elevation). Shows depth, layering, and spatial relationships invisible from the main angle.
- **Right Upper (right half)** — Top-Down View. A bird's-eye overview of the full location. Shows spatial organization: where districts/rooms/zones connect, how roads/rivers/corridors flow, the footprint of key structures. Can retain atmosphere and lighting.
- **Right Lower** — Mid-Distance Shots. 2–4 medium-range views of the most important individual buildings, districts, or landscape features. AI arranges in a flexible grid: 2→side by side, 3→2+1 or 3-across, 4→2×2.
- **Bottom Row** — Detail Close-ups + Color Palette. One continuous horizontal row at ~1/5 height. 2–4 detail panels (architectural ornament, materials, signage/text, structural joints) followed by a fixed-width color palette panel with 4–6 swatches.

All panels sit on a unified clean white or near-white background (e.g., `#FAFAFA` or subtle paper texture), with thin dark divider lines.

## Prompt Structure Formula

```
[Layout instruction] + [Location identity & name] +
[Panel 1: MAIN VISUAL — primary establishing shot] +
[Panel 2: ALTERNATE ANGLE — second broad perspective] +
[Panel 3: TOP-DOWN VIEW — bird's-eye spatial overview] +
[Panel 4: MID-DISTANCE SHOTS — 2-4 key structures] +
[Panel 5: DETAIL CLOSE-UPS — architectural language + signage + materials] +
[Panel 6: COLOR PALETTE — 4-6 dominant swatches with labels] +
[Style suffix]
```

### Formula Components

| Component | Description | Key Info to Include |
|-----------|-------------|---------------------|
| **Layout instruction** | The grid specification | `16:9 location concept design sheet`, `main visual top-left 1/3 width and 4/5 height`, `right upper left = alternate angle, right upper right = top-down view`, `right lower = mid-distance shots AI-flexible grid`, `bottom row = detail close-ups + color palette`, `clean white background with thin dark panel dividers` |
| **Location identity & name** | What this place is | Location name, type/category, a one-line function tag |
| **Panel 1: Main visual** | Primary establishing shot | Full visual: location type, geography/layout, architecture, time/weather, atmosphere, lighting, decorative accents. Richest text. |
| **Panel 2: Alternate angle** | Second broad perspective | What angle, what's newly visible (depth, layering, back of structures). ~2-3 sentences. |
| **Panel 3: Top-down view** | Bird's-eye overview | Spatial organization, footprint shape, flow of paths/zones. Can retain atmospheric lighting. |
| **Panel 4: Mid-distance shots** | 2–4 key structures at medium range | Each: what structure/zone, what makes it distinct, architectural massing and character. ~1-2 sentences each. |
| **Panel 5: Detail close-ups** | Architectural language + signage + materials | Each: what the camera focuses on, what world-building detail this reveals. |
| **Panel 6: Color palette** | 4–6 swatches with labels | Each: color name + material context descriptor. |
| **Style suffix** | Rendering quality, art style | `cinematic location concept sheet`, `photorealistic 8K`, `game environment design reference` |

## Usage Notes
- **Layout first**: The grid instruction must come before panel content.
- **Main visual sets the tone**: Lighting, time of day, and atmosphere should carry through to the others for visual cohesion.
- **Alternate angle must show something new**: Pick an angle that reveals depth, elevation changes, or the "back side" of structures.
- **Top-down is about spatial logic**: Communicates layout, flow, relationships. Can be atmospheric but its primary job is to explain organization.
- **Mid-distance shots = hero buildings**: Each panel highlights one key structure or zone that defines the place.
- **Detail panels = world-building proof**: Signs, materials, craftsmanship — the difference between a generic city and a lived-in world.
- **Color palette panel is a production tool**: Dominant colors of the location as a mood board. Include material context.

## Scoring Rubric

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Location identity** | 1.0 | Does the sheet communicate what kind of place this is and what makes it unique? |
| **Spatial coverage** | 1.2 | Do the establishing shots, top-down view, and mid-distance panels collectively explain the full layout? |
| **Atmospheric consistency** | 1.0 | Does the mood/lighting/weather carry through all panels for visual cohesion? |
| **Architectural language** | 1.0 | Do the detail close-ups reveal a distinctive architectural identity? |
| **Production value** | 0.8 | Is the color palette clear and useful? Are all panels filled with non-redundant information? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

## Common Issues & Adjustments
- **Main visual and alternate angle too similar**: Switch to a more dramatic perspective — bird's-eye, worm's-eye, opposite side.
- **Top-down too schematic**: Keep the same lighting and weather. Show shadows, mist, rooftop clutter from above.
- **Mid-distance panels blur together**: Each should highlight a DIFFERENT zone or structure.
- **Details are generic**: "a decorated wall" → "a limestone frieze of winged figures with eroded faces."
- **Color palette missing context**: Swatch labels should include material references. "Dark teal" → "Dark teal — oxidized copper dome."
- **Bottom row overcrowding**: 3 detail panels + 1 palette = 4 total, comfortable. More than 5 details → trim.

## Example Generation
**User input**: "a vertical cyberpunk megacity called The Spire, 300 floors of stacked neon districts"

**Generated prompt**:  
```
16:9 location concept design sheet layout. The canvas has a clean white background with subtle paper-like texture and thin dark grid lines dividing the panels.

The top-left MAIN VISUAL panel occupies roughly one-third width and four-fifths height — the primary establishing shot. It shows The Spire, a vertical cyberpunk megacity: a monolithic tower-city rising 300 floors from a smog-choked industrial base through a neon mid-section of markets and residential stacks, to a gleaming corporate crown piercing low cloud cover. The tower is not one building but thousands of structures piled, cantilevered, and grafted onto a central superstructure — like a coral reef made of steel and glass. Countless holographic billboards project in Mandarin and English across every surface, their neon pink and cyan glow bleeding through perpetual rain and fog. The base is dark, industrial, lit by orange furnace-glow and welding sparks. The mid-levels are a dense vertical labyrinth of pedestrian bridges, cable cars, and hanging gardens. The upper crown is cold white-blue, clean geometric, protected by energy shield shimmer. Golden hour light struggles through the smog, catching the upper spire in amber while the lower levels remain in permanent twilight. Small label reads "THE SPIRE — Vertical Megacity, 300 Floors."

The right UPPER LEFT panel is the ALTERNATE ANGLE — a worm's-eye view from street level looking straight up through the central vertical atrium. From this angle the tower's interior canyon is visible: thousands of balconies, catwalks, and hanging platforms receding upward into a distant rectangle of pale sky 300 floors above, the walls of the canyon alive with layered neon signage, laundry lines, and creeping vegetation.

The right UPPER RIGHT panel is the TOP-DOWN VIEW — a bird's-eye look at the tower's footprint. The Spire is roughly hexagonal in cross-section, with a hollow central atrium. The base sprawls wider with industrial rings and docking platforms radiating outward. The mid-levels narrow slightly, dense with compartmentalized districts. The crown is a compact geometric hexagon with a landing pad and shield generator at center. Rooftop clutter covers every flat surface. Rain glistens on the rooftops under neon reflections.

The right LOWER HALF contains MID-DISTANCE SHOTS — 3 panels arranged flexibly. Panel 1 — THE INDUSTRIAL BASE: low-angle shot of the ground-level sector, massive furnace stacks belching orange-lit steam, gantry cranes, cargo lifts, workers in hazard suits moving through orange-lit catwalks. Panel 2 — THE MARKET SPINE: a vertical market district spanning floors 120–180, a dense canyon of shop fronts stacked twelve high, connected by suspended bridges and escalators, every surface covered in animated neon advertisements. Panel 3 — THE CROWN GARDENS: the elite upper district around floor 280, wide open plazas with real trees under UV lamps, glass-walled executive apartments overlooking the cloud layer below.

The BOTTOM ROW spans full width at roughly one-fifth height. DETAIL CLOSE-UPS (3 panels, sizing to fit): Panel A — a weathered neon sign in eroded Chinese characters reading "OPEN ALL CYCLES," its flickering pink tube bent and patched, condensation dripping off the glass. Panel B — a close-up of a structural joint where three cantilevered buildings meet, showing layered rust, welded plates, and tangled cables. Panel C — macro shot of a holographic street sign projector, its lens cracked, projecting a distorted flickering arrow onto wet concrete. COLOR PALETTE (fixed-width panel at right end): Swatch 1 "Neon Pink" — signage / Swatch 2 "Cyan Blue" — holograms / Swatch 3 "Industrial Orange" — furnace glow / Swatch 4 "Smog Gray-Green" — ambient fog / Swatch 5 "Cold White-Blue" — crown district / Swatch 6 "Rusted Iron" — structural metal.

Cinematic location concept sheet, photorealistic 8K, game environment design reference, cyberpunk aesthetic.
```
