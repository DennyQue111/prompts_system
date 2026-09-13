# Location (Environment / Setting)

## What This Is
Records the concept design prompt structure for **story locations and environments** — an HDR 4-panel 16:9 layout. 4 panels from the same standing position, each rotated 90°, forming a 360° environmental reference for video generation.

## Files

| File | Purpose |
|---|---|
| `core-t2i.md` | Renderer-neutral location concept content from text |
| `core-i2i.md` | Renderer-neutral location extraction and spatial deduction from references |
| `hdr_layout_instruction.md` | HDR four-view layout specification |
| `midjourney.md` | Midjourney-only establishing still workflow |
| `hdr_layout_instruction.md` | All models | HDR 4-panel layout spec (2×2 grid, 28mm, 90° rotation) |
| `general_layout_instruction.md` | Archived | Old 6-panel design sheet layout — superseded by `hdr_layout_instruction.md` |

## Usage
- Select `core-t2i.md` or `core-i2i.md`, then select one global renderer Adapter.
- If no image model is specified → use `../../adapters/gpt-image.md`; explicit Gemini or Jimeng replaces only the Adapter.
- If the user specifically requests Midjourney → use `midjourney.md`
- For HDR 4-panel layout structure, see `hdr_layout_instruction.md` in this directory
- For GPT anti-noise methodology, also read `../../meta/gpt-image-hygiene.md`.
