---
name: prompts-structure
description: 根据自然语言、图片和剧本自动选择提示词结构并调用可用生成工具。适用于提取人物或背景成概念图、电影静帧、分镜图、关键帧、图片生成单镜头视频，以及人物图加场景图和镜头表或剧本生成视频；也支持只写或评估提示词。Defaults to GPT images and Seedance video; explicit model choices override defaults.
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

Read [references/routing.md](references/routing.md) and choose exactly one primary route for each deliverable. Its high-priority routes are:

| Natural-language intent | Canonical route | Template |
|---|---|---|
| Extract the person/character from an attached image into a character concept sheet | `concept-character-i2i-gpt` | `concept/character/core-i2i.md` + `adapters/gpt-image.md` |
| Extract the background/environment from an attached image into a location concept sheet | `concept-location-i2i-gpt` | `concept/location/core-i2i.md` + `adapters/gpt-image.md` |
| Split a screenplay/script into an importable JSON shot breakdown | `script-shot-breakdown` | `script/shot_breakdown/SKILL.md` |
| Animate an attached image as one continuous shot | `shot-seedance` | `shot/seedance.md` |
| Generate a passage from character/location concepts plus a shot list or script | `sequence-seedance` | `sequence/seedance.md` |

These defaults apply even when the user never mentions `concept-character-i2i`, `concept-location-i2i`, `shot`, `sequence`, GPT, or Seedance.

For requests such as “把剧本拆分成 JSON 镜头表”, “按镜头表 JSON 结构拆剧本”, or “生成可导入镜头表管理页的 JSON”, use `script-shot-breakdown`: read [`script/shot_breakdown/SKILL.md`](script/shot_breakdown/SKILL.md), return or save its `schema_version: 2` JSON, and do not generate media or platform prompts unless the user separately requests them.

## Routing precedence

Resolve conflicts in this order:

1. **Deliverable and action per stage:** identify what the user wants produced, then whether that stage calls for media, a prompt, or analysis. Input images/scripts and quoted examples are not additional deliverables. In “先生成人物概念图，再只写视频提示词”, render the image and return video text; in “只写人物生图提示词，然后生成视频”, return image text and render the video if its inputs are available.
2. **Explicit model:** the user's named model beats the modality default.
3. **Video scope:** a supplied shot list/script or multiple cuts defaults to `sequence`; “把这张图生成视频” defaults to `shot`. An explicit single-shot selection or “一镜到底/全程不切镜” overrides the script default and uses `shot`. Several actions can happen within one continuous shot.
4. **Image form:** a design/reference sheet means `concept`; one finished cinematic still means `frame`; sequential planning panels mean `storyboard`; full-color continuity anchors mean `keyFrames`.
5. **Concept subtype:** use `concept-classification.md` to choose character, entity, prop, location, or vfx.
6. **Source mode:** a reference that supplies subject identity, appearance, composition, or environment means i2i; a reference used only as loose inspiration does not automatically force i2i.

The final action verb is decisive. For example, “基于这份镜头表生成视频” routes to `sequence`, even though “镜头表” could otherwise describe a storyboard input.

## Execution workflow

1. Inspect the user's text and all attached images/files. Assign each input a role: character identity, entity, location, prop, style/look, keyframe, shot list, or script.
2. Select the primary route and model using the precedence above. Do not ask the user to name an internal architecture.
3. For an image route, read exactly one deliverable **Core** and one renderer **Adapter** listed in `references/routing.md`, plus required layout/hygiene files. GPT is the default Adapter; an explicit Gemini or Jimeng choice replaces only the Adapter, not the Core.
   - For spatially constrained `frame`, `storyboard`, or `keyFrames` work, also read [`meta/spatial-continuity.md`](meta/spatial-continuity.md). Build world topology first, then derive what the selected camera can actually see; never assume that naming an intersection or supplying a multi-view sheet defines its perspective projection.
4. Convert narrative or abstract language into visible action, body mechanics, spatial relationships, materials, lighting, and camera behavior. Preserve explicit identity, composition, duration, aspect ratio, and model choices.
5. Build one clean prompt in the selected architecture. Expand layout instructions into actual panel descriptions; the image model cannot read this skill's Markdown files. Give a short route/model notice when useful; keep internal reasoning private.
   - **Concept-sheet hard gate:** For `concept-character-*` routes, the compiled image prompt MUST explicitly contain the selected layout's aspect ratio, panel count, panel order, and per-panel view instructions. Never replace a character concept sheet with a single portrait, single full-body illustration, cinematic still, or three-quarter character shot unless the user explicitly requests that alternate output.
   - For the default character i2i route, the prompt MUST state: `16:9`, `three equal vertical columns`, `LEFT facial close-up`, `CENTER front full body head intentionally cropped at the neck`, and `RIGHT back full body head-to-toe`. If any of these are missing, do not execute the image tool; repair the prompt first.
