## Description

Use this architecture when generating a **single cinematic frame for GPT image models** based on one or more uploaded reference images. The reference image(s) anchor the visual identity of characters, locations, props, or the overall style, while the prompt defines the specific shot emotion, lighting, and material rendering.

Unlike the text-to-image variant (`text_to_image_gpt.md`), this architecture assumes the user has provided visual reference material that must be respected — whether as an exact identity lock (character appearance) or as style DNA extraction (environmental palette, lighting logic, atmospheric treatment).

**For text-to-image without reference images** → use `text_to_image_gpt.md`. **For Gemini** → use `image_to_image_gemini.md`.

---

## When to Use i2i vs t2i

| Scenario | Use This File (i2i) | Use `text_to_image_gpt.md` (t2i) |
|----------|---------------------|-------------------------------------|
| User uploads a character concept image and wants a frame featuring that exact character | ✅ | — |
| User uploads a location concept image and wants a frame set in that environment's style | ✅ | — |
| User uploads a lighting/style reference and wants the frame to match that treatment | ✅ | — |
| User uploads a blockout/spatial layout and wants the frame to follow that geometry | ✅ | — |
| User describes a frame purely from text/script with no visual reference | — | ✅ |
| User uploads a previous frame and wants a variation (different angle, same scene) | ✅ | — |

---

## Reference Image Handling

The core problem i2i solves: **How to tell GPT precisely what to copy from each reference image and what to ignore.**

### Input Structure

User provides:
- **Reference images** (1–N images): character concept, location concept, lighting reference, prop reference, blockout/spatial layout, previous frame, etc.
- **Reference boundaries** (critical): For each reference image, the user MUST specify what it anchors and what it does NOT anchor.
- **Shot instruction**: Emotional intent, lighting direction, material rendering, atmosphere.

### Reference Boundary Rules

| Reference Type | What It Anchors | What It Does NOT Anchor |
|----------------|-----------------|------------------------|
| **Character concept** | Exact face structure, hair, body type, outfit, skin material | Environment, lighting, camera angle, pose |
| **Location concept** | Environmental visual DNA: palette, light ratio, wet surface rendering, atmospheric treatment, spatial structure | Character appearance, facial features |
| **Lighting reference** | Light source behavior, color temperature, reflection patterns, shadow quality | Subject matter, composition |
| **Prop / entity concept** | Exact form, material, glow behavior, proportions | Everything else |
| **Previous frame** | Character identity, style palette, lighting continuity | Camera angle (if changing), composition (if reframing) |
| **Layout / Blockout / Spatial reference** | EXACT spatial layout: object positions, relative distances, camera angle, perspective geometry, road/building configuration | Materials, colors, lighting, atmosphere, surface textures, specific architectural details, annotations, arrows, text labels, dimension lines, wireframe edges |

**Critical distinction:**
- **Character / prop / entity / layout references** → Identity lock (exact reproduction)
- **Environment / lighting / style references** → Style DNA extraction (adopt visual characteristics, not specific objects)

If the user does not explicitly state reference boundaries, the prompt writer MUST ask before generating.

### Multi-Reference Prioritization

1. **Character reference always wins on appearance.**
2. **Lighting reference wins on light behavior.**
3. **Layout reference wins on spatial relationships.** If any text description contradicts the blockout's object positions, camera angle, or spatial geometry, the layout reference overrides. Text must NOT describe spatial relationships when a layout reference is provided.
4. **User text instruction wins on composition and action** — *except when a layout reference is present.* When a blockout/spatial reference is uploaded, text does NOT control composition or spatial layout; it controls style, material, lighting, atmosphere, and emotion only.

---

## Core Principles

1. **One frame = one emotion.** Every compositional choice serves a single emotional intent.
2. **Camera tells the story.** The lens choice IS the storytelling.
3. **Light is emotion.**
4. **Depth creates cinema.** Every frame needs at least three depth planes.
5. **Style Palette is visual DNA.**
6. **Reference anchors identity, text directs the moment.** In i2i, the reference image locks WHAT the subject looks like or WHERE things are; the prompt text controls HOW things look and FEEL.

---

## Visual DNA · 五轴一致性

