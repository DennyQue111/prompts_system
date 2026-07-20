# Location (Environment / Setting)

## What This Is
Records the concept design prompt structure for **story locations and environments** — a multi-panel 16:9 design sheet. Covers establishing shots, alternate angles, top-down overview, mid-distance details, and color palettes.

## Available Model Variants

| Variant | Target | Use Case |
|---------|--------|----------|
| `text_to_image_gemini.md` | Gemini | Generate location from text description |
| `text_to_image_gpt.md` | GPT | Generate location from text (with anti-noise) |
| `image_to_image_gemini.md` | Gemini | Extract & reproduce location style from MJ reference |
| `image_to_image_gpt.md` | GPT | Extract & reproduce location style from MJ reference (with anti-noise) |
| `midjourney.md` | Midjourney | Single atmospheric establishing shot directly in MJ |

## Usage
- If the user wants Gemini → use `text_to_image_gemini.md` or `image_to_image_gemini.md`
- If the user wants GPT → use `text_to_image_gpt.md` or `image_to_image_gpt.md`
- If the user specifically requests Midjourney → use `midjourney.md`
- For image layout structure, see `concept-sheet/location-sheet/`
- For GPT anti-noise methodology, see `../../meta/gpt-image-hygiene.md`
