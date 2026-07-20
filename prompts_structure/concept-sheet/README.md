# Concept-Sheet — Layout Grid

## What This Is
Defines the **panel layout grid** for concept design sheets — which panels exist, their positions and proportions on the 16:9 canvas, what goes in each panel. These files describe the *layout* (the "where"), while `concept/` files describe the *content* (the "what").

## Subdirectories

| Directory | Sheet Type | Layout |
|-----------|-----------|--------|
| `character-sheet/` | Character design sheet | Full-body main visual + viewing angles + expressions + wardrobe |
| `entity-sheet/` | Entity design sheet | Main form + alternate views + detail close-ups + form variations + emotional states |
| `location-sheet/` | Location design sheet | Establishing shot + alternate angles + top-down overview + mid-distance + detail + color palette |

## Usage
- Load the concept content file from `concept/` FIRST, then this sheet layout file
- All three subdirectories have `gemini.md` and `gpt.md` variants
- The layout is the same across models — only the style suffix differs
- For GPT variants, also read `../meta/gpt-image-hygiene.md` before writing
