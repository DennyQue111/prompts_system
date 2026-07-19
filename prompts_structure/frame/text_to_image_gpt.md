## Description

Use this architecture when generating a **single cinematic frame for GPT image models** — a standalone shot that functions as a storyboard cell rendered at full quality. This is the atomic unit of visual storytelling: one composition, one moment, one emotional beat.

A frame is NOT a concept sheet. It's a single image that should feel like a freeze-frame from a finished film.

**For Gemini** → use `text_to_image_gemini.md`. **For image-to-image with reference images** → use `image_to_image_gpt.md`.

---

## Core Principles

1. **One frame = one emotion.** Every compositional choice (angle, focal length, depth, lighting) should serve a single emotional intent.
2. **Camera tells the story.** The lens choice IS the storytelling.
3. **Light is emotion.** Cold blue = clinical, lonely, dead. Warm amber = memory, safety, the past.
4. **Depth creates cinema.** Every frame needs at least three depth planes: foreground element → subject → background.
5. **Style Palette is visual DNA.** Film stock, format, color palette, and camera language remain consistent across all frames.

---

## Visual DNA · 五轴一致性

**电影感 ≠ 真实。** 电影画面的用色和用光并不追求物理正确，而是服务于**心理色彩和情绪色彩**。

视觉风格统一性由以下五个维度决定：

| 维度 | 权重 | 含义 | 示例 |
|------|------|------|------|
| **基调色** | ★ 主导 | 画面整体的色彩倾向——冷/暖/中性，饱和度高低 | 冷蓝+深黑（硬核科幻）、暖金+柔黄（记忆闪回） |
| **光比** | ★ 主导 | 亮部与暗部的反差程度 | 高光比=戏剧张力，低光比=柔和日常 |
| **光硬度/光型** | ★ 主导 | 光源的硬/柔 + 光线方向 | 硬光单源=真相/审问，柔光漫射=梦境/回忆 |
| **逻辑光元类型** | 支撑 | 场景中合理的光源逻辑——光从哪来？为什么是这个颜色？ | 钠灯街灯（暖橙）、月光（冷青） |
| **画面元素质感** | 支撑 | 所有可见表面的材质属性 | 镜面反射、粗糙亚光、湿沥青反光 |

### 使用方法

写任何 frame 之前，先过一遍五轴：
1. 这个镜头的**情绪**是什么？→ 定基调色 + 光比
2. 光从**哪来**、什么**硬度**？→ 定逻辑光元 + 光型
3. 画面里有什么**材质**需要强调或收敛？→ 定质感方向

五轴对齐后，再从 Content Formula 逐字段展开。**五轴是骨架，字段是血肉。**

---

## Prompt Content Formula

```
[Subject + Action/Emotion] + [Composition + Focal length] +
[Lighting: source + color temp + ratio] +
[Atmosphere + color palette] +
[Style suffix]
```

### Content Components

| Component | Description | Key Decisions |
|-----------|-------------|---------------|
| **Subject + Action/Emotion** | Who/what is in frame, their specific micro-action | A character's specific micro-action, not a generic pose |
| **Composition + Focal length** | Framing rule, subject placement, lens choice | See Shot Type and Lens tables below |
| **Lighting** | Source, temperature, quality, emotional function | Hard single-source (dramatic), soft diffused (dream), rim/backlight (silhouette) |
| **Atmosphere + color palette** | Weather, particles, haze, time of day, dominant colors | Rain (melancholy), fog (mystery), dust motes (memory) |
| **Style suffix** | Film stock, format, camera language | See GPT Style Suffix section below |

**GPT word choice** (embed in description, do not append as block):
- Use: balanced detail, controlled material rendering, selective fine detail, smooth dark tones, clean shadow falloff
- Avoid: ultra detailed, 8K, hyper detailed, cinematic bokeh, photorealistic skin pores

---

## Shot Type Quick Reference

| Shot | Focal Length | Subject Framing | Emotional Function |
|------|-------------|-----------------|-------------------|
| Extreme Wide (EWS) | 18–24mm | Figure tiny in landscape | Isolation, scale, awe |
| Wide (WS) | 24–35mm | Full body + environment | Place, context, arrival |
| Medium Wide (MWS) | 35–50mm | Full body, environment recedes | Character in context |
| Medium (MS) | 50mm | Waist-up | Conversation, presence |
| Medium Close-up (MCU) | 65–85mm | Chest-up | Emotion, reaction |
| Close-up (CU) | 85–100mm | Face filling frame | Intense emotion, realization |
| Extreme Close-up (ECU) | 100mm+ | Eye, hand, object detail | Obsession, detail, trigger |
| Over-the-Shoulder (OTS) | 50–85mm | Back of one character, face of another | Witness, relationship, power dynamic |

