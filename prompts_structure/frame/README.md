# Frame (Single Cinematic Frame)

## What This Is
Records the prompt structure for generating a **single cinematic frame** — the atomic unit of visual storytelling. One composition, one moment, one emotional beat. Used as a visual reference (frameRef / look reference) for video generation models: provides color, style, lighting, and atmosphere direction without polluting the video model's own spatial decisions.

A frame is NOT a concept sheet. It's a single image that should feel like a freeze-frame from a finished film.

## Available Files

| File | What It Is |
|------|-------------|
| `core-t2i.md` | Renderer-neutral single-frame architecture — text-to-image |
| `core-i2i.md` | Renderer-neutral single-frame architecture — image-to-image with reference images |
| `midjourney.md` | Frame architecture for Midjourney (with `--` parameter syntax) |
| `style_reference.md` | Visual DNA palette library — film stock, CG anime, color palette, camera language templates |

The model-specific language, anti-noise, and platform controls live in `../adapters/`; the Core defines the shot itself.

## Usage
- Select `core-t2i.md` or `core-i2i.md` by input mode, then load one renderer Adapter. GPT is default; an explicit Gemini or Jimeng selection replaces only the Adapter.
- **Always consult `style_reference.md`** to select the correct visual palette before generating any frame — the Style Palette is project DNA, defined once and applied to every frame for visual continuity
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
