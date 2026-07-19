# Frame (Single Cinematic Frame)

## What This Is
Records the prompt structure for generating a **single cinematic frame** — the atomic unit of visual storytelling. One composition, one moment, one emotional beat. Used as a visual reference (frameRef / look reference) for video generation models: provides color, style, lighting, and atmosphere direction without polluting the video model's own spatial decisions.

A frame is NOT a concept sheet. It's a single image that should feel like a freeze-frame from a finished film.

## Available Files

| File | What It Is |
|------|-------------|
| `text_to_image_gemini.md` | Frame architecture for Gemini 2.5 Flash Image — text-to-image (default) |
| `image_to_image_gemini.md` | Frame architecture for Gemini 2.5 Flash Image — image-to-image with reference images |
| `text_to_image_gpt.md` | Frame architecture for GPT image models — text-to-image (with anti-noise adaptations) |
| `image_to_image_gpt.md` | Frame architecture for GPT image models — image-to-image with reference images (with anti-noise adaptations) |
| `midjourney.md` | Frame architecture for Midjourney (with `--` parameter syntax) |
| `style_reference.md` | Visual DNA palette library — film stock, CG anime, color palette, camera language templates |

## Usage
- If the user specifies a model name, load the corresponding variant file from this directory
- If no model is specified, default to `gemini.md`
- **Always consult `style_reference.md`** to select the correct visual palette before generating any frame — the Style Palette is project DNA, defined once and applied to every frame for visual continuity
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
