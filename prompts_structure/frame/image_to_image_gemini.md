## Description

Use this architecture when generating a **single cinematic frame for Gemini 2.5 Flash Image** based on one or more uploaded reference images. The reference image(s) anchor the visual identity of characters, locations, props, or the overall style, while the prompt defines the specific shot composition, emotion, and camera language.

Unlike the text-to-image variant (`text_to_image_gemini.md`), this architecture assumes the user has provided visual reference material that must be respected — whether as an exact identity lock (character appearance) or as style DNA extraction (environmental palette, lighting logic, atmospheric treatment).

**For text-to-image without reference images** → use `text_to_image_gemini.md`.

---

## When to Use i2i vs t2i

| Scenario | Use This File (i2i) | Use `text_to_image_gemini.md` (t2i) |
|----------|---------------------|-------------------------------------|
| User uploads a character concept image and wants a frame featuring that exact character | ✅ | — |
| User uploads a location concept image and wants a frame set in that environment's style | ✅ | — |
| User uploads a lighting/style reference and wants the frame to match that treatment | ✅ | — |
| User describes a frame purely from text/script with no visual reference | — | ✅ |
| User uploads a previous frame and wants a variation (different angle, same scene) | ✅ | — |

---

## Reference Image Handling

The core problem i2i solves: **How to tell Gemini precisely what to copy from each reference image and what to ignore.** Without explicit boundaries, the model may treat a character reference as mere "style inspiration" (altering the face) or copy irrelevant elements from a location reference into the frame.

### Input Structure

User provides:
- **Reference images** (1–N images): character concept, location concept, lighting reference, prop reference, previous frame, etc.
- **Reference boundaries** (critical): For each reference image, the user MUST specify what it anchors and what it does NOT anchor.
- **Shot instruction**: What kind of frame to generate — shot type, emotional intent, character action, camera angle, etc.

### Reference Boundary Rules

| Reference Type | What It Anchors | What It Does NOT Anchor |
|----------------|-----------------|------------------------|
| **Character concept** | Exact face structure, hair, body type, outfit, skin material. Must be reproduced PRECISELY. | Environment, lighting, camera angle, pose (unless specified) |
| **Location concept** | Environmental visual DNA: palette, light ratio, wet surface rendering, atmospheric treatment, spatial structure | Character appearance, facial features, specific narrative action |
| **Lighting reference** | Light source behavior, color temperature, reflection patterns, shadow quality | Subject matter, composition, specific objects |
| **Prop / entity concept** | Exact form, material, glow behavior, proportions | Everything else |
| **Previous frame** | Character identity, style palette, lighting continuity | Camera angle (if changing), composition (if reframing) |
| **Layout / Blockout / Spatial reference** | EXACT spatial layout: object positions, relative distances, camera angle, perspective geometry, road/building configuration | Materials, colors, lighting, atmosphere, surface textures, specific architectural details, annotations, arrows, text labels, dimension lines, wireframe edges |

**Critical distinction:**
- **Character / prop / entity references** → Identity lock (exact reproduction)
- **Environment / lighting / style references** → Style DNA extraction (adopt visual characteristics, not specific objects)

If the user does not explicitly state reference boundaries, the prompt writer MUST ask before generating. Never assume a generic "extract visual DNA from all references" applies to character images.

### Multi-Reference Prioritization

When multiple reference images are provided, the prompt must establish a clear priority order to prevent conflicting instructions:

1. **Character reference always wins on appearance.** If a location reference shows a character with different hair, the character reference overrides.
2. **Lighting reference wins on light behavior.** If the location reference and lighting reference disagree on color temperature, the lighting reference determines the frame's light quality.
3. **Layout reference wins on spatial relationships.** If any text description contradicts the blockout's object positions, camera angle, or spatial geometry, the layout reference overrides. Text must NOT describe spatial relationships when a layout reference is provided.
4. **User text instruction wins on composition and action** — *except when a layout reference is present.* When a blockout/spatial reference is uploaded, text does NOT control composition or spatial layout; it controls style, material, lighting, atmosphere, and emotion only.

---

## Core Principles

1. **One frame = one emotion.** Every compositional choice (angle, focal length, depth, lighting) should serve a single emotional intent. A high-angle wide shot of a lone figure in rain is loneliness. A tight 85mm of hands trembling over a weapon is tension.
2. **Camera tells the story.** The lens choice IS the storytelling. Wide angle = isolation, immersion. Telephoto = intimacy, compression, pressure. Dutch angle = unease. Eye-level = humanity.
3. **Light is emotion.** Cold blue = clinical, lonely, dead. Warm amber = memory, safety, the past. Hard single-source = interrogation, truth. Soft diffused = dream, memory, afterlife.
4. **Depth creates cinema.** Every frame needs at least three depth planes: foreground element → subject → background. Flat images read as amateur.
5. **Style Palette is visual DNA.** Film stock, format, color palette, and camera language remain consistent across all frames in a project. This is what makes a film look like *itself*.
6. **Reference anchors identity, text directs the moment.** In i2i, the reference image locks WHAT the subject looks like; the prompt text controls WHAT the subject is doing, WHERE the camera is, and HOW the scene feels.

