# Prop (Object / Item)

## What This Is
Records the concept design prompt structure for **props and objects** — items that carry narrative weight: weapons, tools, artifacts, vehicles, everyday objects with story significance.

## Available Model Variants

| Variant | Target | Use Case |
|---------|--------|----------|
| `gemini.md` | Gemini | Generate prop from text description |
| `gpt.md` | GPT | Generate prop from text (with anti-noise) |
| `midjourney.md` | Midjourney | Single prop still directly in MJ |

## Usage
- If the user wants Gemini → use `gemini.md`
- If the user wants GPT → use `gpt.md`
- If the user specifically requests Midjourney → use `midjourney.md`
- For GPT anti-noise methodology, see `../../meta/gpt-image-hygiene.md`
