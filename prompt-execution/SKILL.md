---
name: prompt-execution
description: 指挥剧本到成片的镜头级生产执行，规定拆镜、概念资产、关键帧、视频的生成顺序、人工确认节点、失败重试与状态记录。Use when the user asks to 跑剧本、批量生成镜头、继续上次制作或复盘制作问题。
---

# Prompt Execution

将一份剧本稳定地跑成整组镜头视频的生产调度层。`prompts_structure` 负责“怎么写提示词”，本 skill 负责“先做什么、谁确认、失败了怎么办、经验记到哪里”。

当用户明确在 `ai_image_video_generator` 中使用 **Flux.2 Klein 或由 Codex 直接调用的 GPT 图像模型生图 + MiniMax H3 视频**时，先读 [references/ai-image-video-generator.md](references/ai-image-video-generator.md)。它是该应用的集成档案：说明已实现的接口、资产回填格式和当前仍需人工执行的步骤。它不替代本 skill 的确认门，也不改变其他渲染器的通用流程。

## 总流程

严格按阶段推进，每个阶段完成并记录后才能进入下一阶段：

0. **风格定义**：选定图像模型（Flux / Z-Image / GPT 等）后，用 2-3 张代表性场景试生成（如一张场景建立镜头、一张人物镜头、一张复杂构图），附上候选风格后缀。用户确认风格前不生成任何概念图或分镜。风格一经确认，全项目沿用同一风格后缀，不中途更换。
1. **概念资产**：基于确认的风格和渲染器生成概念资产。**Flux 和 GPT 的流程不同**（详见 [references/pipeline.md](references/pipeline.md) 阶段 1-2）：
   - **Flux**：每个角色生成两类资产——身份锚图（单人正面照，flux t2i，用于 Flux i2i 关键帧参考）+ 角色概念图（front/back 双栏，用于 MiniMax 视频参考）。场景生成场景锚图（flux t2i，无人）。
   - **GPT**：每个角色直接生成角色概念图（可含多视图，同时用于关键帧生成和 MiniMax 视频）。场景生成场景概念图。不需要额外身份锚图。
   - 用户指定使用 `ai_image_video_generator` 的 Flux 角色概念图功能时，直接在 Free Canvas 的 **Image-to-Image → Skill → Concept Image** 页签中选中该角色唯一的源图，补充必要的角色约束后点击"生成角色概念图"，完整使用应用内置流程。不要把该流程拆成多次手工 Flux API 调用、手工做人脸裁切/放大/拼版；详细行为见 [references/ai-image-video-generator.md](references/ai-image-video-generator.md)。生成后将最终概念图及身份锚图路径回填 concepts JSON 的 `reference_images`。
2. **资产确认门**（可选但推荐）：让用户快速过目角色与场景锚图，气质不对在这里改最便宜。
3. **分镜拆解**：用 `prompts_structure/script/shot_breakdown` 把剧本拆成 `concepts + shot_breakdown` 两个 JSON。此时概念图已存在，分镜可参照角色外观和场景空间精确编写 camera/framing/action。
4. **分镜确认门**：先把完整镜头表交给用户过目。用户确认前不生成任何关键帧。确认后记录确认结论，后续改动走增量，不重跑全片。
5. **逐镜关键帧**：按镜头顺序生成关键帧，**Flux 和 GPT 的生成路径不同**（详见 [references/pipeline.md](references/pipeline.md) 阶段 5-6）：
   - **Flux**：首选路径——身份锚图 + 场景锚图 → Flux i2i（flux-kontext）。质检不合格时走三段式回退（camera plate + action plate → 合成）。
   - **GPT**：角色概念图 + 场景概念图 → GPT 直接生成关键帧。
   - 遵守 [references/retry-policy.md](references/retry-policy.md)。
