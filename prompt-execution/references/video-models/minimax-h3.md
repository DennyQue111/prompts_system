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
- Assign prompt labels to the actual ordered images; the exact MiniMax prompt text and label syntax are defined by Prompt Structure and the selected application's transport layer.
- The storyboard supplies layout, action order and camera path; concept images supply identity/design and environment. Do not copy storyboard sheet layout, gutters, arrows or line-art rendering into the video.

## App execution: `ai_image_video_generator`

When using `D:\files\code\ai_image_video_generator`, also read [the application integration note](../ai-image-video-generator.md) for the current API schema and cache paths. Key operational constraints:

- Endpoint: `POST /api/image-to-video`, `model: "comfyui-minimax"`.
- Standard multi-reference request: ordered `reference_images`, `workflow_type: "int8"` for standard full-int8 Ref2VA. Dedicated Pika request: `workflow_type: "pika_ref2va"`.
- Verify every requested reference file exists and its URL resolves before submission. Application defaults and additional request constraints are listed in the integration note.
- Call `GET /api/status` before rendering and require `comfyui_connected=true`.
- Save the exact request JSON, prompt text, reference order, workflow type, dimensions, duration and returned/ComfyUI task ID in the shot record.
- Monitor the submitted task to a terminal state through the API/ComfyUI queue or logs. A delayed HTTP response alone is not evidence of failure; do not resubmit while the same prompt ID is still running.
- App-generated videos are stored under `caches/generation/exports/image_to_video/`. Preserve the returned application URL, copy the file into the project shot folder, verify the copy, then update the shot record.

The application may have additional workflow options or limits after an update. Check its current schema/code and the referenced integration note instead of assuming this adapter is timeless.
