## Description
GPT variant of entity concept generation. Same structure as `gemini.md` with GPT anti-noise adaptations.

**For Gemini** → use `gemini.md`. Full entity architecture → see `concept/entity/gemini.md`.

## GPT-Specific Modifications

### Prompt Formula (augmented)

```
[Subject / Entity type] + [Physical form & structure] + [Materials & textures] +
[Scale & spatial presence] + [Sentience indicators] + [Behavior / agency] +
[Environment / context] +
[🧹 GPT Clean-Render Layer] +
[Style suffix]
```

### GPT Anti-Noise Layer

**Material-Light Definition (write BEFORE the prompt):**
1. What is the entity's primary material? How does it respond to light? (matte/glossy/translucent/emissive/metallic/rough)
2. Where are the contact shadows? (between nested layers, at structural seams, at ground contact)
3. What surfaces should be clean/flat vs detailed?
4. What's the entity-to-background boundary condition? (crisp edge / soft glow / volumetric fade)

**Detail Word Control:**
| ❌ | ✅ |
|---|---|
| ultra detailed | balanced detail |
| micro detail on all surfaces | selective detail on key structural features |
| highly textured | controlled material rendering |
| photorealistic surface | natural material rendering |
| dark atmospheric void | smooth dark tones, low texture background |

**Clean Rendering Block (append to every prompt):**
```
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
smooth background tones, minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks.
```

### Key Rules
1. **Entity panel structure**: same as gemini.md.
2. **Layout reference**: `concept-sheet/entity-sheet/gpt.md`
3. **Every prompt must carry the Clean Rendering Block.**
4. **Abstract/energy-based entities**: "smooth gradients, clean light falloff" — these surfaces are most vulnerable to dirty noise on GPT.
5. Read `meta/gpt-image-hygiene.md` for full methodology.
