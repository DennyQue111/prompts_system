# Entity (Non-Humanoid Sentient)

## What This Is
Records the concept design prompt structure for **non-humanoid sentient entities** — machine intelligences, swarm minds, abstract beings, symbolic entities, creatures, and other beings that are not human or humanoid.

## Files

| File | Purpose |
|---|---|
| `core.md` | Renderer-neutral entity concept content |
| `general_layout_instruction.md` | Entity concept sheet layout |
| `midjourney.md` | Midjourney-only cinematic still workflow |

## Usage
- Select `core.md`, then select one global renderer Adapter. GPT is the default; Gemini replaces only the Adapter.
- If the user specifically requests Midjourney → use `midjourney.md`
- For image layout structure, see `general_layout_instruction.md` in this directory
- For GPT anti-noise methodology, see `../../meta/gpt-image-hygiene.md`

## Face-bearing entities

When a non-humanoid entity has a distinct, story-readable face that needs facial performance (eyes, mouth, expression, or dialogue), retain the entity structure for its anatomy, materials, forms, scale, sentience cues, and behavior, but use the character concept sheet's face-first organization. Default to a clean face close-up plus useful full-form/body views of the same entity. For a three-panel video-reference sheet, follow `../character/simple_layout_instruction.md`, adapting the body panels to the entity's anatomy; do not force a headless crop when the face is structurally part of the creature. Keep the close-up as the sole high-detail facial source to avoid conflicting face depictions. If the face is only a minor sensor and does not need performance, use the ordinary entity layout.
