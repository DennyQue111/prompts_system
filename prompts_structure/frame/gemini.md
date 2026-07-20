## Description
Use this architecture when generating a **single cinematic frame for Gemini 2.5 Flash Image or GPT image models** — a standalone shot that functions as a storyboard cell rendered at full quality. This is the atomic unit of visual storytelling: one composition, one moment, one emotional beat.

A frame is NOT a concept sheet. It's a single image that should feel like a freeze-frame from a finished film.

## Core Principles

1. **One frame = one emotion.** Every compositional choice (angle, focal length, depth, lighting) should serve a single emotional intent. A high-angle wide shot of a lone figure in rain is loneliness. A tight 85mm of hands trembling over a weapon is tension.
2. **Camera tells the story.** The lens choice IS the storytelling. Wide angle = isolation, immersion. Telephoto = intimacy, compression, pressure. Dutch angle = unease. Eye-level = humanity.
3. **Light is emotion.** Cold blue = clinical, lonely, dead. Warm amber = memory, safety, the past. Hard single-source = interrogation, truth. Soft diffused = dream, memory, afterlife.
4. **Depth creates cinema.** Every frame needs at least three depth planes: foreground element → subject → background. Flat images read as amateur.
5. **Style Palette is visual DNA.** Film stock, format, color palette, and camera language remain consistent across all frames in a project. This is what makes a film look like *itself*.

## Visual DNA · 五轴一致性

**电影感 ≠ 真实。** 电影画面的用色和用光并不追求物理正确，而是服务于**心理色彩和情绪色彩**。一个角色内心孤独——画面基调偏冷青、光比拉大、阴影压黑，哪怕场景本身是正午阳光。观众感受到的不是"这个房间长这样"，而是"这个角色的内心是冷的"。

视觉风格统一性由以下五个维度决定。画面之间保持一致的，不是"画得像不像"，而是这五个维度是否对齐：

| 维度 | 权重 | 含义 | 示例 |
|------|------|------|------|
| **基调色** | ★ 主导 | 画面整体的色彩倾向——冷/暖/中性，饱和度高低 | 冷蓝+深黑（硬核科幻）、暖金+柔黄（记忆闪回） |
| **光比** | ★ 主导 | 亮部与暗部的反差程度 | 高光比=戏剧张力，低光比=柔和日常 |
| **光硬度/光型** | ★ 主导 | 光源的硬/柔 + 光线方向 | 硬光单源=真相/审问，柔光漫射=梦境/回忆 |
| **逻辑光元类型** | 支撑 | 场景中合理的光源逻辑——光从哪来？为什么是这个颜色？ | 钠灯街灯（暖橙）、月光（冷青）、车内仪表盘光（冷蓝+暖橙混合） |
| **画面元素质感** | 支撑 | 所有可见表面的材质属性 | 镜面反射（SEVEN 立方体）、粗糙亚光（战斗服）、湿沥青反光（雨夜路面） |

### 使用方法

写任何 frame 之前，先过一遍五轴：

1. 这个镜头的**情绪**是什么？→ 定基调色 + 光比
2. 光从**哪来**、什么**硬度**？→ 定逻辑光元 + 光型
3. 画面里有什么**材质**需要强调或收敛？→ 定质感方向

五轴对齐后，再从 Content Formula 逐字段展开。**五轴是骨架，字段是血肉。** 不是先填字段再调五轴。

> **五轴 + Style Palette 的关系：** 五轴是"控制什么"的理论，Style Palette 是"怎么写"的实践。基调色 → Color Palette，光比+光型 → Lighting table，光元+质感 → Lighting 字段和 Atmosphere 字段中的具体描述。五轴是上游设计决策，Style Palette 是下游表达方式。

## Prompt Content Formula