---

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

---

## Prompt Content Formula

When reference images are provided, the prompt is structured in two layers: the **reference anchoring layer** (what to copy from each image) followed by the **frame direction layer** (the cinematic content formula).

```
[Reference anchoring: explicit boundaries for each uploaded image] +n
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
| **Reference anchoring** | Explicit instruction per uploaded image: what to copy exactly vs. what to extract as DNA | Character = identity lock. Location/lighting = style DNA extraction. Never generic "use the reference." |
| **Shot type + emotional intent** | What kind of shot + what it should make the viewer feel | Wide establishing (awe, isolation), medium (presence, conversation), close-up (intimacy, tension), extreme close-up (obsession, detail), over-the-shoulder (witness, voyeurism) |
| **Subject** | Who/what is in frame, their action/moment | A character's specific micro-action (raising a weapon, touching a ring, looking up at rain), not a generic pose |
| **Lighting** | Source, temperature, quality | Hard single-source (dramatic shadows, interrogation), soft diffused (dream, memory), rim/backlight (silhouette, mystery), practical lights in-frame (world authenticity) |
| **Depth layers** | Foreground → midground → background | Foreground: out-of-focus element near camera (rain on glass, shoulder, debris). Midground: the subject. Background: depth vanishing point |
| **Environment** | Location context from world DNA | Pull from the project's location designs. If the world has "mirror surfaces," the frame's environment should contain them |
| **Camera** | Lens, angle, distance | See `reference.md` Section 5 for focal length guide. High angle = small/vulnerable. Low angle = powerful/threatening. Dutch = unease. Eye-level = human connection |
| **Composition** | Framing rule, subject placement | Rule of thirds (default), center-frame (confrontation, symmetry), negative space left/right (looking room, movement room), leading lines to subject |
| **Atmosphere** | Weather, particles, haze, time of day | Rain (melancholy, cleansing), fog (mystery, isolation), dust motes in light (stillness, memory), smoke/haze (danger, aftermath) |

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

The Style Palette is the **visual DNA** of a project — a set of material, color, and camera decisions that remain consistent across every frame. Gemini image models understand natural language descriptions of film texture, format, color science, and camera language well — use them directly in the prompt.

> **See `style_reference.md`** for the complete palette library (film stock templates, CG anime templates, color palettes, camera language options). Choose one that matches your project's visual direction, then append it as the final content block.
>
> Do not default to any palette — always consult `style_reference.md` and verify against the project's confirmed visual style first.

### i2i Style Adaptation

When reference images are provided, the Style Palette has two possible sources:

1. **Reference-derived style** (default): If the user wants the frame to match the reference's rendering aesthetic, extract the style DNA from the reference and describe it in natural language within the Style Palette block. Do NOT rely on the model to "just copy the style" — describe the film stock, color palette, and rendering quality explicitly.

2. **Project-locked style** (override): If the user wants the reference's character/location identity but rendered in the project's established Style Palette, explicitly state: "Render using the project's confirmed Style Palette: [description from `style_reference.md`] — do not adopt the reference image's rendering style."

### Usage

The Style Palette is appended as the final block of the content prompt. Describe everything in natural language:

```
[Content: reference anchoring + shot type + subject + lighting + depth + environment + camera + composition + atmosphere] +
[Style Palette: film stock, format, color palette, camera language]
```

---

## Usage Notes

- **Start with reference boundaries.** Before writing any cinematic description, explicitly define what each uploaded image anchors and what it does not anchor. This is the single most important step in i2i.
- **Start with emotional intent.** Before any technical description, decide: what should the viewer FEEL? Every choice flows from that.
- **The shot type table is a compass, not a prison.** If a 35mm at eye-level with hard light conveys the right emotion, use it regardless of what the table says.
- **Depth is non-negotiable.** Foreground → subject → background. Always three planes.
- **One frame, one subject, one emotion.** Don't try to fit multiple story beats in a single frame. That's what sequences and storyboards are for.
- **Style Palette is project DNA.** Define it once per project, apply it to every frame. Visual continuity across frames is what separates a film from a collection of images.
- **Movement implication:** Gemini handles motion blur descriptions reasonably well — "mid-stride," "hair caught in wind," "rain frozen mid-fall," "motion blur on passing cars" all work.
- **Never transfer reference image noise:** Compression artifacts, banding, micro-pattern noise, or watermark text from the reference are pollution, not style. Explicitly exclude them if the reference image quality is poor.
- **Character pose is NOT locked by character reference.** A character concept sheet shows the character in a neutral pose. The frame prompt defines the character's action and body language in the scene. Only the character's appearance (face, hair, outfit, proportions) is locked.
- **Blockout / layout reference = spatial authority.** When the user uploads a blockout, wireframe, or annotated spatial diagram, that image is the SOLE authority on object positions, camera angle, and spatial geometry. Do NOT describe spatial relationships (who is where, what is next to what, camera position, composition layout) in the text prompt — doing so creates conflicting instructions and causes the model to ignore the reference. Text handles style, material, lighting, atmosphere, and emotion ONLY.
- **Reference image description must be minimal.** In the `@image` or reference anchoring line, only state what the image is and that spatial relationships are locked to it. Do NOT repeat object positions, spatial layouts, or detailed scene descriptions in the reference line — the image itself carries that information. Repeating it in text creates ambiguity about which source the model should follow.
- **Avoid directional vocabulary when describing motion of elements already in the reference.** Words like "横向" (horizontal/transverse), "对角" (diagonal), "右侧" (right side) are interpreted differently depending on camera angle and may override the reference image's spatial logic. Use "沿当前道路" (along the current road) or "沿现有方向" (along the existing direction) instead — these refer to the inherent relationships in the reference image without introducing new directional concepts.
- **CRITICAL: Current image models (Gemini/GPT) struggle to precisely reproduce spatial layout from blockout/wireframe reference images.** Empirical testing shows that blockout references often fail to anchor layout correctly — the model may misread geometric relationships, convert flat intersections into overpass systems, or ignore directional arrows. When precise spatial layout is required, the more reliable workflow is: upload a **location concept or previous frame for STYLE anchoring** + describe spatial relationships **explicitly in text**.
- **Annotations, arrows, and text labels on reference images are NOT scene content.** If the blockout contains red arrows, dimension lines, text labels, or wireframe edges, explicitly instruct the model: "The [color] arrows / text labels in the reference are ANNOTATIONS only. Do NOT draw them in the final image." The model will otherwise treat annotations as part of the scene.

---

## Key Rules

1. **Prompt must reference uploaded images with explicit boundaries.** Start with "Based on the attached reference image(s)..." and specify what each image anchors AND what it does not anchor. Character = identity lock. Environment = style DNA.
2. **Identity lock means EXACT reproduction.** If the reference character has a specific face shape, hair parting, or outfit detail, the generated frame must preserve it precisely. "Similar" is not enough.
3. **Style DNA extraction means adopt characteristics, not objects.** If the reference location has wet asphalt with orange sodium light reflections, the frame should have wet asphalt with orange sodium light reflections — but it should NOT copy the specific buildings or street layout unless instructed.
4. **User text instruction overrides reference on composition and action.** The reference tells the model what things look like; the text tells the model what is happening and where the camera is.
5. **Check for repetition before output.**
6. **No `--` parameters.** Describe everything in natural language (aspect ratio, style strength, quality are all plain text).
7. **When a layout/blockout reference is provided, the text prompt MUST NOT describe spatial relationships, object positions, or composition layout.** The image is the sole authority on WHERE things are; text controls HOW things look and FEEL. Any text description of spatial relationships risks overriding or corrupting the reference.
8. **Reference image descriptions must be minimal — state what the image is and that spatial layout is locked to it, but do not repeat spatial details.**
9. **Avoid directional vocabulary ("横向", "对角", "右侧") when describing motion of reference-locked elements.** Use "沿当前道路" / "沿现有方向" to refer to inherent spatial relationships in the reference without introducing ambiguous directional concepts.

---

## Output Example Structure

```
Based on the [N] attached reference image(s) — [Image 1: character concept], [Image 2: location concept] ... — generate a single cinematic frame.

