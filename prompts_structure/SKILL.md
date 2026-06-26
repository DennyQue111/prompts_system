
## Description
This skill assists users in two tasks:
1. **Generate prompts** — Based on a given model name and content type (e.g., character, location, prop), automatically construct a high-quality prompt using a predefined architecture template.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

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
2. Locate the architecture file at `model-name/content-category/subtype.md`.  
   Example: `gemini-2.5-flash-image/concept/character.md`
3. Read the architecture file to obtain:
   - Prompt structure formula
   - Useful keywords (environment, emotion, materials, etc.)
   - Use-case notes
   - Scoring rubric specific to that architecture (written at the end of the file)
4. Optionally consult `reference.md` inside the model folder for style snippets that can be appended.
5. Fill the user's description into the structure formula and assemble the final prompt.
6. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric and generate suggestions.
7. Return the result to the user.

## Directory Structure
This skill file resides in a folder organized by model and category:
- Each model has its own directory, e.g., `gemini-2.5-flash-image/`
- Inside model directories, content types become subfolders, e.g., `concept/`
- Subfolders contain `.md` architecture files, e.g., `character.md`, `location.md`, `prop.md`
- An optional cross-category reference file, `reference.md`, holds reusable style templates

Each architecture file is a self-contained "prompt recipe" that includes the structural formula and custom scoring dimensions for that subtype.

## Scoring Mechanism
- Score range: 0–10
- Dimensions are defined inside each architecture file (typically 3–5 dimensions scored individually, then averaged or weighted)
- Suggestions are drawn from the "common issues & adjustments" section found at the end of the architecture file

## Currently Supported Models & Categories
- **gemini-2.5-flash-image**  
  - `concept/`: `character`, `location`, `prop`  
  - Style reference: `reference.md`  
(Additional categories such as `scene` can be added later)

## Example Session
User input:
> Model: gemini-2.5-flash-image, concept – character, a detective in a steampunk trench coat

Skill behavior:
1. Locate `gemini-2.5-flash-image/concept/character.md`
2. Read the character prompt structure
3. Pull "steampunk" style snippet from `reference.md` if needed
4. Compose the full prompt
5. If the user says "score this prompt …", evaluate against the character rubric
