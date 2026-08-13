# Storyboard

## What This Is
Records the prompt structure for generating **storyboards** — visual scripts showing narrative progression through sequential frames. Storyboards communicate scene flow before video production.

## Available Files

| File | What It Is |
|------|-------------|
| `gemini.md` | Full storyboard architecture for Gemini (default) — includes inline scene-type specializations: Action, Dialogue, VFX, Mixed |
| `gpt.md` | GPT-specific overlay — anti-noise, rough pencil style, exclusion list. Load after `gemini.md` |
| `jimeng.md` | 即梦（Jimeng）专用覆盖层 — 中文模块化提示词、2000字限制取舍、相似度滑块参考图控制、黑白线稿三重锚定。Load after `gemini.md` |
| `_archive/` | Archived standalone scene-type files (action/dialogue/vfx) — content has been merged into `gemini.md` |

## Usage
1. **Determine the model** — Gemini, GPT, or 即梦（Jimeng）
2. **Load `gemini.md`** for the full architecture + scene-type specializations
3. **If GPT**: also load `gpt.md` for model-specific overlay
4. **If GPT**: read `../meta/gpt-image-hygiene.md` before writing the prompt
5. **If 即梦**: also load `jimeng.md` for Chinese modular prompt structure, 2000-char limit strategy, and B&W triple-lock method
6. **Determine scene type(s)** — action / dialogue / VFX / mixed. Apply relevant section(s) from `gemini.md` → Scene-Type Specializations

## File Structure (After Merge)

```
storyboard/
├── gemini.md          ← Full architecture + all scene-type sections (action/dialogue/vfx/mixed)
├── gpt.md             ← GPT overlay only (references gemini.md for base structure)
├── jimeng.md          ← 即梦 overlay (Chinese modular prompts, 2000-char limit, similarity slider)
├── README.md          ← This file
└── _archive/
    ├── action.md      ← Archived (merged into gemini.md)
    ├── dialogue.md    ← Archived (merged into gemini.md)
    └── vfx.md         ← Archived (merged into gemini.md)
```
