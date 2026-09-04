# Intent and Model Routing

Use this file after `SKILL.md` identifies the requested deliverable. Select one primary route per deliverable, then read every file in that route's “Read” column. Paths are relative to `prompts_structure/`.

## High-priority natural-language routes

| User intent or close paraphrase | Route | Default model | Read |
|---|---|---|---|
| “把这个图片中间的人物提取出来成人物概念图/角色设定图/三视图” | `concept-character-i2i-gpt` | GPT | `concept/character/image_to_image_gpt.md`; its required base `concept/character/image_to_image_gemini.md`; `concept/character/simple_layout_instruction.md` by default or `general_layout_instruction.md` if a full sheet is requested; both meta hygiene files |
| “把这个背景/场景提取出来成场景概念图/环境设定图/HDR 场景图” | `concept-location-i2i-gpt` | GPT | `concept/location/image_to_image_gpt.md`; its required base `concept/location/image_to_image_gemini.md`; `concept/location/hdr_layout_instruction.md`; both meta hygiene files |
| “把这张图片生成视频/让这张图动起来，我的要求是……” with one continuous beat | `shot-seedance` | Seedance | `shot/seedance.md`; `meta/prompt-hygiene.md`; applicable `performance/` files when a visible character performs |
| “基于人物概念图、场景概念图和这段镜头表/剧本生成这段视频” | `sequence-seedance` | Seedance | `sequence/seedance.md`; `meta/prompt-hygiene.md`; `performance/acting_master_profile.md`, `performance/scene_adaptation.md`, and `performance/eye_life.md` when human/humanoid characters perform |

The phrase need not match word-for-word. Infer by deliverable and input structure.

## Boundaries that prevent common misroutes

| Request | Correct route | Not this |
|---|---|---|
| Remove a background or make a transparent cutout only | Ordinary image edit | Not a character concept sheet |
| Extract a person into a designed reference sheet with views/details | `concept-character-i2i-*` | Not simple masking/cropping |
| Remove people from a scene but preserve one finished composition | `frame-i2i-*` or ordinary image edit, according to wording | Not an HDR location sheet unless a location concept is requested |
| Reconstruct the environment as a reusable multi-view design asset | `concept-location-i2i-*` | Not a single cinematic frame |
| Make one polished cinematic still from references | `frame-i2i-*` | Not `shot`; `shot` outputs video |
| Show a story as planning panels | `storyboard-*` | Not video unless the final verb says to generate video |
| Make full-color per-shot continuity anchors | `keyframes-*` | Not a black-and-white storyboard |
| Animate one still with one uninterrupted camera/action beat | `shot-*` | Not `sequence` |
| Use multiple shots, cuts, a shot table, or several scripted beats | `sequence-*` | Not `shot`, even if only one reference image is supplied |

“提取人物” alone can mean masking. Route to a character concept only when the requested output also says 概念图、设定图、角色参考图、三视图, design sheet, or equivalent. “提取背景” alone can mean object removal; route to a location concept only when the user asks for a reusable environment/location design asset.

## General image routes

The default column below applies only when the user did not name a model.

| Deliverable | Mode | Default | GPT template | Other documented variants |
|---|---|---|---|---|
| Humanoid character concept | t2i | GPT | `concept/character/text_to_image_gpt.md` | Gemini `text_to_image_gemini.md`; MJ `text_to_image_midjourney.md` |
| Humanoid character concept | i2i | GPT | `concept/character/image_to_image_gpt.md` | Gemini `image_to_image_gemini.md`; Jimeng `image_to_image_jimeng.md` |
| Location/environment concept | t2i | GPT | `concept/location/text_to_image_gpt.md` | Gemini `text_to_image_gemini.md`; MJ `midjourney.md` |
| Location/environment concept | i2i | GPT | `concept/location/image_to_image_gpt.md` | Gemini `image_to_image_gemini.md`; Jimeng `image_to_image_jimeng.md` |
| Non-humanoid sentient entity | t2i | GPT | `concept/entity/gpt.md` | Gemini `gemini.md`; MJ `midjourney.md` |
| Inert prop/object | t2i | GPT | `concept/prop/gpt.md` | Gemini `gemini.md`; MJ `midjourney.md` |
| VFX concept from a reference | i2i | GPT | `concept/vfx/image_to_image_gpt.md` | No other local variant |
| Single cinematic frame | t2i | GPT | `frame/text_to_image_gpt.md` | Gemini `text_to_image_gemini.md`; MJ `text_to_image_midjourney.md` |
| Single cinematic frame | i2i | GPT | `frame/image_to_image_gpt.md` | Gemini `image_to_image_gemini.md`; MJ `image_to_image_midjourney.md`; Jimeng `jimeng_image_to_image.md` |
| Full-color keyframe grid | t2i | GPT | `keyFrames/text_to_image_gpt.md` | Gemini `text_to_image_gemini.md` |
| Full-color keyframe/reference sheet | i2i | GPT | `keyFrames/image_to_image_gpt.md` | No other local i2i variant |
| Storyboard | t2i/i2i | GPT | Load `storyboard/gemini.md` as base, then `storyboard/gpt.md` overlay | Gemini base only; Jimeng base + `storyboard/jimeng.md` overlay |

For concept routes, also read that subtype's `README.md` and layout file named by the chosen template. For frame routes, read `frame/style_reference.md`. For keyFrames, consult `keyFrames/examples.md` only when the required output format remains unclear.

## General video routes

| Scope | Default | Template | Alternate explicit model |
|---|---|---|---|
| One continuous shot | Seedance | `shot/seedance.md` | MiniMax H3 → `shot/minimax.md` |
| Multi-shot scene/sequence | Seedance | `sequence/seedance.md` | MiniMax H3 → `sequence/minimax.md` |

Choose scope from narrative structure, not duration alone. A ten-second montage with three cuts is a sequence; a twenty-second unbroken take is a shot.

## Model override examples

- “用 Gemini 把图中人物做成概念图” → character i2i semantics + `concept/character/image_to_image_gemini.md` + Gemini renderer.
- “用即梦生图做场景概念图” → location i2i semantics + `concept/location/image_to_image_jimeng.md` + Jimeng image renderer.
- “用 MiniMax/海螺生成这份镜头表的视频” → sequence semantics + `sequence/minimax.md` + MiniMax renderer.
- “用 GPT 写 Seedance 提示词” → GPT is the writing agent, not the renderer; route remains `shot-seedance` or `sequence-seedance` according to scope.

## Multi-stage requests

When one request asks for both source assets and a video, preserve dependency order:

1. Generate or extract character/location/entity/prop concepts.
2. Generate frame/keyFrames/storyboard only if requested or required by the user's specified workflow.
3. Bind the resulting assets by their real filenames/reference handles.
4. Generate the Seedance/MiniMax shot or sequence.

Do not ask the user to re-upload an artifact that the current agent just generated and can pass directly to the next tool.

## Insufficient or ambiguous inputs

- Missing reference for an explicit i2i request: ask for the image; do not convert silently to t2i.
- Multiple people and no region/name indicating which identity to extract: ask one concise identity question.
- Multiple clearly distinguishable files: infer roles, state the mapping briefly if useful, and proceed.
- Missing creative parameters such as focal length, subtle motion, lighting continuity, or ordinary transition choice: infer them from the architecture and source; do not block execution.
