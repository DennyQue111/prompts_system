# Sequence (Scene-Level Composition)

## What This Is
Records the prompt structure for generating a **sequence** — a scene-level prompt that describes how multiple shots connect and flow together. Used for video generation models that understand narrative progression across shots.

## Available Files

| File | What It Is |
|------|-------------|
| `gemini.md` | Sequence architecture for Gemini 2.5 Flash (default) |
| `gpt.md` | Sequence architecture for GPT models (with anti-noise adaptations) |
| `examples.md` | Worked examples of sequence prompts |

## Usage
- If the user wants Gemini → use `gemini.md`
- If the user wants GPT → use `gpt.md`
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
- Individual shots within a sequence should reference the frame architecture in `../frame/`
