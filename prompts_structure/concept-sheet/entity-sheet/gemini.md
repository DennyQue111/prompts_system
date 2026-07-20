## Description
Use this architecture when the user wants to generate a **concept design sheet** for a non-humanoid sentient entity — a single 16:9 composite image that presents the entity's main look alongside its viewing angles, detail close-ups, form variations, and emotional states in a structured multi-panel layout. This is the "design document" format: a reference sheet that a production team would use to understand the entity's full visual range.

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

- **Main Visual** — top-left, 1/3 width × ~4/5 height. The entity in its default/normal form, full visual presence, with name/label.
- **Right Upper — View Variations** — upper half of the right area. The same default form shown from 2–3 different viewing angles (front, side, top-down, 3/4 perspective, etc.), giving a sense of the entity's three-dimensionality.
- **Right Lower — Detail Close-ups** — lower half of the right area. Close-ups of critical visual components. The AI should determine the best grid arrangement based on how many details are provided: fewer details = larger panels, more details = smaller panels. No need to strictly enforce equal sizes.
- **Bottom Row** — full width, ~1/5 height. One continuous horizontal row. **Form variations first**, then **emotion states**. All panels in this row share the same height. The number of panels can vary (typically 2–3 forms + 2–3 emotions = 4–6 total).

All panels sit on a unified clean white or near-white background (e.g., `#FAFAFA` or subtle paper texture), with thin dark divider lines. Labels appear under each panel in small, clean typography.

## Prompt Structure Formula

```
[Layout instruction] + [Entity identity & name] +
[Panel 1: MAIN VISUAL — default form, rich description] +
[Panel 2: VIEW VARIATIONS — 2-3 different angles of the default form] +
[Panel 3: DETAIL CLOSE-UPS — N panels, AI-determined grid] +
[Panel 4: BOTTOM ROW — form variations then emotion states, one horizontal line] +
[Style suffix]
```

### Formula Components

| Component | Description | Key Info to Include |
|-----------|-------------|---------------------|
| **Layout instruction** | The grid specification | `16:9 concept design sheet`, `main visual top-left 1/3 width and 4/5 height`, `right area split into upper half (view variations) and lower half (detail close-ups, AI decides grid)`, `bottom row full width 1/5 height: form variations on the left, emotion states on the right`, `clean white background with thin dark panel dividers` |
| **Entity identity & name** | Who/what this is | Entity name, type/role, a one-line function tag (e.g., "ZERO — Swarm-Based Collective Consciousness, Game-Master") |
| **Panel 1: Main visual** | The default form, richest description | Full visual description — form/shape, materials, scale, sentience indicators, behavior, lighting. This is the largest rendered area; the most detail lives here. |
| **Panel 2: View variations** | 2–3 different viewing angles of the default form | Each angle: (a) the perspective label (front, side, top, 3/4, back), (b) what's visible from that angle that isn't visible from the main view. Keep each ~1–2 sentences. |
| **Panel 3: Detail close-ups** | Close-up panels, AI arranges freely | Each detail: what the camera focuses on, magnification level, what visual elements to render. Examples: single cube surface macro, liquid interior extreme close-up, arc jumping between cubes, scale comparison with human hand. The AI determines the grid: 2 details → side by side, 3 → 2+1 or 3-across, 4 → 2×2, 5 → flexible. |
| **Panel 4: Bottom row** | Form variations + emotion states, one horizontal row | First group: 2–3 alternative shapes (each a different configuration of the entity). Second group: 2–3 emotional color/energy states (each a different hue, arc tempo, glow intensity). Keep each ~1–2 sentences. |
| **Style suffix** | Rendering quality, art style | `cinematic concept art sheet`, `hyperrealistic 8K`, `game production design reference`, aesthetic tag |

## Usage Notes
- **Layout first**: The grid instruction must be the first thing. Go macro (layout zones) → micro (panel contents).
- **Main visual gets the richest text**: ~4/5 height × 1/3 width is a big render area. This paragraph should be the most detailed.
- **View variations show angles, not forms**: This is about different camera perspectives of the SAME form. If the entity has no permanent geometry (like a swarm), show it from front vs side vs top — the side view might reveal how "thick" the swarm silhouette is, the top view might show a radial symmetry invisible from the front.
- **Detail panel count drives the grid**: Tell the AI explicitly: "arrange the detail panels in a flexible grid — larger panels if fewer details, smaller panels if more" rather than prescribing a fixed layout.
- **Bottom row flows left to right**: Forms first (what other shapes can it be) → emotions (in the same default shape, how does the light change). This creates a natural reading path.
- **Emotion panels are about color and energy tempo**: Don't re-describe form. Name the emotion + specify hue shift + arc speed + glow radius.
- **Unified clean background**: A white or near-white background helps all panels read as one clean composition. Thin dark divider lines separate zones.

