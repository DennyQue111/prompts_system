# Eye Life · 眼部生命系统

## 是什么

视频模型在面部特写中最容易暴露"假"的地方是眼睛——死眼（固定凝视、不眨眼、玻璃质感 catchlights）是最常见的失败模式。眼部生命系统给每个有人脸的镜头提供**可执行的眼部行为描述**，不是"眼睛要有神"这种模糊指令。

## 强制规则

**任何出现可辨识人脸的镜头，动作字段中必须包含眼部行为描述。** 人物越多镜头越近 → 眼部描述越详细。远景 / 背影 / 面具 → 可省略。

## 四项必须描述的眼部行为

### 1. 微跳视（Micro-saccades）

活的眼球永远不会完全静止。微跳视是眼球每秒 2–3 次的微小跳动——不写出来，模型就会给一个凝固的凝视。

```
写法：在"看"的动作中植入扫描路径。

"His eyes shift rapidly — mirror → passenger's hands → door lock — a constant quiet scan, never resting on one point for more than two seconds."
```

**关键**：先定义扫描对象（他在看什么），再定义扫描顺序和节奏。对象要具体——不是"扫视环境"，是"镜子里的人 → 他手里的东西 → 门口"。

### 2. 眨眼质量

不只是"b links"——要写眨眼的**速率**（快/慢/不均匀）、**质感**（轻合/用力挤/不对称）、**和情绪的关联**。

| 眨眼类型 | 写法 | 使用场景 |
|----------|------|----------|
| 慢眨眼 | "slow, deliberate blinks, as if each one interrupts a thought" | 沉思、评估、克制 |
| 快眨眼 | "rapid shallow blinks, staccato rhythm" | 紧张、撒谎、信息过载 |
| 长时间不眨 | "long intervals between blinks, eyes wide and fixed" | 恐惧、威胁、极端专注 |
| 突发的快速一眨 | "a sudden sharp blink as the word lands" | 被击中、突然理解、刺痛 |
| 不对称闭眼 | "one eye closes a fraction before the other" | 怀疑、审视、歪头时 |

```
Good: "Blinking is slow and deliberate, a long blink punctuating the end of each assessment."
Bad: "He blinks."
```

### 3. Catchlights（眼内高光）

Catchlights 是眼睛"活着"的视觉锚点——但写错了就会变成玻璃眼。必须描述光源位置、形状、**是否移动**。

```
Good: "Catchlights are low and warm — a dim dashboard reflection, shifting slightly with each small head movement."
Bad: "Bright catchlights in eyes."
```

关键规则：
- **Catchlights 必须有来源**——不是"眼睛里有个亮点"，是"窗户/屏幕/灯光在角膜上的反射"
- **Catchlights 随头部运动微移**——完全固定的 catchlights = 死眼
- **暗场景中 catchlights 更关键**——因为没有环境光填充，catchlights 是唯一让眼睛不像窟窿的东西

### 4. 目光先行（Eyes Lead Thought）

活的注意力转换是**眼睛先动，然后头转，最后身体跟上**。眼睛→头→身体的时间差距就是"思考"的视觉证据。

```
Good: "Her gaze drifts to the door a full beat before her head turns — the body catching up to a thought already formed."
Bad: "She looks at the door."
```

| 行为 | 意义 |
|------|------|
| 目光先于头部移动 | 主动注意——她自己在想 |
| 头先于目光移动 | 被动反应——她听到了什么 |
| 目光和头同时移动 | 习惯性/机械性——可能不真实 |

## 眼部描述模板（直接填入动作字段）

```text
Eye life: [注意力锚点 — 在看什么] → [扫描路径和节奏] → [眨眼质量] → [catchlights 来源和质感] → [目光与头的时间关系].

示例：
"Eye life: His attention anchors on the rear-view mirror — a quiet triangular scan (mirror → passenger's hands → door lock → mirror) with long intervals between each shift. Blinks are slow and deliberate, each one a punctuation mark at the end of an assessment. Catchlights are low and dim — dashboard reflection, shifting subtly with his breathing. His gaze settles on each target a beat before his head ever turns — the thought arrives first, the body follows."
```

## 镜头距离与眼部细节比例

| 镜头距离 | 眼部描述级别 |
|----------|-------------|
| ECU（极端特写，只有眼睛） | 四项全写，极度详细——微跳视路径、眨眼不对称、catchlights 形状变化 |
| CU（特写，脸占画面大半） | 写三项：扫描路径 + 眨眼质量 + catchlights |
| MCU（中近景，头肩） | 写两项：扫描路径 + 眨眼质量 |
| MS（中景，上半身可见） | 写一项：扫描对象和大致节拍 |
| LS / ELS（远景） | 省略或只写"gaze direction" |
| 背影 / 头盔 / 面具 | 整个省略 |

## 关键规则

1. **眼神是行为，不是表情。** "愤怒的眼神"渲染不出来。"他盯着欠债人的左手——那只手在裤缝上刮擦"可以。
2. **先写看什么，再写怎么看。** 扫描对象必须具体——"他在看门把手上的手印"比"他在看房间"有用一万倍。
3. **Catchlights 必须有来源。** 没有来源的 catchlights = 玻璃眼。
4. **人越多越要明确——谁在看谁。** 三人同框时，每个人的目光锁死一个具体目标，不允许"大家互相对视"这种模糊描述。
5. **眨眼和微跳视分开写。** 微跳视是眼球的微小跳动（扫描路径），眨眼是眼睑的开合——两个独立的生理行为。
