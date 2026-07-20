# Prompt Hygiene — 提示词污染防控

_横切规则：撰写 concept / storyboard / frame / shot 四种产出类型时均须遵守。_

核心原则只有一句话：**告诉模型"当前画面里明确看见什么"，不要告诉它"别生成什么旧错误"。**

---

## 规则 1：否定词是最高风险污染源

❌ `no photorealistic rendering, not live-action, avoid 3D CGI look`
→ 模型听到了 photorealistic、live-action、3D CGI，联想已被激活。

✅ `cel-shaded, 2-3 flat tone levels, uniform outline weight, no gradient blending in shadows`
→ 模型只听到正向目标。

> **铁律：如果某个词不是当前画面必须存在的东西，就别让它出现在 prompt 里。** 包括 "not" "no" "avoid" "unlike" "instead of"。

---

## 规则 2：强联想词要拆成视觉证据

❌ `GANTZ:O style, Demon Slayer aesthetic`
→ 模型对这两个标签的理解不稳定，一个偏 3D 一个偏 2D，可能打架。

✅ `hard-edged cel shading with 2–3 discrete shadow tones, no gradient transition between light and dark areas, character outlines at uniform 2–3px black line weight, metallic surfaces rendered as sharp specular highlights on flat tone, dark sci-fi palette with deep crushed blacks and selective neon rim lighting`
→ 每个词都是画面里可见的东西。

> **如果一个词会召唤某种风格、职业、场景或刻板印象，就拆成"镜头里实际看得见的证据"。**

---

## 规则 3：修正错误 = 重写目标，不是描述旧错误

❌ `Fix the hand from last generation. Make the fingers count correct this time. Not like the version where the ring box was floating.`
→ 模型被"错误的手""漂浮的戒指盒"锚定了。

✅ `Xiao Wu's right hand rests on the steering wheel — five distinct fingers, thumb hooked over the top of the wheel, index finger lifted mid-tap. The red ring box sits firmly on the passenger seat fabric, its base flush with the seat surface, lid closed.`
→ 这是一张全新的、干净的画面描述。

> **迭代时永远不要复述旧 prompt、旧画面、旧错误。直接重写当前镜头。**

---

## 规则 4：抽象词要转成画面证据

| 不说这个（抽象） | 说这个（可见） |
|-----------------|---------------|
| "他感到恐惧" | 肩膀耸起贴近耳朵，瞳孔收缩，嘴唇微张，身体后倾 10° 远离危险方向 |
| "气氛压抑" | 顶光源单点打在人物身上，四周全黑，人物占画面底部 20%，上方 80% 为深黑负空间 |
| "她在思考" | 眼神焦点落在画面外某处，右手无意识地摩挲左手指节，嘴唇轻微抿紧 |
| "关系疏远" | 两人间距超过一臂，视线无交集，前景物体（桌面/栏杆）插入两人之间 |
| "战斗激烈" | 画面中 3–5 条速度线，碎屑悬浮在空中不同深度层，人物衣服边缘有撕裂飘动 |

> **意图、注意力、关系、情绪、身份——这些都是不可见的。转成身体朝向、遮挡关系、手的位置、画面占比、光影边缘。**

---

## 规则 5：镜头词要补上"这个镜头会看到什么"

❌ `Close-up of Xiao Wu.`
→ 模型可能给一个从鼻子到下巴的僵硬人像。

✅ `Close-up: Xiao Wu's face occupies 65% of frame, framed from brow ridge to just below chin. His right eye catches a sharp catchlight — a tiny white specular dot on the cornea. The skin texture at his temple shows subtle tension: a faint crease forming as his brow lifts. Depth of field drops off sharply — his ears and hair edges are slightly soft.`
→ 模型知道这个 close-up 具体"关"的是哪个范围。

> **"中景"不是 magic word。告诉模型：主体占画面多高、能看到什么边界、什么在焦点内什么在外面。**

---

## 规则 6：迭代只改一个变量，其余保持不动

```
上一轮：角色 ok ✅ → 动了 → 场景 ok ✅ → 动了 → 镜头角度 ok ✅ → 不动 → 光影 ❌ → 改了再跑
```

- 迭代修正时：保留成功的文字描述原样不动，只替换失败的那一个变量
- 不要 paste 旧 prompt 后加修改——重写完整的新 prompt，但除了要改的那一个变量，其余逐字照抄成功版本
- 如果三处都失败——不是同时改三处，是重跑一轮只改一处、确认后再改下一处

> **调试 prompt 像调试代码：一次只改一行，才知道是哪行修好了。**

---

## 规则 7：禁止叙事元数据

图像/视频模型不需要知道项目内部的组织信息。任何仅对人类有意义的叙事标签都属于污染。

❌ `SCENE 01 — SUBURBAN RING ROAD`
❌ `复生协议 · 第一幕`
❌ `Character concept sheet for Xiao Wu`
❌ `This is the establishing shot for Sequence 3`
❌ `属于《复生协议》世界观`

✅ 直接描述画面内容，不加场号、项目名、剧本背景、角色隶属关系等元数据：
`A wide four-lane elevated ring road at midnight, cutting through the outer edge of a Chinese city...`

> **例外**：多面板合成图的面板位置标签保留（`TOP-LEFT — MAIN VISUAL`、`BOTTOM ROW — COLOR PALETTE` 等），因为这是模型渲染布局所需的功能性指令，不是叙事元数据。

---

## 通用负面限制（唯一允许的 forbid list）

以下为**所有项目通用**的失败类型——不涉及任何具体角色/场景/道具，可以放入 forbid list：

`identity drift, character face mismatch between frames, outfit color shift, prop deformation, extra limbs or digits, random camera rotation, style drift from cel-shaded to photorealistic, subject blur, spatial jump, floating objects defying scene gravity`

**禁止放入 forbid list 的内容：** 本项目的角色名、道具名、场景名、具体颜色、具体动作。这些是对当前画面"应该出现什么"的描述，不应该出现在负面列表里。

---

## 写作前自检（三问）

写完一个 prompt 后，快速扫一遍：

1. **有否定词吗？** → 转成正向画面描述
2. **有抽象词吗？** → 拆成可见的身体/空间/光影证据
3. **有关键词堆叠吗？** → 每个标签词后面都跟一个"这意味着镜头里看到什么"
