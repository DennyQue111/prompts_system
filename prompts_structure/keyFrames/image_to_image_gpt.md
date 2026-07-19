## Description

GPT variant of KeyFrames for **image-to-image** workflow. Unlike the text-to-image 3×3 grid (`text_to_image_gpt.md`), this architecture generates a **single composite design sheet** based on uploaded reference images. The output contains both reference zones (character / location / lighting) and a variable number of 16:9 landscape keyframe frames arranged according to the user's specified cut count and layout preference.

**For text-to-image 3×3 grid** → use `text_to_image_gpt.md`.

---

## GPT-Specific Modifications

### Why i2i KeyFrames Needs a Different Structure

1. **Reference image anchoring with explicit boundaries**: Character references and environment references serve fundamentally different purposes. The prompt must explicitly instruct GPT to reproduce character appearance EXACTLY (identity lock) while extracting only visual DNA from environment references. Never apply a generic "extract DNA from all references" instruction to character images.
2. **Variable layout**: The number of reference images, reference types, and keyframe counts are all user-defined. The prompt must adapt the canvas layout accordingly — no fixed 3×3 grid.
3. **Frame aspect ratio enforcement**: GPT tends to default to square frames when composing multi-frame layouts. Each keyframe must be explicitly locked to 16:9 landscape (1.77:1).

---

## Input Structure

User provides:
- **Reference images** (1–N images): character concept, location concept, lighting reference, prop reference, etc. — quantity and type depend on scene needs.
- **Reference boundaries** (critical): For each reference image, the user MUST specify what it anchors and what it does NOT anchor. This prevents GPT from applying the wrong reference logic — e.g., treating a character reference as mere "style DNA" instead of exact identity.
- **Cut count**: how many keyframe frames to generate (e.g., 3, 4, 6, 9).
- **Layout preference** (optional): horizontal row, 2×2, 2×3, 3×3, or custom arrangement. If not specified, use the recommended layout from the table below.

### Reference Boundary Rules

| Reference Type | What It Anchors | What It Does NOT Anchor |
|----------------|-----------------|------------------------|
| **Character concept** | Exact face structure, hair, body type, outfit, skin material. Must be reproduced PRECISELY. | Environment, lighting, camera angle |
| **Location concept** | Environmental visual DNA: palette, light ratio, wet surface rendering, atmospheric treatment, spatial structure | Character appearance, facial features |
| **Lighting reference** | Light source behavior, color temperature, reflection patterns | Subject matter, composition |
| **Prop / entity concept** | Exact form, material, glow behavior | Everything else |
| **Layout / Blockout / Spatial reference** | EXACT spatial layout: object positions, relative distances, camera angle, perspective geometry, road/building configuration, frame arrangement within the sheet | Materials, colors, lighting, atmosphere, surface textures, specific architectural details, annotations, arrows, text labels, dimension lines, wireframe edges |

**Critical distinction:**
- **Character references** → Identity lock (exact reproduction)
- **Environment / lighting references** → Style DNA extraction (adopt visual characteristics, not specific objects)

If the user does not explicitly state reference boundaries, the prompt writer MUST ask before generating. Never assume a generic "extract visual DNA from all references" applies to character images.

---

## Layout Templates (Variable by Cut Count)

The overall canvas is a **production design sheet** with two zones: **Reference Zone** (top) and **Keyframe Zone** (bottom). The proportions and arrangement must be designed around a hard constraint: **each keyframe frame is 16:9 landscape (1.77:1), wider than tall, NOT square.**

GPT tends to default to square frames when given open multi-frame layouts. To prevent this, every layout instruction must explicitly define how the 16:9 aspect ratio is preserved — either by making the frame small within a larger cell, or by splitting each cell into "frame area + margin area."

### Two Layout Strategies

**Strategy A: Horizontal Row (1 × N)**
- Keyframes arranged in a single left-to-right row.
- Each keyframe is a small but strict 16:9 rectangle.
- Best for: 1–3 cuts (where frame width is generous enough to remain readable).
- Trade-off: Frame height is small (~20–25% of canvas height), so fine detail may be harder to see.

