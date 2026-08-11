# Midjourney 图片生成 · 反污染方法论

## 核心原则

MJ 没有 negative prompt 字段。它从头到尾只理解一件事：**「我要什么」**。

任何以「不要什么」开头的描述，MJ 都不会识别为否定——它要么当正面描述读进去产生奇怪效果，要么（更好的情况）直接忽略。质量控制靠的是 backbone 的正面词汇密度，不是排除列表。

> 来源：2026-08-02，孢子纪元 v4 9 景 prompt 清理实检——全部 negative block 删除后 prompt 更短、更干净、输出可控性不变。

## 三条铁律

### 1. 不写 negative block

❌ 错误：
```
... --ar 16:9 --stylize 250 --v 8.2
**Negative prompt**: no photorealism, no 3DCG render, no flat moe anime style...
```

✅ 正确：
```
... --ar 16:9 --stylize 250 --v 8.2
```

MJ 会把参数后面的文字当成无效残留或误读为正面描述。写完最后一个参数就停。

### 2. 用 `--no` 只在有人物面部时防 IP 污染

`--no` 是 MJ 唯一真正有效的否定参数，只挂在 `--v 8.2` 后面。**只在有人物面部出镜的场景使用**，且仅写一条。

```
--v 8.2 --no known anime character faces
```

**什么情况不用 `--no`：**
- 纯景观/地景
- 纯生物/妖灵/动物面部
- 纯物体/道具/材质特写
- 无面部可见的人物（远景剪影、背影、手部特写）

原因：backbone 本身已经用正面词汇锁死风格方向——`hand-drawn anime keyframe` + `watercolor-wash` + `fine etching-like linework` 本身就排除了 photorealism、3DCG、flat moe。额外的 `--no` 只在有人脸时防 IP 角色面孔入侵——这是 backbone 挡不住的。

### 3. 正面描述 > 排除描述

| 你担心出现的 | 不要在 prompt 里说「不要」 | 改为正面锁定 |
|---|---|---|
| 照片写实感 | no photorealism | hand-drawn anime keyframe still |
| 3DCG 感 | no 3DCG render | watercolor-wash background rendering |
| 萌系动画 | no moe anime | fine etching-like linework, hand-drawn rendering |
| 好莱坞机甲 | no Hollywood mecha | hand-drawn organic-mechanical hybrid precision |
| CAD 完美线条 | no CAD-perfect lines | subtle offset lines, hand-drawn mechanical detail |
| 高饱和霓虹 | no neon colors | muted earth-tone palette |
| IP 角色面孔 | no known anime character faces | 写在 `--no` 参数中（仅有人物面部时） |

## 结构规范

### Prompt 组成（从左到右）

```
[视觉 backbone] + [场景/主体描述] + [构图/机位] + [渲染细节] + [MJ 参数] + [--no 可选]
```

**每个 prompt 只有一行。** 不分段，不加额外标记。

### Backbone 写法

Backbone 放在 prompt 最开头，用逗号串联，用 6-8 个技术短语锁定风格方向。它本身就是质量闸门：

```yaml
素材媒介: hand-drawn anime keyframe still
线条笔触: fine etching-like linework, watercolor-wash background rendering
密度质感: dense organic texture detailing through layered fine brush strokes
光影逻辑: soft gradient shading, diffused ambient lighting, atmospheric bloom
色彩温度: muted earth-tone palette — deep green ochre warm brown moss teal base
纵深处理: blue-green atmospheric perspective fading into pale mist
```

### 参数区规范

```yaml
通用: --ar 16:9 --stylize 250 --v 8.2
有人物面部: --ar 16:9 --stylize 250 --v 8.2 --no known anime character faces
偏插画/二次元: 可试 --niji 6（替代 --v 8.2）
```

## 常见污染源 & 对策

| 污染源 | 如何进入 prompt | 对策 |
|---|---|---|
| `Negative prompt:` block | 从 SD/Flux 模板惯性带入 | 全部删除。MJ 不理解这个字段 |
| `no X, no Y, no Z` 堆在描述中 | 试图用否定词控制 | 改为正面描述。MJ 对否定词识别不稳定 |
| 过多技术参数 | `24mm, f/2.8, ISO 400, Arri Alexa` | MJ 动画风格下全部不用。用构图描述替代焦距 |
| 摄影皮肤串 | `real human detailed skin, visible pores` | 动画风格下全部不用。用 `soft gradient skin shading` |
| IP 作品名 | `Gantz-inspired, Demon Slayer style` | 绝对禁止。全部拆解为 6 维技术词汇 |
| 参数后继续写内容 | 写完 `--v 8.2` 后又加描述 | 写完参数立刻停。参数后面什么都不能有 |

## 与 GPT image hygiene 的分工

| | GPT hygiene | MJ hygiene |
|---|---|---|
| 核心问题 | 过度微纹理、浑浊阴影、贴图感 | 无 negative 字段、参数后内容被误读 |
| 解决策略 | Clean Rendering Block 逐 artifact 封堵 | backbone 正面锁定 + `--no` 只在必要时使用 |
| 参数体系 | 无参数区，全部写在 prompt 正文 | prompt 正文 + `--ar / --stylize / --v / --no` |
| 共性 | 禁止作品名、禁止摄影皮肤串（各自适配）、正面描述优先 | 同左 |

