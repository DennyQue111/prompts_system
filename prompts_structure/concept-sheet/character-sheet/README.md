# Character Sheet (Character Concept Design Layout)

## What This Is
Defines the 16:9 multi-panel grid layout for humanoid character concept images. Specifies exact panel positions and sizes: main visual, viewing angles, expressions (喜怒哀乐 2×2 grid), and an inventory bottom row for all clothing, accessories, scars, and birthmarks.

## Available Model Variants
- `general.md` — compatible with Gemini 2.5 Flash Image and GPT image models (default)
- (Future: Midjourney, DALL-E, etc.)

## Usage
- For content definitions (what goes into each panel), see `concept/character/`
- If the user specifies a model name, load the corresponding layout variant from this directory
- If no model is specified, default to `general.md`
