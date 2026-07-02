---
name: "prompts-structure"
description: "Generate and evaluate image generation prompts using model-specific architecture templates for character, entity, location, and prop concepts. Invoke when user wants to create or score prompts for AI image models like Gemini 2.5 Flash Image."
---

# Prompts Structure

This skill assists users in two tasks:
1. **Generate prompts** — For a given concept type (character, entity, location, prop) and optionally a model, automatically construct a high-quality image generation prompt combining content specifications and layout structure.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

## Architecture Data Location

All architecture template files are stored at:
`D:\files\github\prompts_system\prompts_structure\`

## Architecture Philosophy: Type-First, Model-Second

The directory hierarchy is organized by **concept type**, not by model:

- **`concept/{type}/`** — defines **WHAT** content the image must include. Each type directory contains one or more model-specific variant files (e.g., `general.md`).
- **`concept-sheet/{type}-sheet/`** — defines **HOW** the image is composed (layout grid, panel positions, 16:9 structure). Same structure: one or more model-specific variant files.

Each type's `README.md` describes the type and lists available model variants. If the user specifies a model, use that variant; otherwise default to `general.md`.

## Input

- **Concept subtype** (e.g., `character`, `entity`, `location`, `prop`)
- **User description / subject** — free text describing the desired content
- (Optional) **Model name** — if specified (e.g., `midjourney`), use the corresponding variant file
- (Optional) **Existing prompt** — when the user wants a score and revision advice

## Output

- One complete prompt that matches the target architecture (content formula + sheet layout combined)
- If evaluating an existing prompt:
  - A numerical score (e.g., 8/10)
  - A list of specific suggestions for improvement

## Workflow

1. Parse the user input to extract concept subtype, model (if specified), and description.
2. **If the subtype is ambiguous**, consult `D:\files\github\prompts_system\prompts_structure\concept-classification.md`.
3. Read the type's README at `D:\files\github\prompts_system\prompts_structure\concept\{type}\README.md` to find available model variants.
4. Read the content architecture at `D:\files\github\prompts_system\prompts_structure\concept\{type}\general.md` (or appropriate variant).
   Obtain: what panels are needed, content formula, scoring rubric.
5. **Follow the "Image Structure" section** at the bottom — it references the sheet file.
6. Read the sheet file at `D:\files\github\prompts_system\prompts_structure\concept-sheet\{type}-sheet\general.md` (or appropriate variant).
   Obtain: layout grid, panel positions, how to write the combined prompt.
7. If the sheet file does not exist (e.g., prop-sheet), use the content file's own structure directly.
8. Optionally consult `D:\files\github\prompts_system\prompts_structure\reference.md` for style snippets.
9. Combine the content formula and sheet layout into the final prompt.
10. If the user supplied an existing prompt, evaluate it against the scoring rubric.
11. Return the result to the user.

## Directory Structure

```
D:\files\github\prompts_system\prompts_structure\
├── SKILL.md
├── concept-classification.md    ← Boundary guide: which type to use
├── reference.md                 ← Cross-type style reference library
├── concept/                     ← Content architectures (WHAT to include)
│   ├── character/
│   │   ├── README.md            ← Type description + available model variants
│   │   └── general.md            ← Prompt structure
│   ├── entity/
│   │   ├── README.md
│   │   └── general.md
│   ├── location/
│   │   ├── README.md
│   │   └── general.md
│   └── prop/
│       ├── README.md
│       └── general.md
├── concept-sheet/               ← Layout architectures (HOW to compose)
│   ├── character-sheet/
│   │   ├── README.md
│   │   └── general.md
│   ├── entity-sheet/
│   │   ├── README.md
│   │   └── general.md
│   └── location-sheet/
│       ├── README.md
│       └── general.md
└── examples/                    ← Detailed session walkthroughs
```

- `concept/` = defines **what** panels and content each concept image needs.
- `concept-sheet/` = defines **how** the image is composed — grid positions, panel sizes, 16:9 structure.
- `reference.md` = reusable style snippets applicable across all types.
- Each type's `README.md` describes the type, lists available model variants, and specifies the default.

## Scoring Mechanism

- Score range: 0–10
- Each content architecture file defines 5 weighted dimensions scored 0–10
- Final score = weighted average
- Suggestions are drawn from the "Common Issues & Adjustments" section

## Currently Supported Types & Model Variants

- **character** → `general.md` (compatible with Gemini 2.5 Flash Image and GPT)
- **entity** → `general.md` (compatible with Gemini 2.5 Flash Image and GPT)
- **location** → `general.md` (compatible with Gemini 2.5 Flash Image and GPT)
- **prop** → `general.md` (compatible with Gemini 2.5 Flash Image and GPT) — sheet pending
- **Style reference**: `reference.md`
- **Classification guide**: `concept-classification.md`

## Example Sessions
See `D:\files\github\prompts_system\prompts_structure\examples\` for detailed walkthroughs:
- `generate-character.md` — Full generation flow for a humanoid character
- `generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
