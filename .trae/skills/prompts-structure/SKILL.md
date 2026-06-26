---
name: "prompts-structure"
description: "Generate and evaluate image generation prompts using model-specific architecture templates for character, entity, location, and prop concepts. Invoke when user wants to create or score prompts for AI image models like Gemini 2.5 Flash Image."
---

# Prompts Structure

This skill assists users in two tasks:
1. **Generate prompts** — Based on a given model name and content type (e.g., character, location, prop), automatically construct a high-quality prompt using a predefined architecture template.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

## Architecture Data Location

All architecture template files are stored at:
`D:\files\github\prompts_system\prompts_structure\`

## Input

- **Model name** (e.g., `gemini-2.5-flash-image`)
- **Content category** (e.g., `concept`)
- **Subtype** (e.g., `character`, `entity`, `location`, `prop`)
- **User description / subject** — free text describing the desired content
- (Optional) **Existing prompt** — when the user wants a score and revision advice

## Output

- One or more complete prompts that match the target architecture
- If evaluating an existing prompt:
  - A numerical score (e.g., 8/10)
  - A list of specific suggestions for improvement

## Workflow

1. Parse the user input to extract model name, content category, subtype, and description.
2. **If the subtype is ambiguous**, consult `D:\files\github\prompts_system\prompts_structure\concept-classification.md` to determine the correct architecture (character vs entity vs prop vs location).
3. Locate the architecture file at `D:\files\github\prompts_system\prompts_structure\{model-name}\{content-category}\{subtype}.md`.
   Example: `D:\files\github\prompts_system\prompts_structure\gemini-2.5-flash-image\concept\character.md`
4. Read the architecture file to obtain:
   - Prompt structure formula
   - Useful keywords (environment, emotion, materials, etc.)
   - Use-case notes
   - Scoring rubric specific to that architecture
5. Optionally consult `D:\files\github\prompts_system\prompts_structure\{model-name}\reference.md` for style snippets.
6. Fill the user's description into the structure formula and assemble the final prompt.
7. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric and generate suggestions.
8. Return the result to the user.

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
    └── concept/
        ├── character.md          ← Humanoid character architecture
        ├── entity.md             ← Non-humanoid sentient entity architecture
        ├── location.md           ← Location/environment architecture
        └── prop.md               ← Prop/object architecture
```

- Each model has its own directory, e.g., `gemini-2.5-flash-image/`
- Inside model directories, content types become subfolders, e.g., `concept/`
- Subfolders contain `.md` architecture files with prompt formulas and scoring rubrics
- `reference.md` holds reusable style templates
- `concept-classification.md` defines the boundary between the four subtypes
- `examples/` contains detailed session walkthroughs; refer here when you need to see the skill in action

## Scoring Mechanism

- Score range: 0–10
- Each architecture file defines 5 weighted dimensions scored 0–10
- Final score = weighted average
- Suggestions are drawn from the "Common Issues & Adjustments" section in each architecture file

## Currently Supported Models & Categories

- **gemini-2.5-flash-image**
  - `concept/`: `character`, `entity`, `location`, `prop`
  - Style reference: `reference.md`
  - **Classification guide**: `concept-classification.md` — read first when subtype is uncertain

## Example Sessions
See `D:\files\github\prompts_system\prompts_structure\examples\` for detailed walkthroughs:
- `generate-character.md` — Full generation flow for a humanoid character
- `generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