---

> 创建：2026-08-02 | 触发：孢子纪元 v4 9 景 MJ prompt 负面块清理实检
> 适用范围：所有 MJ 平台的 prompt_structure 产出

---

## 续篇：Prompt 结构顺序 & 词污染（2026-08-09）

> 来源：孢子纪元 v11 异能者列传——岩蛟/熊灵反复全身机甲不出人脸，三轮调试后锁定根因。

## 核心发现

MJ v8 对 prompt 是**顺序敏感**的——更准确地说，是**顺序优先级递减**：越靠前的词权重越高，越靠后的词权重越低。

当 prompt 开头的词与后面的词产生冲突时，**前面的赢、后面的被覆盖**。

## 三条新铁律

### 4. 优先级递减：主体必须在最前面

MJ 按从左到右的优先级处理 prompt。前 ~20 个词锁死画面主体方向，后面的描述只能在前面的框架内微调。

**规则**：你想要什么 → 把它放在最前面。不是「在 prompt 里写清楚就行」，而是要写在最前面。

**通用表述**：
```
prompt 核心主体的描述必须在 prompt 的最前端。
如果主体是人物面部 → 面部描述在前 5 词。
如果主体是机甲 → 机甲描述在前 5 词。
如果主体是建筑 → 建筑描述在前 5 词。
```

### 5. 前后内容不可冲突——写完需复查覆盖关系

Prompt 中如果有 A、B 两个描述互相冲突（A 隐含 B 不可能），MJ 会取**先出现的**，后出现的被忽略。

**规则**：写完 prompt 后，检查是否存在以下覆盖模式：
- 写了「脸」又写了「全覆式头盔」→ 头盔在前则脸消失，脸在前则头盔消失
- 写了「裸露皮肤」又写了「全身铠甲」→ 先写哪个，哪个生效
- 写了「透明」又写了「不透明」→ 先写的生效

**正面写法**：明确想要什么、不想要什么，但不要说「不要 X 要 Y」——直接只写 Y，把 X 排除在 prompt 之外。

❌ 冲突写法：
```
A heavily-built warrior in full battle armor — face visible
```
「full battle armor」隐含全覆式 → face 被覆盖。

✅ 无冲突写法（想露脸）：
```
A man with bare head and face clearly visible — armor plates on shoulders and forearms
```
armor 只限定在肩臂，不隐含覆盖面部。

✅ 无冲突写法（想全机甲）：
```
A heavily-built warrior in full sealed battle armor — helmet with angular visor, no skin visible
```
全机甲就写全机甲，不写 face。

### 6. 复查清单

写完 MJ prompt 后过一遍：

- [ ] **主体是什么？它在前 5 个词吗？**
- [ ] **有无冲突描述？**（如同时提到露脸 + 头盔/面罩/全身甲）
- [ ] **后出现的描述是否会覆盖前面的？**（如前面写 face visible，后面写 helmet）
- [ ] **如果想露某个部位（脸/手/皮肤），prompt 中有没有任何词暗示它被遮盖？**
- [ ] **style 描述是否只出现一次？**

## 实战案例：岩蛟 v1→v4 调试记录

| 版本 | 状态 | 问题 | 诊断 |
|---|---|---|---|
| v1 | ❌ 全身机甲无脸 | face 在 ~80 词，warrior + heavy battle armor 在前 10 词 | 优先级递减：armor 在前，face 被覆盖 |
| v2 | ❌ 加 helmet visor retracted 仍无脸 | 写了 helmet 这个词，且仍在 armor 描述之后 | 冲突未解决：helmet 即使 retracted 仍然「存在」 |
| v3 | ❌ 删 helmet、负面向加 no helmet | 负面约束中出现了 helmet 词，MJ 仍识别 | MJ 对实体名词敏感，no helmet 里的 helmet 照样触发 |
| v4 | ✅ 出脸 | face 移至第 4 词、全文零冲突词、warrior→man、armor 弱化 | 优先级 + 无冲突 + 正面描述 |

**案例总结**：
- 目标是露脸 → face 写最前面、不写任何遮盖面部的东西（包括否定式）
- 案例中 `warrior→man`、`battle armor→armor plates` 只是这个特定场景的替换——**通用原则是优先级递减 + 防冲突，不是某个具体词的替换**

## 典型冲突场景速查

| 你想要 | 检查 prompt 中是否有 | 处理 |
|---|---|---|
| 人脸露出 | helmet, mask, visor, faceplate, full-coverage, sealed | 全部删除。正面写 bare head / face visible |
| 全机甲 | face, skin, bare, exposed | 全部删除。正面写 full sealed armor / helmet |
| 举手/手部特写 | gauntlet 覆盖全手, hidden hands | 删掉覆盖描述，正面写 bare hands / fingers visible |
| 皮肤/身体露出 | full body armor, full-coverage | 限定 armor 范围（shoulders/chest/legs only） |

## 检查清单

写 MJ prompt 前过一遍：

- [ ] 主体在前 5 词
- [ ] 全文无冲突描述（想要 X 露出 → 没有任何词暗示 X 被遮盖）
- [ ] 如果 topic 变了（如全机甲场景），上述规则反向适用——不要生搬硬套
- [ ] style 只写一遍
