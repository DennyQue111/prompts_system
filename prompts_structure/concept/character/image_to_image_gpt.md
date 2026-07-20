## Description
Use this architecture when extracting + reproducing a character from a **Midjourney reference image** for **GPT**.

GPT amplifies micro-texture noise in i2i mode — the reference image's texture artifacts can "seed" aggressive detail in the output. This architecture includes anti-noise controls specific to the i2i pipeline.

**For Gemini** → use `image_to_image_gemini.md`.

## Workflow (5 Steps)

Same as Gemini: Source Observation → Style Analysis → Subject Extraction → View Deduction → Output Prompt.
Full methodology: see `concept/character/image_to_image_gemini.md`.

## GPT-Specific Modifications

### Style Analysis (Step 2) — Add noise detection
When analyzing the reference image, explicitly flag:
- **Noise regions**: dark shadow areas with banding or color noise
- **Texture overdrive zones**: surfaces with excessive micro-detail
- **Gradient artifacts**: skin/fabric areas with visible step artifacts
- **Clean zones**: areas where detail is appropriately controlled — model these for GPT output

### Output Prompt (Step 5)

Reference-anchored structure:

```
Based on the attached reference image — [brief subject ID] — generate a full character concept design sheet. EXTEND from the reference, not create from scratch.

[Layout instruction: 16:9 character concept design sheet, clean near-white background...] +

MAIN VISUAL — reproduce the reference image exactly + text/label fixes + costume detail corrections +
VIEW VARIATIONS — deduced from reference: back view, profile, etc. +
EXPRESSIONS — 4 expressions in 2×2 grid +
BOTTOM ROW — clothing, accessories, body marks laid flat +

Style: [keywords extracted from reference — 1 line only] +

Avoid: [~10-15 scene-relevant terms only]
```

### GPT Word Choice Guide

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed reference extraction | balanced style transfer |
| micro detail everywhere | selective fine detail on key surfaces |
| highly textured rendering | controlled material rendering |
| photorealistic skin pores | natural facial planes, subtle skin texture |
| cinematic bokeh background | clean blurred background |

### Negative Prompt (character-specific, short)

```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, pasted-on texture, muddy shadows,
uniform plastic gloss, milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise, facial artifact marks,
reference artifact bleed, compression grain transfer.
```

## Key Rules

1. Use gemini.md for Steps 1-4 (observation, analysis, extraction, deduction).
2. **Prompts must reference the image**: start with "Based on the attached reference image..."
3. **Anti-noise is in word choice, not an appended block** — use the word choice table while writing.
4. **Negative prompt is short and scene-specific** — never dump the full generic methodology.
5. Never transfer the reference image's compression artifacts or noise texture — treat these as pollution, not style.
6. Background in output must be "clean smooth background" explicitly.
7. **Check for repetition before output.**
8. Read `meta/gpt-image-hygiene.md` for full methodology.

## Scoring Rubric

[Same as image_to_image_gemini.md]