**Image 1 — Character Reference ([Name]):**
This is the EXACT character identity source. You MUST reproduce [Name]'s appearance PRECISELY as shown:
[face structure, hair, body type, outfit]. Face, hair, body, and outfit must match the reference EXACTLY.
Do NOT alter the character's appearance. Do NOT copy the background, lighting, or camera angle from this image.

**Image 2 — Location Reference ([Location name]):**
Extract and adopt ONLY the visual DNA: [palette, light ratio, atmospheric treatment, wet surface rendering, spatial structure].
Do NOT copy specific buildings or landmarks beyond what is needed for environmental context.
Do NOT copy any character or figure that may appear in this reference.

## Frame Direction

[Shot type + emotional intent: e.g., Medium close-up, tension and revelation]

[Subject: who/what is in the frame, their specific action/moment]

[Lighting: source, temperature, quality, emotional function]

[Depth layers: foreground element → midground subject → background]

[Environment: location context, pulled from world DNA or location reference]

[Camera: lens focal length, angle, distance, any movement implication]

[Composition: framing rule, subject placement, negative space]

[Atmosphere: weather, particles, haze, time of day]

## Style Palette

[Film stock + format + color palette + camera language, either derived from reference or project-locked]
```

---

## Differences from Text-to-Image Variant

| Aspect | `text_to_image_gemini.md` | `image_to_image_gemini.md` (this file) |
|--------|---------------------------|----------------------------------------|
| Input | Text description only | Text + 1–N reference images |
| Character appearance | Described from scratch | Locked to reference (exact reproduction) |
| Location style | Described from scratch | Extracted from reference as style DNA |
| Prompt opening | Content formula directly | Reference anchoring layer + content formula |
| Style Palette | Project-locked only | Reference-derived OR project-locked |
| Risk | Inconsistent character face | Reference noise transfer (avoid via explicit exclusion) |