```
[Shot type + emotional intent] +
[Subject: who/what is in the frame, their action/moment] +
[Lighting: source, temperature, quality, emotional function] +
[Depth layers: foreground element → midground subject → background] +
[Environment: location context from world DNA] +
[Camera: lens focal length, angle, distance, any movement implication] +
[Composition: framing rule, subject placement, negative space] +
[Atmosphere: weather, particles, haze, time of day] +
[Style Palette: film stock + format + color palette + camera language]
```

### Content Components

| Component | Description | Key Decisions |
|-----------|-------------|---------------|
| **Shot type + emotional intent** | What kind of shot + what it should make the viewer feel | Wide establishing (awe, isolation), medium (presence, conversation), close-up (intimacy, tension), extreme close-up (obsession, detail), over-the-shoulder (witness, voyeurism) |
| **Subject** | Who/what is in frame, their action/moment | A character's specific micro-action (raising a weapon, touching a ring, looking up at rain), not a generic pose |
| **Lighting** | Source, temperature, quality | Hard single-source (dramatic shadows, interrogation), soft diffused (dream, memory), rim/backlight (silhouette, mystery), practical lights in-frame (world authenticity) |
| **Depth layers** | Foreground → midground → background | Foreground: out-of-focus element near camera (rain on glass, shoulder, debris). Midground: the subject. Background: depth vanishing point |
| **Environment** | Location context from world DNA | Pull from the project's location designs. If the world has "mirror surfaces," the frame's environment should contain them |
| **Camera** | Lens, angle, distance | See `reference.md` Section 5 for focal length guide. High angle = small/vulnerable. Low angle = powerful/threatening. Dutch = unease. Eye-level = human connection |
| **Composition** | Framing rule, subject placement | Rule of thirds (default), center-frame (confrontation, symmetry), negative space left/right (looking room, movement room), leading lines to subject |
| **Atmosphere** | Weather, particles, haze, time of day | Rain (melancholy, cleansing), fog (mystery, isolation), dust motes in light (stillness, memory), smoke/haze (danger, aftermath) |

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

## Style Palette

The Style Palette is the **visual DNA** of a project — a set of material, color, and camera decisions that remain consistent across every frame. Gemini and GPT image models understand natural language descriptions of film texture, format, color science, and camera language well — use them directly in the prompt.

> **See `style_reference.md`** for the complete palette library (film stock templates, CG anime templates, color palettes, camera language options). Choose one that matches your project's visual direction, then append it as the final content block.
>
> Do not default to any palette — always consult `style_reference.md` and verify against the project's confirmed visual style first.

### Usage

The Style Palette is appended as the final block of the content prompt. Unlike Midjourney, Gemini/GPT models do not use `--` parameter syntax — describe everything in natural language:

```
[Content: shot type + subject + lighting + depth + environment + camera + composition + atmosphere] +
[Style Palette: film stock, format, color palette, camera language]
```

## Usage Notes
- **Start with emotional intent.** Before any technical description, decide: what should the viewer FEEL? Every choice flows from that.
- **The shot type table is a compass, not a prison.** If a 35mm at eye-level with hard light conveys the right emotion, use it regardless of what the table says.
- **Depth is non-negotiable.** Foreground → subject → background. Always three planes.
- **One frame, one subject, one emotion.** Don't try to fit multiple story beats in a single frame. That's what sequences and storyboards are for.
- **Style Palette is project DNA.** Define it once per project, apply it to every frame. Visual continuity across frames is what separates a film from a collection of images.
- **Movement implication:** Gemini/GPT handle motion blur descriptions reasonably well — "mid-stride," "hair caught in wind," "rain frozen mid-fall," "motion blur on passing cars" all work.

## Differences from Midjourney Variant
- **No `--` parameters.** Describe everything in natural language (aspect ratio, style strength, quality are all plain text).
- **Style Palette is a first-class section.** Gemini/GPT's strength is understanding natural language descriptions of film texture and color — lean into this.
- **No CG anime workaround needed.** Gemini/GPT image models have different moderation paths than Chinese platforms (即梦/豆包).
- **Same content formula, same lens tables.** The *what* doesn't change between models — only the *how*.
