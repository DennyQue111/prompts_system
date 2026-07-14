# Character (Humanoid Character)

## What This Is
Records the concept design prompt structure for **human / humanoid characters**. Used to generate multi-panel reference sheets containing: full-body main visual, viewing angles, 喜怒哀乐 expressions, and an inventory of all clothing items, accessories, scars, and birthmarks displayed individually.

## Available Model Variants

### Text-to-Image
- `text_to_image_general.md` — compatible with Gemini 2.5 Flash Image and GPT image models (default): multi-panel 16:9 concept sheet
- `text_to_image_midjourney.md` — Midjourney-specific: single cinematic character still

### Image-to-Image (Reference → Concept)
- `image_to_image_general.md` — MJ reference image → Gemini/GPT character prompt: extract character from a Midjourney image, preserve face/hairstyle/body/art style, generate three-view deduction, output Gemini-compatible prompt for reproduction

### Sheet Layout
- For image layout structure, see `concept-sheet/character-sheet/`

## Usage
- **Text-to-image**: If the user describes a character from scratch and wants a concept sheet, load `text_to_image_general.md` (or `text_to_image_midjourney.md` if targeting Midjourney).
- **Image-to-image**: If the user uploads a reference image (e.g., MJ output) and wants to extract a character for reproduction in another model, load `image_to_image_general.md`.
- If no model is specified, default to `text_to_image_general.md`.
