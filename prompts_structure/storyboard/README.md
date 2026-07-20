# Storyboard

## What This Is
Records the prompt structure for generating **storyboards** — visual scripts showing narrative progression through sequential frames. Storyboards communicate scene flow before video production.

## Available Files

| File | What It Is |
|------|-------------|
| `gemini.md` | Storyboard architecture for Gemini 2.5 Flash Image (default) |
| `gpt.md` | Storyboard architecture for GPT image models (with anti-noise adaptations) |
| `action.md` | Action sequence storyboard structure |
| `dialogue.md` | Dialogue-heavy scene storyboard structure |
| `vfx.md` | VFX-heavy beat storyboard structure |

## Usage
- Pick the sub-type file (`action.md` / `dialogue.md` / `vfx.md`) based on scene content first
- Then load the model variant (`gemini.md` or `gpt.md`) for the output architecture
- For GPT image generation, also read `../meta/gpt-image-hygiene.md` before writing the prompt
