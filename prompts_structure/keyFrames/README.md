# KeyFrames

## What This Is
Records the prompt structure for generating **keyframes** — sequential story beats from a scene composed into a single reference sheet. Used to lock visual consistency across an entire scene before generating individual shots or feeding to video models.

Two distinct architectures:
- **Text-to-Image Grid**: A single 3×3 grid generated from text prompts only (9 frames in one image).
- **Image-to-Image Design Sheet**: A composite sheet generated from uploaded reference images, containing both reference zones (character/location/lighting) and a variable number of 16:9 landscape keyframe frames arranged by user-defined layout.

## Available Files

| File | What It Is |
|------|-------------|
| `core-t2i.md` | Renderer-neutral 3×3 full-color keyframe grid |
| `core-i2i.md` | Renderer-neutral composite reference sheet with variable layout and 16:9 keyframe frames |
| `examples.md` | Full worked example of a complete 9-grid keyframe prompt |

## Usage
- Select `core-t2i.md` or `core-i2i.md`, then load one renderer Adapter. GPT is default; Gemini replaces only the Adapter where the host supports it.
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
- See `examples.md` for the concrete output format
