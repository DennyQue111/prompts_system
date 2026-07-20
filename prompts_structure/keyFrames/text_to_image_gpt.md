## Description
GPT variant of KeyFrames — 3×3 grid single-image visual consistency anchor. Same structure as `gemini.md`. Anti-noise embedded in word choice and grid-level control.

**For Gemini** → use `gemini.md`. Full keyFrames architecture → see `keyFrames/gemini.md`.

## GPT-Specific Modifications

### Why KeyFrames on GPT Needs Extra Care
The 3×3 grid packs 9 scenes into one image. GPT tends to:
1. Apply different texture density to different grid cells
2. Generate noisy cell borders/separators
3. Produce inconsistent grain levels across cells

### Grid-Level Control Language
Use in prompt body — these words replace the old appended block:
- Cell separators: "crisp 2px lines, clean near-white"
- Cross-cell consistency: "consistent rendering quality across all 9 cells"
- No macro texture variation between cells

### Per-Cell Word Choice
For each of the 9 cells, brief material-level control in the description:
```
Cell X: [scene content] — [primary surface] under [light source], [matte/glossy/wet], clean rendering
```

### Negative Prompt (grid-specific, short)
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
cell-to-cell texture inconsistency, grid line artifacts, separator border noise,
dirty texture buildup, muddy shadows, clipped highlights, crushed blacks.
```

## Key Rules

1. **Grid structure**: same as gemini.md.
2. **Anti-noise is in word choice per cell + grid-level language, not an appended block.**
3. **Cell separators must be "crisp clean lines"** — GPT decorates grid lines with noise artifacts.
4. **All 9 cells share the same clean word choice pattern** — don't vary texture vocabulary per cell.
5. **Check for repetition before output.**
6. Read `meta/gpt-image-hygiene.md` for full methodology.