6. For a media stage, read [references/execution.md](references/execution.md), discover the matching generation capability in the host, pass actual references, and return the artifact or precise job status. For a prompt-only stage, return the prompt without rendering.
7. For a multi-stage request, run dependencies in order and reuse outputs: concept assets first, then keyframes/frame if requested, then shot/sequence video.

## Input binding

- One attachment plus “这张图/这个人物/这个背景” binds to that attachment.
- For several attachments, infer roles from visible content, filenames, and the user's nearby wording; preserve a stable name-to-file map in the prompt.
- “中间的人物/左边的人/后面的建筑” is a region selector. Isolate that region semantically; do not treat unrelated image content as part of the subject.
- Character extraction preserves identity, face, body, clothing, accessories, and distinctive marks while removing unrelated people and scenery from the concept-sheet content.
- Location extraction preserves spatial logic, architecture, palette, lighting, and atmosphere while excluding characters and reconstructing occluded environment where necessary. Unseen back views and spaces are consistent design inferences, not recovered facts; preserve observed features and avoid inventing prominent identity marks or unrelated structures.
- In Seedance prompts, bind every reference with the exact filename or host-supported reference token and a unique character/location name. Do not invent filenames.
- Ask one concise question only when a missing attachment or genuinely ambiguous identity would change the result. Infer ordinary creative details from the request and references.

## Model resolution

Normalize common names only to select a template family; retain any exact version, provider, and stage-specific model choice for execution:

- `GPT`, `ChatGPT 生图`, `OpenAI image`, `gpt-image`, `ImageGen` → GPT image.
- `Gemini`, `Nano Banana` → Gemini image.
- `Midjourney`, `MJ` → Midjourney image.
- `即梦生图`, `Jimeng image` → Jimeng image.
- `Seedance`, `即梦视频` → Seedance video.
- `MiniMax`, `海螺`, `Hailuo` → MiniMax video.

Bare “即梦/Jimeng” means Jimeng image for an image stage and Seedance for a video stage. A model mentioned as the source (“这张 MJ 图”) or writer (“用 GPT 写 Seedance 提示词”) is not the target renderer. Within a revision such as “改成竖版，再来一张”, inherit the active stage's model and references; start unrelated new work with the modality defaults unless the user set a continuing preference.

If the requested model has no native variant, follow the adaptation rules in `references/routing.md` and still execute when a compatible tool exists. Missing template and missing renderer are different conditions. If a model cannot produce the requested modality or exact requested version cannot be selected, report the mismatch; do not substitute another model.

## Shared quality rules

- Read `meta/prompt-hygiene.md` before any prompt.
- For every GPT image route, read `adapters/gpt-image.md` and `meta/gpt-image-hygiene.md`.
- Use `concept-classification.md` when the concept subtype is not explicit or could be confused with another subtype.
- For character performance in shot/sequence video, read the applicable files under `performance/` before writing actions; a simple environment-only move does not need a character acting profile.
- Respect the selected template's layout, duration, character limit, reference syntax, and negative-prompt policy.
- User instructions override template defaults, including layout, one-take direction, style, and output count. Within this library, this entrypoint resolves routing and execution; the selected renderer Adapter compiles the shared Core into model-specific syntax; shared hygiene is applied within those constraints.
- Keep functional reference names, `@TAG` bindings, shot timing, and panel labels. Omit unrelated lore or project-management metadata.
- Preserve the user's/project's supplied style profile; otherwise infer style from the reference. Optional style snippets live in `style-profiles/style-library.md`. Sibling `../style-profiles/` is optional and must not block a copied standalone skill.

## Other local workflows

For world expansion/世界观九景, read `world_view/SKILL.md` and its required references. Treat that module as the worldbuilding prompt planner; for actual images requested through this router, retain GPT as the unspecified renderer and apply `references/execution.md`. A nine-view study of one locked scene remains `keyFrames`, not world expansion. For an explicit acting-profile request, read `performance/README.md` and return the requested acting material; do not render media merely because performance is used upstream of video.

Pass the whole skill directory to another agent, including its references and templates. Route names such as `concept-character-i2i-gpt` are local workflow identifiers, not separately installed skills. Host-specific generation skills are discovered at runtime; this folder itself supplies no model credentials or video backend.

## Completion check

Before responding, verify: correct route, correct model, correct reference binding, correct output mode (media vs prompt), no silent model fallback, and no invented input filenames. When generation was requested and a compatible tool exists, a prompt without the generated artifact is incomplete.
