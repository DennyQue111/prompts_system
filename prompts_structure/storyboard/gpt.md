## Description
GPT variant of storyboard — multi-frame narrative sequence. Same structure as `gemini.md` with GPT anti-noise.

**For Gemini** → use `gemini.md`. Full storyboard architecture → see `storyboard/gemini.md`.
**Scene-type specializations**: `action.md`, `dialogue.md`, `vfx.md` are model-agnostic (apply to both Gemini and GPT).

## GPT-Specific Modifications

### Storyboard Frame Anti-Noise
Storyboard frames are simpler/sketchier than concept art — but GPT still over-details them. Control:

**Per-frame control (append to each frame in the storyboard):**
```
clean rendering, balanced detail,
controlled line work, clean shading with no residual noise,
smooth clean backdrop, minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, dirty texture buildup,
repetitive micro-pattern noise, muddy shadows, compressed blacks,
background noise artifacts, sketch-line artifacts.
```

### Storyboard Prompt Composition (GPT)
```
[📐 Storyboard Header:]
[number of frames] storyboard, [row layout],
clean near-white background, clean panel borders,
minimal clean typography for labels.

[FRAME 1:]
[shot type + angle + focal length] — [description] +
clean rendering, balanced detail, controlled line work +
no panel border artifacts

[FRAME 2:]
[shot type + angle + focal length] — [description] +
clean rendering, balanced detail, controlled line work +
no panel border artifacts

[...]

[🧹 Global clean-render:]
All frames: consistent detail level,
clean panel separators, no background texture bleed,
clean typography for frame numbers and shot labels.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
panel border noise, inconsistent frame rendering,
dirty texture buildup, typography artifacts.
```

### Key Rules
1. **Storyboard structure**: same as gemini.md.
2. **Every frame must carry its per-frame clean-render anchor.**
3. **All frames in a storyboard must share the same detail level** — inconsistent frame quality breaks storyboard readability.
4. **Panel borders: "clean thin lines"** — GPT decorates storyboard panel borders aggressively.
5. **Scene-type specializations (action/dialogue/vfx)**: apply per-frame clean anchor to whichever scene type. The specialization logic itself is model-agnostic.
6. Read `meta/gpt-image-hygiene.md` for full methodology.
