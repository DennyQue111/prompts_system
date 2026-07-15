# KeyFrames

## What This Is
Records the prompt structure for generating **keyframes** — sequential story beats from a scene composed into a single reference sheet. Used to lock visual consistency across an entire scene before generating individual shots or feeding to video models.

Two distinct architectures:
- **Text-to-Image Grid**: A single 3×3 grid generated from text prompts only (9 frames in one image).
- **Image-to-Image Design Sheet**: A composite sheet generated from uploaded reference images, containing both reference zones (character/location/lighting) and a variable number of 16:9 landscape keyframe frames arranged by user-defined layout.

## Available Files

| File | What It Is |
|------|-------------|
| `gemini.md` | KeyFrame architecture for Gemini 2.5 Flash Image (default) — 3×3 grid |
| `text_to_image_gpt.md` | KeyFrame architecture for GPT image models — 3×3 grid with anti-noise |
| `image_to_image_gpt.md` | GPT i2i composite design sheet with variable layout, reference zones, and 16:9 keyframe frames |
| `examples.md` | Full worked example of a complete 9-grid keyframe prompt |

## Usage
- If the user wants Gemini → use `gemini.md`
- If the user wants GPT text-to-image 3×3 grid → use `text_to_image_gpt.md`
- If the user wants GPT image-to-image with reference images and flexible frame count → use `image_to_image_gpt.md`
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
- See `examples.md` for the concrete output format
