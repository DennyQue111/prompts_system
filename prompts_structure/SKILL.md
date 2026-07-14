
## Description
This skill assists users in two tasks:
1. **Generate prompts** — For a given concept type (character, entity, location, prop) and optionally a model, automatically construct a high-quality image generation prompt combining content specifications and layout structure.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

**Important**: Before determining which architecture to use, consult `concept-classification.md` to verify the correct subtype — especially for cases where a subject could be miscategorized (e.g., sentient non-humanoid beings should use `entity`, not `character` or `prop`).

## Architecture Philosophy: Type-First, Model-Second

The directory hierarchy is organized by **concept type**, not by model:

- **`concept/{type}/`** — defines **WHAT** content the image must include. Each type directory contains one or more model-specific variant files (e.g., `general.md`).
- **`concept-sheet/{type}-sheet/`** — defines **HOW** the image is composed (layout grid, panel positions, 16:9 structure). Same structure: one or more model-specific variant files.

Each type's `README.md` describes the type and lists available model variants. If the user specifies a model, use that variant; otherwise default to `general.md`.

## Core Principles (applied across all types)

1. **Personality-to-Visual Translation**: AI models don't understand abstract adjectives. Every personality trait must be translated into visible physical cues before entering the prompt. "He is loyal" → "he unconsciously positions his body half a step in front of his teammates."
2. **Prototype Outfit Rule**: Write what the garment was BEFORE it became what it is now. "Combat suit adapted from a wedding tuxedo" is ten times more distinctive than "black tactical suit."
3. **Lens Focal Length**: Include a specific focal length (e.g., `shot on a 50mm lens`) when the target model understands camera terminology. See `reference.md` Section 5 for the full focal length guide.
4. **CG Anime Fallback**: For platforms with strict realism/person filters (即梦, 豆包), use 3D CG anime styles (Section 6 in `reference.md`) to route through different moderation paths.

## Input
- **Concept subtype** (e.g., `character`, `entity`, `location`, `prop`)
- **User description / subject** — free text describing the desired content
- (Optional) **Reference image** — if the user uploads an image (e.g., MJ output) and asks to extract/reproduce content from it, use the corresponding `image_to_image_*` variant
- (Optional) **Model name** — if specified (e.g., `midjourney`), use the corresponding variant file
- (Optional) **Existing prompt** — when the user wants a score and revision advice

## Output
- One complete prompt that matches the target architecture (content formula + sheet layout combined)
- If evaluating an existing prompt:
  - A numerical score (e.g., 8/10)
  - A list of specific suggestions for improvement

## Workflow
1. Parse the user input to extract concept subtype, model (if specified), and description.
2. **Detect i2i vs t2i**: If the user uploaded a reference image and wants to extract/reproduce content from it, route to `image_to_image_{type}.md` instead of the text-to-image variant. Skip to step 4 with the i2i file.
3. **If the subtype is ambiguous**, consult `concept-classification.md` to determine the correct architecture (character vs entity vs prop vs location).
4. Read the type's README at `concept/{type}/README.md` to understand what this type is and to find the available model variants.
5. Read the content architecture at the appropriate variant file identified in step 4 (for t2i: `general.md` or model-specific variant; for i2i: `image_to_image_general.md` or `image_to_image_{model}.md`):
   - Obtain: what panels are needed, content formula, scoring rubric
6. **Follow the "Image Structure" section** at the bottom — it references the corresponding sheet file.
7. Read the sheet file at `concept-sheet/{type}-sheet/general.md` (or appropriate variant):
   - Obtain: layout grid, panel positions, how to write the combined layout + content prompt
8. If the sheet file does not yet exist (e.g., prop-sheet), use the content file's own structure directly.
9. Optionally consult `reference.md` for style snippets.
10. Combine the content formula and sheet layout into the final prompt.
11. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric.
12. Return the result to the user.

