## Description
Use this architecture when generating an image of a humanoid character with **GPT** — a multi-panel concept design sheet (16:9).

GPT tends to produce "dirty" images (uncontrolled micro-texture, residual noise, muddy shadows). Anti-noise is embedded in word choice, not appended as a long block.

**For Gemini** → use `text_to_image_gemini.md`.

## Core Principle: Show, Don't Tell

Same as Gemini: every personality trait must be translated into a visible physical cue before it enters the prompt. "He is loyal" → "He unconsciously positions his body half a step in front of his teammates."

### Personality-to-Visual Translation (same dimensions as Gemini)

| Dimension | What to Describe |
|-----------|-----------------|
| **Body language** | Weight distribution, shoulder angle, head tilt, reaction speed |
| **Hand state** | Calluses, scars, dirt under nails, grip style, resting position |
| **Signature micro-gesture** | One recurring unconscious action |
| **Contrast shot** | One visual contradiction that reveals hidden depth |

## Panel Content (same as Gemini)

| Panel | Content | What to Describe |
|-------|---------|-----------------|
| **Main Visual** (~1/3 width, ~4/5 height) | Full-body, default outfit, neutral expression | Face → Hair → Build → Body language → Outfit (prototype rule) → Accessories & body marks → Posture |
| **View Variations** (upper-right half) | 2–3 angles (front, back, side) | ~1 sentence each. Only what's NEW. |
| **Expressions** (lower-right half, 2×2 grid) | Joy / Anger / Sorrow / Happiness | Each: brow position + eye shape + mouth + tension |
| **Bottom Row** (full width, ~1/5 height) | All clothing, accessories, scars, birthmarks | Clothing laid flat. Marks as body close-ups. |

## Prompt Formula

```
[Subject: name + age + role] +
[Face + Hair + Build — highlight face/body contrast] +
[Personality-to-Visual: body language + hand state + signature gesture + contrast shot] +
[Outfit: outer → inner → bottom → shoes. Prototype rule: "combat-adapted [original garment]"] +
[Accessories & body marks] +
[Posture] +
[Layout instruction: 16:9 concept design sheet, clean near-white background, subtle paper texture, thin dark panel dividers, exact grid positions from concept-sheet/character-sheet/gpt.md]
```

## GPT Anti-Noise: Pre-Writing Checklist

Define before writing (do NOT output to model):
- **Main materials**: skin, hair, each garment fabric, each accessory material
- **Surface response**: matte/satin/rough/wet/reflective — each material's light behavior
- **Light direction**: main light + color temp + rim light (if any)
- **Contact shadows**: only at real seams, collars, cuffs, belt line, under chin
- **Exposure control**: highlights not blown, shadows with readable structure

## GPT Word Choice Guide

| ❌ Avoid (triggers GPT noise) | ✅ Use in description |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective fine detail on key surfaces only |
| highly textured | controlled material rendering |
| realistic texture | natural texture only |
| cinematic bokeh | clean blurred background |
| dark atmospheric background | smooth dark tones, low texture background |
| wet glossy | subtle reflections, strict wet/dry boundaries |
| photorealistic skin texture | natural facial planes, matte skin with soft specular highlights |

## Negative Prompt (scene-specific, short)

Tailor ~10-15 terms to the character. Example for a character sheet:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise, facial artifact marks.
```

## If Output Is Already Dirty → Regenerate Fresh

Don't i2i repair a dirty image (amplifies noise). Regenerate with fresh prompt, keeping subject/pose/composition but rebuilding the material-light-detail stack from scratch.

## Key Rules

1. Personality first — same as Gemini.
2. Prototype rule — same as Gemini.
3. Expression contrast — same as Gemini.
4. Scan for hidden items — same as Gemini.
5. **Layout reference**: `concept-sheet/character-sheet/gpt.md`
6. **Anti-noise is in word choice, not an appended block** — use the word choice table while writing. Negative prompt is short and scene-specific.
7. **Never use "ultra detailed", "8K", "hyper detailed", "photorealistic skin texture"** — these trigger dirty rendering on GPT.
8. **Material-light definition is NOT optional** — single-most important pre-writing step.
9. **Background must be explicitly "smooth clean background"** — not "studio background" or left unspecified.
10. **Check for repetition before output** — delete anything that says the same thing twice.
11. Read `meta/gpt-image-hygiene.md` for full methodology.

## Scoring Rubric (same as Gemini)

[Use the scoring rubric from `text_to_image_gemini.md`]
