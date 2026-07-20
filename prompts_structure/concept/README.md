# Concept — Content Architecture

## What This Is
Defines **what information to put into each panel** of a concept design sheet — character traits, location atmosphere, entity form language, prop details. These files describe the *content* (the "what"), while `concept-sheet/` files describe the *layout grid* (the "where").

## Subdirectories

| Directory | Content Type | Files |
|-----------|-------------|-------|
| `character/` | Human/humanoid characters | text_to_image / image_to_image, gemini + gpt + midjourney |
| `entity/` | Non-humanoid sentient beings | gemini + gpt + midjourney |
| `location/` | Environments and settings | text_to_image / image_to_image, gemini + gpt + midjourney |
| `prop/` | Objects and items | gemini + gpt + midjourney |

## Usage
- Load the concept content file FIRST, then the sheet layout file from `concept-sheet/`
- For GPT variants, also read `../meta/gpt-image-hygiene.md` before writing
