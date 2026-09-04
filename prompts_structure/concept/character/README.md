# Character (Humanoid / Human)

## What This Is
Records the concept design prompt structure for **human and humanoid characters** — a multi-panel 16:9 design sheet. Covers personality-to-visual translation, faces, body types, outfits, accessories, and expressions.

## Available Model Variants

| Variant | Target | Use Case |
|---------|--------|----------|
| `text_to_image_gemini.md` | Gemini | Generate character from text description |
| `text_to_image_gpt.md` | GPT | Generate character from text (with anti-noise) |
| `image_to_image_gemini.md` | Gemini | Extract & reproduce character from MJ reference |
| `image_to_image_gpt.md` | GPT | Extract & reproduce character from MJ reference (with anti-noise) |
| `image_to_image_jimeng.md` | 即梦 (Jimeng) | Extract a character into a simple video-reference sheet |
| `text_to_image_midjourney.md` | Midjourney | Single cinematic character still directly in MJ |

## Usage
- If no model is specified → default to the applicable GPT file
- If the user wants Gemini → use `text_to_image_gemini.md` or `image_to_image_gemini.md`
- If the user wants GPT → use `text_to_image_gpt.md` or `image_to_image_gpt.md`
- If the user wants 即梦 (Jimeng) for i2i → use `image_to_image_jimeng.md`
- If the user specifically requests Midjourney → use `text_to_image_midjourney.md`
- For a full production sheet, see `general_layout_instruction.md`; for the default i2i video-reference sheet, see `simple_layout_instruction.md`
- For GPT anti-noise methodology, see `../../meta/gpt-image-hygiene.md`
