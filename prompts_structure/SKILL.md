
## Description
This skill assists users in two tasks:
1. **Generate prompts** — For a given concept type (character, entity, location, prop) and optionally a model, automatically construct a high-quality image generation prompt combining content specifications and layout structure.
2. **Evaluate prompts** — Score a user-provided prompt on multiple dimensions and deliver concrete, actionable suggestions for improvement.

**Important**: Before determining which architecture to use, consult `concept-classification.md` to verify the correct subtype — especially for cases where a subject could be miscategorized (e.g., sentient non-humanoid beings should use `entity`, not `character` or `prop`).

## Architecture Philosophy: Type-First, Model-Second

The directory hierarchy is organized by **concept type**, not by model:

- **`concept/{type}/`** — defines **WHAT** content the image must include. Each type directory contains one or more model-specific variant files.
- **`concept-sheet/{type}-sheet/`** — defines **HOW** the image is composed (layout grid, panel positions, 16:9 structure). Same structure: one or more model-specific variant files.

**Gemini/GPT Split**: As of July 2026, Gemini and GPT have separate variant files (`gemini.md` / `gpt.md`). GPT image generation is prone to "dirty" images (uncontrolled micro-texture, muddy shadows, residual noise). GPT variants include anti-noise discipline. See `meta/gpt-image-hygiene.md` for the full methodology.

Each type's `README.md` describes the type and lists available model variants. If the user specifies a model, use that variant; otherwise default to `gemini.md`.

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
5. Read the content architecture at the appropriate variant file identified in step 4:
   - Gemini → `gemini.md` (or `text_to_image_gemini.md` / `image_to_image_gemini.md` for character/location)
   - GPT → `gpt.md` (or `text_to_image_gpt.md` / `image_to_image_gpt.md` for character/location)
   - Midjourney → `midjourney.md` (or `text_to_image_midjourney.md` for character)
   - If user didn't specify → default to `gemini.md`
   - This file defines the **content formula** — WHAT the image must include
6. **Follow the "Image Structure" section** at the bottom — it references the corresponding sheet file.
7. Read the sheet file at `concept-sheet/{type}-sheet/` matching the model (`gemini.md` or `gpt.md`):
   - Obtain: layout grid, panel positions, model-specific style suffix
8. If the sheet file does not yet exist (e.g., prop-sheet), use the content file's own structure directly.
9. Optionally consult `reference.md` for style snippets.
10. **If GPT: read `meta/gpt-image-hygiene.md`** for the anti-noise Clean Rendering Block and Negative Prompt Block before writing the prompt.
11. Combine the content formula and sheet layout into the final prompt.
12. If the user supplied an existing prompt, evaluate it against the architecture's scoring rubric.
13. Return the result to the user.

