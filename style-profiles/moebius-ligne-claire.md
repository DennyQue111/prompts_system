# Moebius · 清线幻想（Ligne Claire）

**用途**：MJ 图像生成，替换水彩/软渐变风格为 Moebius 式的法式清线平面美学。
**对应视觉**：Moebius（Jean Giraud）式的均匀细线 + 平面色块填充 + 超现实有机形态 + 广阔构图中的渺小人物。
**关键约束**：全文禁写 `Moebius`、`Jean Giraud`、`Ligne Claire`、`Arzach` 或任何作品名。只描述线条/着色/色彩/构图/形态的纯参数。

**适合场景**：奇异地理、有机×机械交织、陌生生态、幻想世界的"清晰可见的怪异"——不是模糊的梦，而是极其清晰的异世界。

---

## 线条

```
clean uniform thin outline around every form — ligne claire precision,
consistent line weight with no thick-to-thin variation,
no hatching, no cross-hatching, no ink splatter,
every object fully enclosed by a continuous thin contour line,
linework reads as precise hand-drawn ink — not mechanical, not sketchy
```

- 均匀细线，无粗细变化
- 每个形态都有完整封闭的轮廓线
- 零排线、零交叉线、零飞墨
- 精密但不机械——是手绘的精确，不是 CAD 的直线

## 着色 / 光影

```
flat color areas with minimal internal shading,
shadows rendered as separate flat color planes with clear thin outlines dividing them — 
not gradient blended, not soft airbrush,
no atmospheric bloom, no soft light falloff, no ambient occlusion,
light and shadow are distinct outlined shapes of different color,
three-tone shading at most: base color + one shadow tone + occasional highlight plane,
daylight scenes: open and bright with minimal shadow,
night scenes: deep colored shadows but still rendered as flat distinct shapes
```

- 平面色块填充，阴影是独立的有轮廓色面
- 不渐变、不喷枪、不柔光漫射
- 最多三层色调：基色 + 一阶阴影 + 偶尔高光面
- 日景开放明亮、少阴影；夜景用深色面但仍然是平涂

## 笔触 / 纹理

```
no watercolor wash, no brush stroke texture, no impasto,
texture comes from dense subject-matter linework — 
intricate surface details drawn with the same fine uniform line,
not from rendering technique or material simulation,
every texture element (scales, leaves, circuit traces, wood grain) 
is individually drawn as clean thin lines,
no painterly surface variation
```

- 零水彩晕染、零笔触纹理、零厚涂
- 纹理全部来自线条描绘的内容细节——鳞片、叶脉、电路线、木纹一律用均匀细线画出
- 不是材料模拟，是画出来的
- 无绘画性表面变化

## 色彩逻辑

```
clean distinct color palette — turquoise, coral pink, ochre, sage green, 
dusty lavender, warm cream, deep indigo, burnt orange,
colors are separated by thin outlines, never bleeding into each other,
strategic bright accent colors against dominant earth-and-pastel base,
shadow colors are richer deeper tones of the base (sage green shadow = deep teal, 
ochre shadow = burnt umber), not black or grey,
no fluorescent neon, no muddy desaturated greys
```

- 干净清晰：青绿 / 珊瑚粉 / 赭石 / 鼠尾草绿 / 灰紫 / 暖奶油 / 深靛蓝 / 焦橙
- 色彩被细线隔开，不互渗
- 主调柔和土色+粉彩，点缀色明亮但不荧光
- 阴影是基色的更深饱和度版本，不用黑/灰
- 零荧光霓虹、零脏灰色

## 构图与空间

```
wide expansive compositions with extreme depth of field,
tiny figures dwarfed by vast surreal landscapes,
strong foreground framing elements — large silhouetted forms at edges,
deep perspective lines drawing the eye through multiple spatial layers 
to a distant focal point,
geometric-organic hybrid forms — floating land masses, 
impossible architecture that reads as both biological and designed,
flat picture-plane quality: depth through scale and overlap, not atmospheric haze,
no depth of field blur, no fog-based depth cues
```

- 广阔构图 + 极端纵深
- 渺小人物 vs 巨大超现实景观
- 前景大剪影物制造边框
- 多层空间透视线引导视线
- 几何×有机混合形态——浮岛、既是生物又是建筑的形式
- 深度靠尺度对比和遮挡，不用空气透视雾
- 无景深模糊

## 人物 / 角色渲染（有人物时追加）

```
small figures rendered with same uniform fine outline as environment,
clean flat color on skin and clothing — no gradient skin shading,
facial features reduced to essential lines — eyes as simple dots or small shapes,
minimal detail on faces, no photorealism in features,
characters feel like precise tiny illustrations placed within vast landscapes,
proportions natural, not exaggerated anime, not chibi
```

- 小人物用与环境相同的均匀细线处理
- 皮肤和衣物平面着色，无渐变
- 面部特征简化——眼睛是点或小形
- 人物是精确的小插图，放置于巨大景观中
- 比例自然，非夸张 anime，非 chibi

---

## Backbone Preset（直接贴入 prompt）

```
detailed ligne claire illustration, clean uniform thin outline enclosing every form, 
consistent fine lineweight with no hatching or cross-hatching, 
flat color areas with minimal shading, shadows as separate flat outlined color planes — 
not gradient blended, 
no watercolor wash, no brush stroke texture, no atmospheric bloom, 
texture through dense fine linework on surfaces — every scale leaf and surface detail individually drawn, 
clean distinct palette: turquoise coral-pink ochre sage-green dusty-lavender warm-cream deep-indigo, 
strategic bright accents against earth-and-pastel base, 
wide expansive composition with extreme depth, 
tiny figures in vast surreal landscapes, 
strong foreground framing with large silhouetted forms, 
deep perspective lines through multiple spatial layers, 
geometric-organic hybrid forms, 
flat picture-plane depth through scale and overlap — no depth-of-field blur, no atmospheric haze
```

## Negative Prompt

```
no watercolor, no gradient shading, no soft airbrush, no atmospheric bloom, 
no depth of field blur, no photographic lens effects, no film grain, 
no photorealism, no 3DCG render, no realistic human skin texture, 
no thick variable linework, no ink splatter, no hatching, no cross-hatching, 
no high-saturation neon colors, no black or grey shadows, no muddy desaturated colors, 
no chibi proportions, no exaggerated anime expressions, 
no CAD-perfect mechanical lines, no procedural texture maps, 
no fog-based depth, no ambient occlusion shading,
no known character faces, no known anime or comic styles
```

## MJ Parameters

```
--ar 9:16 --stylize 250 --v 8.2
```

备选（若需更纯的平面插画感）：`--niji 6`

---

## 与其它 style-profile 的差异速查

| 维度 | Abyss | Gantz/KNY | Porcelain | **Moebius** |
|------|-------|-----------|-----------|-------------|
| 线条 | 纤细均匀 | 粗细变化 cel | 无轮廓线 | **均匀细线每物有边** |
| 着色 | 软渐变 | 硬 cel 阴影 | 内发光渐变 | **平面色块无渐变** |
| 纹理 | 水彩晕染 | 无 | 透光材料 | **密集线稿细节** |
| 纵深 | 空气透视雾 | 摄影式 | 留白构图 | **尺度对比无雾** |
| 色调 | 土色+荧光 | 冷暖对抗 | 玉石白+青花蓝 | **粉彩土色+亮色点缀** |
| 适合 | 幽深奇观 | 战斗/动态 | 诗意静物 | **奇异地理/陌生生态** |
