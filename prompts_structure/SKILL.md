
## Description
This skill assists users in two tasks:
1. **Generate prompts** — Based on a given model name and content type (e.g., character, entity, location, prop), automatically construct a high-quality prompt using a predefined architecture template.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

**Important**: Before determining which architecture to use, consult `concept-classification.md` to verify the correct subtype — especially for cases where a subject could be miscategorized (e.g., sentient non-humanoid beings should use `entity`, not `character` or `prop`).

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
2. **If the subtype is ambiguous**, consult `concept-classification.md` to determine the correct architecture (character vs entity vs prop vs location).
3. Locate the architecture file at `model-name/content-category/subtype.md`.  
   Example: `gemini-2.5-flash-image/concept/character.md`
4. Read the architecture file to obtain:
   - Prompt structure formula
   - Useful keywords (environment, emotion, materials, etc.)
   - Use-case notes
   - Scoring rubric specific to that architecture (written at the end of the file)
5. Optionally consult `reference.md` inside the model folder for style snippets that can be appended.
6. Fill the user's description into the structure formula and assemble the final prompt.
7. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric and generate suggestions.
8. Return the result to the user.

## Directory Structure
This skill file resides in a folder organized by model and category:
- Each model has its own directory, e.g., `gemini-2.5-flash-image/`
- Inside model directories, content types become subfolders, e.g., `concept/`
- Subfolders contain `.md` architecture files, e.g., `character.md`, `entity.md`, `location.md`, `prop.md`
- An optional cross-category reference file, `reference.md`, holds reusable style templates
- `concept-classification.md` at the root defines the boundary between the four subtypes and should be consulted before loading any architecture when the subject type is ambiguous
- `examples/` folder contains detailed session walkthroughs for each subtype

Each architecture file is a self-contained "prompt recipe" that includes the structural formula and custom scoring dimensions for that subtype.

## Scoring Mechanism
- Score range: 0–10
- Dimensions are defined inside each architecture file (typically 3–5 dimensions scored individually, then averaged or weighted)
- Suggestions are drawn from the "common issues & adjustments" section found at the end of the architecture file

## Currently Supported Models & Categories
- **gemini-2.5-flash-image**  
  - `concept/`: `character`, `entity`, `location`, `prop`  
  - Style reference: `reference.md`  
  - **Classification guide**: `concept-classification.md` — read first when subtype is uncertain  
(Additional categories such as `scene` can be added later)

## Example Sessions
See `examples/` folder for detailed walkthroughs:
- `examples/generate-character.md` — Full generation flow for a humanoid character
- `examples/generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `examples/evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
