# Camera and Style Adaptation

## Use a replaceable capture profile

Represent camera language as a profile instead of a fixed brand string:

```yaml
camera_position:
camera_height:
subject_distance:
focal_length:
aperture_or_depth_of_field_intent:
lens_character:
capture_medium_or_emulation:
framing_device:
motion_trace_in_still:
```

Let an explicit user or cinematography profile replace any of these fields.

## Keep photographic causality accurate

- Treat perspective as primarily determined by camera position and subject distance.
- Treat focal length as controlling field of view; when framing is held constant, changing focal length usually implies moving the camera, which changes perspective.
- Treat depth of field as a combined result of aperture, focus distance, focal length, sensor/format, and output conditions.
- Describe only the variables that materially help the image generator.

Prefer phrases such as:

```text
camera close to the worker at waist height, 24mm field of view preserving the machinery around them
camera held far across the valley, 135mm compression stacking travelers against the storm front
eye-level intimate close-up, 85mm portrait field of view, shallow focus held on the listener's reaction
```

## Choose rather than standardize

Use an adaptive default:

- Broad geography or architecture: consider 18–35mm with a clearly stated camera position.
- Observational daily life: consider 35–50mm.
- Intimate reaction: consider 65–100mm.
- Distant layered scale: consider 100–200mm.

These are starting ranges, not aspect-to-lens mandates. Override them when the scene or user requires a different relationship.

Do not combine a digital camera with literal analog film capture. If a digital acquisition look with film response is desired, describe `analog film emulation`, `film-print color response`, or another explicit emulation rather than `analog film stock`.

## Apply style as an override layer

Translate a requested visual direction into concrete properties:

- Composition and subject density.
- Camera proximity and lens behavior.
- Light source, direction, softness, contrast, and color temperature.
- Palette and saturation.
- Material rendering and atmospheric density.
- Capture texture and highlight response.

Avoid imitating a living creator or studio by name. Describe the requested visual traits. If another approved cinematography skill is explicitly active, accept its concrete camera and lighting profile without retaining incompatible defaults from this skill.

## Add human texture conditionally

Use concise natural-skin language only when a human face is clearly visible in a near shot:

```text
natural human skin texture, visible pores and subtle imperfections, soft facial peach fuzz catching the motivated light
```

Skip it for distant people, backs, silhouettes, masks, hidden faces, non-human beings, stylized animation, or shots where the face cannot resolve that detail.

