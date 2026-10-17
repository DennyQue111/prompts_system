# ai_image_video_generator · image generation → MiniMax H3 integration

Use this reference only when the target is `D:\files\code\ai_image_video_generator` and the user has selected Flux.2 Klein or Codex-direct GPT image generation for images, and MiniMax H3 for video. It maps `prompt-execution` onto the application's real capabilities as of 2026-10-17.

## What the application can do now

| Production need | Application capability | Practical constraint |
|---|---|---|
| Persist concepts and a shot list | `POST /api/shot_breakdowns/save` or the Project Management UI | Stores a concepts file and a shot-breakdown file linked by `project_id`. |
| Generate a Flux key image | `POST /api/text-to-image`, `model: "comfyui-flux2"` | Flux dimensions must be multiples of 16; use the returned `/static/projects/...` URL as the asset path. |
| Refine an existing asset with Flux | `POST /api/image-to-image`, `model: "comfyui-flux-kontext"`; use inpaint where a local correction is needed | Preserve the core identity and topology in the edit prompt; do not use a multi-view sheet as a single-shot composition reference. |
| Prepare a MiniMax H3 keyframe | Generate one complete, camera-matched cinematic frame with the selected project renderer | **Do not use a crop from a storyboard/contact sheet as the final keyframe.** Use a native, clean 16:9 image at least 1536×864 pixels (prefer 1920×1080 or the highest clean 16:9 output supported). It must be at least as large as the submitted video dimensions; never send a tiny crop and rely on H3 to upscale it. |
| Generate a Flux character concept image | Free Canvas → Image-to-Image → Skill → Concept Image; select exactly one character source image, optionally enter extra constraints, then click “生成角色概念图” | This is an application-native end-to-end workflow. Let the UI run its ordered Flux front view, Flux back view, direct headless-body crop, SeedVR2 2× face source, and final combined concept sheet; it also preserves the intermediate assets on the canvas. Do not manually reproduce these steps with separate API calls or hand-built crops/composites when this workflow is available. Use the final combined sheet for MiniMax, not for Flux keyframe composition. |
| Produce a MiniMax H3 video | `POST /api/image-to-video`, `model: "comfyui-minimax"` | Requires 1–9 `reference_images`; default is 8 s at 1344×768 when duration and size are omitted. **Width and height must each be divisible by 32** (for example, 1280×704 or 1344×768); 1280×720 will fail at the MiniMax conditioning node. |
| Derive a per-shot MiniMax prompt | `POST /api/shot-video-prompt` | Requires an existing `project_id`, `shot_id`, and the selected reference-image URLs. |
| Work on a shot in isolation | Project Management → open shot canvas | The canvas is a useful per-shot workspace; it is not a batch runner. |

The application copies generated outputs into `outputs/_temp/generator_outputs/` and serves them as `/static/projects/...`. Never replace these paths with guessed local paths when writing JSON.

## GPT direct-image asset handoff

When the user selects GPT as the **project-wide primary image renderer**, Codex calls the image-generation capability directly rather than the app's Flux generation endpoints. MiniMax remains unchanged. GPT output is not a transient chat illustration: it must be made a first-class application asset before it is used as an anchor, keyframe, or video reference.

### Renderer consistency

- Use the selected primary renderer consistently for all newly generated project anchors, camera plates, action plates, and approved keyframes. Do not mix Flux and GPT output as peer production assets within one project merely for convenience; their rendering signatures can break continuity.
- Flux inpainting is allowed only as an explicitly recorded local repair of an approved GPT image. It is not permission to use Flux for unrelated full-frame assets.
- Preserve already approved legacy assets unless the user asks to replace them. If the project switches primary renderer partway through, explain that affected anchors and dependent keyframes need regeneration to regain a coherent look.

### Character concept images for MiniMax

