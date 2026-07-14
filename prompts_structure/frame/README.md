# Frame (Single Cinematic Frame)

## What This Is
Records the prompt structure for generating a **single cinematic frame** — the atomic unit of visual storytelling. One composition, one moment, one emotional beat. Used as a visual reference (frameRef / look reference) for video generation models: provides color, style, lighting, and atmosphere direction without polluting the video model's own spatial decisions.

A frame is NOT a concept sheet. It's a single image that should feel like a freeze-frame from a finished film.

## Available Model Variants
- `general.md` — compatible with Gemini 2.5 Flash Image and GPT image models (default)
- `midjourney.md` — Midjourney variant with `--` parameter syntax

## Usage
- If the user specifies a model name, load the corresponding variant file from this directory
- If no model is specified, default to `general.md`
- The **Style Palette** section (film stock / format / color palette / camera language) should be defined once per project and applied to every frame for visual continuity
- For style references applicable across all types, see `../reference.md`
