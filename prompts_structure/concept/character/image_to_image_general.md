## Description
Use this architecture when the user uploads a Midjourney-generated reference image and wants to **extract a character** from it, then generate a Gemini/GPT-compatible concept-character prompt that reproduces the character — preserving face, hairstyle, body type, and most critically, the original art style.

The core problem this solves: MJ images have a distinct rendering aesthetic that pure text-to-image prompts struggle to reproduce in other models. This structure bridges that gap by systematically deconstructing the visual DNA of the MJ reference and translating it into a prompt language that Gemini/GPT can interpret.

**Input:** MJ reference image + user instruction (e.g., "提取画面中心的人物", "取左边穿夹克的那个人", "要这个人带着她的护手和围巾")

**Output:** A character prompt in `text_to_image_general.md` format, but filled with observed (not imagined) content, plus style preservation keywords.

---

## Workflow (5 Steps)

### Step 1: Source Observation — What the Image Actually Shows

Describe ONLY what is objectively visible. Do not invent, do not embellish.

| Category | What to Observe |
|----------|----------------|
| **Face** | Shape (oval/square/round/heart/angular), face width-to-height ratio, notable features (strong jawline, high cheekbones, wide-set eyes), skin tone, any scars/freckles/birthmarks/tattoos VISIBLE on the face |
| **Eyes** | Shape (almond/round/hooded/monolid), size relative to face, eyelash visibility, eye color, gaze direction, any distinctive eye makeup or markings |
| **Nose** | Bridge height, width, tip shape, nostril visibility at current angle |
| **Mouth** | Lip fullness, width relative to face, cupid's bow definition, current expression |
| **Hair** | Style description (undercut/layered/slicked-back/loose/messy), length, color, texture (straight/wavy/curly/rough/silky), parting direction, how it falls around the face, any hair accessories |
| **Body build** | Shoulder width, neck thickness, torso-to-leg ratio impression, overall mass (lean/athletic/bulky/slender), height impression at current angle |
| **Hands (if visible)** | Hand size relative to body, finger length/taper, visible calluses/scars, nail condition, any rings/jewelry |
| **Clothing** | Layer by layer, outside to inside, top to bottom. For each piece: type, color, material appearance, visible seams/buttons/zippers/fasteners, wear marks, any integrated tech or weapon elements |
| **Accessories** | Jewelry, watches, belts, harnesses, holsters, bags, tech devices — location on body, visual prominence |
| **Body marks** | Tattoos, scars, burns, birthmarks — location, size, color, shape detail |
| **Pose & angle** | Current camera angle (eye-level/low/high), body orientation (front/side/3/4), what body parts are visible vs. hidden |

**Rule:** If an element is obscured by shadow, depth of field blur, or another object, note "not visible / obscured" — do not guess.

---

### Step 2: Style Analysis — Deconstructing the MJ Rendering Aesthetic

This is the most critical section. The MJ image has a specific rendering style that Gemini needs to approximate. Break it down into the following dimensions:

#### 2.1 Line Quality
| Aspect | Options / Examples |
|--------|-------------------|
| Line presence | Prominent visible line art / Subtle thin lines / No visible outlines |
| Line weight consistency | Uniform / Variable (thick on contours, thin on interior) |
| Line character | Clean mechanical / Expressive brush-stroke / Sketch-like / Ink-style |
| Color of lines | Black / Dark brown / Colored to match adjacent area / No lines |

#### 2.2 Shading Method
| Aspect | Options / Examples |
|--------|-------------------|
| Shading type | Flat cel shading (1-2 shadow tones, hard edges) / Soft gradient shading (smooth transitions) / Hard shadow (Gantz-style deep black shadows, sharp edge, high contrast) / Ambient occlusion only / No shading (flat color) |
| Shadow depth | Light shadows (low contrast) / Medium (naturalistic) / Deep black (Gantz-style, 8:1+ ratio) |
| Highlight style | Sharp specular (anime eye catchlight) / Soft bloom / Rim light only / No highlights |
| Self-shadowing | Visible / Absent |

