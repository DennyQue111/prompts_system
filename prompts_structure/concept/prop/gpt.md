## Description
GPT variant of prop concept generation. Same structure as `gemini.md`. Anti-noise is embedded in word choice, not appended as a long block.

**For Gemini** → use `gemini.md`. Full prop architecture → see `concept/prop/gemini.md`.

## Prompt Formula (augmented)

```
[Subject / Prop] + [Material & texture] + [Size & scale] +
[Condition & age] + [Key details & features] +
[Composition & perspective] + [Environment / context] +
[Style suffix]
```

## GPT Anti-Noise: Pre-Writing Checklist

Define before writing (do NOT output to model):
1. Primary material + how it responds to light (polished metal vs matte ceramic vs aged wood — very different)
2. What's reflective vs light-absorbing?
3. Contact shadows: between components, at seams, where the object meets its surface
4. What surfaces should be clean vs textured?

## GPT Word Choice Guide

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective detail on material boundaries only |
| highly textured surface | controlled material rendering |
| photorealistic macro texture | natural texture only |
| cinematic bokeh background | clean smooth background |

## Negative Prompt (prop-specific, short)

```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
surface artifact noise, faux watermark.
```

## Key Rules

1. **Prop composition**: same as gemini.md. Hero shot (centered, dramatic lighting) works best.
2. **Anti-noise is in word choice, not an appended block** — use the word choice table while writing. Negative prompt is short and scene-specific.
3. **Reflective surfaces (metal, glass, wet)**: write "subtle reflections with clean boundaries" — GPT over-drives reflections into noise.
4. **Aged/worn props**: "controlled wear patterns, natural aging only" — no random noise masquerading as patina.
5. **Check for repetition before output.**
6. Read `meta/gpt-image-hygiene.md` for full methodology.
