## Description
Use this architecture when generating a location/environment image with **GPT**. GPT tends to produce dirty location images — residual texture noise in shadows, muddy atmospheric gradients, hidden watermark-like marks in backgrounds.

Anti-noise discipline is embedded in word choice, not appended as a long block.

**For Gemini** → use `text_to_image_gemini.md`.

## Prompt Formula

```
[Location type] + [Geography & spatial layout] + [Architecture & structural elements] +
[Time & weather conditions] + [Atmosphere & mood] + [Lighting & color palette] +
[Detail accents] +
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
| **Style suffix** | Rendering quality + art style |

## GPT Anti-Noise: Pre-Writing Checklist

Define before writing the prompt (do NOT output this to model):
- **Primary surface materials**: each surface type and how it responds to light (wet vs dry, matte vs reflective)
- **Light source logic**: direction + color temp of each source
- **Contact shadows**: only at real architectural seams, eaves, road edges
- **Exposure**: shadows with readable structure, highlights not blown

## GPT Word Choice Guide

| ❌ Avoid (triggers GPT noise) | ✅ Use in description |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective detail on architectural surfaces only |
| highly textured surfaces | controlled material rendering |
| cinematic bokeh background | clean depth of field with smooth falloff |
| dark atmospheric background | smooth dark tones, low texture background |
| realistic wet ground | subtle reflections, strict wet/dry boundaries |
| photorealistic texture | natural texture only |

## GPT Style Suffix

Simple rendering descriptors — avoid camera-brand language (Arri, IMAX, etc.) which triggers excessive texture:
```
16:9 cinematic wide establishing shot, [time of day], [weather],
controlled color grading, clean atmosphere, smooth gradients
```

## Negative Prompt (scene-specific, short)

Tailor ~10-15 terms to actual scene. Example for night/rain:
```
Avoid: ghost texture, repetitive micro-pattern noise, dirty texture buildup,
muddy shadows, clipped highlights, crushed blacks, dark-band noise,
sky gradient artifacts, fog noise patterns, milky reflections.
```

For other scene types, curate from `meta/gpt-image-hygiene.md`.

## Key Rules

1. Focal anchor — same as Gemini.
2. Time of day is non-negotiable — same as Gemini.
3. Atmosphere > object inventory — same as Gemini.
4. Include ceiling height / room scale for interiors — same as Gemini.
5. Avoid list-like descriptions — same as Gemini.
6. **Layout reference**: `concept-sheet/location-sheet/gpt.md`
7. **Anti-noise is in word choice, not appended block** — use the word choice table while writing. Negative prompt is short and scene-specific.
8. **Background gradients must be explicitly "smooth"** — GPT defaults to noisy gradient transitions.
9. **Dark scenes are highest risk** — use "smooth dark tones with readable shadow floor."
10. **Check for repetition before output** — delete anything that says the same thing twice.
11. Read `meta/gpt-image-hygiene.md` for full methodology.

## Scoring Rubric

[Same as text_to_image_gemini.md]
