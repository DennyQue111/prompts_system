# ai_image_video_generator · image generation → MiniMax H3 integration

Use this reference only when the target is `D:\files\code\ai_image_video_generator` and the user has selected Flux.2 Klein or Codex-direct GPT image generation for images, and MiniMax H3 for video. It maps `prompt-execution` onto the application's real capabilities as of 2026-10-17.

## What the application can do now

| Production need | Application capability | Practical constraint |
|---|---|---|
| Persist concepts and a shot list | `POST /api/shot_breakdowns/save` or the Project Management UI | Stores a concepts file and a shot-breakdown file linked by `project_id`. |
| Generate a Flux key image | `POST /api/text-to-image`, `model: "comfyui-flux2"` | Flux dimensions must be multiples of 16; use the returned `/static/projects/...` URL as the asset path. |
| Refine an existing asset with Flux | `POST /api/image-to-image`, `model: "comfyui-flux-kontext"`; use inpaint where a local correction is needed | Preserve the core identity and topology in the edit prompt; do not use a multi-view sheet as a single-shot composition reference. |
| Prepare a MiniMax H3 keyframe | Generate one complete, camera-matched cinematic frame with the selected project renderer | **Do not use a crop from a storyboard/contact sheet as the final keyframe.** Use a native, clean 16:9 image at least 1536×864 pixels (prefer 1920×1080 or the highest clean 16:9 output supported). It must be at least as large as the submitted video dimensions; never send a tiny crop and rely on H3 to upscale it. |
| Generate a Flux character concept image | Free Canvas → Image-to-Image → Skill → Concept Image; select exactly one character source image, optionally enter extra constraints, then click “生成角色概念图” | This is an application-native end-to-end workflow. Let the UI run its ordered Flux front view on a seamless pure-white studio background, Flux back view on the same background, direct headless-body crop, SeedVR2 2× face source, and final combined concept sheet. The face-detail panel crops the upper half of the 2× image starting at its top edge (`y=0`), prioritizing complete hair and head over showing the torso. Intermediate assets remain on the canvas. Do not manually reproduce these steps with separate API calls or hand-built crops/composites when this workflow is available. Use the final combined sheet for MiniMax, not for Flux keyframe composition. |
| Produce a MiniMax H3 video | `POST /api/image-to-video`, `model: "comfyui-minimax"` | `first_frame_image` alone uses I2VA. `reference_images` alone use Ref2VA. When both are supplied, the backend places the keyframe first in the Ref2VA Picture sequence and separately connects the same image to official `MiniMaxH3AddGuide` at frame 0; this avoids the installed T8 node's disabled Hybrid path. The keyframe counts as Picture 1, so at most 8 additional references can be supplied (9 total Picture images). Either a first frame or 1–9 references is required. Default is 8 s at 1344×768 when duration and size are omitted. **Width and height must each be divisible by 32** (for example, 1280×704 or 1344×768); 1280×720 will fail at the MiniMax conditioning node. See the prompt-transport note below for text-conditioning fields. |
| Derive a per-shot MiniMax prompt | `POST /api/shot-video-prompt` | Requires an existing `project_id`, `shot_id`, and the selected reference-image URLs. |
| Work on a shot in isolation | Project Management → open shot canvas | The canvas is a useful per-shot workspace; it is not a batch runner. |

The application copies generated outputs into `outputs/_temp/generator_outputs/` and serves them as `/static/projects/...`. Never replace these paths with guessed local paths when writing JSON.

### MiniMax H3 prompt transport

- The H3 branch forwards the request's single `prompt` string to the workflow. It has no independent dialogue or `negative_prompt` channel; do not invent request fields or describe a text block as native negative conditioning.
- The backend translates project tags such as `@图片1` to MiniMax's native `<Picture 1>` tags. When `first_frame_image` and `reference_images` are both supplied, Picture 1 is the keyframe (also anchored at frame 0 by AddGuide); user references follow as Picture 2, Picture 3, etc. Author prompts and image-role labels using that numbering.
- Ref2VA references alone are not exact first-frame constraints. For shots that must begin on a generated keyframe, pass it through `first_frame_image` and keep character/style references in `reference_images`; the backend runs Ref2VA plus the official AddGuide node at frame index 0. The AddGuide keyframe is separate from the text-encoder Picture reference, which is why the backend also includes the keyframe as Picture 1.
- Prompt composition—including dialogue placement, positive/negative separation, and motion wording—belongs to `prompts_structure/shot/minimax.md` or `prompts_structure/sequence/minimax.md`, not this integration reference.
- Keep the exact submitted prompt in the production record when reproducibility matters. Record that any labeled negative section was part of the same text string.

## GPT direct-image asset handoff

When the user selects GPT as the **project-wide primary image renderer**, Codex calls the image-generation capability directly rather than the app's Flux generation endpoints. MiniMax remains unchanged. GPT output is not a transient chat illustration: it must be made a first-class application asset before it is used as an anchor, keyframe, or video reference.

### Renderer consistency

- Use the selected primary renderer consistently for all newly generated project anchors, camera plates, action plates, and approved keyframes. Do not mix Flux and GPT output as peer production assets within one project merely for convenience; their rendering signatures can break continuity.
- Flux inpainting is allowed only as an explicitly recorded local repair of an approved GPT image. It is not permission to use Flux for unrelated full-frame assets.
- Preserve already approved legacy assets unless the user asks to replace them. If the project switches primary renderer partway through, explain that affected anchors and dependent keyframes need regeneration to regain a coherent look.

### Character concept images for MiniMax

Renderer-specific application behavior for generating character concepts:

- **Flux primary renderer:** use the application's Concept Image workflow from a selected character source. In Free Canvas, select exactly one source image, open Image-to-Image → Skill → Concept Image, enter concise extra constraints only where needed, and click “生成角色概念图”. Let the application run the complete workflow: Flux front and back views on a seamless pure-white studio background with soft, even studio lighting; local face detection and direct headless-body crop from the front image; SeedVR2 2× face source; then the final combined concept sheet. The face-detail panel uses the upper half of the 2× source, cropped downward from its top edge so the head and hair remain complete; torso inclusion is secondary. Intermediate assets and the sheet remain on the canvas. Do not substitute manually orchestrated endpoint calls or hand-built crops/composites; do not ask Flux to regenerate a headless body. If several characters are requested, run the tab once per character with that character's single source image selected.
- **GPT primary renderer:** generate the character concept image directly with GPT and persist it as an application asset using the GPT handoff rules below. Do not route the asset through the Flux Concept Image workflow merely to match its layout.

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

## Project persistence contract

- Project endpoints expect the paired `*_concepts.json` and `*_shot_breakdown.json` in schema version 2, linked by a shared `project_id` and valid `concepts_file` reference.
- Use actual `/static/projects/...` URLs returned by the application in `reference_images`, `keyframe_url`, and `video_url`; keep the ordered `reference_images` list aligned with the order used for image labels in the selected prompt template.
- The current persistence route preserves unknown shot fields, so production state and real asset URLs may be stored under a per-shot `production` object. Overall stage progression is defined in `prompt-execution/SKILL.md`; this file only records the application's storage shape.

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
