
## Description
This skill generates high-quality image and video generation prompts. For a given concept type (character, entity, location, prop) and optionally a model, it automatically constructs a prompt combining content specifications and layout structure.

**Important**: Before determining which architecture to use, consult `concept-classification.md` to verify the correct subtype — especially for cases where a subject could be miscategorized (e.g., sentient non-humanoid beings should use `entity`, not `character` or `prop`). For video sequences with character performance, consult `performance/` BEFORE writing shot-level descriptions — the acting profile drives what the camera captures.

## Architecture Philosophy: Type-First, Model-Second

The directory hierarchy is organized by **concept type**, not by model:

- **`concept/{type}/`** — defines **WHAT** content the image must include AND **HOW** it is composed. Each type directory contains model-specific variant files plus a `general_layout_instruction.md` that defines the 16:9 panel grid shared across all models.
- **`performance/`** — defines **HOW characters behave**. Before any video sequence or shot is written, characters must have acting profiles (master profile, scene adaptation rules, eye life). This is an upstream layer that feeds into sequence/ and shot/ fields.

**Gemini/GPT Split**: As of July 2026, Gemini and GPT have separate variant files (t2i: `text_to_image_gemini.md` / `text_to_image_gpt.md`, i2i: `image_to_image_gemini.md` / `image_to_image_gpt.md`). For simpler types with t2i only (entity, prop), the files are still `gemini.md` / `gpt.md`. GPT image generation is prone to "dirty" images (uncontrolled micro-texture, muddy shadows, residual noise). GPT variants include anti-noise discipline. See `meta/gpt-image-hygiene.md` for the full methodology.

Each type's `README.md` describes the type and lists available model variants. If the user specifies a model, use that variant; if unspecified, read the type's README.md first to find the correct default file — never assume `gemini.md` exists in every directory.

## Core Principles (applied across all types)

1. **Personality-to-Visual Translation**: AI models don't understand abstract adjectives. Every personality trait must be translated into visible physical cues before entering the prompt. "He is loyal" → "he unconsciously positions his body half a step in front of his teammates."
2. **Prototype Outfit Rule**: Write what the garment was BEFORE it became what it is now. "Combat suit adapted from a wedding tuxedo" is ten times more distinctive than "black tactical suit."
3. **Lens Focal Length**: Include a specific focal length (e.g., `shot on a 50mm lens`) when the target model understands camera terminology. See `reference.md` Section 5 for the full focal length guide.
4. **CG Anime Fallback**: For platforms with strict realism/person filters (即梦 Jimeng, 豆包), use 2D/3D CG anime styles. 即梦 has its own dedicated i2i architecture at `frame/jimeng_image_to_image.md` — use that instead of generic CG anime fallback when the target platform is 即梦. See also Section 6 in `reference.md` for CG anime style snippets.

## Input
- **Concept subtype** (e.g., `character`, `entity`, `location`, `prop`)
- **User description / subject** — free text describing the desired content
- (Optional) **Reference image** — if the user uploads an image (e.g., MJ output) and asks to extract/reproduce content from it, use the corresponding `image_to_image_*` variant
- (Optional) **Model name** — if specified (e.g., `midjourney`, `jimeng`), use the corresponding variant file

## Output
- One complete prompt that matches the target architecture (content formula + sheet layout combined)

## Workflow
1. Parse the user input to extract concept subtype, model (if specified), and description.
2. **Detect i2i vs t2i**: If the user uploaded a reference image and wants to extract/reproduce content from it, route to `image_to_image_{type}.md` instead of the text-to-image variant. Skip to step 4 with the i2i file.
3. **If the subtype is ambiguous**, consult `concept-classification.md` to determine the correct architecture (character vs entity vs prop vs location).
4. Read the type's README at `concept/{type}/README.md` to understand what this type is and to find the available model variants.
5. Read the content architecture at the appropriate variant file identified in step 4:
   - **Gemini t2i** → `text_to_image_gemini.md` (keyFrames, storyboard, frame, character, location) or `gemini.md` (entity, prop — t2i only)
   - **Gemini i2i** → `image_to_image_gemini.md` (frame, character, location, vfx — where i2i variants exist)
   - **GPT t2i** → `text_to_image_gpt.md` (keyFrames, storyboard, frame, character, location) or `gpt.md` (entity, prop — t2i only)
   - **GPT i2i** → `image_to_image_gpt.md` (keyFrames, frame, character, location, vfx)
   - **Midjourney** → `midjourney.md` (entity, prop, location) or `text_to_image_midjourney.md` (character, frame)
   - **Jimeng / 即梦** → `jimeng_image_to_image.md` (frame i2i), `image_to_image_jimeng.md` (character i2i)
   - **Seedance** → `seedance.md` (sequence, shot)
   - If user didn't specify → read the type's README.md to find the default Gemini file
   - This file defines the **content formula** — WHAT the image must include
