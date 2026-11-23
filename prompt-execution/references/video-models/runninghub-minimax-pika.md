# MiniMax H3 Pika Ref2VA through RunningHub

This adapter records transport and runtime behavior for the `ai_image_video_generator` RunningHub integration. Prompt wording remains in `prompts_structure/shot/minimax.md` or `prompts_structure/sequence/minimax.md`.

## Endpoint and configuration

- Use the RunningHub **AI App** endpoint: `POST https://www.runninghub.cn/openapi/v2/run/ai-app/{app_id}`.
- Do not substitute `/run/workflow/{workflow_id}` for this integration. RunningHub may publish either API type; follow the endpoint shown by the current published API export.
- The backend app ID is configured as `RUNNINGHUB_PIKA_APP_ID` in `backend/.env`. Keep API keys and webhook tokens private; do not copy them into project prompts or logs.
- The local route is `POST /api/runninghub/minimax-pika`. It accepts `prompt`, `reference_images`, `width`, `height`, `duration`, and `fps`; references are uploaded to RunningHub before task submission.
- Include the configured `webhookUrl`; poll `GET /api/runninghub/tasks/{task_id}` until terminal status. On success this route downloads/caches returned video files under `caches/generation/exports/image_to_video/runninghub/`.

## Verified node mapping

The current published 9-reference AI App API export maps:

| Input | Node ID | Field | Submitted value |
|---|---:|---|---|
| Prompt | `10` | `prompt` | Exact rendered prompt string |
| Duration | `8` | `value` | Requested seconds as a string |
| FPS | `19` | `value` | Requested frame rate as a string |
| Reference images 1–9 | `20, 22, 24, 26, 28, 30, 32, 34, 36` | `image` | Uploaded RunningHub file name, or `None` for unused slots |

The request body uses `nodeInfoList`, `instanceType: "default"`, `usePersonalQueue: "false"`, and the webhook URL. Compare these IDs and fields with the latest published API export after republishing; do not assume that a new app/workflow preserves old node IDs. In particular, distinguish AI App and workflow endpoints.

## Duration and output verification

- The duration widget feeds the graph's frame-length expression; output length is aligned to valid MiniMax H3 frame groups. A 4-second request at 24fps was observed to produce 107 frames, or 4.4583 seconds, at 24fps. Treat this as frame alignment, not as a 15-second request.
- Always use `ffprobe` on the downloaded result to verify actual duration, frame rate, frame count, dimensions, and audio stream. Never infer correctness from the submitted values or task `SUCCESS` alone.
- A previous request to a stale/different published endpoint returned 124 frames at 8fps (15.5 seconds). If that output recurs, inspect the current app ID, endpoint type, and node mapping before another render; do not describe the duration as correctly applied.
- Save the task ID, app ID, prompt, reference order, submitted duration/FPS, actual media metadata, and webhook-cached path in the shot record. Copy the video into the project's `sequence/video/{SHOT_ID}/` directory and verify the copied file.

## Restart behavior

After changing the backend implementation or `backend/.env` app ID, restart the backend so its loaded code/config matches the published API. Direct calls to RunningHub can be used for diagnosis, but production submissions should use the local route so its webhook and output caching behavior remain consistent.