## Scoring Rubric

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Layout clarity** | 1.2 | Is the grid structure clearly described — main visual zone, right halves, bottom row? |
| **Entity identity** | 1.0 | Does the sheet communicate what this being is and its core visual DNA at a glance? |
| **View & form coverage** | 1.0 | Are viewing angles meaningful and form variations distinct? |
| **Emotion range** | 0.8 | Does the emotion section show clear visual contrast in color/energy? |
| **Detail depth** | 1.0 | Do the close-ups reveal construction secrets invisible at full-body scale? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

## Common Issues & Adjustments
- **View variations confused with form variations**: View = same form, different camera angle. Form = different shape entirely. Keep them separated.
- **Detail grid too rigid**: Don't force "2×2 grid of 4 cells." Say "arrange the N detail panels in a flexible grid that best fits the count" and let the model decide.
- **Bottom row overcrowding**: 6 total panels in one row (3 forms + 3 emotions) is the upper limit in 16:9. If the user has more, suggest trimming to 2+2 or 3+2.
- **Name label missing**: Include entity name visible near the main visual panel.
- **Emotion panels unreadable small text**: If the bottom row has 6 panels, emotion labels should be very short — just the emotion word and one color keyword.

## Example Generation
**User input**: "a swarm entity made of thousands of micro black cubes, call it Seven, it can change form and has emotional light"

**Generated prompt**:  
```
16:9 concept design sheet layout. The canvas has a clean white background with subtle paper-like texture and thin dark grid lines dividing the panels.

The top-left MAIN VISUAL panel occupies roughly one-third width and four-fifths height. It shows Zero in its default hovering humanoid silhouette form: a tall vaguely-human outline composed of thousands of tiny 1cm mirror-black cubes, each cube edge traced with hair-thin cold blue-white light. Through transparent micro-windows on each cube face, a sealed black semi-liquid churns restlessly within — alive, never solidifying — with deep blue electrical arcs flickering through the fluid. The cubes are in constant gentle motion, flipping and shifting like a swarm of sentient steel fireflies, maintaining the humanoid contour. The form hovers silently in void. Small luminous label text reads "ZERO — Default Form."

The right UPPER HALF contains VIEW VARIATIONS — 3 views of the default form. FRONT VIEW (already shown in main): the humanoid silhouette with faint facial suggestion. SIDE VIEW: the swarm profile reveals the form is only a few centimeters thick, a flat cutout-like depth from this angle, cubes stacked densely in shallow layers with arcs jumping across the narrow interior. TOP-DOWN VIEW: the swarm seen from above forms an organic vaguely-circular cluster with cubes radiating outward in loose tendrils, revealing internal light pulsing through the gaps.

The right LOWER HALF contains DETAIL CLOSE-UPS — 4 panels, arranged by the AI in a 2×2 grid. Panel 1 — macro close-up of a single 1cm cube, its mirror surface reflecting a distorted micro-world, hair-thin blue edge light, transparent window on one face showing the black liquid inside. Panel 2 — extreme close-up inside the liquid chamber, the churning black semi-liquid with deep blue lightning branching through it like a microscopic storm. Panel 3 — an arc leaping between two adjacent cubes, frozen mid-spark, the plasma bridge twisting as a blue-white filament with branching tendrils. Panel 4 — scale reference: the collapsed fist-sized core next to a human hand.

The BOTTOM ROW spans the full width at roughly one-fifth height — one horizontal line. First, FORM VARIATIONS (left half): Panel A — CIRCULAR ARRAY: cubes spread into a wide flat spinning ring, arcs jumping radially forming a halo glow. Panel B — INFORMATION WALL: cubes lock into a seamless flat rectangular surface, internal arc-light visible as a grid of glowing cells like a data display. Panel C — COLLAPSED CORE: swarm compresses into a fist-sized dense cluster, arcs wild and frenetic, a small blazing blue-white sun. Then, EMOTION STATES (right half): Panel A — CALM: cold blue-white, slow steady arc rhythm, low even luminance. Panel B — ANGER: deep red to crimson arcs, rapid jagged pulses, cubes vibrating with stray sparks. Panel C — ALERT: bright orange to white rapid strobing, cubes snapping into brief geometric patterns.

Cinematic concept art sheet, hyperrealistic 8K, game production design reference, dark sci-fi aesthetic, Gantz-inspired.
```
