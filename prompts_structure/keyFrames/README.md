# KeyFrames (3×3 Grid)

## What This Is
Records the prompt structure for generating **keyframes** — a single 16:9 composite with 9 frames arranged in a 3×3 grid. Each cell is a sequential story beat from a scene. Used to lock visual consistency across an entire scene before generating individual shots.

## Available Files

| File | What It Is |
|------|-------------|
| `gemini.md` | KeyFrame architecture for Gemini 2.5 Flash Image (default) |
| `gpt.md` | KeyFrame architecture for GPT image models (with anti-noise adaptations) |
| `examples.md` | Full worked example of a complete 9-grid keyframe prompt |

## Usage
- If the user wants Gemini → use `gemini.md`
- If the user wants GPT → use `gpt.md`
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
- See `examples.md` for the concrete output format
