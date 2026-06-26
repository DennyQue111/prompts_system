---
name: "prompts-structure"
description: "Generate and evaluate image generation prompts using model-specific architecture templates for character, location, and prop concepts. Invoke when user wants to create or score prompts for AI image models like Gemini 2.5 Flash Image."
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
- **Subtype** (e.g., `character`, `location`, `prop`)
- **User description / subject** — free text describing the desired content
- (Optional) **Existing prompt** — when the user wants a score and revision advice

## Output

- One or more complete prompts that match the target architecture
- If evaluating an existing prompt:
  - A numerical score (e.g., 8/10)
  - A list of specific suggestions for improvement

## Workflow

1. Parse the user input to extract model name, content category, subtype, and description.
2. Locate the architecture file at `D:\files\github\prompts_system\prompts_structure\{model-name}\{content-category}\{subtype}.md`.
   Example: `D:\files\github\prompts_system\prompts_structure\gemini-2.5-flash-image\concept\character.md`
3. Read the architecture file to obtain:
   - Prompt structure formula
   - Useful keywords (environment, emotion, materials, etc.)
   - Use-case notes
   - Scoring rubric specific to that architecture
4. Optionally consult `D:\files\github\prompts_system\prompts_structure\{model-name}\reference.md` for style snippets.
5. Fill the user's description into the structure formula and assemble the final prompt.
6. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric and generate suggestions.
7. Return the result to the user.

## Directory Structure

```
D:\files\github\prompts_system\prompts_structure\
├── SKILL.md
└── gemini-2.5-flash-image/
    ├── reference.md          ← Cross-category style reference library
    └── concept/
        ├── character.md      ← Character prompt architecture
        ├── location.md       ← Location/environment prompt architecture
        └── prop.md           ← Prop/object prompt architecture
```

- Each model has its own directory, e.g., `gemini-2.5-flash-image/`
- Inside model directories, content types become subfolders, e.g., `concept/`
- Subfolders contain `.md` architecture files with prompt formulas and scoring rubrics
- `reference.md` holds reusable style templates (artistic medium, rendering quality, aesthetic movements, color palettes, camera/lens)

## Scoring Mechanism

- Score range: 0–10
- Each architecture file defines 5 weighted dimensions scored 0–10
- Final score = weighted average
- Suggestions are drawn from the "Common Issues & Adjustments" section in each architecture file

## Currently Supported Models & Categories

- **gemini-2.5-flash-image**
  - `concept/`: `character`, `location`, `prop`
  - Style reference: `reference.md`

## Example Session

**User input:**
> Model: gemini-2.5-flash-image, concept – character, a detective in a steampunk trench coat

**Skill behavior:**
1. Read `D:\files\github\prompts_system\prompts_structure\gemini-2.5-flash-image\concept\character.md`
2. Obtain the character prompt structure formula
3. Pull "steampunk" style snippet from `reference.md` if needed
4. Fill in the formula and compose the full prompt
5. Return the composed prompt to the user

**If user also says** "score this prompt: a detective":
1. Score against the character rubric: Clarity 5, Detail 3, Consistency 4, Environment 1, Creativity 3
2. Weighted total = ~3.3/10
3. Suggestions: Add clothing details, emotion, environment, and a style suffix.