For every recurring or speaking character, create and approve one MiniMax-facing character concept image before submitting that character's first video shot. A concept image supplements the current-shot keyframe: the keyframe controls composition and action, while the concept image preserves identity, wardrobe, front/back silhouette, and face detail when a shot moves close to the actor.

- **Flux primary renderer:** use the application's Concept Image workflow from a selected character source. In Free Canvas, select exactly one source image, open Image-to-Image → Skill → Concept Image, enter concise extra constraints only where needed, and click “生成角色概念图”. Let the application run the complete workflow: Flux front view, Flux back view, local face detection and direct headless-body crop from the front image, SeedVR2 2× face source, and final combined concept sheet. Intermediate assets and the sheet remain on the canvas. Do not substitute manually orchestrated endpoint calls or hand-built crops/composites; do not ask Flux to regenerate a headless body. If several characters are requested, run the tab once per character with that character's single source image selected.
- **GPT primary renderer:** generate the character concept image directly with GPT and persist it as an application asset using the GPT handoff rules below. Do not route the asset through the Flux Concept Image workflow merely to match its layout.
- **MiniMax binding:** every shot containing one or more principal characters must include the approved current-shot keyframe plus the corresponding character concept image for each such character. A character-free shot needs only its current-shot keyframe unless another reference is materially necessary. Stay within the backend maximum of nine references.
- Describe the roles in the MiniMax prompt when necessary: the keyframe is the opening-frame composition, and the concept image is the character-detail authority. Do not request the concept-sheet layout itself to appear in the video.

### Required local persistence

Save GPT-generated raster output under the same application-owned directories used by Flux, never only in the chat or an external temporary location:

