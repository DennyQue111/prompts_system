---
name: prompt-execution
description: 指挥剧本到成片的镜头级生产执行，规定拆镜、概念资产、关键帧、视频的生成顺序、人工确认节点、失败重试与状态记录。Use when the user asks to 跑剧本、批量生成镜头、继续上次制作或复盘制作问题。
---

# Prompt Execution

将一份剧本稳定地跑成整组镜头视频的生产调度层。`prompts_structure` 负责“怎么写提示词”，本 skill 负责“先做什么、谁确认、失败了怎么办、经验记到哪里”。

当用户明确在 `ai_image_video_generator` 中使用 **Flux.2 Klein 生图 + MiniMax H3 视频**时，先读 [references/ai-image-video-generator.md](references/ai-image-video-generator.md)。它是该应用的集成档案：说明已实现的接口、资产回填格式和当前仍需人工执行的步骤。它不替代本 skill 的确认门，也不改变其他渲染器的通用流程。

## 总流程

严格按阶段推进，每个阶段完成并记录后才能进入下一阶段：

1. **拆镜**：用 `prompts_structure/script/shot_breakdown` 把剧本拆成 `concepts + shot_breakdown` 两个 JSON。
2. **分镜确认门**：先把完整镜头表交给用户过目。用户确认前不生成任何媒体。确认后记录确认结论，后续改动走增量，不重跑全片。
3. **概念资产**：为每个主要角色生成身份锚图，为每个重复出现的场景生成场景锚图，跨镜头关键道具同理。资产路径回填 concepts JSON 的 `reference_images`。
4. **资产确认门**（可选但推荐）：让用户快速过目角色与场景锚图，气质不对在这里改最便宜。
5. **逐镜关键帧**：按镜头顺序生成关键帧，遵守 [references/retry-policy.md](references/retry-policy.md)。
6. **关键帧质检**：逐镜核对身份、构图、空间关系、动作起始状态；不合格先修提示词重生成，不带废片往下走。
7. **回填镜头表**：关键帧通过质检后，立即把文件路径写入镜头表 JSON 对应镜头的 `reference_images`。概念资产（角色/场景/道具锚图）生成后同样回填 concepts JSON。保持 JSON 与磁盘产物实时一致，前端和后续 agent 读到的永远是最新状态。
8. **逐镜视频**：用合格关键帧 + 角色/场景锚图组装视频提示词并提交，同样遵守重试策略。使用 MiniMax H3 时优先绑定“角色身份锚图 + 当前镜头关键帧”；只有确有必要时再加入场景或道具锚图，且总数不超过后端支持上限。
9. **回收与复盘**：全部镜头跑完后核对状态表，把新问题追加到 [references/lessons-learned.md](references/lessons-learned.md)。

各阶段的输入输出细节见 [references/pipeline.md](references/pipeline.md)。

## 状态跟踪

为每个镜头维护状态，任何时候都要能回答“哪一镜进行到哪一步”：

`pending → breakdown_confirmed → anchors_ready → keyframe_ready → video_submitted → video_done`

异常态：`blocked(原因)`。任何镜头不得静默跳过——失败必须记录原因进入 blocked，本轮其余镜头跑完后统一回补。

## 执行纪律

- 单镜时长默认 ≤ 8 秒；超出时在拆镜阶段就拆成连续镜，并在 `continuity` 标注“尾帧续接”。
- 并发分开控制：本地提示词服务（如 11434）串行调用；渲染提交（ComfyUI / MiniMax）可适度并行。
- 自动提示词接口偶发超时时，允许绕过它手工组装视频提示词，但必须在状态记录里标注“手工提示词”。
- 开工前先确认渲染后端连通（如后端 status 里 `comfyui_connected=true`），不连通不批量提交。
- 已知坑先查 [references/lessons-learned.md](references/lessons-learned.md)，不要重复踩。
- 不把“已有单镜生成接口”误称为“已具备小说一键全自动生产”。若当前应用没有编排器，应明确执行到哪一个确认门，并逐镜记录或回填，而不是假定批处理、质检和重试已经发生。
- 当直接使用“场景锚图 + 人物锚图”生成关键帧后，仍出现机位、空间拓扑、姿态、身份或左右侧别错误时，不要无限强化一条提示词。若应用集成档案支持，改用其中的“三段式关键帧回退”。
