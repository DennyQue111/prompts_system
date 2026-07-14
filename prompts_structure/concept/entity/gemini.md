
## Description
Use this architecture when the user wants to generate an image of **a sentient, non-humanoid entity** — a being that possesses consciousness, agency, or narrative presence but does not conform to the humanoid body plan. This includes AI manifestations, god-projections, alien consciousness, elemental beings, abstract sentient constructs, and any character whose "form" is inseparable from its identity. The generated image is always a multi-panel concept design sheet (16:9) that presents the entity's full visual range as a video production reference.

**Not for**: humanoid characters with clothes and limbs → use `character`.  
**Not for**: inert objects without consciousness → use `prop`.

## What the Image Must Include

This architecture defines **what content goes into each panel** of the entity concept image. The final image is a single 16:9 composite with the following panels:

| Panel Area | Content | Detail Level |
|------------|---------|--------------|
| **Main Visual** | The entity in its default/normal form, full presence | Richest description: form/shape, materials, scale, sentience indicators, behavior, lighting |
| **View Variations** | 2–3 different viewing angles of the default form | Each angle: what's newly visible that isn't seen from the front (side reveals thickness, top reveals radial symmetry, etc.) |
| **Detail Close-ups** | Close-ups of critical visual components (materials, internal structure, energy effects, scale reference) | Panel count drives grid layout — 2→side by side, 3→flexible, 4→2×2, 5+→AI decides |
| **Bottom Row** | Form variations (2–3) then emotion states (2–3), one horizontal row | Forms first (left), emotions second (right). Each ~1-2 sentences |

## Prompt Content Formula

For the main visual description, structure the text as:

[Subject / Entity type] + [Physical form & structure] + [Materials & textures] + [Scale & spatial presence] + [Sentience indicators] + [Behavior / agency] + [Environment / context] + [Style suffix]

### Content Components

| Component | Description | What to Cover |
|-----------|-------------|---------------|
| **Subject / Entity type** | What kind of conscious being this is | Entity name, type/role, narrative function (game-master, guardian, oracle, etc.) |
| **Physical form & structure** | Geometry, layers, internal vs external, how it's built | Overall shape, structural hierarchy (core → shell → surface), any embedded features (eyes, sensory organs), how components interact |
| **Materials & textures** | What it is made of, surface quality | Material names (obsidian, mirror-black, liquid mercury), optical properties (glossy, matte, translucent), surface details (edge light, micro-texture) |
| **Scale & spatial presence** | Size relative to known references | Numerical size, comparison object (fist-sized, human-scale), how it occupies space (hovering, floating, filling the horizon) |
| **Sentience indicators** | Visual cues of awareness/aliveness | Eyes (embedded, blinking), glow rhythms, reactive surfaces, any non-facial signal that says "this thing is alive" |
| **Behavior / agency** | What the entity is doing or capable of doing | Static behavior (staring, hovering, pulsing) or dynamic (rotating, blinking, form-shifting). Pick one clear primary behavior |
| **Environment / context** | Surrounding space | Void, altar, rift, chamber — minimal backgrounds preferred when the entity's form is the primary subject |
| **Style suffix** | Artistic style | From `../../reference.md` |

## Usage Notes
- Entities thrive on **material contrast** — interior vs exterior tension (magma inside obsidian, light inside shadow).
- **Sentience indicators are the make-or-break component.** Without them, the entity reads as a prop. An eye, a glow rhythm, a responsive surface — these separate a dead object from a living presence.
- **Personality-to-Visual for entities**: Non-humanoid beings also need their inner nature translated into visible cues:

| Entity Trait (don't write) | Visual Translation (write this instead) |
|---------------------------|----------------------------------------|
| Ancient / timeless | Surface shows geological layering, slow erosion patterns, movement at tectonic speed |
| Benevolent / protective | Warm light leaks from internal cracks, form curves around smaller beings like cupped hands |
| Cold / indifferent | Perfect geometric symmetry, zero surface imperfections, light reflects without absorption |
| Hungry / predatory | Surfaces ripple toward the viewer, edges sharpen when facing living things, ambient light dims around its perimeter |
| Broken / mourning | Chunks missing from its form, internal light flickers irregularly, asymmetrical posture, fragments orbit slowly |
- Gemini handles geometric precision well (spheres, crystals, floating structures) — lean into precise form descriptions.
- Scale anchors matter enormously for non-human forms. Without a body to reference, the viewer needs to know whether this thing is palm-sized or building-sized.
- Behavior/agency can be static (staring, hovering) or dynamic (pulsing, rotating, blinking).
- Use minimal or void backgrounds when the entity's form is the primary subject.

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Entity identity** | 1.0 | Is the entity type and narrative role immediately identifiable? |
| **Form distinctiveness** | 1.0 | Is the physical form unique, memorable, and well-structured in description? |
| **Material/texture specificity** | 1.2 | Does the prompt specify materials, surfaces, and optical qualities that guide rendering? |
| **Sentience communication** | 1.2 | Can the viewer perceive consciousness/awareness/aliveness from the visual description? |
| **Narrative presence** | 0.6 | Does the entity suggest a story role — guardian, judge, oracle, observer, gatekeeper? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: The entity feels alive, visually striking, and narratively charged.
- 7–8: Strong visual identity but sentience or narrative role could be sharper.
- 5–6: Core concept exists but reads more like a prop than a conscious being.
- 1–4: Ambiguous — viewer won't know they're looking at a sentient entity.

## Common Issues & Adjustments
- **Entity confused with prop**: If the prompt describes only materials and form but gives no signal of consciousness → it's a prop. Add an eye, a glow, a movement, a reactive surface.
- **No scale anchor**: "floating in space" gives no size reference → add a measurement or comparison object.
- **Over-describing function**: "a being that controls the rules of the game" → describe what it looks like and how it behaves visually, not its metaphysical powers.
- **Humanoid leakage**: If the entity starts growing arms, legs, or clothing → switch to `character`.
- **Form variations and emotion states are distinct**: Forms = different physical configurations of the cubes/matter. Emotions = same form but different light color/arc tempo/glow intensity. Don't confuse them.

## Image Structure
For the **layout grid, panel positions, and 16:9 composition**, see:
→ **`concept-sheet/entity-sheet/general.md`**

That file defines:
- Exact panel positions (main visual top-left 1/3×4/5, view variations upper-right, details lower-right AI-flexible grid, bottom row full-width)
- How to write the full combined prompt with layout instructions + panel content
- Detailed example generation
- Sheet-specific scoring and common issues

The agent workflow is: read this file for **what** content to generate → read the corresponding sheet file for **how** to compose the image → combine both into the final prompt.
