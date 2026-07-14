## Description
GPT variant of multi-shot sequence pre-vis (Seedance video production blueprint). Same structure as `gemini.md` with GPT anti-noise.

**For Gemini** → use `gemini.md`. Full sequence architecture → see `sequence/gemini.md`.

## GPT-Specific Modifications

### Anti-Noise for Sequence Shots
Each shot in the sequence is a single image frame — GPT tends to produce inconsistent noise profiles across shots. Control strategy:

1. **Same clean-render anchor for ALL shots**: every shot prompt must share the identical Clean Rendering Block suffix.
2. **Consistent background control**: all shots share background texture level specification.
3. **Frame consistency check**: verify that shot-to-shot transitions don't introduce new noise patterns.

### Clean Rendering Block (append to EVERY shot prompt in the sequence)
```
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
[background per shot],
minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks.
```

### GPT Sequence Style Suffix
```
[shot description], 16:9 cinematic still,
controlled color grading matching sequence-wide palette,
clean atmosphere with consistent detail level
```

### Key Rules
1. **Sequence structure**: same as gemini.md.
2. **Every shot prompt must carry the identical Clean Rendering Block** — consistency is critical.
3. **Time-of-day transitions**: when lighting changes across the sequence, update the lighting description but keep the clean-render tail identical.
4. **No shot-level style deviation**: all shots share the same anti-noise anchor to avoid jarring texture shifts between cuts.
5. Read `meta/gpt-image-hygiene.md` for full methodology.
