
## Description
This skill assists users in two tasks:
1. **Generate prompts** — For a given model and concept type (character, entity, location, prop), automatically construct a high-quality image generation prompt combining content specifications and layout structure.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

**Important**: Before determining which architecture to use, consult `concept-classification.md` to verify the correct subtype — especially for cases where a subject could be miscategorized (e.g., sentient non-humanoid beings should use `entity`, not `character` or `prop`).

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
2. **If the subtype is ambiguous**, consult `concept-classification.md` to determine the correct architecture (character vs entity vs prop vs location).
3. Read the content architecture at `model-name/concept/subtype.md`:
   - Example: `gemini-2.5-flash-image/concept/character.md`
   - Obtain: panel content definitions, content formula, scoring rubric
4. **Follow the "Image Structure" section** at the bottom of the content file — it references the corresponding sheet file.
5. Read the sheet file at `model-name/concept-sheet/subtype-sheet.md`:
   - Example: `gemini-2.5-flash-image/concept-sheet/character-sheet.md`
   - Obtain: layout grid, panel positions, how to write the combined layout + content prompt
6. Optionally consult `reference.md` inside the model folder for style snippets.
7. Combine the content formula and sheet layout into the final prompt.
8. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric.
9. Return the result to the user.

## Directory Structure
This skill file resides in a folder organized by model and category:
- Each model has its own directory, e.g., `gemini-2.5-flash-image/`
- `concept/` contains architecture files defining **what content** goes into each concept image. Each file references its sheet counterpart for layout.
- `concept-sheet/` contains sheet files defining **how the image is composed** — grid layout, panel positions, 16:9 structure, and full example generation.
- `reference.md` holds reusable style templates
- `concept-classification.md` at the root defines the boundary between the four subtypes
- `examples/` folder contains detailed session walkthroughs

Each concept file + sheet file pair is a complete "prompt recipe."

## Scoring Mechanism
- Score range: 0–10
- Dimensions are defined inside each concept architecture file (typically 5 weighted dimensions scored 0–10)
- Final score = weighted average
- Suggestions are drawn from the "common issues & adjustments" section at the end of the file

## Currently Supported Models & Categories
- **gemini-2.5-flash-image**
  - `concept/`: `character`, `entity`, `location`, `prop` — content architectures
  - `concept-sheet/`: `entity-sheet`, `character-sheet` — (location-sheet and prop-sheet pending)
  - Style reference: `reference.md`
  - **Classification guide**: `concept-classification.md`
(Additional models and categories can be added later)

## Example Sessions
See `examples/` folder for detailed walkthroughs:
- `examples/generate-character.md` — Full generation flow for a humanoid character
- `examples/generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `examples/evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
