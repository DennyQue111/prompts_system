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
| `text_to_image_midjourney.md` | Midjourney | Single cinematic character still directly in MJ |

## Usage
- If the user wants Gemini → use `text_to_image_gemini.md` or `image_to_image_gemini.md`
- If the user wants GPT → use `text_to_image_gpt.md` or `image_to_image_gpt.md`
- If the user specifically requests Midjourney → use `text_to_image_midjourney.md`
- For image layout structure, see `concept-sheet/character-sheet/`
- For GPT anti-noise methodology, see `../../meta/gpt-image-hygiene.md`
