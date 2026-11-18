# MiniMax H3 — execution adapter

This file records **execution and input-binding behavior** for MiniMax H3. It does not define prompt sections, wording, action timing prose, dialogue syntax, or negative-constraint style. For those, use `prompts_structure/shot/minimax.md` or `prompts_structure/sequence/minimax.md` according to shot form.

## Workflow selection

- Use the full int8 H3 model variant by default. Do not switch to pruned to save time or memory without explaining the reason and getting user approval.
- Use the standard Ref2VA workflow for ordinary multi-reference generation.
- If the user selects Pika H3 Flex Ref2VA, use the dedicated Pika Ref2VA graph with its Pika LoRA. Do not substitute standard Ref2VA or pass the legacy `int8` alias for this request.
- Ref2VA images are visual guidance, not hard frame locks. Pika H3 Flex Ref2VA is multi-reference only; it does not accept first- or last-frame lock fields.
- First-frame + references may use Ref2VA + AddGuide when a hard opening anchor is requested. Native first-and-last locking is a separate FL2VA mode without ordinary reference images. Do not combine native tail-frame locking with references.

## Reference binding

- Confirm the app's actual reference array and ordering before submission. In storyboard-led mode, put the **merged complete storyboard first**, followed by character/entity/prop design concepts, with the sole location concept last. Do not send separate storyboard panels as separate videos or as a substitute for the merged board unless the user explicitly chooses that input strategy.
- In keyframe-led mode, place the approved keyframe first, followed by design concepts. Avoid submitting multiple inconsistent full-color frames that compete for composition or background authority.
- **Plate-opening exception:** When a specific live-action plate must be the opening image and the user still chooses Pika Ref2VA, order references as **plate opening frame → merged storyboard → character/entity/prop concepts → sole location concept**. This overrides storyboard-first because the plate defines the actual opening composition. Reorder `@图片N` labels to match. Plate-first is still only a visual priority, never a hard first-frame lock.
- Pika may reproduce a multi-view character sheet or storyboard layout as an opening frame even when the prompt labels it “design only” or “motion only.” Role wording does not neutralize strong image content. If that happens, verify the actual uploaded images/order, then change reference priority or curate a less layout-heavy design reference; do not rely on adding more negative prose.
- Transparent foreground objects follow their depicted overlap: if the face sits behind a clear orb/glass, the model may show or refract it inside. Specify screen-space placement, relative size and a visible gap in both the storyboard and prompt; a negative line alone does not fix overlapping composition.
- If the actual plate must be frame 0, use the supported Ref2VA + AddGuide first-frame path instead of Pika. Do not promise that prompt wording or plate-first ordering guarantees an exact opening under Pika.
- Assign prompt labels to the actual ordered images; the exact MiniMax prompt text and label syntax are defined by Prompt Structure and the selected application's transport layer.
- The storyboard supplies layout, action order and camera path; concept images supply identity/design and environment. Do not copy storyboard sheet layout, gutters, arrows or line-art rendering into the video.

## Storyboard reference resolution (local Ref2VA app)

- Keep the individual storyboard panels and full-resolution merged board as the project masters. Before sending a merged board to the local MiniMax Ref2VA/Pika Ref2VA workflow, make a separate, aspect-preserving **conditioning copy** at a practical lower resolution. Do not crop panels, stretch the board, change the grid, or overwrite the full-resolution master.
- In the current `ai_image_video_generator` Pika graph, `MiniMaxH3ReferenceToVideo` uses `ref_image_size: "max"` with a 2048 px short-edge ceiling. Images whose short edge is below that ceiling are kept at their supplied dimensions. A very wide 5052×1900 contact sheet therefore remains about 9.6 MP and can add substantial reference-latent and VRAM load.
- TIDE_0010 provided a useful controlled comparison: the 5052×1900 five-panel board with four total references, 12 s at 1344×768, failed with CUDA OOM; the same board downsampled proportionally to 2352×885 (about 2.1 MP) succeeded with the same prompt, reference count and video settings. This is evidence that storyboard pixel dimensions can affect VRAM demand, not a universal guarantee for other shots or hardware.
- Use a separate, aspect-preserving storyboard conditioning copy whose **longest edge is no larger than 1920 px**; for a landscape board this means width 1920 px (height scales proportionally). Treat 1920 px as the maximum, not a target to exceed for short-edge reasons. Preserve every panel, the grid, and panel readability; never crop or stretch. If linework/effects become unreadable at this cap, simplify or recompose the storyboard panels before merging rather than sending a larger sheet. JPEG quality around 82–88 is a reasonable size reduction when it preserves line clarity.
- Save the conditioning copy as a distinct versioned asset under the app's canonical cache tree (for example, a filename containing `_conditioning_1920w`), keep the project master unchanged, and put the conditioning copy in the storyboard's usual first-reference position unless the plate-opening exception above applies. Record both paths, the conditioning dimensions, file size and hash in the shot log/request. Verify the uploaded ComfyUI input dimensions/hash and the actual ordered `LoadImage` references before relying on the run.

## App execution: `ai_image_video_generator`

When using `D:\files\code\ai_image_video_generator`, also read [the application integration note](../ai-image-video-generator.md) for the current API schema and cache paths. Key operational constraints:

- Endpoint: `POST /api/image-to-video`, `model: "comfyui-minimax"`.
- Standard multi-reference request: ordered `reference_images`, `workflow_type: "int8"` for standard full-int8 Ref2VA. Dedicated Pika request: `workflow_type: "pika_ref2va"`.
- Verify every requested reference file exists and its URL resolves before submission. Application defaults and additional request constraints are listed in the integration note.
- Call `GET /api/status` before rendering and require `comfyui_connected=true`.
- Save the exact request JSON, prompt text, reference order, workflow type, dimensions, duration and returned/ComfyUI task ID in the shot record.
- Monitor the submitted task to a terminal state through the API/ComfyUI queue or logs. A delayed HTTP response alone is not evidence of failure; do not resubmit while the same prompt ID is still running.
- For a plate-opening Pika run, visually inspect the generated frame 0 and the water/plate transition. Record whether the video actually begins on the plate; successful rendering alone does not mean the opening was followed.
- App-generated videos are stored under `caches/generation/exports/image_to_video/`. Preserve the returned application URL, copy the file into the project shot folder, verify the copy, then update the shot record.

The application may have additional workflow options or limits after an update. Check its current schema/code and the referenced integration note instead of assuming this adapter is timeless.
