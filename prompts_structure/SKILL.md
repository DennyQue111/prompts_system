---
name: prompts-structure
description: Route natural-language image and video creation requests to the correct local prompt architecture, bind attached references, and execute generation when a compatible renderer is available. Use for concept sheets, cinematic frames, keyframes, storyboards, single-shot image-to-video, or multi-shot sequence generation. Defaults to GPT for images and Seedance for video unless the user names another model.
---

# Prompts Structure

Turn the user's intended deliverable into a finished image/video or a production-ready prompt. The user does not need to name a template, route, or model.

## Non-negotiable defaults

- Image request with no model named: use **GPT image generation** and the GPT variant of the selected architecture.
- Video request with no model named: use **Seedance** and the Seedance shot or sequence architecture.
- An explicit model choice overrides these defaults. Never silently render with a different model.
- If the user asks to create, generate, render, extract into, or make media, build the prompt internally and invoke the compatible generation tool when one is available. Do not stop at showing the prompt.
- If the user explicitly asks for a prompt, template, rewrite, evaluation, or analysis, return text only unless they also ask to generate.
- If the requested renderer is unavailable, do not claim generation succeeded. Return the ready-to-run prompt and state which renderer/tool is missing.

## Route before writing

Read [references/routing.md](references/routing.md) and choose exactly one primary route for each deliverable. Its four high-priority routes are:

| Natural-language intent | Canonical route | Template |
|---|---|---|
| Extract the person/character from an attached image into a character concept sheet | `concept-character-i2i-gpt` | `concept/character/image_to_image_gpt.md` |
| Extract the background/environment from an attached image into a location concept sheet | `concept-location-i2i-gpt` | `concept/location/image_to_image_gpt.md` |
| Animate an attached image as one continuous shot | `shot-seedance` | `shot/seedance.md` |
| Generate a passage from character/location concepts plus a shot list or script | `sequence-seedance` | `sequence/seedance.md` |

These defaults apply even when the user never mentions `concept-character-i2i`, `concept-location-i2i`, `shot`, `sequence`, GPT, or Seedance.

## Routing precedence

Resolve conflicts in this order:

1. **Final deliverable:** video beats image; an image deliverable beats prompt-only work; an explicit prompt-only request prevents rendering.
2. **Explicit model:** the user's named model beats the modality default.
3. **Video scope:** a supplied shot list/script, multiple shots, edits/cuts, or several story beats means `sequence`; one image animated as one continuous camera take means `shot`.
4. **Image form:** a design/reference sheet means `concept`; one finished cinematic still means `frame`; sequential planning panels mean `storyboard`; full-color continuity anchors mean `keyFrames`.
5. **Concept subtype:** use `concept-classification.md` to choose character, entity, prop, location, or vfx.
6. **Source mode:** a reference that supplies subject identity, appearance, composition, or environment means i2i; a reference used only as loose inspiration does not automatically force i2i.

The final action verb is decisive. For example, “基于这份镜头表生成视频” routes to `sequence`, even though “镜头表” could otherwise describe a storyboard input.

## Execution workflow

1. Inspect the user's text and all attached images/files. Assign each input a role: character identity, entity, location, prop, style/look, keyframe, shot list, or script.
2. Select the primary route and model using the precedence above. Do not ask the user to name an internal architecture.
3. Read only the files listed for that route in `references/routing.md`, including required base/layout/hygiene files.
4. Convert narrative or abstract language into visible action, body mechanics, spatial relationships, materials, lighting, and camera behavior. Preserve explicit identity, composition, duration, aspect ratio, and model choices.
5. Build one clean prompt in the selected architecture. Do not expose internal chain-of-thought or template assembly unless requested.
6. If media was requested, invoke the selected renderer with the attached references and composed prompt. Return the generated artifact. If only a prompt was requested, return the prompt.
7. For a multi-stage request, run dependencies in order and reuse outputs: concept assets first, then keyframes/frame if requested, then shot/sequence video.

## Input binding

- One attachment plus “这张图/这个人物/这个背景” binds to that attachment.
- For several attachments, infer roles from visible content, filenames, and the user's nearby wording; preserve a stable name-to-file map in the prompt.
- “中间的人物/左边的人/后面的建筑” is a region selector. Isolate that region semantically; do not treat unrelated image content as part of the subject.
- Character extraction preserves identity, face, body, clothing, accessories, and distinctive marks while removing unrelated people and scenery from the concept-sheet content.
- Location extraction preserves spatial logic, architecture, palette, lighting, and atmosphere while excluding characters and reconstructing occluded environment where necessary.
- In Seedance prompts, bind every reference with the exact filename or host-supported reference token and a unique character/location name. Do not invent filenames.
- Ask one concise question only when a missing attachment or genuinely ambiguous identity would change the result. Infer ordinary creative details from the request and references.

## Model resolution

Normalize common names before selecting files:

- `GPT`, `ChatGPT 生图`, `OpenAI image`, `gpt-image`, `ImageGen` → GPT image.
- `Gemini`, `Nano Banana` → Gemini image.
- `Midjourney`, `MJ` → Midjourney image.
- `即梦生图`, `Jimeng image` → Jimeng image.
- `Seedance`, `即梦视频` → Seedance video.
- `MiniMax`, `海螺`, `Hailuo` → MiniMax video.

If the explicit model lacks a native variant for the chosen route, keep the route semantics but do not pretend an unsupported template exists. Use a documented compatible base only when the route reference says to; otherwise deliver the closest model-neutral prompt and clearly identify the limitation.

## Shared quality rules

- Read `meta/prompt-hygiene.md` before any prompt.
- For every GPT image route, also read `meta/gpt-image-hygiene.md`.
- Use `concept-classification.md` when the concept subtype is not explicit or could be confused with another subtype.
- For character performance in shot/sequence video, read the applicable files under `performance/` before writing actions; a simple environment-only move does not need a character acting profile.
- Respect the selected template's layout, duration, character limit, reference syntax, and negative-prompt policy.
- Do not add project names, scene IDs, lore, or other narrative metadata to model prompts unless they are functional labels required by a multi-panel layout.

## Completion check

Before responding, verify: correct route, correct model, correct reference binding, correct output mode (media vs prompt), no silent model fallback, and no invented input filenames. When generation was requested and a compatible tool exists, a prompt without the generated artifact is incomplete.
