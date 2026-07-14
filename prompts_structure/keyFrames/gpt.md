## Description
GPT variant of KeyFrames — 3×3 grid single-image visual consistency anchor. Same structure as `gemini.md` with GPT anti-noise.

**For Gemini** → use `gemini.md`. Full keyFrames architecture → see `keyFrames/gemini.md`.

## GPT-Specific Modifications

### Why KeyFrames on GPT Needs Extra Care
The 3×3 grid packs 9 scenes into one image. GPT tends to:
1. Apply different texture density to different grid cells
2. Generate noisy cell borders/separators
3. Produce inconsistent grain levels across cells

### Anti-Noise Strategy

**Grid-level control (append to the full grid prompt):**
```
3×3 grid single image, 16:9 composite,
clean near-white cell separators with crisp 2px lines,
consistent rendering quality across all 9 cells,
balanced detail, clean gradients, controlled highlights,
no texture variation between grid cells,
smooth background tones, minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, cell-to-cell texture inconsistency,
grid line artifacts, separator border noise,
dirty texture buildup, muddy shadows, clipped highlights, crushed blacks.
```

### Per-Cell Material Control
For each of the 9 cells, brief material-light definition:
```
Cell X: [scene content] — [primary surface] under [light source], [matte/glossy/wet], clean rendering
```

### Key Rules
1. **Grid structure**: same as gemini.md.
2. **The 3×3 composite prompt must carry the full grid-level anti-noise block.**
3. **Cell separators must be "crisp clean lines"** — GPT decorates grid lines with noise artifacts.
4. **All 9 cells share the same clean-render anchor** — don't vary texture density per cell.
5. Read `meta/gpt-image-hygiene.md` for full methodology.
