---
name: project-structure
description: Universal file structure & naming conventions for Denny's AI short-film projects. Use when starting a new script project, or when an agent needs to know where to place/write files (script, world_view, concept, scenes, export), how to name prompts/images/videos, or what the production workflow is. Generic by design — works for any project (《复生协议》《孢子纪元》or future ones). Concrete example: see references/复生协议_案例.md. Triggers: "新项目怎么建目录", "文件放哪", "命名规范", "按这个 skill 的结构来", "project structure".
---

# Project Structure（AI 短片项目通用结构）

## Overview

本 skill 定义 Denny 所有 AI 短片项目的**通用目录结构、命名规范、工作流管线**。任何新剧本项目都按此结构初始化；任何 agent 接手项目时读本文件即可知道文件该放哪里、该怎么命名，无需重新扫描目录。

**设计原则：概念层与生产层分离**
- `concept/` 放设计（角色长什么样）→ 上游
- `scenes/` 放生产（镜头怎么拍）→ 下游
- 世界观看全局，script 定剧情，export 收成片

## 世界观与剧本的关系

**世界观是容器，剧本是容器里的故事。**

- **世界观（world_view/）** = 一个大世界的整体设定：地理、科技、种族、历史、视觉宪法。属于整个世界，全局共享
- **剧本（script/）** = 这个大世界中某个/某些人或生物的一段故事。**一个世界观可以承载多个剧本**（如主线 + 外传/番外）

**对结构的影响（很小，刻意为之）：**
1. `world_view/` 和 `concept/` 是**世界级资产**：同一世界内的多个剧本共享同一套世界观设定和角色/场景/道具设计，不按剧本复制
2. `script/` 下可放多个剧本文件：`Script.md`（主线）+ `Script_{外传名}.md`，或按 `script/{剧本名}/` 分子目录
3. **分场分镜头不因剧本而变**：不同剧本 = 不同场次组，统一按 `scenes/{N}_{缩写}/` 全局连续编号（N 跨剧本递增，不按剧本重置）。每个剧本引用自己的场次区间即可
4. 生产资产（keyFrames/sequence/export）按场次存放，天然归属对应剧本

**现有实例**：《孢子纪元》= 单世界观多剧本（主线 + `side_stories/` 铁笼兔灵/机械怪人/烬夜）；《复生协议》= 单世界观单剧本（见 `references/复生协议_案例.md`）。

## 通用目录结构

```
{项目名}/
├── PROJECT.md                  ← ★ 权威结构 + 进度（项目唯一真相源）
├── script/
│   ├── Script.md               ← ★ 剧本（每镜头含 Camera/Movement/Lighting）
│   └── Script_{外传名}.md      ← 同一世界观下的其他剧本（可选，见「世界观与剧本的关系」）
├── world_view/                 ← 世界观视觉宪法（世界级资产，多剧本共享）
│   ├── prompts/                ← ★ 主目录（世界观/MJ 提示词，中英双语）
│   └── images/                 ← 世界观参考图（按幕或主题分子目录）
├── concept/                    ← 概念设计（世界级资产，多剧本共享；每项 = 一个文件夹）
│   ├── character/{名字}/       ← SOUL.md（灵魂定义）+ image/ + prompt/
│   ├── entity/{name}/          ← 非人实体：image/ + prompt/ + reference/
│   ├── location/{Name}/        ← 场景：image/ + prompt/ + ref/
│   ├── prop/                   ← 道具：全量文档 + 单道具文件夹
│   ├── vfx/{name}/             ← 特效：image/ + prompt/ + reference/
│   └── poster/                 ← 海报概念
├── scenes/
│   └── {N}_{缩写}/             ← 每场一个文件夹（N=全局序号跨剧本递增，缩写=英文主题）
│       ├── storyboard/         ← ★ 分镜（镜头确认 + 视频生成参考，见「Storyboard 定位」）
│       ├── keyFrames/          ← ★ 3×3 九宫格关键帧：prompts/ + image/（+ camera_ref/）
│       ├── layout/             ← Blender 白模 .blend + 空间位置参考
│       ├── frameRef/           ← 全彩单帧 look reference（prompt/）【可选】
│       ├── location/           ← 场景设计：images/ + prompts/ 【可选】
│       ├── sequence/           ← 多镜头序列视频：prompts/ + mp4 + edited/
│       ├── shot/               ← 单镜头视频 prompt 【可选】
│       └── {缩写}.pur          ← 剪辑工程文件
├── export/                     ← 成片（final/ 放定稿）
└── reference/                  ← 项目级参考图（structure/ world_view/ 等）
```