视觉风格统一性由以下五个维度决定。画面之间保持一致的，不是"画得像不像"，而是这五个维度是否对齐：

| 维度 | 权重 | 含义 | 示例 |
|------|------|------|------|
| **基调色** | ★ 主导 | 画面整体的色彩倾向 | 冷蓝+深黑（硬核科幻）、暖金+柔黄（记忆闪回） |
| **光比** | ★ 主导 | 亮部与暗部的反差程度 | 高光比=戏剧张力，低光比=柔和日常 |
| **光硬度/光型** | ★ 主导 | 光源的硬/柔 + 光线方向 | 硬光单源=真相/审问，柔光漫射=梦境/回忆 |
| **逻辑光元类型** | 支撑 | 场景中合理的光源逻辑 | 钠灯街灯（暖橙）、月光（冷青） |
| **画面元素质感** | 支撑 | 所有可见表面的材质属性 | 镜面反射、粗糙亚光、湿沥青反光 |

### 使用方法

写任何 frame 之前，先过一遍五轴：
1. 这个镜头的**情绪**是什么？→ 定基调色 + 光比
2. 光从**哪来**、什么**硬度**？→ 定逻辑光元 + 光型
3. 画面里有什么**材质**需要强调或收敛？→ 定质感方向

五轴对齐后，再从 Content Formula 逐字段展开。

---

## Prompt Content Formula

When reference images are provided, the prompt is structured in two layers: the **reference anchoring layer** followed by the **frame direction layer**.

```
[Reference anchoring: explicit boundaries for each uploaded image] +
[Subject + Action/Emotion] + [Composition + Focal length] +
[Lighting: source + color temp + ratio] +
[Atmosphere + color palette] +
[Style suffix]
```

### Content Components

| Component | Description | Key Decisions |
|-----------|-------------|---------------|
| **Reference anchoring** | Explicit instruction per uploaded image: what to copy exactly vs. what to extract as DNA | Character = identity lock. Location/lighting = style DNA extraction. Layout = spatial authority. |
| **Subject + Action/Emotion** | Who/what is in frame, their specific micro-action | A character's specific micro-action, not a generic pose |
| **Composition + Focal length** | Framing rule, subject placement, lens choice | *Skip if layout reference is provided* |
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

### i2i Style Adaptation

When reference images are provided, the Style Palette has two possible sources:

1. **Reference-derived style** (default): If the user wants the frame to match the reference's rendering aesthetic, extract the style DNA from the reference and describe it explicitly.

2. **Project-locked style** (override): If the user wants the reference's identity but rendered in the project's established Style Palette, explicitly state: "Render using the project's confirmed Style Palette — do not adopt the reference image's rendering style."

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
3. Where are the contact shadows?
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

