
---
name: "prompts-structure"
description: "Generate and evaluate image generation prompts using model-specific architecture templates for character, entity, location, and prop concepts. Invoke when user wants to create or score prompts for AI image models like Gemini 2.5 Flash Image."
---

# Prompts Structure

This skill assists users in two tasks:
1. **Generate prompts** — For a given model and concept type (character, entity, location, prop), automatically construct a high-quality image generation prompt combining content specifications and layout structure.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

## Architecture Data Location

All architecture template files are stored at:
`D:\files\github\prompts_system\prompts_structure\`

## Architecture Philosophy: Content + Structure

Each concept type is defined by **two files working together**:

- **`concept/{subtype}.md`** — defines **WHAT** content the image must include (panels, content formula, scoring rubric). This tells you what to describe.
- **`concept-sheet/{subtype}-sheet.md`** — defines **HOW** the image is composed (layout grid, panel positions, 16:9 structure). This tells you how to arrange it.

The two files are always used together — `concept/` files point to their corresponding `concept-sheet/` file in a section called "Image Structure" at the bottom.

## Input

- **Model name** (e.g., `gemini-2.5-flash-image`)
- **Concept subtype** (e.g., `character`, `entity`, `location`, `prop`)
- **User description / subject** — free text describing the desired content
- (Optional) **Existing prompt** — when the user wants a score and revision advice

## Output

- One complete prompt that matches the target architecture (content formula + sheet layout combined)
- If evaluating an existing prompt:
  - A numerical score (e.g., 8/10)
  - A list of specific suggestions for improvement

## Workflow

1. Parse the user input to extract model name, concept subtype, and description.
2. **If the subtype is ambiguous**, consult `D:\files\github\prompts_system\prompts_structure\concept-classification.md` to determine the correct architecture (character vs entity vs prop vs location).
3. Read the content architecture at `D:\files\github\prompts_system\prompts_structure\{model-name}\concept\{subtype}.md`.
   Example: `gemini-2.5-flash-image\concept\character.md`
   Obtain: panel content definitions, content formula, scoring rubric.
4. **Follow the "Image Structure" section** at the bottom of the content file — it references the corresponding sheet file.
5. Read the sheet file at `D:\files\github\prompts_system\prompts_structure\{model-name}\concept-sheet\{subtype}-sheet.md`.
   Example: `gemini-2.5-flash-image\concept-sheet\character-sheet.md`
   Obtain: layout grid, panel positions, how to write the combined layout + content prompt.
6. If the sheet file does not yet exist (e.g., location-sheet.md), the concept file's own formula provides the complete prompt structure — use it directly.
7. Optionally consult `D:\files\github\prompts_system\prompts_structure\{model-name}\reference.md` for style snippets.
8. Combine the content formula and sheet layout into the final prompt.
9. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric.
10. Return the result to the user.

## Directory Structure

```
D:\files\github\prompts_system\prompts_structure\
├── SKILL.md
├── concept-classification.md    ← Boundary guide: when to use which architecture
├── examples/                    ← Detailed session walkthroughs
│   ├── README.md
│   ├── generate-character.md
│   ├── generate-entity.md
│   └── evaluate-prompt.md
└── gemini-2.5-flash-image/
    ├── reference.md              ← Cross-category style reference library
    ├── concept/                  ← Content architectures (WHAT to include)
    │   ├── character.md          ← Humanoid character panels + formula
    │   ├── entity.md             ← Non-humanoid entity panels + formula
    │   ├── location.md           ← Location/environment formula
    │   └── prop.md               ← Prop/object formula
    └── concept-sheet/            ← Layout architectures (HOW to compose)
        ├── entity-sheet.md       ← Entity layout grid (16:9)
        ├── character-sheet.md    ← Character layout grid (16:9)
        └── location-sheet.md     ← Location layout grid (16:9)
```

- Each model has its own directory, e.g., `gemini-2.5-flash-image/`
- `concept/` = defines **what** panels and content each concept image needs. Each file references its sheet counterpart for layout.
- `concept-sheet/` = defines **how** the image is composed — grid positions, panel sizes, 16:9 structure, and full example generation.
- `reference.md` holds reusable style templates.
- `concept-classification.md` defines the boundary between the four subtypes.

## Scoring Mechanism

- Score range: 0–10
- Each concept architecture file defines 5 weighted dimensions scored 0–10
- Final score = weighted average
- Suggestions are drawn from the "Common Issues & Adjustments" section in each architecture file

## Currently Supported Models & Categories

- **gemini-2.5-flash-image**
  - `concept/`: `character`, `entity`, `location`, `prop` — content architectures
  - `concept-sheet/`: `entity-sheet`, `character-sheet`, `location-sheet` — (prop-sheet pending)
  - Style reference: `reference.md`
  - **Classification guide**: `concept-classification.md`

## Example Sessions
See `D:\files\github\prompts_system\prompts_structure\examples\` for detailed walkthroughs:
- `generate-character.md` — Full generation flow for a humanoid character
- `generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
