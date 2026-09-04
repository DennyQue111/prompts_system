# Concept — Content Architecture

## What This Is
Defines **what information to put into each panel** of a concept design sheet — character traits, location atmosphere, entity form language, prop details. These files describe the *content* (the "what"), while each subtype's named layout file describes the *layout grid* (the "where").

## Subdirectories

| Directory | Content Type | Files |
|-----------|-------------|-------|
| `character/` | Human/humanoid characters | text_to_image / image_to_image, gemini + gpt + midjourney |
| `entity/` | Non-humanoid sentient beings | gemini + gpt + midjourney |
| `location/` | Environments and settings | text_to_image / image_to_image, gemini + gpt + midjourney |
| `prop/` | Objects and items | gemini + gpt + midjourney |

## Usage
- Load the concept content file first, then the layout file named by that subtype/template (`general_layout_instruction.md`, `simple_layout_instruction.md`, or `hdr_layout_instruction.md`)
- For GPT variants, also read `../meta/gpt-image-hygiene.md` before writing
