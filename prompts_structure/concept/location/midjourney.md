## Description
Use this architecture when generating a **single-image location prompt for Midjourney**. Produces one cinematic establishing shot of an environment or setting — optimized for MJ's strength in atmosphere, scale, and environmental storytelling.

Unlike `general.md` (multi-panel location sheet), this is a single atmospheric frame designed to establish the world's visual language in one image.

## Core Principles

1. **Mood first, geography second.** MJ cares about light, color, and atmosphere more than architectural accuracy. Lead with the feeling, then describe the space.
2. **The world-view IS the location description.** Every location in a project should feel like a natural extension of the world DNA — if the world is "cold blue, rain, mirrors," every location inherits these materials and lighting.
3. **Depth layers matter.** Foreground silhouette → midground subject → background depth. Three layers minimum for cinematic depth.
4. **The "lived in" principle.** A location should show traces of use — scuff marks, rust, debris, signs that things happened here before the camera arrived.

## Prompt Content Formula

```
[Location type + function in story] +
[World-view atmosphere injection: light, weather, color temperature] +
[Spatial composition: foreground → midground → background] +
[Architecture & materials: what it's built from, textured by world DNA] +
[Lived-in details: wear, debris, traces of past events] +
[Scale reference: human figure or doorway for size read] +
[Camera & composition: lens, angle, framing] +
[MJ style parameters]
```

### Content Components

| Component | Description | World-View Integration |
|-----------|-------------|----------------------|
| **Location type** | What this place is + its narrative function (safe zone, arena, threshold) | Name the location in world terms — "废弃都市遗迹第7区" not "ruined city" |
| **Atmosphere injection** | Light source, color temp, weather, time of day | Directly from world DNA — every location shares the world's light logic |
| **Spatial composition** | Foreground → midground → background layers | Guide MJ's depth: foreground element (ruined pillar, rain-streaked window) → midground subject → background vanishing point |
| **Architecture & materials** | Building/terrain materials, construction style | World materials: if the world is "mirror surfaces everywhere," describe mirror-fragment architecture |
| **Lived-in details** | Wear, rust, debris, traces of use | Implies passage of time and survivors — bloodstains on arena walls, scratched tally marks, abandoned gear |
| **Scale reference** | Human figure or known object | A single survivor's silhouette provides instant scale read |
| **Camera & composition** | Lens, angle, framing | Default: 24mm wide for scale, 50mm for intimate spaces. Low angle for awe, high angle for vulnerability |

## MJ-Specific Parameters

Default: `--ar 16:9 --style raw --s 200 --q 2 --v 6.1`

- Higher stylization (`--s 200–300`) for atmospheric/mood-driven locations
- `--s 50–100` for clean architectural reference shots
- `--ar 3:2` for vertical spaces (interiors, towers)

## Usage Notes
- **Lead with light.** The first atmospheric sentence is the most important. "Rain-streaked ruins bathed in cold blue emergency lights" sets the entire visual direction.
- **Depth sells scale.** Always include at least one foreground element (close) and one background vanishing point (far). Flat compositions fail.
- **Lived-in ≠ messy.** A few deliberate details (one bloodstain, one broken chair) do more work than "cluttered with debris."
- **The world-view IS your reference.** Don't invent new colors or materials — pull from the world DNA. If the world has no warm light, no location should have warm light (unless it's a deliberate story beat).