## Directory Structure
```
prompts_structure/
├── SKILL.md
├── concept-classification.md    ← Boundary guide: which type to use
├── reference.md                 ← Cross-type style reference library
├── concept/                     ← Content architectures (WHAT to render)
│   ├── character/
│   │   ├── README.md
│   │   ├── text_to_image_gemini.md     ← Gemini: multi-panel concept sheet
│   │   ├── text_to_image_gpt.md        ← GPT: multi-panel concept sheet (anti-noise)
│   │   ├── image_to_image_gemini.md    ← MJ ref → Gemini: extract + reproduce
│   │   ├── image_to_image_gpt.md       ← MJ ref → GPT: extract + reproduce (anti-noise)
│   │   └── text_to_image_midjourney.md ← MJ: single cinematic character still
│   ├── entity/
│   │   ├── README.md
│   │   ├── gemini.md                   ← Gemini: multi-panel concept sheet
│   │   ├── gpt.md                      ← GPT: multi-panel concept sheet (anti-noise)
│   │   └── midjourney.md               ← MJ: single cinematic entity still
│   ├── location/
│   │   ├── README.md
│   │   ├── text_to_image_gemini.md     ← Gemini: multi-panel concept sheet
│   │   ├── text_to_image_gpt.md        ← GPT: multi-panel concept sheet (anti-noise)
│   │   ├── image_to_image_gemini.md    ← MJ ref → Gemini: extract + reproduce
│   │   ├── image_to_image_gpt.md       ← MJ ref → GPT: extract + reproduce (anti-noise)
│   │   └── midjourney.md               ← MJ: single atmospheric establishing shot
│   └── prop/
│       ├── README.md
│       ├── gemini.md                   ← Gemini: prop still
│       ├── gpt.md                      ← GPT: prop still (anti-noise)
│       └── midjourney.md               ← MJ: prop still
├── concept-sheet/               ← Layout architectures (HOW to compose)
│   ├── character-sheet/
│   │   ├── README.md
│   │   ├── gemini.md                  ← Layout grid + Gemini style suffix
│   │   └── gpt.md                     ← Layout grid + GPT style suffix (anti-noise)
│   ├── entity-sheet/
│   │   ├── README.md
│   │   ├── gemini.md                  ← Layout grid + Gemini style suffix
│   │   └── gpt.md                     ← Layout grid + GPT style suffix (anti-noise)
│   └── location-sheet/
│       ├── README.md
│       ├── gemini.md                  ← Layout grid + Gemini style suffix
│       └── gpt.md                     ← Layout grid + GPT style suffix (anti-noise)
├── frame/                       ← Single cinematic frame (frameRef / look reference)
│   ├── README.md
│   ├── gemini.md                ← Gemini: one shot, one emotion, one composition
│   ├── gpt.md                   ← GPT: one shot, one emotion, one composition (anti-noise)
│   ├── midjourney.md            ← MJ: one shot, one emotion, one composition (with --params)
│   └── style_reference.md       ← Frame-level style reference architecture
├── keyFrames/                   ← Multi-image visual consistency lock (3x3 grid)
│   ├── gemini.md                ← Gemini: 9-grid single-image anchor
│   ├── gpt.md                   ← GPT: 9-grid single-image anchor (anti-noise)
│   └── examples.md              ← KeyFrames usage examples
├── world_view/                  ← World-building visual constitution
│   ├── midjourney_animation.md  ← MJ: 9-aspect establishing shots, animation style
│   └── midjourney_realistic.md  ← MJ: 9-aspect establishing shots, realistic style
├── storyboard/                  ← Multi-frame narrative sequence
│   ├── gemini.md                ← Gemini: visual script for scenes
│   ├── gpt.md                   ← GPT: visual script for scenes (anti-noise)
│   ├── action.md                ← Action-heavy scene spec (model-agnostic)
│   ├── dialogue.md              ← Dialogue-heavy scene spec (model-agnostic)
│   └── vfx.md                   ← VFX-heavy scene spec (model-agnostic)
├── sequence/                    ← Timed multi-shot pre-vis
│   ├── gemini.md                ← Gemini + Seedance: video production blueprint
│   ├── gpt.md                   ← GPT: video production blueprint (anti-noise)
│   └── examples.md              ← Sequence usage examples
├── meta/                        ← Cross-cutting prompt quality standards
│   ├── prompt-hygiene.md        ← Prompt hygiene checklist and best practices
│   └── gpt-image-hygiene.md     ← GPT anti-noise methodology (July 2026)
└── examples/                    ← Detailed session walkthroughs
    ├── README.md
    ├── generate-character.md
    ├── generate-entity.md
    └── evaluate-prompt.md

## Currently Supported Types & Model Variants

### Concept Types (content-driven)
- **character** → `text_to_image_gemini.md` (Gemini, multi-panel sheet), `text_to_image_gpt.md` (GPT, multi-panel sheet with anti-noise), `image_to_image_gemini.md` (MJ ref → Gemini), `image_to_image_gpt.md` (MJ ref → GPT with anti-noise), `text_to_image_midjourney.md` (MJ)
- **location** → `text_to_image_gemini.md` (Gemini, multi-panel sheet), `text_to_image_gpt.md` (GPT, multi-panel sheet with anti-noise), `image_to_image_gemini.md` (MJ ref → Gemini), `image_to_image_gpt.md` (MJ ref → GPT with anti-noise), `midjourney.md` (MJ)
- **entity** → `gemini.md` (Gemini, multi-panel sheet), `gpt.md` (GPT, multi-panel sheet with anti-noise), `midjourney.md` (MJ)
- **prop** → `gemini.md` (Gemini), `gpt.md` (GPT with anti-noise), `midjourney.md` (MJ)

### New Types (outside concept/)
- **frame** → `gemini.md` (Gemini, single cinematic frame — frameRef / look reference), `gpt.md` (GPT, single cinematic frame with anti-noise), `midjourney.md` (MJ, single cinematic frame with --params), `style_reference.md` (frame-level style reference architecture)
- **keyFrames** → `gemini.md` (Gemini, 3×3 grid single-image anchor for visual consistency), `gpt.md` (GPT, 3×3 grid with anti-noise), `examples.md`
- **world_view** → `midjourney_animation.md` (MJ, 9-aspect world-building, animation style), `midjourney_realistic.md` (MJ, 9-aspect world-building, realistic style)
- **storyboard** → `gemini.md` (Gemini, multi-frame narrative sequence), `gpt.md` (GPT, multi-frame with anti-noise), `action.md` (action-heavy scenes, model-agnostic), `dialogue.md` (dialogue-heavy scenes, model-agnostic), `vfx.md` (VFX-heavy scenes, model-agnostic)
- **sequence** → `gemini.md` (Gemini + Seedance, timed multi-shot sequence — video pre-vis blueprint), `gpt.md` (GPT, timed multi-shot with anti-noise), `examples.md`

### Shared
- **reference.md** — Cross-type style library (artistic medium, rendering, aesthetics, color palettes, lens focal lengths, CG anime styles)
- **concept-classification.md** — Decision guide for type boundaries
- **meta/prompt-hygiene.md** — Prompt hygiene checklist and best practices (apply before final delivery)
- **meta/gpt-image-hygiene.md** — GPT anti-noise methodology (July 2026, mandatory read before writing any GPT prompt)

(Future: DALL-E, Flux, Sora variants can be added as new files within each type directory)

## Example Sessions
See `examples/` folder for detailed walkthroughs:
- `examples/generate-character.md` — Full generation flow for a humanoid character
- `examples/generate-entity.md` — Full generation flow for a non-humanoid sentient entity
- `examples/evaluate-prompt.md` — Scoring an existing prompt against an architecture rubric
