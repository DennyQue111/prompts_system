## Description
GPT variant of entity concept generation. Same structure as `gemini.md`. Anti-noise is embedded in word choice, not appended as a long block.

**For Gemini** → use `gemini.md`. Full entity architecture → see `concept/entity/gemini.md`.

## Prompt Formula (augmented)

```
[Subject / Entity type] + [Physical form & structure] + [Materials & textures] +
[Scale & spatial presence] + [Sentience indicators] + [Behavior / agency] +
[Environment / context] +
[Style suffix]
```

## GPT Anti-Noise: Pre-Writing Checklist

Define before writing (do NOT output to model):
1. Primary material + how it responds to light: matte/glossy/translucent/emissive/metallic/rough
2. Contact shadows: between nested layers, at structural seams, at ground contact
3. What surfaces should be clean/flat vs detailed?
4. Entity-to-background boundary: crisp edge / soft glow / volumetric fade

## GPT Word Choice Guide

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed | balanced detail |
| micro detail on all surfaces | selective detail on key structural features |
| highly textured | controlled material rendering |
| photorealistic surface | natural material rendering |
| dark atmospheric void | smooth dark tones, low texture background |

## Negative Prompt (scene-specific, short)

Tailor to entity type. Example for material-based entity:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks.
```

## Key Rules

1. **Entity panel structure**: same as gemini.md.
2. **Layout reference**: `concept-sheet/entity-sheet/gpt.md`
3. **Anti-noise is in word choice, not an appended block** — use the word choice table while writing. Negative prompt is short and scene-specific.
4. **Abstract/energy-based entities**: "smooth gradients, clean light falloff" — these surfaces are most vulnerable to dirty noise on GPT.
5. **Check for repetition before output.**
6. Read `meta/gpt-image-hygiene.md` for full methodology.