**Strategy B: Grid with Internal Cell Split (Recommended for 4+ cuts)**
- Keyframes arranged in a multi-row grid (2×2, 2×3, 3×3).
- **Each cell is split vertically:**
  - **Upper 85–90% of cell height:** The actual 16:9 landscape frame (strict 1.77:1, wider than tall). A thin clean border separates the frame from the cell edge.
  - **Lower 10–15% of cell height:** Clean neutral margin area below the frame. The `CUT X` label sits here. This margin ensures the frame above is not stretched or distorted.
- Best for: 4–9 cuts.
- Trade-off: Each frame is a thumbnail, but aspect ratio is protected by the internal split.

### Recommended Layouts by Cut Count

| Cuts | Strategy | Arrangement | Reference Zone | Keyframe Zone |
|------|----------|-------------|----------------|---------------|
| 1–3 | A | 1 row horizontal | Top 40–45% | Bottom 55–60%, 1×N row, strict 16:9 frames |
| 4 | B | 2×2 grid | Top 35–40% | Bottom 60–65%, 2×2 grid, cell upper-85% = 16:9 frame |
| 5–6 | B | 2 rows × 3 cols | Top 30–35% | Bottom 65–70%, 2×3 grid, cell upper-85% = 16:9 frame |
| 7–9 | B | 3 rows × 3 cols | Top 25–30% | Bottom 70–75%, 3×3 grid, cell upper-85% = 16:9 frame |
| Custom | A or B | User-defined | Flexible | Flexible — must specify how 16:9 is preserved |

**Why Strategy B is needed:**
In a 16:9 canvas, placing four 16:9 frames in a 2×2 grid without internal cell splitting is geometrically impossible — the four frames alone would consume the entire canvas height, leaving no room for the reference zone. The internal cell split (frame + margin) solves this by making the 16:9 frame occupy only the upper portion of each cell, while the lower margin absorbs the excess vertical space.

---

## Reference Zone Specification (User-Defined Content)

The reference zone contents are **not fixed** — they adapt to what the user uploads and what the scene requires.

Common reference zone modules (mix and match as needed):

```
CHARACTER REFERENCE (Left or Top-Left)
- Derived from character concept image(s)
- Clean neutral near-gray background
- Contents decided by user: full-body turns, expression close-ups, costume details, hand close-ups, etc.
- All views must share identical face structure, hair, and outfit

LOCATION REFERENCE (Right or Top-Right)
- Derived from location concept image(s)
- Wide establishing shot + detail thumbnails as needed
- Lighting thumbnails: key light source, practical lights, environmental reflections

PROP / ENTITY REFERENCE (Optional, smaller panel)
- Derived from prop/entity concept images
- Size reference, material detail, glow/light behavior
```

**Rule**: The prompt writer must describe the reference zone contents explicitly based on the actual reference images provided — do not use a generic placeholder.

---

## Per-Cut Content Formula

Each keyframe frame uses the same 5-field structure as `gemini.md`, adapted for GPT anti-noise word choice:

```
[Subject + Action/Emotion] + [Camera: focal length + angle + movement] +
[Lighting: source + color temp + ratio] +
[Composition & Depth: FG → MG → BG + subject placement] +
[Continuity: connection to previous/next cut]
```

**GPT word choice** (embed in description, do not append as block):
- Use: balanced detail, controlled material rendering, selective fine detail, smooth dark tones, clean shadow falloff
- Avoid: ultra detailed, 8K, hyper detailed, cinematic bokeh, photorealistic skin pores

---

## Global Style Lock (Sequence-Wide)

Appended once after all per-cut descriptions. Defines the visual DNA shared across all frames and reference zones:

```
3D CG anime cinematic render, GANTZ:O (2016) style, Unreal Engine 5 quality,
cel-shaded characters with detailed 3D face models, dark sci-fi aesthetic,
Japanese CG anime film, dramatic cinematic lighting,
glossy wet surfaces with controlled reflections, 16:9 aspect ratio.
```

> Swap per project. Always verify against `frame/style_reference.md`.

**Sequence palette**: Define dominant cool/warm ratio, light source progression, and any cross-cut color shifts (e.g., "warm orange in cuts 1–4, cold blue introduced from cut 5 onward").

**Vocabulary lock**: All cuts and reference zones share the same controlled texture vocabulary to prevent frame-to-frame style drift.

---

## Anti-Noise & Clean Rendering

Clean rendering, balanced detail, natural texture only, controlled material rendering,
clean gradients, controlled highlights, smooth background tones, minimal repetitive patterns.