Tailor to frame content. Example:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise.
```

Curate from `meta/gpt-image-hygiene.md` based on actual scene content. Keep it short (~10–15 terms).

---

## Usage Notes

- **Start with reference boundaries.** Before writing any cinematic description, explicitly define what each uploaded image anchors and what it does not anchor.
- **Start with emotional intent.** Before any technical description, decide: what should the viewer FEEL?
- **Depth is non-negotiable.** Foreground → subject → background. Always three planes.
- **One frame, one subject, one emotion.**
- **Background must be explicitly controlled**: "clean smooth background" OR "clean shallow depth of field" — never left implied.
- **Faces in single frames**: "natural facial planes, matte skin with soft specular highlights" — highest-risk area for dirty pore noise on GPT.
- **Dark/atmospheric frames**: add "smooth dark tones with readable shadow detail."
- **Anti-noise is in word choice, not an appended block** — embed clean vocabulary directly into the description.
- **Never transfer reference image noise:** Compression artifacts, banding, micro-pattern noise are pollution, not style.
- **Blockout / layout reference = spatial authority.** When the user uploads a blockout, that image is the SOLE authority on object positions, camera angle, and spatial geometry. Do NOT describe spatial relationships in the text prompt — doing so creates conflicting instructions.
- **CRITICAL: Current image models (Gemini/GPT) struggle to precisely reproduce spatial layout from blockout/wireframe reference images.** Empirical testing shows that blockout references often fail to anchor layout correctly — the model may misread geometric relationships, convert flat intersections into overpass systems, or ignore directional arrows. When precise spatial layout is required, the more reliable workflow is: upload a **location concept or previous frame for STYLE anchoring** + describe spatial relationships **explicitly in text**.
- **Reference image description must be minimal.** In the reference anchoring line, only state what the image is and that spatial relationships are locked to it. Do NOT repeat object positions, spatial layouts, or detailed scene descriptions in the reference line — the image itself carries that information. Repeating it in text creates ambiguity about which source the model should follow.
- **Avoid directional vocabulary when describing motion of elements already in the reference.** Words like "横向" (horizontal/transverse), "对角" (diagonal), "右侧" (right side) are interpreted differently depending on camera angle and may override the reference image's spatial logic. Use "沿当前道路" (along the current road) or "沿现有方向" (along the existing direction) instead — these refer to the inherent relationships in the reference image without introducing new directional concepts.
- **Annotations, arrows, and text labels on reference images are NOT scene content.** If the blockout contains red arrows, dimension lines, text labels, or wireframe edges, explicitly instruct the model: "The [color] arrows / text labels in the reference are ANNOTATIONS only. Do NOT draw them in the final image." The model will otherwise treat annotations as part of the scene.
- **Character pose is NOT locked by character reference.** Only appearance (face, hair, outfit, proportions) is locked.

---

## Key Rules

1. **Prompt must reference uploaded images with explicit boundaries.** Character = identity lock. Environment = style DNA. Layout = spatial authority.
2. **Identity lock means EXACT reproduction.** "Similar" is not enough.
3. **Style DNA extraction means adopt characteristics, not objects.**
4. **User text instruction overrides reference on composition and action** — *except when a layout reference is present.*
5. **When a layout/blockout reference is provided, the text prompt MUST NOT describe spatial relationships, object positions, or composition layout.** The image is the sole authority on WHERE things are; text controls HOW things look and FEEL.
6. **Reference image descriptions must be minimal — state what the image is and that spatial layout is locked to it, but do not repeat spatial details.**
7. **Avoid directional vocabulary ("横向", "对角", "右侧") when describing motion of reference-locked elements.** Use "沿当前道路" / "沿现有方向" to refer to inherent spatial relationships in the reference without introducing ambiguous directional concepts.
8. **Check for repetition before output.**
9. **No `--` parameters.** Describe everything in natural language.
10. Read `meta/gpt-image-hygiene.md` for full methodology.

---

## Output Example Structure

```
Based on the [N] attached reference image(s) — [Image 1: character concept], [Image 2: location concept] ... — generate a single cinematic frame.

**Image 1 — Character Reference ([Name]):**
This is the EXACT character identity source. You MUST reproduce [Name]'s appearance PRECISELY as shown:
[face structure, hair, body type, outfit]. Face, hair, body, and outfit must match the reference EXACTLY.
Do NOT alter the character's appearance. Do NOT copy the background, lighting, or camera angle from this image.

**Image 2 — Location Reference ([Location name]):**
Extract and adopt ONLY the visual DNA: [palette, light ratio, atmospheric treatment, etc.].
Do NOT copy specific buildings or landmarks beyond what is needed for environmental context.

## Frame Direction

[Subject + Action/Emotion]

[Composition + Focal length] — *skip if layout reference is provided*

[Lighting: source, temperature, quality, emotional function]

[Atmosphere + color palette]

## Style Palette

[Film stock + format + color palette + camera language, either derived from reference or project-locked]

## Negative Prompt

Avoid: [Scene-specific negative terms, ~10–15 terms]
```

---

## Differences from Text-to-Image Variant

| Aspect | `text_to_image_gpt.md` | `image_to_image_gpt.md` (this file) |
|--------|---------------------------|----------------------------------------|
| Input | Text description only | Text + 1–N reference images |
| Character appearance | Described from scratch | Locked to reference (exact reproduction) |
| Location style | Described from scratch | Extracted from reference as style DNA |
| Spatial layout | Described from text | Locked to layout reference (if provided) |
| Prompt opening | Content formula directly | Reference anchoring layer + content formula |
| Style Palette | Project-locked only | Reference-derived OR project-locked |
| Risk | Inconsistent character face | Reference noise transfer (avoid via explicit exclusion) |