---

## Lens + Emotion Mapping

| Emotional Intent | Lens | Angle | Lighting |
|-----------------|------|-------|----------|
| Loneliness / isolation | 24mm wide | High angle | Single cold source, long shadows |
| Intimacy / connection | 85mm | Eye-level | Soft warm, shallow DOF |
| Tension / danger | 50mm | Dutch 3–5° tilt | Hard single-source, deep blacks |
| Power / threat | 35mm | Low angle | Backlight silhouette or hard top-light |
| Memory / flashback | 50mm | Eye-level | Soft diffused, warm amber, slight haze |
| Revelation / truth | 85mm | Eye-level → slight push | Light source revealed in frame |
| Despair / loss | 24–35mm | High angle | Cold blue, rain or fog, desaturated |
| Hope / safety | 50mm | Eye-level | Warm practical lights, golden hour |

---

## Style Palette

The Style Palette is the **visual DNA** of a project. GPT image models understand natural language descriptions of film texture and color — use them directly.

> **See `style_reference.md`** for the complete palette library. Choose one that matches your project's visual direction, then append it as the final content block.

### GPT Style Suffix (single frames)

Avoid elaborate camera-brand language on GPT:
```
16:9 cinematic still, [time of day], [light source description],
controlled color grading, clean atmosphere, smooth highlight rolloff
```

---

## GPT Anti-Noise: Pre-Writing Checklist

Single frames have no context — the model has nothing to infer. Define explicitly:
1. Main surface material: what is the dominant visible surface?
2. Light response: matte/satin/glossy/wet/mirror?
3. Where are the contact shadows? (under chin, at collar, at object contact points, on ground plane)
4. What's in the background? Must specify texture level control.

## GPT Word Choice Guide

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective detail on key surfaces |
| highly textured | controlled material rendering |
| photorealistic skin pores | natural facial planes, matte skin with soft specular highlights |
| cinematic bokeh | clean depth of field with smooth falloff |
| dark atmospheric background | smooth dark tones, clean shadow falloff |

---

## Negative Prompt (frame-specific, short)

Tailor to frame content. Example for a character frame:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise.
```

Curate from `meta/gpt-image-hygiene.md` based on actual scene content. Keep it short (~10–15 terms).

---

## Usage Notes

- **Start with emotional intent.** Before any technical description, decide: what should the viewer FEEL?
- **Depth is non-negotiable.** Foreground → subject → background. Always three planes.
- **One frame, one subject, one emotion.** Don't try to fit multiple story beats in a single frame.
- **Background must be explicitly controlled**: "clean smooth background" OR "clean shallow depth of field" — never left implied.
- **Faces in single frames**: "natural facial planes, matte skin with soft specular highlights" — highest-risk area for dirty pore noise on GPT.
- **Dark/atmospheric frames**: add "smooth dark tones with readable shadow detail."
- **Anti-noise is in word choice, not an appended block** — use the word choice table while writing.
- **Movement implication:** GPT handles motion blur descriptions reasonably well.

---

## Key Rules

1. **Frame composition**: same as gemini.md.
2. **Anti-noise is in word choice, not an appended block** — embed clean vocabulary directly into the description.
3. **Background must be explicitly controlled**: "clean smooth background" OR "clean shallow depth of field" — never left implied.
4. **Faces in single frames**: "natural facial planes, matte skin with soft specular highlights" — highest-risk area for dirty pore noise.
5. **Dark/atmospheric frames**: add "smooth dark tones with readable shadow detail."
6. **Check for repetition before output.**
7. **No `--` parameters.** Describe everything in natural language.
8. Read `meta/gpt-image-hygiene.md` for full methodology.

---

## Differences from Gemini Variant

| Aspect | `text_to_image_gemini.md` | `text_to_image_gpt.md` (this file) |
|--------|---------------------------|-------------------------------------|
| Anti-noise | Not needed | Embedded in word choice per field |
| Style suffix | Natural language film stock description | Simplified: "16:9 cinematic still, controlled color grading, clean atmosphere" |
| Skin/face description | Detailed skin texture | "natural facial planes, matte skin with soft specular highlights" |
| Negative prompt | Not used | Short scene-specific list (~10–15 terms) |
| Camera brand language | Arri 65mm, Cooke anamorphic, etc. | Avoid elaborate camera-brand language |
