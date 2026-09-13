# Character (Humanoid / Human)

## What This Is
Records the concept design prompt structure for **human and humanoid characters** — a multi-panel 16:9 design sheet. Covers personality-to-visual translation, faces, body types, outfits, accessories, and expressions.

## Files

| File | Purpose |
|---|---|
| `core-t2i.md` | Renderer-neutral character concept content from text |
| `core-i2i.md` | Renderer-neutral character extraction and view deduction from references |
| `simple_layout_instruction.md` | Default three-column video-reference sheet |
| `general_layout_instruction.md` | Full production design sheet |
| `text_to_image_midjourney.md` | Midjourney-only cinematic still workflow |

## Usage
- Select `core-t2i.md` or `core-i2i.md` by input mode, then select one global renderer Adapter.
- If no image model is specified → use `../../adapters/gpt-image.md`.
- If the user wants Gemini or Jimeng → replace only the Adapter with `../../adapters/gemini-image.md` or `../../adapters/jimeng-image.md`.
- If the user specifically requests Midjourney → use `text_to_image_midjourney.md`
- For a full production sheet, see `general_layout_instruction.md`; for the default i2i video-reference sheet, see `simple_layout_instruction.md`
- For GPT anti-noise methodology, also read `../../meta/gpt-image-hygiene.md`.
