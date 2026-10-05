# ai_image_video_generator · Flux.2 Klein → MiniMax H3 integration

Use this reference only when the target is `D:\files\code\ai_image_video_generator` and the user has selected Flux.2 Klein for images and MiniMax H3 for video. It maps `prompt-execution` onto the application's real capabilities as of 2026-10-05.

## What the application can do now

| Production need | Application capability | Practical constraint |
|---|---|---|
| Persist concepts and a shot list | `POST /api/shot_breakdowns/save` or the Project Management UI | Stores a concepts file and a shot-breakdown file linked by `project_id`. |
| Generate a Flux key image | `POST /api/text-to-image`, `model: "comfyui-flux2"` | Flux dimensions must be multiples of 16; use the returned `/static/projects/...` URL as the asset path. |
| Refine an existing asset with Flux | `POST /api/image-to-image`, `model: "comfyui-flux-kontext"`; use inpaint where a local correction is needed | Preserve the core identity and topology in the edit prompt; do not use a multi-view sheet as a single-shot composition reference. |
| Produce a MiniMax H3 video | `POST /api/image-to-video`, `model: "comfyui-minimax"` | Requires 1–9 `reference_images`; default is 8 s at 1344×768 when duration and size are omitted. |
| Derive a per-shot MiniMax prompt | `POST /api/shot-video-prompt` | Requires an existing `project_id`, `shot_id`, and the selected reference-image URLs. |
| Work on a shot in isolation | Project Management → open shot canvas | The canvas is a useful per-shot workspace; it is not a batch runner. |

The application copies generated outputs into `outputs/_temp/generator_outputs/` and serves them as `/static/projects/...`. Never replace these paths with guessed local paths when writing JSON.

## Required production order

1. **Prepare JSON, do not render yet.** Use `script-shot-breakdown` to create the paired `*_concepts.json` and `*_shot_breakdown.json` with schema version 2. Save or import them into the application, keeping a shared `project_id` and a valid `concepts_file` reference.
2. **Obtain user approval of the shot table.** Check scene coverage, duration, continuity, and whether the required shot count is acceptable. Do not start Flux or MiniMax work before this approval.
3. **Create reusable anchors.** Generate a production-ready single-character identity anchor for every recurring/speaking character, a location anchor for every recurring location, and a prop anchor when a prop has continuity significance. Write their real application URLs into the matching `reference_images` lists in concepts JSON.
4. **Approve anchors when identity or art direction is important.** This is recommended before generating many dependent frames.
5. **Generate and inspect each keyframe.** Use Flux with the relevant identity/location anchors. Each output must satisfy the shot's camera, visible action start state, identity, lighting, and space before it can be used for video.
6. **Immediately record approved assets.** Add the accepted keyframe URL to that shot's `reference_images`; do not wait until the end of a batch. A separate `production` object may be retained on a shot for status metadata because the current persistence route preserves unknown shot fields.
7. **Generate video per shot.** Build the MiniMax H3 prompt from the selected shot JSON using `shot/minimax.md`. Bind the character identity anchor and the approved current-shot keyframe first. Add only necessary extra anchors, maximum nine total.
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
- A multi-view character sheet is an approval artifact, not the preferred composition authority for a keyframe. Generate or select a separate single-character identity anchor for shots.
- Use the shot keyframe as the composition anchor and the character image as the identity anchor. Explain the role of every supplied reference image in the prompt when ambiguity would cause drift.

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