6. **关键帧质检**：逐镜核对身份、构图、空间关系、动作起始状态；不合格先修提示词重生成，不带废片往下走。
7. **回填镜头表**：关键帧通过质检后，立即把文件路径写入镜头表 JSON 对应镜头的 `reference_images`。概念资产（角色/场景/道具锚图）生成后同样回填 concepts JSON。保持 JSON 与磁盘产物实时一致，前端和后续 agent 读到的永远是最新状态。
8. **逐镜视频**：用合格关键帧 + 角色/场景锚图组装视频提示词并提交，同样遵守重试策略。使用 MiniMax H3 时，含角色镜头必须绑定"当前镜头关键帧 + 每个画内主要角色的概念图"；无角色镜头只绑定当前镜头关键帧。只有确有必要时再加入场景或道具锚图，且总数不超过后端支持上限。
   - 提示词内容按镜头形态选用 `prompts_structure/shot/minimax.md`（连续单镜）或 `prompts_structure/sequence/minimax.md`（含剪辑的序列）；不要在执行层重复模板里的台词、动作、负面约束等写法。Execution 在此阶段只负责绑定并核对参考素材、调用接口、监控任务、检查产物并记录状态。若关键帧必须作为视频首帧，按集成档案将其单独绑定为 `first_frame_image`，人物/外观图仍作为 `reference_images`；不得仅因关键帧出现在提示词或参考图列表中就视为已施加首帧约束。应用接口限制见 `references/ai-image-video-generator.md`。
   - **Entity 参考图**：镜头涉及 entity 时，将该 entity 最完整、已确认的概念图直接作为 MiniMax 的设计参考，锁定身份、材质、结构和整体设计。再按具体镜头中 entity 实际出现的形态、尺度、构图位置和状态，生成一张镜头专用的单体参考图并一并提交；概念图负责“它是什么”，镜头专用图负责“它在本镜头里长什么样/处于什么状态”。在提示词中明确各图职责，镜头专用图需遵守关键帧的空间和构图。
   - **复杂特效过程参考图**：当 entity 或其他主体需要多阶段、难以仅靠文字描述的形态变化（如粒子聚合、群体拆分重组、流体生物成形、实体转化为界面），在视频提交前准备专用过程示意图。用约 3–5 个有序阶段明确起始、中间和最终状态，确保阶段顺序、运动方向、主体位置关系及最终设计与已确认概念一致；简单、单一动作不需要额外制作过程图。
   - 将过程图作为额外运动/阶段参考，与当前镜头关键帧、角色概念图、entity 概念图及镜头专用 entity 参考图一并绑定。提示词逐段写清“过程图第几格/图几 → 视频多少秒 → entity 的可见状态与运动”，特别核对图中真实运动方向和先后顺序，不要用想当然的动作描述覆盖参考图。
   - **严格区分画面职责**：关键帧是视频第一帧以及整幅画面的构图、机位、场景、人物位置和空间关系的唯一权威；entity 概念图和镜头专用 entity 图限定 entity 的设计与本镜状态；过程图只限定该 entity/主体的特效变化流程、阶段顺序和运动方向。提示词要明确过程图只是局部特效动作参考，并要求该变化发生在关键帧对应的场景和位置中。过程图中的分格、编号、边框、背景和排版不属于视频画面，不能将其描述成镜头、分镜或视频构图，也不能让过程图取代关键帧。
   - 若特效的最终结果是屏幕、投影、符号或其他具有设计细节的画内图像，另行绑定清晰的最终图像参考；过程图负责变化顺序，entity 概念图负责设计权威，镜头专用图负责本镜头呈现状态，最终图负责完成态内容。
9. **回收与复盘**：全部镜头跑完后核对状态表，把新问题追加到 [references/lessons-learned.md](references/lessons-learned.md)。

各阶段的输入输出细节见 [references/pipeline.md](references/pipeline.md)。

## 状态跟踪

为每个镜头维护状态，任何时候都要能回答“哪一镜进行到哪一步”：

`pending → style_confirmed → anchors_ready → breakdown_confirmed → keyframe_ready → video_submitted → video_done`

异常态：`blocked(原因)`。任何镜头不得静默跳过——失败必须记录原因进入 blocked，本轮其余镜头跑完后统一回补。

## 执行纪律

- 单镜时长默认 ≤ 8 秒；超出时在拆镜阶段就拆成连续镜，并在 `continuity` 标注“尾帧续接”。
- 并发分开控制：本地提示词服务（如 11434）串行调用；渲染提交（ComfyUI / MiniMax）可适度并行。
- 自动提示词接口偶发超时时，允许绕过它手工组装视频提示词，但必须在状态记录里标注“手工提示词”。
- 开工前先确认渲染后端连通（如后端 status 里 `comfyui_connected=true`），不连通不批量提交。
- 已知坑先查 [references/lessons-learned.md](references/lessons-learned.md)，不要重复踩。
- 不把“已有单镜生成接口”误称为“已具备小说一键全自动生产”。若当前应用没有编排器，应明确执行到哪一个确认门，并逐镜记录或回填，而不是假定批处理、质检和重试已经发生。
- 当直接使用“场景锚图 + 人物锚图”生成关键帧后，仍出现机位、空间拓扑、姿态、身份或左右侧别错误时，不要无限强化一条提示词。若应用集成档案支持，改用其中的“三段式关键帧回退”。