6. **Follow the "Image Structure" section** at the bottom — it references the corresponding sheet layout.
7. Read the layout file at `concept/{type}/general_layout_instruction.md` (or `simple_layout_instruction.md` for video-reference layouts):
   - **general_layout**: Full production design sheet with expressions, view variations, item inventory
   - **simple_layout** (character only): 3-column video-reference layout — face close-up / front / back
   - For i2i → video workflows, prefer `simple_layout_instruction.md`
   - Style suffix is derived from the project's `style_profile.md`, not hardcoded in layout files
8. If the layout file does not yet exist (e.g., prop), use the content file's own structure directly.
9. Optionally consult `reference.md` for style snippets.
10. **If GPT: read `meta/gpt-image-hygiene.md`** for anti-noise word choice and scene-specific negative terms. Do NOT copy methodology blocks — clean language lives in panel description word choice, not appended text.
11. Combine the content formula and sheet layout into the final prompt.
12. Return the result to the user.

## Directory Structure
```
prompts_structure/
├── SKILL.md
├── concept-classification.md    ← Boundary guide: which type to use
├── reference.md                 ← Cross-type style reference library
├── concept/                     ← Content architectures (WHAT to render)
│   ├── character/
│   │   ├── README.md
│   │   ├── general_layout_instruction.md   ← Layout grid & panel definitions (full production sheet)
│   │   ├── simple_layout_instruction.md    ← Simplified 3-column layout (video reference: face / front / back)
│   │   ├── text_to_image_gemini.md     ← Gemini: multi-panel concept sheet
│   │   ├── text_to_image_gpt.md        ← GPT: multi-panel concept sheet (anti-noise)
│   │   ├── image_to_image_gemini.md    ← MJ ref → Gemini: extract + reproduce
│   │   ├── image_to_image_gpt.md       ← MJ ref → GPT: extract + reproduce (anti-noise)
│   │   ├── image_to_image_jimeng.md    ← 即梦 i2i: ref → character ref sheet (Chinese, simple_layout, video input)
│   │   └── text_to_image_midjourney.md ← MJ: single cinematic character still
│   ├── entity/
│   │   ├── README.md
│   │   ├── general_layout_instruction.md   ← Layout grid & panel definitions
│   │   ├── gemini.md                   ← Gemini: multi-panel concept sheet
│   │   ├── gpt.md                      ← GPT: multi-panel concept sheet (anti-noise)
│   │   └── midjourney.md               ← MJ: single cinematic entity still
│   ├── location/
│   │   ├── README.md
│   │   ├── general_layout_instruction.md   ← Layout grid & panel definitions
│   │   ├── text_to_image_gemini.md     ← Gemini: multi-panel concept sheet
│   │   ├── text_to_image_gpt.md        ← GPT: multi-panel concept sheet (anti-noise)
│   │   ├── image_to_image_gemini.md    ← MJ ref → Gemini: extract + reproduce
│   │   ├── image_to_image_gpt.md       ← MJ ref → GPT: extract + reproduce (anti-noise)
│   │   └── midjourney.md               ← MJ: single atmospheric establishing shot
│   ├── prop/
│   │   ├── README.md
│   │   ├── gemini.md                   ← Gemini: prop still
│   │   ├── gpt.md                      ← GPT: prop still (anti-noise)
│   │   └── midjourney.md               ← MJ: prop still
│   └── vfx/                      ← Visual effects concepts (portals, energy, FX)
│       └── image_to_image_gpt.md       ← GPT i2i: ref → VFX concept (anti-noise)
├── frame/                       ← Single cinematic frame (frameRef / look reference)
│   ├── README.md
│   ├── gemini.md                ← Gemini t2i: one shot, one emotion, one composition
│   ├── gpt.md                   ← GPT t2i: one shot, one emotion, one composition (anti-noise)
│   ├── text_to_image_gemini.md  ← Gemini t2i: extended single frame
│   ├── text_to_image_gpt.md     ← GPT t2i: extended single frame (anti-noise)
│   ├── text_to_image_midjourney.md ← MJ t2i: single cinematic frame with --params
│   ├── image_to_image_gemini.md ← Gemini i2i: ref → single cinematic frame
│   ├── image_to_image_gpt.md    ← GPT i2i: ref → single cinematic frame (anti-noise)
│   ├── image_to_image_midjourney.md ← MJ i2i: ref → single cinematic frame
│   ├── jimeng_image_to_image.md ← 即梦 i2i: ref → single frame (Chinese prompt, similarity slider)
│   ├── midjourney.md            ← MJ: one shot, one emotion, one composition (with --params)
│   └── style_reference.md       ← Frame-level style reference architecture
├── keyFrames/                   ← Multi-image visual consistency lock (3x3 grid)
│   ├── README.md
│   ├── text_to_image_gemini.md  ← Gemini: 9-grid single-image anchor
│   ├── text_to_image_gpt.md     ← GPT t2i: 9-grid single-image anchor (anti-noise)
│   ├── image_to_image_gpt.md    ← GPT i2i: ref → 9-grid (anti-noise)
│   └── examples.md              ← KeyFrames usage examples
├── performance/                 ← Character acting & behavior (upstream of video sequences)
│   ├── README.md
│   ├── acting_master_profile.md ← 150-220 word character acting profile template
│   ├── scene_adaptation.md      ← Scene-level acting adaptation rules + Five Pillars
│   └── eye_life.md              ← Mandatory eye behavior system for human faces
├── world_view/                  ← World-building visual constitution (V11)
│   ├── SKILL.md                 ← V11 orchestrator: 9 aspects + continuity bible + shot matrix
│   ├── midjourney_animation.md  ← MJ animation-style world prompt
│   ├── midjourney_realistic.md  ← MJ realistic-style world prompt
│   ├── references/              ← On-demand references
│   │   ├── world-aspects.md
│   │   ├── continuity-and-shot-planning.md
│   │   ├── camera-and-style-adaptation.md
│   │   ├── platform-renderers.md
│   │   └── output-formats.md
│   ├── style-profiles/          ← Optional: drop-in style presets
│   │   ├── realistic.md         ← Photographic cinematic: Arri 65mm, film stock, skin detail
│   │   └── anime.md             ← Gantz × Demon Slayer fusion: hand-drawn, cel shading, no focal lengths
│   └── _archive/                ← Old V9-based files (kept for reference, not active)
├── shot/                        ← Single-shot video generation (single frame → video)
│   └── seedance.md              ← Seedance single-shot video production blueprint
├── storyboard/                  ← Multi-frame narrative sequence
│   ├── text_to_image_gemini.md  ← Gemini: visual script for scenes
│   ├── text_to_image_gpt.md     ← GPT: visual script for scenes (anti-noise)
│   ├── action.md                ← Action-heavy scene spec (model-agnostic)
│   ├── dialogue.md              ← Dialogue-heavy scene spec (model-agnostic)
│   └── vfx.md                   ← VFX-heavy scene spec (model-agnostic)
├── sequence/                    ← Timed multi-shot pre-vis (video generation)
│   ├── README.md
│   ├── seedance.md              ← Seedance video production blueprint
│   └── examples.md              ← Sequence usage examples
├── meta/                        ← Cross-cutting prompt quality standards
│   ├── prompt-hygiene.md        ← Prompt hygiene checklist and best practices
│   └── gpt-image-hygiene.md     ← GPT anti-noise methodology (July 2026)
└── examples/                    ← Detailed session walkthroughs
    ├── README.md
    ├── generate-character.md
    └── generate-entity.md

## Currently Supported Types & Model Variants

### Concept Types (content-driven)
- **character** → `text_to_image_gemini.md` (Gemini, multi-panel sheet), `text_to_image_gpt.md` (GPT, multi-panel sheet with anti-noise), `image_to_image_gemini.md` (MJ ref → Gemini), `image_to_image_gpt.md` (MJ ref → GPT with anti-noise), `image_to_image_jimeng.md` (即梦 i2i, ref → character ref sheet with simple_layout, Chinese prompt), `text_to_image_midjourney.md` (MJ)
- **location** → `text_to_image_gemini.md` (Gemini, multi-panel sheet), `text_to_image_gpt.md` (GPT, multi-panel sheet with anti-noise), `image_to_image_gemini.md` (MJ ref → Gemini), `image_to_image_gpt.md` (MJ ref → GPT with anti-noise), `midjourney.md` (MJ)
- **entity** → `gemini.md` (Gemini, multi-panel sheet), `gpt.md` (GPT, multi-panel sheet with anti-noise), `midjourney.md` (MJ)
- **prop** → `gemini.md` (Gemini), `gpt.md` (GPT with anti-noise), `midjourney.md` (MJ)
- **vfx** → `image_to_image_gpt.md` (GPT i2i, ref → VFX concept with anti-noise)

### New Types (outside concept/)
- **frame** → `gemini.md` / `text_to_image_gemini.md` (Gemini t2i, single cinematic frame), `gpt.md` / `text_to_image_gpt.md` (GPT t2i, single cinematic frame with anti-noise), `image_to_image_gemini.md` (Gemini i2i, ref → single frame), `image_to_image_gpt.md` (GPT i2i, ref → single frame with anti-noise), `image_to_image_midjourney.md` (MJ i2i, ref → single frame), `jimeng_image_to_image.md` (即梦 i2i, ref → single frame, Chinese prompt), `midjourney.md` (MJ, single cinematic frame with --params), `text_to_image_midjourney.md` (MJ t2i), `style_reference.md` (frame-level style reference architecture)
- **keyFrames** → `text_to_image_gemini.md` (Gemini t2i, 3×3 grid single-image anchor), `text_to_image_gpt.md` (GPT t2i, 3×3 grid with anti-noise), `image_to_image_gpt.md` (GPT i2i, ref → 3×3 grid with anti-noise), `examples.md`
- **performance** → `acting_master_profile.md` (150-220 word character acting profile), `scene_adaptation.md` (scene-level acting adaptation + Five Pillars), `eye_life.md` (mandatory eye behavior for human faces) — upstream layer that feeds into sequence/shot fields
- **world_view** → SKILL.md (V11 orchestrator), `midjourney_animation.md` (MJ animation world prompt), `midjourney_realistic.md` (MJ realistic world prompt), `style-profiles/realistic.md` (photographic cinematic), `style-profiles/anime.md` (Gantz × Demon Slayer fusion)
- **storyboard** → `text_to_image_gemini.md` (Gemini, multi-frame narrative sequence), `text_to_image_gpt.md` (GPT, multi-frame with anti-noise), `action.md` (action-heavy scenes), `dialogue.md` (dialogue-heavy scenes), `vfx.md` (VFX-heavy scenes)
- **shot** → `seedance.md` (Seedance single-shot video production blueprint)
- **sequence** → `seedance.md` (Seedance multi-shot pre-vis with @TAG binding, first-frame rules, spatial landmarks, format modes), `examples.md`

### Shared
- **reference.md** — Cross-type style library (artistic medium, rendering, aesthetics, color palettes, lens focal lengths, CG anime styles)
- **concept-classification.md** — Decision guide for type boundaries
- **meta/prompt-hygiene.md** — Prompt hygiene checklist and best practices (apply before final delivery)
- **meta/gpt-image-hygiene.md** — GPT anti-noise methodology (July 2026, mandatory read before writing any GPT prompt)

(Future: DALL-E, Flux, Sora variants can be added as new files within each type directory. Jimeng/即梦 i2i is already supported via `frame/jimeng_image_to_image.md`.)

## Example Sessions
See `examples/` folder for detailed walkthroughs:
- `examples/generate-character.md` — Full generation flow for a humanoid character
- `examples/generate-entity.md` — Full generation flow for a non-humanoid sentient entity
