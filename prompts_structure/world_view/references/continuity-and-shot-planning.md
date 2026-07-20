# Continuity and Shot Planning

## Build the continuity bible

Define these fields before drafting prompts:

```yaml
world_name:
geography:
climate:
era_and_technology:
inhabitant_traits:
body_covering:
signature_materials:
architecture_grammar:
tools_and_transport:
animal_ecology:
recurring_symbols:
color_palette:
lighting_logic:
weather_and_atmosphere:
surface_texture:
forbidden_drift:
```

Keep entries visual and generative. Prefer observable evidence over lore. For example, write `salt-whitened reed capes tied with oxidized copper` instead of `a culture that values endurance`.

Use `forbidden_drift` to prevent accidental changes such as unexplained neon technology, unrelated clothing silhouettes, new building materials, different species anatomy, or a conflicting climate.

## Analyze a reference image

Extract only visible or strongly supported evidence:

- Subject and body covering.
- Setting, terrain, architecture, and spatial scale.
- Dominant and accent colors.
- Light direction, softness, contrast, and time cues.
- Materials, wear, weather, and atmosphere.
- Implied labor, ritual, social relation, or ecology.

Distinguish observation from invention. Let the world grow from the evidence without copying the source composition or claiming unsupported cultural facts.

## Plan the shot matrix

Plan each frame with these fields:

```yaml
aspect:
narrative_question:
scene:
visible_action:
foreground:
midground:
background:
continuity_anchors:
camera_position:
subject_distance:
focal_length_intent:
light_and_weather:
emotional_intensity_1_to_5:
before_after_trace:
```

Require at least three `continuity_anchors` in every frame. Recur anchors naturally; do not paste the entire bible into every prompt.

## Control variation

Across a full nine-frame set:

- Include establishing, medium, close, and detail scales.
- Mix eye-level, low, high, overhead, obstructed, reflected, or framed viewpoints when narratively useful.
- Avoid using the same focal-length band more than three times unless the user requests a uniform visual system.
- Include at least two quiet frames and one high-pressure frame.
- Avoid repeating the same primary location, action, or compositional device.
- Preserve screen-world logic even while varying camera language.

## Preserve lived-in realism

Show use, consequence, and imperfect material reality:

- Worn cloth, repaired tools, soot, condensation, tracks, mud, salt, dust, scratches, smoke, breath, or weathering.
- Hands doing work, bodies carrying weight, paths made by repetition, and architecture altered by occupation.
- Practical or environmentally motivated light rather than decorative studio lighting unless the world calls for it.

Do not force grain, haze, mud, or decay into clean, stylized, animated, or ceremonial worlds when those traits contradict the premise.

