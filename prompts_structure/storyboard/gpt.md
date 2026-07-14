## Description
GPT variant of storyboard — multi-frame narrative sequence. Same structure as `gemini.md`. Storyboard frames are simpler/sketchier than concept art — but GPT still over-details them.

**For Gemini** → use `gemini.md`. Full storyboard architecture → see `storyboard/gemini.md`.
**Scene-type specializations**: `action.md`, `dialogue.md`, `vfx.md` are model-agnostic (apply to both Gemini and GPT).

## Storyboard Prompt Composition (GPT)

```
[📐 Storyboard Header:]
[number of frames] storyboard, [row layout],
clean near-white background, clean thin panel borders,
minimal clean typography for labels.

[FRAME 1:]
[shot type + angle + focal length] — [description]
(controlled line work, clean shading, smooth backdrop)

[FRAME 2:]
[shot type + angle + focal length] — [description]
(controlled line work, clean shading, smooth backdrop)

[...]

All frames: consistent detail level,
clean panel separators, no background texture bleed.

Avoid: ghost texture, dirty texture buildup, panel border noise,
inconsistent frame rendering, typography artifacts.
```

## GPT Word Choice Guide (per frame)

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed sketch | controlled line work, clean shading |
| highly textured rendering | balanced detail, smooth backdrop |
| photorealistic storyboard | clean panel composition |

## Key Rules

1. **Storyboard structure**: same as gemini.md.
2. **Anti-noise is in per-frame word choice, not an appended block** — "controlled line work, clean shading, smooth backdrop" in each frame description is sufficient.
3. **All frames must share the same detail level** — inconsistent frame quality breaks storyboard readability.
4. **Panel borders: "clean thin lines"** — GPT decorates storyboard panel borders aggressively.
5. **Scene-type specializations (action/dialogue/vfx)**: apply per-frame clean vocabulary to whichever scene type. The specialization logic itself is model-agnostic.
6. **Check for repetition before output.**
7. Read `meta/gpt-image-hygiene.md` for full methodology.
