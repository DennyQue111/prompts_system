# prompts_system

AI 影视提示词与制作流程库。

给 agent 的入口是 [SKILL.md](SKILL.md)；本 README 只作为供人快速浏览的目录地图。要让支持技能发现的 agent 稳定读取本库，应引用或安装这个目录下的 `SKILL.md`，而不是依赖 README。

## 模块

| 目录 | 用途 |
| --- | --- |
| `style-profiles/` | 可复用的视觉风格技术拆解：线条、材质、光影、颜色、构图与角色渲染。 |
| `prompts_structure/` | 提示词结构库：世界观、概念设计、单帧、关键帧、单镜头、序列、表演与剧本拆解。 |
| `prompt-execution/` | 实际制作编排：拆镜、审核门、锚图、关键帧、逐镜视频、重试和状态记录。 |
| `project-structure/` | AI 短片项目的通用目录、命名和资产组织规范。 |
| `outputs/` | 运行过程中生成的提示词与辅助输出。 |

## prompts_structure

按最终交付物选择结构：

- `world_view/`：世界观视觉宪法和氛围探索。
- `concept/`：角色、实体、场景、道具和 VFX 概念。
- `frame/`、`keyFrames/`：镜头参考帧与关键帧组。
- `shot/`：一个连续镜头的视频提示词。
- `sequence/`：有多个剪辑段落的时间序列提示词。
- `performance/`：角色表演、行为拍子和场景适配。
- `script/`：剧本和镜头表拆解。

## prompt-execution

当任务从“写提示词”进入“实际生成媒体”时，先读 `prompt-execution/SKILL.md`。它定义拆镜确认、概念锚图、关键帧、视频生成、质检和失败处理的顺序。

使用本地 `D:\files\code\ai_image_video_generator` 时，同时阅读 `prompt-execution/references/ai-image-video-generator.md`：其中记录 Flux.2 Klein → MiniMax H3 的接口、资产路径和执行限制。当前 MiniMax H3 输出的宽和高必须都能被 32 整除；未传时长时应用默认 8 秒，但单镜头时长可按镜头需要指定。

## project-structure

项目结构与提示词结构相互配合：`project-structure/` 解决“资产存在哪里、如何命名”，其余模块解决“提示词如何构建和如何执行”。
