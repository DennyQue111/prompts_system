## Description
Use this architecture when generating a location/environment image with **GPT**. GPT tends to produce dirty location images — residual texture noise in shadows, muddy atmospheric gradients, hidden watermark-like marks in backgrounds. This architecture includes anti-noise discipline.

**For Gemini** → use `text_to_image_gemini.md`.

## Prompt Formula

```
[Location type] + [Geography & spatial layout] + [Architecture & structural elements] +
[Time & weather conditions] + [Atmosphere & mood] + [Lighting & color palette] +
[Detail accents] +
[🧹 GPT Clean-Ready Layer — SEE BELOW] +
[Style suffix]
```

## Key Components (same as Gemini)

| Component | What It Covers |
|-----------|---------------|
| **Location type** | Fundamental category |
| **Geography & spatial layout** | Scale, depth, terrain, spatial relationships |
| **Architecture & structure** | Building style, materials, key structures |
| **Time & weather** | Time of day, season, weather |
| **Atmosphere & mood** | Emotional quality |
| **Lighting & color** | Dominant light sources, color temperature |
| **Detail accents** | Small storytelling elements |
| **Style suffix** | Rendering quality + art style (GPT-optimized — see below) |

## 🧹 GPT Anti-Noise Layer (MANDATORY)

### Step 1: Material-Light Definition
Before writing the prompt, define for the location:
- **Primary surface materials**: asphalt/concrete/glass/metal/water/vegetation/stone — each one
- **How each surface responds to light**: wet vs dry, matte vs reflective, rough vs smooth
- **Light source logic**: where each light comes from and what color it casts
- **Contact shadows**: only at real architectural seams, under eaves, at road edges
- **Exposure control**: dark areas with readable structure, not crushed black; highlights not blown

### Step 2: Detail Word Control

| ❌ Avoid (GPT dirty) | ✅ Use instead |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective detail on architectural surfaces only |
| highly textured surfaces | controlled material rendering |
| cinematic bokeh background | clean depth of field with smooth falloff |
| dark atmospheric background | smooth dark tones, low texture background |
| realistic wet ground | subtle reflections, strict wet/dry boundaries |
| photorealistic texture | natural texture only |

### Step 3: Clean Rendering Block (paste at end of every prompt)

```
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
clean depth of field, smooth background tones,
smooth dark tones with readable shadow detail,
minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, milky reflections,
clipped highlights, crushed blacks, dark-band noise,
sky gradient artifacts, fog noise patterns.
```

### Step 4: GPT Style Suffix Options
GPT location prompts work best with simpler rendering descriptors:
```
16:9 cinematic wide establishing shot, [time of day], [weather],
controlled color grading, clean atmosphere, smooth gradients
```
Avoid elaborate camera-brand style suffixes (Arri, IMAX, etc.) — they trigger excessive texture on GPT.

## Key Rules (GPT-extended)

1. Focal anchor — same as Gemini.
2. Time of day is non-negotiable — same as Gemini.
3. Atmosphere > object inventory — same as Gemini.
4. Include ceiling height / room scale for interiors — same as Gemini.
5. Avoid list-like descriptions — same as Gemini.
6. **Layout reference**: `concept-sheet/location-sheet/gpt.md`
7. **Every prompt must carry the Clean Rendering Block. No exceptions.**
8. **Background gradients must be explicitly "smooth"** — GPT defaults to noisy gradient transitions.
9. **Dark scenes are highest risk for GPT** — add "smooth dark tones with readable shadow floor" for any night / interior scene.
10. Read `meta/gpt-image-hygiene.md` for full methodology.

## Scoring Rubric

[Same as text_to_image_gemini.md]