| Asset kind | Local directory | Public URL prefix | Filename prefix |
|---|---|---|---|
| Text-derived anchor or keyframe | `D:\files\code\ai_image_video_generator\outputs\_temp\generator_outputs\text_to_image\` | `/static/projects/_temp/generator_outputs/text_to_image/` | `gpt_txt2img_` |
| Reference-guided edit, camera plate, action plate, or composite | `D:\files\code\ai_image_video_generator\outputs\_temp\generator_outputs\image_to_image\` | `/static/projects/_temp/generator_outputs/image_to_image/` | `gpt_img2img_` |

- Use a collision-safe filename ending in a short unique identifier and preserve the generated file extension.
- Verify the file exists locally, then construct the `/static/projects/...` URL from its path relative to `outputs/`. Do not invent a URL before the file is present.
- The file is discoverable by the existing frontend because FastAPI mounts `outputs/` at `/static/projects/`; no separate frontend path, upload directory, or remote URL is required.
- If the direct image-generation tool cannot provide a writable local artifact, stop before recording a fake path. Use a supported artifact export/ingest step first, then verify the saved bytes. Do not silently fall back to a remote URL.

### JSON records

Keep the existing `reference_images`, `keyframe_url`, and `video_url` paths exactly as application URLs. Record renderer provenance alongside them so a later run can reproduce the project without guessing:

```json
{
  "production": {
    "image_renderer": "gpt-image",
    "generation_method": "text_to_image",
    "prompt": "actual submitted image prompt",
    "reference_images": ["/static/projects/_temp/generator_outputs/text_to_image/gpt_txt2img_xxxxxxxx.png"],
    "keyframe_url": "/static/projects/_temp/generator_outputs/image_to_image/gpt_img2img_xxxxxxxx.png"
  }
}
```

For a three-stage fallback, retain `camera_plate_url`, `action_plate_urls`, and `keyframe_method` as already specified below, and set `image_renderer` to `gpt-image`. Pass the approved local `/static/projects/...` URLs to MiniMax in exactly the same way as Flux URLs.

## Required production order

1. **Prepare JSON, do not render yet.** Use `script-shot-breakdown` to create the paired `*_concepts.json` and `*_shot_breakdown.json` with schema version 2. Save or import them into the application, keeping a shared `project_id` and a valid `concepts_file` reference.
2. **Obtain user approval of the shot table.** Check scene coverage, duration, continuity, and whether the required shot count is acceptable. Do not start Flux or MiniMax work before this approval.
3. **Create reusable anchors and character concepts.** Generate a production-ready single-character identity anchor and a MiniMax character concept image for every recurring/speaking character, a location anchor for every recurring location, and a prop anchor when a prop has continuity significance. Write their real application URLs into the matching `reference_images` lists in concepts JSON.
4. **Approve anchors when identity or art direction is important.** This is recommended before generating many dependent frames.
5. **Generate and inspect each keyframe.** Use Flux with the relevant identity/location anchors. Each output must satisfy the shot's camera, visible action start state, identity, lighting, and space before it can be used for video.
6. **Immediately record approved assets.** Add the accepted keyframe URL to that shot's `reference_images`; do not wait until the end of a batch. A separate `production` object may be retained on a shot for status metadata because the current persistence route preserves unknown shot fields.
7. **Generate video per shot.** Build the MiniMax H3 prompt from the selected shot JSON using `shot/minimax.md`. For any character shot, bind the approved current-shot keyframe and every on-screen principal character's approved concept image. Add only necessary extra anchors, maximum nine total.
8. **Record results and exceptions.** Store the final video URL in the shot's `production.video_url` (or an equivalent agreed project status record) and mark the state. Record failures as `blocked` with the reason; do not silently skip them.

Suggested status payload, kept alongside the canonical shot fields:

```json
{
  "production": {
    "status": "keyframe_ready",
    "keyframe_url": "/static/projects/_temp/generator_outputs/text_to_image/example.png",
    "video_url": "",
    "attempts": 1,
    "note": "identity and 180-degree screen direction verified"
  }
}
```

Valid progression remains: `pending → breakdown_confirmed → anchors_ready → keyframe_ready → video_submitted → video_done`. Use `blocked(原因)` for a failed dependency.

## Prompt and reference binding

- For Flux, read `prompts_structure/adapters/flux-image.md` with the relevant concept/frame/keyframe core. Repeat visible identity traits, exact shot geometry, foreground/midground/background, material cues, and lighting instead of relying on style shorthand.
- For MiniMax, read `prompts_structure/shot/minimax.md` for a continuous shot or `prompts_structure/sequence/minimax.md` when the requested result contains cuts. The selected model is a renderer override; do not use Seedance-specific syntax.
- A multi-view character concept sheet is not the preferred composition authority for a Flux keyframe. Generate or select a separate single-character identity anchor for Flux shots; use the concept sheet as a MiniMax character-detail reference instead.
- For MiniMax character shots, use the current shot keyframe as the composition anchor and the character concept image as the identity/detail anchor. Explain the role of every supplied reference image in the prompt when ambiguity would cause drift.

## MiniMax H3 dialogue and motion

For a shot with spoken dialogue, put the exact dialogue text **once only** in a dedicated `对白` section. Include the speaker, an approximate start/end time window, delivery, and lip-sync instruction. In the action description, refer to “the shot's only line” rather than repeating its words; in the sound-design section, describe ambience and effects without quoting the dialogue again. This avoids duplicating/competing text conditioning and worked in the `FWW_0010` v003 controlled retest, where the line became correct. This is a verified prompt practice, not a guarantee that every H3 generation will speak perfectly.

For background motion, make the intended motion hierarchy explicit. Separate continuous wind-driven motion (hair, grass, loose fabric, clouds) from elements that should stay still or move only slightly. State positive, observable bounds where practical—for example, “the coaster track remains empty throughout, with no train/cars/passengers” or “the Ferris wheel rotates no more than about 3° over five seconds in a light breeze.” Avoid relying on vague adverbs such as “slowly” alone. Check for contradictions across action, camera, and sound sections before submission.

## Three-stage keyframe fallback for difficult shots

Use this fallback only after a direct keyframe attempt from a location anchor and character anchor fails visual QC for an important constraint: target camera/viewpoint, spatial topology, character pose, identity, or left/right anatomy. It is particularly useful for a new angle derived from a wide location concept, a character who must perform a specific action, a multi-person interaction, or a prosthetic/weapon whose side cannot flip.

Do **not** make it the default for every simple transition shot. If a direct keyframe is already consistent, keep the simpler route.

### 1. Camera plate

Starting from the location anchor, make an **environment-only** image at the target shot's actual camera position, lens, height, view direction, and visible topology. This is not a generic alternate location view.

- Describe what is visible, what is occluded, and where the subject will stand.
- Request an empty plate: no people, creatures, or silhouettes.
- Preserve only the location's material, lighting, and structural authority; do not force the original overview's composition.
- If an unwanted person appears, first perform a dedicated removal edit on the plate before proceeding. Never composite a new actor over an accidental actor.

### 2. Character action plate

Starting from the single-character identity anchor, make an image that contains only the required actor in the target shot's pose, facing, framing, and action start state.

- Use a neutral/studio background so the actor remains unambiguous.
- State screen-side anatomy in visible terms, for example: `the character's anatomical LEFT prosthetic arm appears on the viewer's RIGHT; the viewer's LEFT arm is natural human skin`. Also state `exactly one mechanical arm and one human arm` when relevant.
- Keep camera, lighting, and environment out of this prompt except for what affects the pose. This image is the authority for identity, clothing, anatomy, and action—not location composition.

