## Description
GPT variant of prop concept generation. Same structure as `gemini.md` with GPT anti-noise adaptations.

**For Gemini** → use `gemini.md`. Full prop architecture → see `concept/prop/gemini.md`.

## GPT-Specific Modifications

### Prompt Formula (augmented)

```
[Subject / Prop] + [Material & texture] + [Size & scale] +
[Condition & age] + [Key details & features] +
[Composition & perspective] + [Environment / context] +
[🧹 GPT Clean-Render Layer] +
[Style suffix]
```

### GPT Anti-Noise Layer

**Material-Light Definition (write BEFORE the prompt):**
1. Primary material + how it responds to light (polished metal vs matte ceramic vs aged wood — very different)
2. What's reflective vs light-absorbing?
3. Where are the contact shadows? (between components, at seams, where the object meets its surface)
4. What surfaces should be clean vs textured?

**Detail Word Control:**
| ❌ | ✅ |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective detail on material boundaries only |
| highly textured surface | controlled material rendering |
| photorealistic macro texture | natural texture only |
| cinematic bokeh background | clean smooth background |

**Clean Rendering Block (append to every prompt):**
```
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
clean smooth background, minimal repetitive patterns,
physically distinct material classes with clean boundaries.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
surface artifact noise, faux watermark.
```

### Key Rules
1. **Prop composition**: same as gemini.md. Hero shot (centered, dramatic lighting) works best.
2. **Every prompt must carry the Clean Rendering Block.**
3. **Reflective surfaces (metal, glass, wet)**: write "subtle reflections with clean boundaries" — GPT over-drives reflections into noise.
4. **Aged/worn props**: "controlled wear patterns, natural aging only" — no random noise masquerading as patina.
5. Read `meta/gpt-image-hygiene.md` for full methodology.
