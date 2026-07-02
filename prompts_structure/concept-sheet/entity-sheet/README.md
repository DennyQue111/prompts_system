# Entity Sheet (Entity Concept Design Layout)

## What This Is
Defines the 16:9 multi-panel grid layout for non-humanoid sentient entity concept images. Specifies exact panel positions and sizes: main visual, viewing angles, detail close-ups (AI-flexible grid), and a bottom row for form variations and emotion states.

## Available Model Variants
- `general.md` — compatible with Gemini 2.5 Flash Image and GPT image models (default)
- (Future: Midjourney, DALL-E, etc.)

## Usage
- For content definitions (what goes into each panel), see `concept/entity/`
- If the user specifies a model name, load the corresponding layout variant from this directory
- If no model is specified, default to `general.md`
