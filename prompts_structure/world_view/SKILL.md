---
name: mokeaigc-worldbuilder
description: A MOKE-AIGC cinematic worldbuilding skill that builds a coherent imaginary world from a short idea, mood, culture, location, genre, name, or reference image, then reveals it through a connected set of nine static-image prompts covering inhabitants, animals, architecture, landscape, daily life, migration and transport, sound and culture, power and pressure, and an intimate portrait. Use for 电影感世界观构建、视觉开发、虚构文化探索、参考图世界延展、九张同属一部未拍电影的连贯静帧。Do not use for one-off image prompts, character sheets, screenplay shot lists, video motion prompts, or nine compositions of one locked scene.
---

# MOKE-AIGC Visual Worldbuilder

**Brand:** MOKE-AIGC

## Mission

Turn one creative spark into a believable world that feels lived in rather than designed, then reveal it through nine cinematic stills from the same unseen film. Make every frame show behavior, material use, spatial relationships, and a trace of what happened immediately before or after.

Keep world coherence as the core. Apply platform, lens, style, and bilingual adaptations only after the world is stable.

## Keep the boundary

Handle:

- Fictional-world visual development from text or a reference image.
- Nine connected stills that reveal different functions of one world.
- A user-requested subset of the nine aspects.
- Generic or platform-adapted static-image prompts.

Route elsewhere:

- One locked scene explored through nine camera compositions.
- Video motion, camera movement, timing, transitions, or clip continuation.
- Character sheets, turnaround views, or identity-lock packages.
- Screenplay breakdowns, shot lists, or continuity editing.
- A single ordinary image prompt with no world-expansion intent.

Do not silently absorb these neighboring tasks. Finish the worldbuilding portion only when it is independently useful, then state the appropriate downstream task.

## Apply instruction priority

Resolve conflicts in this order:

1. User's explicit content, format, platform, language, camera, and count requirements.
2. Selected platform syntax.
3. An explicitly selected cinematography or visual-style profile.
4. The world's continuity bible.
5. This skill's defaults.

Never let a default camera, lens, film stock, negative prompt, aspect ratio, or output language override the user or an explicitly selected style profile.

## Use defaults without interrogating the user

Start from one meaningful input. Do not ask an intake questionnaire.

Use these defaults when omitted:

```yaml
platform: generic
aspect_ratio: 16:9
aspect_count: 9
output_mode: compact
base_rendering: cinematic observational realism
capture_profile: adaptive
```

If the user gives no creative spark at all, ask one short question. Otherwise proceed and disclose important assumptions briefly at the top of the result.

Do not ask for Midjourney `--sref`, `--profile`, version, or HD settings. Use them only when supplied or explicitly requested.

## Load only the needed references

- Read [world-aspects.md](references/world-aspects.md) and [continuity-and-shot-planning.md](references/continuity-and-shot-planning.md) for every worldbuilding run.
- Read [camera-and-style-adaptation.md](references/camera-and-style-adaptation.md) when specifying lenses, camera placement, depth of field, human texture, or a style profile.
- Read [platform-renderers.md](references/platform-renderers.md) only when the user names a target generator or requests platform-ready syntax.
- Read [output-formats.md](references/output-formats.md) when the user requests Production mode, full bilingual output, separated camera/lighting fields, or a non-default deliverable.

## Run the workflow

### 1. Lock the creative intent

Extract the non-negotiable subject, mood, culture, geography, era, realism level, and user exclusions. For a reference image, infer visual evidence without copying it literally or replacing the user's premise.

### 2. Build the continuity bible

Create a compact internal continuity bible before writing prompts. Define climate, inhabitants, body covering, materials, architecture, tools, ecology, recurring symbols, palette, lighting logic, texture, and forbidden drift. Show a concise version to the user; keep operational details internal.

### 3. Plan the aspect matrix

Plan the requested aspects before drafting prose. Give each aspect one distinct narrative function, scene, action, scale, camera position, and emotional intensity. Reuse at least three continuity anchors in every frame.

### 4. Write platform-neutral scenes

For each frame, describe:

```text
subject and visible action
+ spatial relationship and foreground/midground/background
+ continuity anchors
+ camera position, subject distance, and focal-length intent
+ motivated light, weather, materials, and wear
+ a trace of before/after
```

Make the camera observe an event; never arrange a catalog display, character lineup, empty architectural render, poster, or generic concept-art tableau.

### 5. Apply capture and style choices

Choose camera language to serve the scene. Do not prepend a universal camera-brand string. Treat focal length together with camera position and subject distance; do not claim focal length alone determines perspective.

Apply detailed human-skin language only when a clearly visible human face is near enough for that detail to matter.

### 6. Render for the target platform

Keep scene semantics shared but render syntax separately for each platform. Do not copy Midjourney parameters or negative syntax into other generators.
Do not add platform documentation, parameter explanations, citations, or generator commentary unless the user asks for them.

### 7. Deliver in the requested mode

Use Compact mode by default: poetic world name, 2–3 sentence concept, concise continuity anchors, then one Chinese visual intention and one executable prompt per aspect. Use Production mode only on request.

### 8. Validate silently

Before answering, repair any failure:

- Correct task routing and requested aspect count.
- Distinct narrative purpose for every aspect.
- At least three recurring continuity anchors per frame.
- No unexplained drift in era, technology, species, clothing, materials, architecture, palette, or climate.
- No repeated primary scene or action.
- Purposeful variation in distance, height, framing, and intensity.
- Concrete visible action and spatial depth in every prompt.
- No contradictory camera or capture-medium claims.
- No human-skin detail when faces are absent, distant, hidden, or non-human.
- Correct platform syntax with no empty or invented parameters.
- User instructions override every default.

Do not print the validation checklist unless the user asks for an audit.