## 命名规范（通用）

**场次目录**：`{N}_{缩写}` — `1_CAD`、`2_FWW`（缩写 = 该场英文主题首字母，如 Crisis And Death → CAD）
**镜头编号**：`{缩写}_{4位镜号}` — `CAD_0010`；多镜头区间 `CAD_0010-0040`
**提示词文件**：`{Name}_{type}_{model}_v{N}.txt|md`
- `Name`：对象名，PascalCase — `Xiaowu_CombatSuit`
- `type`：`concept` / `keyframe` / `sequence` / `frame` / `single_shot` / `location` …
- `model`：`gemini` / `gpt` / `jimeng` / `midjourney`(mj) / `seedance`
- 方向词可插入 type 位置：`text_to_image`(t2i) / `image_to_image`(i2i) / `finalframe` / `background` / `topdown`
- 版本：`v001`、`v002`… **永不覆盖旧文件，永远开新版本号**

**硬规则**：
- 图片文件名 = 对应 prompt 文件名（一一对应，方便校对）
- Gemini / GPT prompt 用英文（英文更准）；Jimeng（即梦）i2i 用中文；MJ 用英文
- 文件名用英文/拼音（中文名场景可用中文目录，如 `character/小武/`）

## 工作流管线（文件流向）

```
world_view/（世界观视觉宪法）
  → concept/（角色/实体/场景/道具/VFX 概念设计）
  → scenes/{N}/layout/（Blender 白模，纯空间参考）
  → scenes/{N}/storyboard/（分镜：生成视频前确认每个镜头；可直接作视频参考）【可选】
  → scenes/{N}/keyFrames/（九宫格关键帧，t2i + i2i 多轮迭代）
  → scenes/{N}/sequence/（Seedance 视频生成）
  → export/（剪辑成片）
```

**模型分工**（通用）：
| 模型 | 用途 |
|------|------|
| Gemini 2.5 Flash | 概念设计 + keyframes 的 t2i/i2i（定型主力） |
| GPT | 概念设计 + keyframes 的 t2i/i2i（需 hygiene 规则防脏图） |
| Jimeng 即梦 | i2i keyframes（视频输入用，中文 prompt） |
| Midjourney | t2i 概念/世界观（9 景成套产出） |
| Seedance | 序列视频生成 |

## Storyboard 定位

**Storyboard 是保留流程，两个核心用途：**

1. **视频生成前的镜头确认**：在生成视频前确认每个镜头的情况（构图/内容/衔接），是镜头规划的预览工具
2. **直接作为参考生成视频**：storyboard 图可以直接作为 reference 输入视频模型生成视频

**注意（历史教训）**：B&W 线稿对视频模型有「角色外观污染」风险——线稿画得越好，模型越容易把线稿特征当成角色外观。因此：
- 作为镜头确认/规划工具 → 无碍，放心用
- 直接作为视频生成参考 → 注意角色外观漂移风险，必要时叠加 `concept/` 全彩角色图约束
- 空间关系参考仍以 Blender 白模（`layout/`）为准，storyboard 与白模互补不冲突

## 使用方式

1. **新项目**：按「通用目录结构」初始化空目录 + 写 `PROJECT.md`；若世界观已有其他剧本，`world_view/` + `concept/` 直接复用，只新增 `script/` 剧本文件和自己的场次
2. **命名**：所有新文件按「命名规范」生成
3. **找文件/放文件**：按目录结构定位；不确定时读项目自己的 `PROJECT.md`
4. **参考实现**：`references/复生协议_案例.md` 是完整落地案例（真实项目，含命名细节和踩坑记录）

## References

- `references/复生协议_案例.md` — ★ 复生协议落地案例（目录注释 + 命名细节 + 关键文件 + legacy 踩坑）
- `references/复生协议_full-tree.md` — 复生协议完整文件树（自动生成，332 条）
- `scripts/generate_tree.py` — 重新生成 full-tree（`python3 scripts/generate_tree.py --project-path <项目路径>`）