## Directory Structure
```
prompts_structure/
├── SKILL.md
├── concept-classification.md    ← Boundary guide: which type to use
├── reference.md                 ← Cross-type style reference library
├── concept/                     ← Content architectures (WHAT to include)
│   ├── character/
│   │   ├── README.md
│   │   ├── text_to_image_general.md    ← Gemini/GPT: multi-panel concept sheet
│   │   ├── text_to_image_midjourney.md ← MJ: single cinematic character still
│   │   └── image_to_image_general.md   ← MJ ref → Gemini: extract + reproduce
│   ├── entity/
│   │   ├── README.md
│   │   ├── general.md
│   │   └── midjourney.md
│   ├── location/
│   │   ├── README.md
│   │   ├── general.md
│   │   └── midjourney.md
│   └── prop/
│       ├── README.md
│       ├── general.md
│       └── midjourney.md
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
├── frame/                       ← Single cinematic frame (frameRef / look reference)
│   ├── README.md
│   ├── general.md               ← Gemini/GPT: one shot, one emotion, one composition
│   └── midjourney.md            ← MJ: one shot, one emotion, one composition (with --params)
├── world_view/                  ← NEW: World-building visual constitution
│   └── midjourney.md            ← MJ: 9-aspect establishing shots (MOKEAIGC)
├── storyboard/                  ← NEW: Multi-frame narrative sequence
│   └── general.md               ← Gemini/GPT: visual script for scenes
├── sequence/                    ← NEW: Timed multi-shot pre-vis
│   └── general.md               ← Gemini/GPT + Seedance: video production blueprint
└── examples/                    ← Detailed session walkthroughs
```

- `concept/` = defines **what** panels and content each concept image needs. Each type has its own directory with one or more model variant files.
- `concept-sheet/` = defines **how** the image is composed — grid positions, panel sizes, 16:9 structure. Same directory-per-type structure.
- `reference.md` = reusable style snippets applicable across all types.
- `concept-classification.md` = decision guide for character vs entity vs prop vs location.
- Each type's `README.md` describes the type, lists available model variants, and specifies the default.

## Scoring Mechanism
- Score range: 0–10
- Dimensions are defined inside each content architecture file (typically 5 weighted dimensions scored 0–10)
- Final score = weighted average
- Suggestions are drawn from the "common issues & adjustments" section

## Currently Supported Types & Model Variants

### Concept Types (content-driven)
- **character** → `text_to_image_general.md` (Gemini/GPT, multi-panel sheet), `text_to_image_midjourney.md` (MJ, single cinematic still), `image_to_image_general.md` (MJ reference → Gemini prompt, extract + reproduce)
- **entity** → `general.md` (Gemini/GPT, multi-panel sheet), `midjourney.md` (MJ, single cinematic still)
- **location** → `general.md` (Gemini/GPT, multi-panel sheet), `midjourney.md` (MJ, single cinematic still)
- **prop** → `general.md` (Gemini/GPT, multi-panel sheet), `midjourney.md` (MJ, single cinematic still)

### New Types (outside concept/)
- **frame** → `general.md` (Gemini/GPT, single cinematic frame — frameRef / look reference), `midjourney.md` (MJ, single cinematic frame with --params)
- **world_view** → `midjourney.md` (MJ, 9-aspect world-building establishing shots based on MOKEAIGC framework)
- **storyboard** → `general.md` (Gemini/GPT, multi-frame narrative sequence — visual script)
- **sequence** → `general.md` (Gemini/GPT + Seedance, timed multi-shot sequence — video pre-vis blueprint)

### Shared
- **reference.md** — Cross-type style library (artistic medium, rendering, aesthetics, color palettes, lens focal lengths, CG anime styles)
- **concept-classification.md** — Decision guide for type boundaries

(Future: DALL-E, Flux, Sora variants can be added as new files within each type directory)

## Example Sessions
See `examples/` folder for detailed walkthroughs:
- `examples/generate-character.md` — Full generation flow for a humanoid character
- `examples/generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `examples/evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
