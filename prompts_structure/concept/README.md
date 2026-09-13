# Concept — Content Architecture

## What This Is
Defines **what information to put into each panel** of a concept design sheet — character traits, location atmosphere, entity form language, prop details. These files describe the *content* (the "what"), while each subtype's named layout file describes the *layout grid* (the "where").

## Subdirectories

| Directory | Content Type | Files |
|-----------|-------------|-------|
| `character/` | Human/humanoid characters | `core-t2i` / `core-i2i` + one renderer Adapter; MJ remains specialized |
| `entity/` | Non-humanoid sentient beings | `core.md` + one renderer Adapter; MJ remains specialized |
| `location/` | Environments and settings | `core-t2i` / `core-i2i` + one renderer Adapter; MJ remains specialized |
| `prop/` | Objects and items | `core.md` + one renderer Adapter; MJ remains specialized |

## Usage
- Load the subtype Core first, then exactly one renderer Adapter, then its named layout file (`general_layout_instruction.md`, `simple_layout_instruction.md`, or `hdr_layout_instruction.md`).
- GPT is the default Adapter and also requires `../meta/gpt-image-hygiene.md`.
