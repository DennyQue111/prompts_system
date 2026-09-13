# Storyboard

## What This Is
Records the prompt structure for generating **storyboards** — visual scripts showing narrative progression through sequential frames. Storyboards communicate scene flow before video production.

## Available Files

| File | What It Is |
|------|-------------|
| `core.md` | Renderer-neutral storyboard architecture — action, dialogue, VFX, and mixed scene specializations |
| `../adapters/gpt-image.md` | GPT anti-noise, clean-ink / rough-pencil constraints, exclusions |
| `../adapters/gemini-image.md` | Gemini prompt compilation |
| `../adapters/jimeng-image.md` | Jimeng Chinese modules, 2,000-character discipline, B&W control |
| `_archive/` | Archived standalone scene-type files (action/dialogue/vfx) — content has been merged into `core.md` |

## Usage
1. **Determine the model** — default to GPT when unspecified; otherwise honor Gemini, GPT, or 即梦（Jimeng）
2. **Load `core.md`** for the full architecture + scene-type specializations
3. **Load exactly one renderer Adapter** for model-specific compilation
4. **If GPT**: read `../meta/gpt-image-hygiene.md` before writing the prompt
5. **Determine scene type(s)** — action / dialogue / VFX / mixed. Apply relevant sections from `core.md`.

## File Structure (After Merge)

```
storyboard/
├── core.md            ← Full architecture + all scene-type sections (action/dialogue/vfx/mixed)
├── ../adapters/       ← One selected renderer adapter
├── README.md          ← This file
└── _archive/
    ├── action.md      ← Archived (merged into core.md)
    ├── dialogue.md    ← Archived (merged into core.md)
    └── vfx.md         ← Archived (merged into core.md)
```
