
## Description
Use this architecture when the user wants to generate an image of **a humanoid character** — a being with a recognizable head, torso, limbs, and face, capable of expressing emotion through facial features and body language. The generated image is always a multi-panel concept design sheet (16:9) that presents the character's full visual range as a video production reference.

**Not for**: non-humanoid sentient entities → use `entity`.

## What the Image Must Include

This architecture defines **what content goes into each panel** of the character concept image. The final image is a single 16:9 composite with the following panels:

| Panel Area | Content | Detail Level |
|------------|---------|--------------|
| **Main Visual** | Full-body, default outfit, neutral expression, standing posture | Richest description — every visual signal: face, hair, build, outfit from outer to inner to shoes, accessories, posture |
| **View Variations** | 2–3 camera angles of the same default appearance | Each angle: what's newly visible (back view → hair rear, jacket back, shoulder width; side → profile, build thickness, clothing drape) |
| **Expressions / 喜怒哀乐** | 4 shoulder-up or face-only panels: 喜 (joy), 怒 (anger), 哀 (sorrow), 乐 (happiness) | Each: emotion label + key facial changes (brow position, eye shape, mouth, wrinkles/tension) |
| **Wardrobe & Body Marks** | All clothing items, accessories, scars, birthmarks — each in its own panel, one horizontal row | Clothing laid flat or on ghost mannequin. Scars/birthmarks as cropped body close-ups. More items → smaller panels. |

## Prompt Content Formula

For the main visual description, structure the text as:

[Subject: name + age + role] + [Facial features: shape, proportions, expression] + [Hair] + [Build / physique] + [Outfit: outer → inner → bottom → shoes] + [Accessories & body marks] + [Posture / stance] + [Style suffix]

### Content Components

| Component | Description | What to Cover |
|-----------|-------------|---------------|
| **Subject** | Who this character is | Name, age, profession/role, one-line archetype (e.g., "28-year-old office worker turned death game survivor") |
| **Facial features** | Face shape, proportions, key impression | Face width, jawline, cheekbones, nose, mouth, overall "feel" (honest, sharp, gentle, etc.), any distinguishing marks |
| **Hair** | Hairstyle, color, maintenance level | Length, cut style, color, how it falls, tidiness, any battle-wear changes |
| **Build / physique** | Body type, height, frame | Height, build type, shoulder width, arm/leg thickness, the "silhouette" — contrast between face and body if notable |
| **Outfit** | Clothing from outer to inner to bottom to shoes | Each layer's cut, color, fabric, function. If the outfit has lore (e.g., "wedding suit adapted for combat"), include that |
| **Accessories & body marks** | Rings, necklaces, scars, birthmarks, tattoos | Visibility rules (e.g., "ring appears as translucent glimmer for split-second only"), scar location and appearance |
| **Posture / stance** | How the character stands/holds themselves | Default pose, what it communicates about personality (alert, guarded, relaxed, burdened) |
| **Style suffix** | Artistic style | From `../../reference.md`: e.g., "cinematic character concept sheet, photorealistic 8K, game production character design reference" |

## Usage Notes
- The main visual description is the anchor — it occupies ~1/3 width × ~4/5 height and gets the richest paragraph.
- Expression panels must show **clear contrast**: joy (eye crinkle + smile) vs anger (brow down + jaw tight) vs sorrow (inner brows up + unfocused eyes) vs happiness (wide relaxed smile + bright eyes). Avoid "same face, slightly different mouth."
- Always scan the user's character description for **hidden wearable items and body marks** (rings, scars, birthmarks, tattoos) and include them in the wardrobe row.
- If the character has multiple outfit variants or battle-damage stages, pick the default/earliest state for the main visual and note variants can be separate sheets.

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Character identity** | 1.0 | Does the sheet communicate who this character is, their build, face, and overall vibe at a glance? |
| **Detail coverage** | 1.2 | Are facial features, hair, build, outfit, accessories, and body marks all covered? |
| **View completeness** | 0.8 | Do the viewing angles reveal meaningful silhouette/drape information? |
| **Expression range** | 1.0 | Are 喜怒哀乐 visually distinct? Can the viewer tell each emotion apart? |
| **Wardrobe & marks inventory** | 1.0 | Are all wearable items, scars, and birthmarks accounted for and individually displayed? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: Production-ready. A video model has everything it needs.
- 7–8: Strong core; one zone could use more items or contrast.
- 5–6: Zones blur together or some clothing/marks are missing.
- 1–4: Reads more like a portrait than a reference sheet.

## Common Issues & Adjustments
- **Missing subject**: Prompt starts with environment or style → add the character as the clear subject.
- **Vague face**: "a warrior" → add face shape, proportions, and the honest/sharp/gentle impression.
- **Clashing build and face**: The user describes a massive body but forgets to mention it → always link build and face in the main visual as contrast if notable.
- **Expressions too subtle**: Video model references need CLEAR facial changes. Don't be subtle.
- **Wardrobe row missing items**: Scan the full character description for rings, scars, birthmarks, tattoos.

## Image Structure
For the **layout grid, panel positions, and 16:9 composition**, see:
→ **`concept-sheet/character-sheet/general.md`**

That file defines:
- Exact panel positions (main visual top-left 1/3×4/5, view variations upper-right, expressions lower-right 2×2, wardrobe row bottom full-width)
- How to write the full combined prompt with layout instructions + panel content
- Detailed example generation
- Sheet-specific scoring and common issues

The agent workflow is: read this file for **what** content to generate → read the corresponding sheet file for **how** to compose the image → combine both into the final prompt.
