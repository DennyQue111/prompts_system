# Performance · 角色表演层

表演层是 prompts_structure 的上游模块——先有角色如何表演，再有镜头如何拍摄。

## 定位

| 层 | 管什么 | 范例 |
|----|--------|------|
| concept/character | 角色长什么样 | 身高、体型、服装、发型、肤色 |
| **performance/** | 角色怎么演 | 重心、速率、眼神、声线、行为逻辑 |
| sequence/shot | 镜头怎么拍 | 运镜、焦距、时长、衔接 |
| concept/location | 在哪演 | 环境、建筑、光照 |

**表演的本质不是情绪展示，而是压力下的行为。** "愤怒"渲染不出来，"我想让你还钱"可以。

## 文件

| 文件 | 用途 |
|------|------|
| `acting_master_profile.md` | 角色表演主档案模板（150-220 词） |
| `scene_adaptation.md` | 场景级表演改写规则 + 五支柱 |
| `eye_life.md` | 眼部生命系统（所有镜头强制） |

## 使用方式

1. 先生成 Master Profile（角色表演主档案）
2. 写每个镜头时，根据 Scene Adaptation 规则改写表演
3. 确保 Eye Life 规则在有人脸的镜头中始终落实
4. 表演描述写入 Sequence/Shot 的「动作」字段

## 与其他模块的关系

- **不需要参考图**——表演层描述的是行为模式，不是视觉外观
- **Model-agnostic**——适用于任何视频模型（Seedance、即梦、Sora 等）
- **和 concept/character 互补**——concept 管模型知道谁是谁，performance 管模型知道怎么做

## 视频提示词前置检查（强制）

生成任何 MiniMax、Seedance 或即梦视频提示词前，先读取本目录中与当前角色和镜头相关的 `acting_master_profile.md`、`eye_life.md` 与 `scene_adaptation.md`。提交前确认每个角色的具体视线目标、扫描顺序、微跳视、眨眼质量、catchlights 来源、目光→头部→身体的先后；多人同框逐人指定看谁并明确谁不看镜头；动作包含预备、发力、峰值、回收、恢复；摄影机左右与角色自身左右分开定义；武器、义肢和身体状态写明切换时机。