#### 2.3 Color Palette
| Aspect | What to Capture |
|--------|-----------------|
| Overall temperature | Cool-dominant / Warm-dominant / Neutral / Mixed (where?) |
| Saturation level | Highly saturated / Desaturated / Selective saturation (saturated skin + muted environment, etc.) |
| Primary colors | The 2-4 dominant colors in the image |
| Accent colors | Small-area high-impact colors (neon accents, glowing elements) |
| Skin tone | Specific skin color + undertone (warm/yellow/olive/cool/pink/neutral) |

#### 2.4 Material & Texture Rendering
| Material | How It's Rendered |
|----------|-------------------|
| Skin | Smooth matte / Visible pores / Glossy / Subsurface scattering / Anime-flat |
| Fabric | Matte cotton / Glossy synthetic / Rough canvas / Fine weave visible / Latex sheen |
| Metal | Mirror-polished chrome / Brushed matte / Anodized colored / Weathered/rusted |
| Leather | Grain visible / Smooth gloss / Worn creased |
| Hair | Individual strands / Clustered blocks / Silky gradient / Matte texture |
| Glowing elements | Bloom radius / Color bleed on adjacent surfaces / Core brightness |

#### 2.5 Proportions & Stylization Level
| Aspect | What to Capture |
|--------|-----------------|
| Head-to-body ratio | Realistic (~1:7.5) / Anime-heroic (~1:8) / Slightly stylized (~1:6) |
| Facial feature placement | Realistic / Anime-stylized (larger eyes, smaller nose & mouth) / Semi-realistic |
| Overall style category | Photorealistic / Semi-realistic / Anime-inspired realism / Full anime / Comic style |

#### 2.6 Lighting & Atmosphere
| Aspect | What to Capture |
|--------|-----------------|
| Key light direction | Front / Top / Side / Bottom / Rim-lit / Multi-source |
| Key light quality | Hard (sharp shadows) / Soft (diffuse shadows) |
| Fill light | Present (details visible in shadow) / Absent (deep black shadows) |
| Atmosphere | Clear / Haze / Fog / Dust / Rain / Lens flare / Glow bloom |

**Style Preservation Keywords (compile from above analysis):**
After filling 2.1–2.6, distill the analysis into a compact keyword string like:
```
[line quality keyword], [shading keyword], [color keyword], [material keyword], [proportion keyword], [lighting keyword], [overall style category keyword]
```

This string will be prepended to the final Gemini prompt to anchor the style.

---

### Step 3: Character Extraction — Isolate the Target

Define exactly WHO is being extracted from the image:

1. **Target specification**: Which character? (center figure / leftmost / the one in the red jacket / etc.)
2. **Exclusions**: What is NOT the character? (background, other figures, environmental effects, UI overlays)
3. **User additions**: Any extra requirements the user specified — e.g., "keep her tactical gauntlets," "add a clan tattoo on the left arm," "include the scarf wrapped around the neck"
4. **Contradiction resolution**: If the user asks for something that conflicts with the image (e.g., "keep her hair but make it shorter"), note the conflict and prioritize the user's instruction over the observed image.

---

### Step 4: Three-View Deduction — Inferring Hidden Angles

The reference image shows ONE angle. The character concept sheet needs front/side/back. Separate what's observed from what's inferred.

#### Front View
```
Based on: [current camera angle — front/profile/3/4/back]
- Observed elements: [list directly visible body/clothing details]
- Inferred elements (if angle is NOT front): [list what front view would look like based on visible clues]
```

#### Side Profile
```
- Face profile: [infer from visible face shape — nose bridge projection, chin recession, jaw angle]
- Body profile: [infer from visible build — chest depth, back curve, shoulder roundness]
- Clothing side: [infer from visible front details — side zipper placement, seam continuation, layering thickness]
```

#### Back View
```
- Hair back: [infer from front/side visible hair — length, layering, how it falls]
- Clothing back: [infer from front details — back collar shape, any back decals/patches, seam continuation]
- Body back: [infer from visible build — shoulder blade definition, back width, spine line]
```

