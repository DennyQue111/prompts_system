
## Description
Use this architecture when the user wants to design **a sentient, non-humanoid entity** — a being with agency or narrative presence that does not follow a human body plan. This includes AI manifestations, alien consciousnesses, elemental beings, abstract sentient constructs, and creatures whose form is central to their identity. The default deliverable is one adaptable 16:9 multi-panel concept sheet: a design master for communicating identity, important forms, structure, and behavior. It is not automatically the best direct input image for a video model.

**Not for**: humanoid characters with clothes and limbs → use `character`.  
**Not for**: inert objects without consciousness → use `prop`.

## What the Image Must Include

Choose only the panels that materially help explain this entity. Do not force every entity into the same panel recipe:

| Panel Area | Content | Detail Level |
|------------|---------|--------------|
| **Primary form(s)** | The form or forms most important to the story | Give the main story form enough area to read its full silhouette, materials, scale, and sentience cues. A transforming entity may need two co-primary forms rather than one tiny secondary variant. |
| **View variations** | Additional angles when 3D structure is hard to infer from one view | Front/side/back/top as useful; omit redundant views when the entity is a clear abstract silhouette. |
| **Structure details** | Core, surface, internal mechanism, signature effect, or scale cue | Select details that explain identity or continuity; omit decorative close-ups that do not help recognition. |
| **Form / state changes** | Story-relevant alternate morphologies and/or visible emotional states | Show form changes when the body actually changes. Show emotion states only when light, motion, or silhouette visibly changes; neither row is mandatory. |

## Prompt Content Formula

For the main visual description, structure the text as:

[Subject / Entity type] + [Story-relevant form(s)] + [Physical structure & shared identity markers] + [Materials & textures] + [Scale] + [Visible sentience / behavior] + [Only useful views/details/states] + [Style]

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
| **Style** | Rendering approach | Preserve the user's or project's supplied style; otherwise infer it from the reference or requested medium. Use an available style profile only when one is relevant. |

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
- A supported renderer handles geometric precision well (spheres, crystals, floating structures) — lean into precise form descriptions.
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
- **Humanoid leakage**: If the intended design requires stable human anatomy, a human face, or ordinary clothing, route to `character`. Temporary fluid appendages or a roughly upright monster silhouette do not by themselves make an entity humanoid.
- **Form variations and emotion states are distinct**: forms change the entity's physical configuration; emotions keep the form and change visible signals such as light, movement, or pulse. Include only the categories that matter for this entity.

## Image Structure
For adaptable **layout options and panel priorities** on the default 16:9 design sheet, see:
→ **`general_layout_instruction.md`** in this directory

That file offers layout patterns for fixed-form, multi-form/transforming, and swarm/abstract entities. Choose the pattern that gives the important forms and shared identity cues enough space; its panel proportions are guidance, not a mandatory grid.

## From design sheet to video references

- Treat the full concept sheet as the entity's **design master**. It locks identity, form logic, materials, and shared details.
- For a video shot, select or create a clean **single-view reference** showing the specific form and approximate framing that should appear in that shot. If the video tool supports multiple references, the concept sheet may accompany it as a secondary design reference; do not make the video model guess which panel to use.
- Do not use the multi-panel sheet as a literal first frame unless the user wants the sheet itself animated. Keep labels, diagrams, and unrelated form panels out of a shot-specific anchor.
- For a transformation shot, identify the starting and ending forms and the invariant that connects them (core, markings, material pattern). Use storyboard/keyframes to define intermediate beats; only generate separate transition references when the requested workflow needs them.

Workflow: use this file to decide **what** must be designed → use `general_layout_instruction.md` to choose **how** to arrange it → compile a clean renderer-specific prompt. When video is later requested, use the design sheet as the source of truth and bind only the shot-relevant reference(s).


