## Description
GPT variant of multi-shot sequence pre-vis (Seedance video production blueprint). Same structure as `gemini.md`. Anti-noise is embedded in each shot's word choice, not appended as a long block.

**For Gemini** → use `gemini.md`. Full sequence architecture → see `sequence/gemini.md`.

## GPT-Specific Modifications

### Anti-Noise for Sequence Shots
Each shot is a single image frame. GPT produces inconsistent noise profiles across shots if not controlled. Control strategy:
1. Same clean word choice for ALL shots — don't vary texture vocabulary per shot
2. Consistent background control — all shots share background texture level specification
3. Frame consistency check: verify shot-to-shot word choices don't introduce new noise patterns

### GPT Word Choice Guide (per shot)

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed, 8K | balanced detail |
| micro detail everywhere | controlled rendering |
| highly textured | clean material rendering |
| photorealistic | natural texture only |

### GPT Sequence Style Suffix (per shot)
```
[shot description], 16:9 cinematic still,
controlled color grading matching sequence-wide palette,
clean atmosphere with consistent detail level
```

### Negative Prompt (append to each shot, identical across sequence)
Keep short and scene-specific. Example:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, clipped highlights, crushed blacks.
```

## Key Rules

1. **Sequence structure**: same as gemini.md.
2. **Anti-noise is in word choice per shot, not an appended block** — every shot uses the same controlled vocabulary.
3. **Time-of-day transitions**: update lighting description but keep clean vocabulary identical across shots.
4. **No shot-level vocabulary deviation** — all shots share the same word choice pattern to avoid jarring texture shifts between cuts.
5. **Check for repetition before output.**
6. Read `meta/gpt-image-hygiene.md` for full methodology.
