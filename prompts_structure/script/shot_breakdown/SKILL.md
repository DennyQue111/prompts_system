---
name: script-shot-breakdown
description: 将影视剧本拆分为可直接导入镜头表管理页的 schema_version 2 JSON。适用于需要角色、场景、道具与逐镜头摄影信息的剧本结构化，不生成图片、视频或平台提示词。
---

# Script Shot Breakdown

将剧本转化为镜头表管理页的唯一数据结构。输出用于后续由其他 Agent 编写 Seedance、MiniMax 等单镜头提示词；本 skill 只拆镜头，不生成媒体或视频提示词。

## 输出规则

- 输出必须是一个可解析的 JSON 对象；不要包裹 Markdown 代码块、解释、标题或注释。
- 顶层固定使用 `schema_version: 2`，并使用 `characters`、`scenes`、`props`、`shots` 四个数组。
- 角色、场景、道具只在各自数组中描述一次；镜头通过稳定的 `id` 引用它们，避免重复外貌或环境文字。
- 若剧本已经提供镜头号、焦段、机位、方位、运镜或时长，忠实保留，不重写导演意图。剧本未规定时，做克制、连续、可拍摄的补充，不臆造剧情、角色、道具、对白或风格。
- 先在内部完成逐场拆分和连续性检查，再一次性输出完整 JSON。不要输出内部分析。
- 如果用户明确指定输出路径，在确认 JSON 合法后写入该路径；没有指定路径时，仅返回 JSON。

## Canonical JSON Schema

```json
{
  "name": "项目或剧本名称",
  "schema_version": 2,
  "characters": [
    {
      "id": "xiaowu",
      "name": "小武",
      "description": "仅保留跨镜头一致所需的身份、外观和关键服装/义体信息。",
      "reference_images": []
    }
  ],
  "scenes": [
    {
      "id": "SAE",
      "name": "贫民区 T 路口",
      "time": "夜",
      "environment": "仅保留跨镜头稳定的空间、光源、地面与关键地标。",
      "reference_images": []
    }
  ],
  "props": [
    {
      "id": "amber_relic",
      "name": "琥珀遗物",
      "description": "仅当该道具需要跨镜头保持身份、位置或状态时收录。",
      "reference_images": []
    }
  ],
  "shots": [
    {
      "id": "SAE_0010",
      "shot_no": "SAE_0010",
      "scene": "SAE",
      "duration": 4,
      "characters": ["xiaowu"],
      "camera": {
        "framing": "背面膝上景",
        "lens": "50mm",
        "height": "低机位",
        "movement": "缓慢跟拍"
      },
      "action": "镜头内实际可见的角色行动、道具状态和画面事件。",
      "dialogue": [],
      "continuity": "与上一镜头衔接所必需的空间方位、视线、角色姿态、道具状态或运动方向。",
      "reference_images": []
    }
  ]
}
```

## Field Requirements

### IDs and references

- `id` 使用稳定、简短、ASCII 的 snake_case；镜头 `id` 和 `shot_no` 可以使用剧本既有编号，如 `SAE_0010`。
- `shots[].scene` 必须等于一个 `scenes[].id`。
- `shots[].characters` 只包含 `characters[].id`。
- `props` 不必在每个镜头重复列出；只有影响镜头叙事或连续性时，在 `action` 或 `continuity` 中以名称说明状态。

### Concepts

- `characters[].description`：只放跨镜头一致所需的可见身份信息，不写剧情、情绪史或每镜头动作。
- `scenes[].environment`：只放固定空间关系、关键地标、基础时间/光源信息，不复制每镜头构图。
- `props`：只收录持续出现、被交互或身份必须锁定的重要道具；一次性道具可留在相关镜头的 `action`。
- `reference_images` 初始化为 `[]`，由镜头表管理页后续维护。

### Shots

- `duration` 是秒数，使用数字；剧本没有明确时按动作和对白作保守估算。
- `camera.framing` 写景别和必要视角，例如“正面中景”“背面膝上景”“平视近景群像”。
- `camera.lens` 写明确焦段；原剧本未指定时可省略为 `""`，不要凭空加入复杂镜头语言。
- `camera.height` 写机位高度或角度；未指定时为 `""`。
- `camera.movement` 写固定、跟拍、缓推、横摇等摄影机行为；未指定且画面应静止时写“固定镜头”。
- `action` 只写这一镜可见的画面、动作、反应和必要道具状态，不写模型平台提示词、风格词或冗长人物设定。
- `dialogue` 必须是数组；每条格式为 `{ "speaker": "角色名", "line": "台词", "tone": "语气" }`。没有对白时使用 `[]`。
- `continuity` 只记录下一次生成或剪辑真正需要的连续性锚点。独立镜头可为 `""`。

## Quality Check Before Delivery

检查并修复后再输出：

1. JSON 可解析，所有数组和对象闭合，字段名与 schema 完全一致。
2. 每个镜头都有 `id`、`shot_no`、`scene`、`duration`、`characters`、完整 `camera`、`action`、`dialogue`、`continuity`、`reference_images`。
3. 场景、角色 ID 引用存在且不重复；镜头编号按剧本顺序排列。
4. 每段关键动作和对白至少被一个镜头覆盖；没有为了“丰富”而新增剧情。
5. 相邻镜头的方向、人物位置、道具状态和动作余势在 `continuity` 中可追踪。
6. 不写 `prompt`、`generation_prompt`、`negative_prompt`、平台模型名或媒体生成参数；这些由下游视频提示词 Agent 处理。