If character faces appear in keyframes, add:
Natural facial planes, matte skin with soft specular highlights, subtle pores only where visible,
clean eye highlights, hair grouped into readable strands.

If dark/atmospheric frames dominate, add:
Smooth dark tones with readable shadow floor, clean value separation around the silhouette.

Frame-to-frame texture consistency across all cuts.

---

## Negative Prompt (Scene-Specific, Short)

Curate from `meta/gpt-image-hygiene.md` based on actual scene content. Example for rainy night urban scene:

```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, clipped highlights, crushed blacks,
frame border noise, grid line artifacts, separator border decoration,
over-detailed distant facades, neon glow overdrive, daylight, clear weather,
second person, waxy skin, dirty pore noise.
```

---

## Key Rules

1. **Prompt must reference uploaded images with explicit boundaries**: Start with "Based on the attached reference image(s)..." and specify what each image anchors AND what it does not anchor. Character = identity lock. Environment = style DNA.
2. **No fixed grid size**: The layout adapts to the user's cut count and reference image set. Never default to 3×3 without checking user intent.
3. **Each keyframe frame is 16:9 landscape (1.77:1)**: Explicitly state "wider than tall, aspect ratio 1.77:1, NOT square" in the layout instruction. For 4+ cuts, use the internal cell split (upper 85–90% = frame, lower 10–15% = margin) to preserve 16:9 within a 2×2/2×3/3×3 grid.
4. **Reference zone content is user-defined**: Describe what goes into character/location/prop panels based on the actual reference images provided.
5. **Anti-noise lives in word choice per frame + layout-level language**: Use the same clean vocabulary across all cuts and reference zones.
6. **Negative prompt is scene-specific and short**: ~10–15 terms. Never dump the full generic methodology.
7. **Never transfer reference image noise**: Compression artifacts, banding, micro-pattern noise are pollution, not style.
8. **Annotations, arrows, and text labels on reference images are NOT scene content.** If the blockout contains red arrows, dimension lines, text labels, or wireframe edges, explicitly instruct the model: "The [color] arrows / text labels in the reference are ANNOTATIONS only. Do NOT draw them in the final image." The model will otherwise treat annotations as part of the scene.
9. **When a layout/blockout reference is provided, the text prompt MUST NOT describe spatial relationships, object positions, or composition layout.** The image is the sole authority on WHERE things are; text controls HOW things look and FEEL. Any text description of spatial relationships risks overriding or corrupting the reference.
10. **Check for repetition before output.**
11. Read `meta/gpt-image-hygiene.md` for full methodology.

---

## Output Example Structure

```
Based on the [N] attached reference image(s) — [Image 1: character concept], [Image 2: location concept] ... —
generate a single comprehensive keyframe design sheet.

**Image 1 — Character Reference ([Name]):**
This is the EXACT character identity source. You MUST reproduce [Name]'s appearance PRECISELY as shown:
[face structure, hair, body type, outfit]. Face, hair, body, and outfit must match the reference EXACTLY
across all keyframe frames. Do NOT alter the character's appearance.

**Image 2 — Location Reference ([Location name]):**
Extract and adopt ONLY the visual DNA: [palette, light ratio, atmospheric treatment, etc.].
Do NOT copy specific buildings or landmarks beyond what is needed for the location reference zone.

## Overall Canvas Layout

A single 16:9 image organized as a production design sheet with two horizontal zones.

TOP ZONE (upper 40% of canvas): Split into two side-by-side reference panels ...

BOTTOM ZONE (lower 60% of canvas): A 2×2 grid of 4 keyframe cells labeled CUT 1 through CUT 4.
Each cell is split vertically:
- Upper part (roughly 85–90% of cell height): The actual cinematic keyframe frame —
  this MUST be a 16:9 landscape rectangular frame, wider than tall, aspect ratio 1.77:1,
  NOT square. The frame edge is a thin clean border.
- Lower part (roughly 10–15% of cell height): A clean neutral margin area below the frame.
  The SHOT_ID label sits here in small light gray text.

## CUT 1 · SHOT_ID · Brief Description
[5-field content formula]

## CUT 2 · SHOT_ID · Brief Description
[5-field content formula]

... (repeat for each cut)

## Global Style Lock
[Style suffix + palette + vocabulary lock]

## Clean Rendering
[Anti-noise rendering block tailored to scene]

Avoid: [Scene-specific negative terms]
```
