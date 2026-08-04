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
