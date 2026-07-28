# 来自深渊 · 技术拆解版

**用途**：MJ / 动画风格图像生成时，替换动画标题为纯技术词汇，避免角色/人脸污染。
**对应视觉**：《来自深渊》式的纤细手绘 + 水彩背景 + 软环境光 + 有机×机械交织质感。
**关键约束**：全文禁写 `Made in Abyss` 或任何作品名。只描述线条/笔触/着色/光影/色彩/构图的纯参数。

---

## 线条

```
fine etching-like linework with consistent thin weight, no thick battle-shonen outlines, 
no ink splatter, no sketchy line variation
```

- 纤细均匀，铜版画质感
- 有机但精致，不粗细不一
- 不飞墨，不速写式

## 笔触 / 材质

```
watercolor-wash background rendering with soft bleeding color transitions,
dense organic texture detailing through layered fine brush strokes,
hand-drawn organic-mechanical hybrid precision — machine parts with subtle hand-drawn offset, not CAD-perfect lines
```

- 背景水彩晕染，色块互渗，边缘不硬
- 有机物（苔藓、树皮、菌类）密集细笔触层叠
- 机械部件手绘偏移，非 CAD 直线

## 着色 / 光影

```
soft gradient shading, no hard cel shading edges,
diffused ambient lighting with atmospheric bloom and gentle light falloff,
bioluminescent glow rendered as soft halo, not sharp highlights,
blue-green atmospheric perspective fading into distance
```

- 软渐变着色，不 cel 硬阴影
- 环境光：生物荧光、天光、雾中散射
- 高光是柔光环，不是锐利白点
- 远景蓝绿色空气透视，颜色随距离洗淡

## 色彩逻辑

```
muted earth-tone palette: deep green, ochre, warm brown, moss teal as base,
accent highlights: cyan, soft pink, amber gold as bioluminescent glow,
no high-saturation neon colors, no synthetic color palette
```

- 主色域：深绿、赭石、暖棕、苔青
- 点缀色：青蓝、柔粉、琥珀金
- 零高饱和霓虹色

## 构图特征

```
extreme vertical depth layering from foreground to distant background,
scale contrast: tiny figures dwarfed by massive environment,
foreground framing elements like tree trunks or giant leaves creating a peeking-through composition,
natural lens-like depth of field with foreground and background soft blur
```

- 极端前中后景垂直分层
- 渺小人物 vs 巨大环境
- 前景框架物制造窥视感
- 自然景深模糊

---

## Backbone Preset（直接贴入 prompt）

```
hand-drawn anime keyframe still, fine etching-like linework with consistent thin weight, 
watercolor-wash background rendering with soft bleeding color transitions, 
dense organic texture detailing through layered fine brush strokes, 
hand-drawn organic-mechanical hybrid precision, 
soft gradient shading with diffused ambient lighting and atmospheric bloom, 
bioluminescent glow rendered as soft halo, 
blue-green atmospheric perspective, 
muted earth-tone palette — deep green ochre warm brown moss teal base, 
cyan soft-pink amber-gold accent highlights, 
extreme vertical depth layering with foreground framing elements, 
scale contrast between tiny figures and massive environment
```

## 人物渲染（有人物时追加）

```
hand-drawn anime character rendering with soft gradient skin shading, 
delicate facial features without heavy outlines, 
subtle skin tone variation, 
natural proportions without exaggerated anime features, 
no character-specific markings, no scar patterns, no distinctive hair styles from existing series
```

## Negative Prompt

```
no photorealism, no photographic film grain, no live-action, no 3DCG render, 
no realistic human skin texture, no photographic lens blur, 
no flat moe anime style, no generic isekai anime, no chibi proportions, 
no thick battle-shonen outlines, no ink splatter, no hard cel shading edges, 
no high-saturation neon colors, no CAD-perfect mechanical lines, 
no known anime character faces, no character-specific markings or scars
```

## MJ Parameters

```
--ar 16:9 --stylize 250 --v 8.1
```

备选：偏写实则切 `--niji 6`
