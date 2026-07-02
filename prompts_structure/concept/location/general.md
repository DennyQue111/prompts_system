
## Description
Use this architecture when the user wants to generate an image focused on **a location or environment** — the setting where a story unfolds. This covers landscapes, interiors, cityscapes, fantasy realms, and atmospheric spaces. The structure prioritizes spatial composition, mood, and environmental storytelling.

## Prompt Structure Formula
[Location type] + [Geography & spatial layout] + [Architecture & structural elements] + [Time & weather conditions] + [Atmosphere & mood] + [Lighting & color palette] + [Detail accents] + [Style suffix]

### Formula Components

| Component                             | Description                                                  | Examples / Keywords                                                                                                   |
| ------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Location type**                     | The fundamental category of the space                        | "A misty mountain temple", "a neon-drenched cyberpunk street", "an overgrown Victorian greenhouse", "a desert oasis"  |
| **Geography & spatial layout**        | Scale, depth, terrain, spatial relationships                 | "nestled in a steep valley", "sprawling across three floating islands", "a narrow alley between towering buildings"   |
| **Architecture & structural elements** | Building style, materials, key structures                     | "weathered stone arches covered in ivy", "holographic billboards and chrome walkways", "vaulted glass ceiling"        |
| **Time & weather conditions**         | Time of day, season, weather                                 | "golden hour with long shadows", "midnight under a full moon", "fog rolling in from the sea", "autumn, crimson leaves" |
| **Atmosphere & mood**                 | Emotional quality of the space                               | "serene and sacred", "ominous and claustrophobic", "bustling with hidden danger", "lonely and abandoned"              |
| **Lighting & color palette**          | Dominant light sources and color temperature                 | "warm amber lanterns against cool blue twilight", "harsh neon pink and cyan", "soft diffused sunlight through canopy"  |
| **Detail accents**                    | Small environmental storytelling elements                    | "prayer flags fluttering in the wind", "steam vents hissing from grates", "overgrown vines cracking the stone floor"  |
| **Style suffix**                      | Artistic style, rendering quality                            | See `reference.md` for options (e.g., "cinematic wide shot", "matte painting, epic scale", "photorealistic landscape") |

## Usage Notes
- Locations benefit from a clear focal anchor — a building, a tree, a light source — around which the scene is composed.
- Atmospheric and lighting keywords are the strongest drivers of location quality. Invest more detail here than in object-level specifics.
- Time of day dramatically changes the feel; always specify it unless the user wants flexibility.
- For interiors, include a hint about the ceiling height and room scale to avoid cramped compositions.
- Avoid listing every object in the scene — use "detail accents" to sprinkle narrative flavor rather than cataloging inventory.

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Location identity** | 1.0 | Is the type of place immediately clear? The viewer should know where they are. |
| **Spatial composition** | 1.0 | Is there a sense of scale, depth, and spatial organization? |
| **Atmospheric quality** | 1.2 | Does the prompt convey a strong mood through lighting, weather, and color? |
| **Visual distinctiveness** | 1.0 | Does the location feel unique and memorable, not generic? |
| **Narrative potential** | 0.8 | Does the environment suggest stories that could happen there? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: A vivid, emotionally resonant location ready for production.
- 7–8: Strong atmosphere but could use one more spatial or lighting detail.
- 5–6: The setting is described but lacks atmosphere or distinctiveness.
- 1–4: Too vague to differentiate from a thousand similar places.

## Common Issues & Adjustments
- **No time/weather**: "a forest" → "an ancient pine forest at dawn, mist clinging to the forest floor, golden rays piercing the canopy".
- **Generic architecture**: "a castle" → "a crumbling Gothic castle, blackened stone, jagged spires silhouetted against a blood-red sunset".
- **Missing focal point**: Wide landscapes fade into generic blobs without a visual anchor; add a distinctive structure or light source.
- **Mood/lighting mismatch**: "haunted house, bright sunny day" → either commit to "bright, uncanny, too-perfect" or shift to "overcast, crepuscular rays through broken shutters".
- **List-like description**: Don't enumerate objects; integrate them into the spatial narrative.

## Image Structure
For the **layout grid, panel positions, and 16:9 composition**, see:
→ **`concept-sheet/location-sheet/general.md`**

That file defines:
- Exact panel positions (main visual top-left 1/3×4/5, alternate angle + top-down upper-right, mid-distance shots lower-right AI-flexible grid, bottom row detail close-ups + color palette)
- How to write the full combined prompt with layout instructions + panel content
- Detailed example generation
- Sheet-specific scoring and common issues

The agent workflow is: read this file for **what** content to generate → read the corresponding sheet file for **how** to compose the image → combine both into the final prompt.