### 3. Final composite

Submit the camera plate and character action plate together to the multi-image edit workflow. State their roles explicitly and in order:

1. **Reference 1 / camera plate** is absolute authority for frame size, camera, road/room geometry, architectural perspective, background, and light direction.
2. **Reference 2 / character action plate** is absolute authority for actor identity, pose, wardrobe, and side-specific anatomy.
3. Specify the actor's screen placement and scale, then require matched contact shadow, wet reflection or other surface interaction.

The final output must be checked as a new keyframe, not accepted merely because the intermediate plates were correct. Common final-composite defects are the actor being too small, new bystanders, lost contact shadow, or a mirrored prosthetic.

### Retry and records

- Treat this as a **workflow change**, not permission to retry the same final prompt indefinitely. Each individual plate or final composite gets at most one prompt-corrected retry under the standard retry policy.
- Keep failed intermediate files for diagnosis, but only append an approved final composite to `shots[].reference_images`.
- Record accepted intermediates in the shot's `production` object so a later agent can reproduce or revise the frame:

```json
{
  "production": {
    "camera_plate_url": "/static/projects/...",
    "action_plate_urls": ["/static/projects/..."],
    "keyframe_method": "three_stage_composite",
    "keyframe_url": "/static/projects/..."
  }
}
```

- If the final composite remains wrong after its correction attempt, set the shot to `blocked(原因)` and preserve the successful plate URLs. A later pass may use inpainting or a different renderer without rebuilding the approved plates.

## Present limitation: no autonomous batch runner

The application currently offers independent generation endpoints, manual reference selection, and per-shot prompt generation. It does **not** yet provide an endpoint that automatically:

- accepts a novel and produces the paired breakdown JSON files;
- loops through all shots to submit Flux generations;
- performs visual quality control, retries, and approval gates;
- feeds approved images into MiniMax and writes video results back to every shot.

Therefore, an agent may perform this workflow in controlled, confirmed stages, but must not claim that pressing one control will finish an entire novel. A future orchestrator should implement the same stage order and status transitions in `prompt-execution/SKILL.md`, rather than bypassing them.

## Readiness check before rendering

Before the first media submission, call `GET /api/status`. Rendering requires the FastAPI service and its ComfyUI connection to be available. If either is unavailable, stop before submitting a batch; preserve the JSON plan and report the unavailable dependency.
