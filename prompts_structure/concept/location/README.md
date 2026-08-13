# Location (Environment / Setting)

## What This Is
Records the concept design prompt structure for **story locations and environments** — an HDR 4-panel 16:9 layout. 4 panels from the same standing position, each rotated 90°, forming a 360° environmental reference for video generation.

## Available Files

| File | Target | Use Case |
|------|--------|----------|
| `text_to_image_gemini.md` | Gemini | Generate location from text description |
| `text_to_image_gpt.md` | GPT | Generate location from text (with anti-noise) |
| `image_to_image_gemini.md` | Gemini | Extract & reproduce location style from MJ reference |
| `image_to_image_gpt.md` | GPT | Extract & reproduce location style from MJ reference (with anti-noise) |
| `image_to_image_jimeng.md` | 即梦 (Jimeng) | Extract location style from reference, Chinese modular prompt |
| `midjourney.md` | Midjourney | Single atmospheric establishing shot directly in MJ |
| `hdr_layout_instruction.md` | All models | HDR 4-panel layout spec (2×2 grid, 28mm, 90° rotation) |
| `general_layout_instruction.md` | Archived | Old 6-panel design sheet layout — superseded by `hdr_layout_instruction.md` |

## Usage
- If the user wants Gemini → use `text_to_image_gemini.md` or `image_to_image_gemini.md`
- If the user wants GPT → use `text_to_image_gpt.md` or `image_to_image_gpt.md`
- If the user wants 即梦 (Jimeng) → use `image_to_image_jimeng.md` (i2i only)
- If the user specifically requests Midjourney → use `midjourney.md`
- For HDR 4-panel layout structure, see `hdr_layout_instruction.md` in this directory
- For GPT anti-noise methodology, see `../../meta/gpt-image-hygiene.md`
