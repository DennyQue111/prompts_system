---
name: shot-planning
description: 将剧本大纲或场次剧本设计成可执行的镜头表，安排叙事信息、人物动作、空间关系与镜头衔接，并输出关联的 concepts 与 shot_breakdown JSON。用于故事板和逐镜生成之前的镜头规划。
---

# Shot Planning

先把剧本大纲或场次剧本拆成叙事拍点，明确每段的情绪、观众需要获得的信息、角色的行动与反应，以及场景空间和动作连续性；再设计镜头覆盖，最后转化为概念资料与镜头拆分表两个关联 JSON 文件。输出供后续故事板与逐镜生成使用；本 skill 不生成媒体或平台提示词。

## 输出规则

- 必须生成两个独立且可解析的 JSON 文件：`{PROJECT_CODE}_concepts.json` 与 `{PROJECT_CODE}_shot_breakdown.json`；不要把 concepts 与 shots 合并到同一个文件。
- 两个文件必须使用相同的 `project_id`、`project_code`、`project_name` 与 `schema_version: 2`。
- `concepts` 文件只包含 `characters`、`locations`、`props`；`shot_breakdown` 文件只包含 `shots` 与 `concepts_file` 引用。
- 角色、场景、道具只在 concepts 文件中描述一次；镜头通过稳定的 `id` 引用它们，避免重复外貌或环境文字。
- 若剧本已经提供镜头号、焦段、机位、方位、运镜或时长，忠实保留，不重写导演意图。剧本未规定时，做克制、连续、可拍摄的补充，不臆造剧情、角色、道具、对白或风格。
- 先在内部完成逐场拆分和连续性检查，再生成两个文件。不要输出内部分析。
- 如果用户明确指定输出目录，在确认 JSON 合法后将两个文件写入该目录；没有指定目录时，返回两个完整 JSON，并清楚标明各自文件名。

## 镜头调度与覆盖

拆分每个场景时，主动考虑镜头类型搭配，避免“一段内容一个镜头”的平铺直叙：

- **建立镜头**：每个新场景、或人物位置关系发生变化时，先安排一个中远景／全景机位，交待谁在哪、面向谁、环境关键地标。后续反打和特写都依赖这个空间基准。
- **正反打**：对话场景不要用一个双人镜头覆盖到底；在关键信息交换处拆出说话者镜头与听者镜头，过肩或干净单人镜头均可。
- **反应特写**：重要台词、信息揭示或情绪转折点之后，给听者一个反应镜头（特写或近景），即使他没有台词。
- **细节插入镜头**：对叙事关键的道具、手部动作、书面内容，可单独给插入镜头，不把信息全挤在全景里。
- **景别变化**：同一场内混合远／全／中／近／特，避免连续三个镜头使用同一景别和同一机位方向。
- **克制原则**：以上是“该有则有”，不是凑数。每个镜头必须有明确叙事功能（交待、推进、反应、强调）；剧本明确一镜到底或长镜头调度时，忠实保留导演意图。

时长按动作、对白和情绪停顿估算。若目标视频模型难以在一个生成片段内完成该镜头，可拆成连续镜，并在后一镜 `continuity` 写明与前镜尾帧和动作余势的衔接；不要把某个模型的默认时长当成分镜规则。

## Project Identity and Filenames

1. 将剧本名称翻译为简短英文工作名，并取英文单词首字母作为大写 `PROJECT_CODE`。例如“孢子纪元” → `Spore Age` → `SA`。用户明确提供项目代号时，始终优先使用用户代号。
2. 默认 `project_id` 为当天日期加项目代号：`YYYYMMDD_PROJECT_CODE`。例如 2026-09-18 的“孢子纪元”为 `20260918_SA`。
3. 默认文件名为 `{PROJECT_CODE}_concepts.json` 与 `{PROJECT_CODE}_shot_breakdown.json`，例如 `SA_concepts.json`、`SA_shot_breakdown.json`。
4. 日期加代号无法覆盖“同一天、同一代号、重复创建”的情况。写入目录前如发现同名项目 ID 或文件已存在，不要覆盖：使用递增后缀，例如 `20260918_SA_02`、`SA_02_concepts.json`、`SA_02_shot_breakdown.json`；或按用户提供的新代号处理。

## Canonical JSON Schemas

### `{PROJECT_CODE}_concepts.json`

```json
{
  "project_id": "20260918_SA",
  "project_code": "SA",
  "project_name": "孢子纪元",
  "schema_version": 2,
  "characters": [
    {
      "id": "xiaowu",
      "name": "小武",
      "description": "仅保留跨镜头一致所需的身份、外观和关键服装/义体信息。",
      "reference_images": []
    }
  ],
  "locations": [
    {
      "id": "loc_slum_t_intersection",
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
  ]
}
```

### `{PROJECT_CODE}_shot_breakdown.json`

```json
{
  "project_id": "20260918_SA",
  "project_code": "SA",
  "project_name": "孢子纪元",
  "schema_version": 2,
  "concepts_file": "SA_concepts.json",
  "shots": [
    {
      "id": "SAE_0010",
      "shot_no": "SAE_0010",
      "scene": "SAE",
      "location": "loc_slum_t_intersection",
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

### Project IDs and references

- `project_id` 是两个文件的关联键；`concepts_file` 必须等于同批次生成的 concepts 文件名。
- `id` 使用稳定、简短、ASCII 的 snake_case；镜头 `id` 和 `shot_no` 可以使用剧本既有编号，如 `SAE_0010`。
- `shots[].scene` 是剧本中的场次／场景代号，例如 `SAE`；它不引用 concepts 文件。
- `shots[].location` 必须等于一个 `locations[].id`，用于引用该镜头所处的稳定环境概念。
- `shots[].characters` 只包含 `characters[].id`。
- `props` 不必在每个镜头重复列出；只有影响镜头叙事或连续性时，在 `action` 或 `continuity` 中以名称说明状态。

### Concepts

- `characters[].description`：只放跨镜头一致所需的可见身份信息，不写剧情、情绪史或每镜头动作。
- `locations[].environment`：只放固定空间关系、关键地标、基础时间/光源信息，不复制每镜头构图。
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
2. 每个镜头都有 `id`、`shot_no`、`scene`、`location`、`duration`、`characters`、完整 `camera`、`action`、`dialogue`、`continuity`、`reference_images`。
3. 两个文件的 `project_id`、`project_code`、`project_name`、`schema_version` 一致，且 `concepts_file` 正确指向 concepts 文件。
4. location、角色 ID 引用存在且不重复；镜头编号按剧本顺序排列。
5. 每段关键动作和对白至少被一个镜头覆盖；没有为了“丰富”而新增剧情。
6. 相邻镜头的方向、人物位置、道具状态和动作余势在 `continuity` 中可追踪。
7. 每个场景有可追踪的空间基准（建立镜头或等效交待）；对话场景在关键信息交换处有正反打或反应镜头覆盖，情绪转折点有反应特写；同一场内景别与机位方向有变化。
8. 单镜 `duration` 能容纳动作、对白及必要反应；长镜头若需分段生成，已标注片段之间的动作衔接。
9. 不写 `prompt`、`generation_prompt`、`negative_prompt`、平台模型名或媒体生成参数；这些由下游视频提示词 Agent 处理。
