## Description
Use this architecture when extracting + reproducing a location/environment from a **Midjourney reference image** for **GPT**.

GPT i2i amplifies reference image noise — compression artifacts, dark-band mud, micro-pattern noise all get aggressively rendered in the output. This architecture filters reference pollution while preserving style DNA.

**For Gemini** → use `image_to_image_gemini.md`.

## Workflow (5 Steps)

Same as Gemini: Source Observation → Style Analysis → Location Extraction → Spatial Deconstruction → Output Prompt.
Full methodology: see `concept/location/image_to_image_gemini.md`.

## GPT-Specific Modifications

### Style Analysis (Step 2) — Add noise detection
When analyzing the reference image, explicitly flag:
- **Noise regions**: dark shadow areas with banding or color noise
- **Texture overdrive zones**: surfaces with excessive micro-detail that would read as "dirty" on GPT
- **Gradient artifacts**: sky or fog areas with visible step artifacts
- **Clean zones**: areas where detail is appropriately controlled — these are the model for GPT output

### Output Prompt (Step 5) — append GPT Clean-Render Layer:

```
[style preservation keywords] +

[Layout instruction: 16:9 location concept design sheet, clean near-white background...] +

MAIN VISUAL — [establishing shot, content from gemini workflow] +

ALTERNATE ANGLE — [from gemini workflow] +

TOP-DOWN VIEW — [from gemini workflow] +

MID-DISTANCE SHOTS — [from gemini workflow] +

BOTTOM ROW — [from gemini workflow] +

🧹 GPT CLEAN-RENDER LAYER:
Preserve the reference image's creative style (color palette, light ratio, atmosphere, camera language, material palette) but FILTER OUT:
— Reference's dark-band noise and shadow artifacts
— Compression grain in gradient regions
— Excessive micro-texture on distant surfaces
— Reference's background noise pattern

Apply controlled detail:
— Architectural surfaces: texture only on near-plane materials, not distant facades
— Sky/atmosphere: smooth clean gradients, no step artifacts
— Ground/wet surfaces: subtle reflections with clean boundaries, not full mirror noise
— Shadows: smooth dark tones with readable detail, not muddy crushed blacks

clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
smooth background tones, clean depth of field,
smooth dark tones with readable shadow detail,
minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, milky reflections,
clipped highlights, crushed blacks, dark-band noise,
sky gradient artifacts, fog noise patterns,
reference artifact bleed, compression grain transfer.
```

### Detail Word Control in Output Prompt

| ❌ Avoid | ✅ Use |
|---|---|
| ultra detailed environment | balanced spatial detail |
| micro texture on all surfaces | selective texture on architectural focus points |
| highly textured rendering | controlled material rendering |
| atmospheric cinematic bokeh | clean depth of field |
| dark atmospheric scene | smooth dark tones, clean shadow falloff |

## Key Rules (GPT-extended)

1. Use gemini.md for Steps 1-4 — identical workflow.
2. In Step 5, always append the GPT Clean-Render Layer.
3. **Never transfer reference image noise** — compression artifacts, banding, micro-pattern noise are pollution, not style.
4. **Reference background texture ≠ style** — extract only color palette, light ratio, and atmosphere from the reference background, not its noise profile.
5. **Wet/dark scenes are highest risk** — add "smooth dark tones, subtle reflections with clean boundaries" for any night/rain/fog location.
6. Read `meta/gpt-image-hygiene.md` for full methodology.
