## Description
Use this architecture when extracting + reproducing a character from a **Midjourney reference image** for **GPT**.

GPT tends to amplify micro-texture noise in i2i mode — the reference image's texture artifacts can "seed" aggressive detail in the output. This architecture includes anti-noise controls specific to the i2i pipeline.

**For Gemini** → use `image_to_image_gemini.md`.

## Workflow (5 Steps)

Same as Gemini: Source Observation → Style Analysis → Subject Extraction → View Deduction → Output Prompt.
Full methodology: see `concept/character/image_to_image_gemini.md`.

## GPT-Specific Modifications

### Step 5 (Output Prompt) — append this block:

```
[style preservation keywords] +

[Layout instruction: 16:9 character concept design sheet, clean near-white background...] +

MAIN VISUAL — [full-body, content from gemini workflow] +

VIEW VARIATIONS — [from gemini workflow] +

EXPRESSIONS — [from gemini workflow] +

BOTTOM ROW — [from gemini workflow] +

🧹 GPT CLEAN-RENDER LAYER:
Preserve the reference image's creative style (line quality, shading, color grading, material rendering, camera language) but filter OUT:
— All micro-texture noise from the reference
— Reference's compression artifacts
— Reference's dark-band noise or muddy shadow regions

Apply controlled detail only to key surfaces:
— Face: natural facial planes, matte skin with soft specular highlights, subtle pores only where visible
— Hair: grouped into readable strands, not individual micro-fibers
— Clothing fabric: weave texture only on near-plane surfaces, not distant fabric
— Background: clean smooth tones, no texture transfer from reference background

clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
clean blurred background, smooth background tones,
minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise, facial artifact marks,
reference artifact bleed, compression grain transfer.
```

### Detail Word Control in Output Prompt

| ❌ Avoid | ✅ Use |
|---|---|
| ultra detailed reference extraction | balanced style transfer |
| micro detail everywhere | selective fine detail on key surfaces |
| highly textured rendering | controlled material rendering |
| photorealistic skin pores | natural facial planes, subtle skin texture |
| cinematic bokeh background | clean blurred background |

## Scoring Rubric

[Same as image_to_image_gemini.md]

## Key Rules (GPT-extended)

1. Use gemini.md for Steps 1-4 (observation, analysis, extraction, deduction) — identical workflow.
2. In Step 5 (output prompt), always append the GPT Clean-Render Layer above.
3. Never transfer the reference image's compression artifacts or noise texture — treat these as pollution, not style.
4. Background in output must be "clean smooth background" explicitly, regardless of reference image's background.
5. Read `meta/gpt-image-hygiene.md` for full methodology.
