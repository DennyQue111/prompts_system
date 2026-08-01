# Gantz × 鬼灭之刃 · 技术拆解版

**用途**：MJ / 动画风格图像生成时，替换动画标题为纯技术词汇，避免角色/人脸污染。
**对应视觉**：Gantz 的硬阴影+写实解剖 + 鬼灭的流动线条+情绪色彩。
**关键约束**：全文禁写 `Gantz`、`Kimetsu no Yaiba`、`Demon Slayer` 或任何作品名。只描述线条/笔触/着色/光影/色彩/构图的纯参数。

---

## 线条

```
sharp clean linework with controlled weight variation, 
precise anatomical contour lines on figures, 
expressive fluid linework on energy effects and water — brush-stroke organic flow,
no scratchy or overly sketchy lines
```

- 锐利、干净的线稿，有控制的粗细变化
- 人物轮廓用精确解剖线
- 能量/水特效线稿流动感强、笔触感

## 笔触 / 材质

```
cel-shaded rendering on figures and hard surfaces with sharp shadow edges,
painterly atmospheric background art with expressive brush texture,
energy and water effects rendered with organic brush-stroke quality,
tactical gear and weapons with hand-drawn mechanical detail — precise but not CAD-sterile
```

- 人物和硬表面：cel 着色，阴影边缘锐利
- 背景：手绘感的情绪笔触
- 特效：有机笔触质地
- 道具：手绘机械精度

## 着色 / 光影

```
hard cel shading with deep black shadows and high light-to-shadow contrast ratio,
sharp rim light edges on figures and gear,
cold blue overall color temperature as dominant ambient,
warm amber emotional accent lighting for intimate moments,
visible on-screen light sources casting dramatic directional shadows
```

- 硬 cel 阴影，高对比度
- 锐利边缘光
- 冷蓝色温为主
- 暖琥珀色用于情绪重音
- 可见光源投射戏剧化方向阴影

## 色彩逻辑

```
cold blue and steel gray as dominant ambient palette,
warm amber and gold as emotional accent colors,
deep crimson for intensity and threat moments,
rich atmospheric color grading with deliberate warm/cool temperature contrast,
muted midtones with saturated shadow colors
```

- 主色域：冷蓝、钢灰
- 情绪点缀：暖琥珀、金
- 强压场景：深红
- 冷暖色温刻意对比
- 中间调沉稳，阴影饱和

## 构图特征

```
dramatic low-angle compositions for scale and power,
compressed telephoto perspective for looming threats,
shallow focus on emotional close-ups with painterly background bokeh,
dynamic diagonal framing for action scenes,
impact frames and motion speed lines for combat intensity
```

- 戏剧化低角度
- 压缩长焦透视
- 浅焦情绪特写
- 动态对角线动作构图
- 冲击帧+速度线

---

## Backbone Preset（直接贴入 prompt）

```
hand-drawn anime keyframe still, sharp clean linework with controlled weight variation, 
precise anatomical contour lines, expressive fluid brush-stroke linework on effects, 
cel-shaded rendering on figures with deep black shadows and high contrast, 
painterly atmospheric background art, 
hard cel shading with sharp rim light edges, 
cold blue dominant ambient color temperature, 
warm amber emotional accent lighting, 
dramatic directional shadows from visible light sources, 
cold blue and steel gray palette with amber gold accent highlights
```

## 人物渲染（有人物时追加）

```
hand-drawn anime character rendering with detailed cel shading, 
realistic facial proportions with anatomical precision, 
expressive eyes with sharp highlights, subtle skin tone gradients, 
visible contour line art on facial features,
no character-specific markings from known series, no distinctive anime protagonist hairstyles
```

## Negative Prompt

```
no photorealism, no photographic film grain, no live-action, no 3DCG render, 
no realistic human skin texture, no photographic lens blur, 
no flat moe anime style, no generic isekai anime, no chibi proportions, 
no soft watercolor-wash rendering, no pastel color palette, 
no known anime character faces, no character-specific markings, 
no CAD-perfect mechanical lines, no synthetic neon color scheme
```

## MJ Parameters

```
--ar 16:9 --stylize 250 --v 8.2
```

备选：偏写实则切 `--niji 6`
