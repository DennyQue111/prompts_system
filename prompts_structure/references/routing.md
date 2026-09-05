# Intent and Model Routing

Use this file after `SKILL.md` identifies the requested deliverable. Select one primary route per deliverable, then read every file in that route's “Read” column. Paths containing directories are relative to the skill root; bare filenames in a variant row are relative to the primary template's directory. Follow required base-file links in a selected template before writing, even when the base is named for a different model.

## High-priority natural-language routes

| User intent or close paraphrase | Route | Default model | Read |
|---|---|---|---|
| “把这个图片中间的人物提取出来成人物概念图/角色设定图/三视图” | `concept-character-i2i-gpt` | GPT | `concept/character/image_to_image_gpt.md`; its required base `concept/character/image_to_image_gemini.md`; `concept/character/simple_layout_instruction.md` by default or `general_layout_instruction.md` if a full sheet is requested; both meta hygiene files |
| “把这个背景/场景提取出来成场景概念图/环境设定图/HDR 场景图” | `concept-location-i2i-gpt` | GPT | `concept/location/image_to_image_gpt.md`; its required base `concept/location/image_to_image_gemini.md`; `concept/location/hdr_layout_instruction.md`; both meta hygiene files |
| “把这张图片生成视频/让这张图动起来，我的要求是……” with one continuous beat | `shot-seedance` | Seedance | `shot/seedance.md`; `meta/prompt-hygiene.md`; applicable `performance/` files when a visible character performs |
| “基于人物概念图、场景概念图和这段镜头表/剧本生成这段视频” | `sequence-seedance` | Seedance | `sequence/seedance.md`; `meta/prompt-hygiene.md`; `performance/acting_master_profile.md`, `performance/scene_adaptation.md`, and `performance/eye_life.md` when human/humanoid characters perform |

The phrase need not match word-for-word. Infer by deliverable and input structure.

“调取背景成概念图” and “提取背景成概念图” have the same route. Correct obvious typos from context, such as “根据剧本生活这段视频” meaning “生成这段视频”; do not reinterpret them when multiple meanings remain plausible.

Character i2i defaults to the existing simple layout: facial close-up / front body cropped at the neck / full back view. An explicit “正面、侧面、背面三视图” requires those three full-body views instead, with the heads preserved. “三视图” alone conventionally means front/side/back; it is not a synonym for this library's special simple layout. Explicit panel counts/views override defaults. Location i2i defaults to the HDR four-view sheet; a requested single environment view overrides that layout.

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
| Use multiple shots, cuts, or a shot table/script without a one-take override | `sequence-*` | Not `shot`, even if only one reference image is supplied |

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

For concept routes, read that subtype's `README.md` if present and the layout file named by the chosen template; vfx has no README. For frame routes, read `frame/style_reference.md`. For keyFrames, consult `keyFrames/examples.md` only when the required output format remains unclear. GPT entity/prop variants use their sibling `gemini.md` bases. Loading a Gemini base for methodology does not select the Gemini renderer.

## Adaptation when no exact template exists

- Entity/prop extraction with references: use the selected model's entity/prop base, observe the subject first, replace invented details with observed attributes, bind the actual reference, and infer only needed hidden views. Record the mode as i2i; do not invent an `image_to_image_*` filename.
- VFX without references: reuse `concept/vfx/image_to_image_gpt.md` for its effect form and lifecycle structure, omit reference-only instructions, and mark t2i adaptation.
- Another explicit model (such as Kling or Sora video): use the same shot/sequence semantics and a model-neutral adaptation of the default architecture. Read the actual provider's available skill/tool documentation for syntax and parameters; remove incompatible Seedance-specific tags or negative fields. Keep the explicitly chosen model and render if its tool supports the task.
- When an available variant produces a single still but the user requests a sheet (for example an MJ character sheet), adapt the layout explicitly rather than silently delivering a single still. A text-only location HDR request can combine `concept/location/text_to_image_gpt.md` with `concept/location/hdr_layout_instruction.md`; do not require a needless intermediate image.
- For any adaptation, preserve the requested content, references, and output form. Briefly state that the template was adapted. If the actual tool cannot support the required modality or references, use the unavailable-capability handling in `references/execution.md`.

## General video routes

| Scope | Default | Template | Alternate explicit model |
|---|---|---|---|
| One continuous shot | Seedance | `shot/seedance.md` | MiniMax H3 → `shot/minimax.md` |
| Multi-shot scene/sequence | Seedance | `sequence/seedance.md` | MiniMax H3 → `sequence/minimax.md` |

Choose scope from camera/edit structure, not duration or action count alone. A ten-second montage with three cuts is a sequence; a twenty-second unbroken take is a shot. “按这段剧本一镜到底” and “只生成镜头表第 3 镜” use `shot`.

## Model override examples

- “用 Gemini 把图中人物做成概念图” → character i2i semantics + `concept/character/image_to_image_gemini.md` + Gemini renderer.
- “用即梦生图把这张背景做成场景概念图” → location i2i semantics + `concept/location/image_to_image_jimeng.md` + Jimeng image renderer.
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
