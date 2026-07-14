# GPT 图片生成 · 反脏图方法论

## 核心原则

脏图的本质不是"细节不够"，而是**细节失控**——模型不知道哪些表面该有细节，哪些该干净。

不要在 prompt 里堆 `ultra detailed / 8K / hyper detailed / cinematic bokeh`，这会放大问题。

## 三层结构（按顺序）

### 第一层：材质-光线层（先建正向画面）

回答问题再落笔：
1. 主材质是什么（皮肤/布料/金属/湿沥青/玻璃/混凝土）
2. 表面怎么响应光（哑光/缎面/粗糙/湿润/反射/吸光）
3. 光从哪里来（主光方向+色温+边缘光，只保留有用的）
4. 相似颜色材质怎么区分（靠明度、冷暖、粗糙度、反光宽度、接触阴影）
5. 曝光保护（高光不死白，暗部不糊黑，阴影有可读结构）
6. 接触阴影只在真实接缝/重叠/褶皱/落地位置出现

### 第二层：细节控制词替换

| 危险词（导致脏） | 替换为（可控） |
|---|---|
| ultra detailed | balanced detail |
| hyper detailed | selective fine detail |
| micro detail everywhere | detail concentrated only on meaningful surfaces |
| highly textured | controlled material rendering |
| wet glossy | subtle reflections, strict wet/dry boundaries |
| cinematic bokeh | clean blurred background |
| dark atmospheric background | smooth dark tones, low texture background |
| realistic texture | natural texture only |

### 第三层：负面约束（短而准，不放旧失败记忆）

好负面词（失败类型，不指向具体物体）：
```
ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, muddy shadows, noisy bokeh,
dirty AO halos, uniform plastic gloss, pasted-on texture,
milky reflections, clipped highlights, crushed blacks,
low-contrast residual textures, dirty texture buildup
```

❌ 不要写：no dirty face marks / no strange weapon / no blue-purple shadow glow
→ 这些具体失败物仍会进入模型注意力

## GPT 提示词尾部（追加以防脏图）

```
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
smooth background tones, minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks.
```

## 人像专项

```
natural facial planes, matte skin with soft specular highlights,
subtle pores only where visible, clean eye highlights,
hair grouped into readable strands.
Avoid: waxy skin, dirty pore noise, facial artifact marks.
```

## 暗场景专项

```
smooth dark tones with readable shadow floor,
clean value separation around the silhouette,
low texture background, controlled rim light.
Avoid: muddy shadows, crushed blacks, background artifacts, dirty AO halos.
```

## 脏图已出→不要局部修

不要连续 i2i 修同一张脏图（会把脏纹放大）。直接 clean-slate regeneration：保留主体/构图/风格，重建材质-光线-细节层。

## 终检清单

1. 主材质和光线响应写清楚了吗
2. 危险细节词替换了吗（ultra detailed → balanced detail 等）
3. 暗部有可读结构吗
4. 接触阴影只在真实接缝吗
5. 背景低纹理/干净吗
6. 负面词短而准、只放失败类型吗
7. 末尾贴了 clean rendering 块吗