#### Color & Texture Reference
```
- Skin hex: [#approximate]
- Hair hex: [#approximate]
- Primary clothing hex: [#approximate]
- Accent glow hex: [#approximate] (if any glowing elements)
- Key material descriptions: [short list for consistency across views]
```

**Rule for deduction:** Mark every inferred element as "inferred" — never present an inference as an observation. This lets the user know what's guaranteed (observed) vs. what's estimated (inferred).

---

### Step 5: Gemini Output Prompt

The final prompt, formatted for Gemini/GPT image generation. Follow the panel layout from `concept-sheet/character-sheet/general.md` but fill ALL content from Steps 1-4 observations and inferences.

```
[Style preservation keywords from Step 2.6] +

[Layout instruction: 16:9 character concept design sheet, clean white background...] +

TOP-LEFT — MAIN VISUAL:
[Character subject extracted from Step 1 observation + Step 3 user additions] +
[Face: from Step 1 face observation] +
[Hair: from Step 1 hair observation] +
[Build: from Step 1 body build observation] +
[Personality-to-Visual (if body language/hand state/signature gesture visible in reference)] +
[Outfit: from Step 1 clothing observation, layered outside→in, top→bottom] +
[Accessories & body marks: from Step 1] +
[Posture: from Step 1 pose observation]

UPPER-RIGHT — VIEW VARIATIONS:
[Front view: from Step 4 front view] +
[Back view: from Step 4 back view] +
[Side profile: from Step 4 side profile]

LOWER-RIGHT — EXPRESSIONS (2×2 grid, shoulder-up):
[Joy / Anger / Sorrow / Happiness, based on the character's face structure from Step 1]

BOTTOM ROW:
[All clothing items, accessories, body marks from Step 1 as individual panels]

[Style suffix from concept-sheet/character-sheet/general.md, adapted with Step 2 keywords]
```

---

## Key Rules

1. **Observe, don't invent.** If the character's left hand is hidden behind the body, write "left hand: not visible." Do not guess "probably wearing a matching glove."
2. **Style analysis is mandatory.** A character prompt without style keywords will produce Gemini's default aesthetic, which will NOT match the MJ reference. Always complete Step 2 fully.
3. **Mark inferences.** Every detail in the three-view that is NOT directly visible in the reference must be tagged as "[推断]" or "inferred."
4. **Respect user additions.** If the user says "keep her face but change the outfit to a white lab coat," the face comes from observation and the outfit comes from the user instruction. The user's explicit instruction overrides observed content.
5. **Cross-reference the reference.** If the MJ image has multiple characters, verify the extraction target is unambiguous. If not, ask the user to clarify (e.g., "left figure in red" vs. "center figure with glasses").
6. **No artistic reinterpretation.** The purpose is reproduction, not improvement. If the MJ character has slightly uneven eyes, describe the unevenness — don't "fix" it.

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Style analysis skipped → Gemini output looks generic | Always complete Step 2 — the style keywords are what make the reproduction possible |
| Three-view fully invented not inferred | Check each hidden-angle detail against what the visible angle provides as clues |
| Clothing described as "a black tactical suit" | Break down to specific pieces with material and cut detail observed from the image |
| Character floats — no background/environment context | The concept sheet uses a clean white background as specified in `concept-sheet/character-sheet/general.md` |
| User additions ignored | Step 3.3: always check for user extra requirements before generating the final prompt |

---

## Usage Notes

- **When to use this**: User uploads a reference image (MJ or other) and asks to extract/reproduce a character from it.
- **When to use `text_to_image_general.md` instead**: User describes a character from imagination/script — no reference image provided.
- **Future extension**: `image_to_image_midjourney.md` for MJ→MJ style reference transfer (using `--sref` or image prompt mode).
- **Sheet layout**: Always pair with `concept-sheet/character-sheet/general.md` for the panel grid specification.
- **Image quality**: If the reference image is low resolution or heavily cropped, note visibility limits in Step 1 and prioritize what IS visible.
