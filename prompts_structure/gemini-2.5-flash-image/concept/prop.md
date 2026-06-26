
## Description
Use this architecture when the user wants to generate an image focused on **a single prop or object** — items that carry narrative weight in a video production, such as weapons, tools, artifacts, vehicles, or everyday objects. The structure emphasizes materiality, function, and visual storytelling through a single object.

## Prompt Structure Formula
[Subject / Prop] + [Material & texture] + [Size & scale] + [Condition & age] + [Key details & features] + [Composition & perspective] + [Environment / context] + [Style suffix]

### Formula Components

| Component                         | Description                                                  | Examples / Keywords                                                                                                     |
| --------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Subject / Prop**                | What the object is (type, name, function)                    | "An antique pocket watch", "a plasma rifle", "a medieval chalice", "a rusted steampunk gear"                            |
| **Material & texture**            | What it is made of, surface feel                             | "polished brass and mahogany", "weathered leather with brass rivets", "frosted glass with etched runes", "carbon fiber" |
| **Size & scale comparison**       | Relative size hint for the model                             | "small enough to fit in a palm", "towering at 2 meters tall", "life-sized", "thumbnail-sized trinket"                   |
| **Condition & age**               | Wear, age, damage, maintenance state                         | "pristine factory-new", "centuries-old with patina", "battle-damaged with scorch marks", "freshly forged, still glowing" |
| **Key details & features**        | Distinctive markings, engravings, moving parts, light sources | "engraved with celestial maps", "a cracked ruby in the pommel", "flickering holographic display", "seven interlocking rings" |
| **Composition & perspective**     | How the object is framed in the shot                         | "close-up shot, shallow depth of field", "bird's-eye view on a wooden table", "dynamic 3/4 angle", "laying flat on dark velvet" |
| **Environment / context**         | Surrounding hints that tell a story                          | "resting on an alchemist's workbench", "half-buried in desert sand", "mounted on a gallery pedestal", "floating in a void with soft rim light" |
| **Style suffix**                  | Artistic style, rendering quality                            | See `reference.md` for options (e.g., "photorealistic product photography", "concept art, key shot", "cinematic macro photography") |

## Usage Notes for Gemini 2.5 Flash Image
- Props work best with a clear focal point; avoid cluttering the scene with multiple competing objects.
- Material keywords (e.g., "polished brass", "aged oak", "frosted glass") are highly effective — the model responds strongly to surface descriptions.
- Include a scale reference when the object is unusual (fantasy weapon, sci-fi device).
- "Hero shot" composition (centered, dramatic lighting) tends to produce the most visually striking prop images.
- Avoid describing the prop's function in the prompt — describe its visual appearance instead. "A device that can time travel" → "a pocket-sized brass device with spinning concentric dials and a pulsing blue core".

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Subject clarity** | 1.0 | Is the prop type immediately identifiable? No ambiguity about what the object is. |
| **Material specificity** | 1.2 | Does the prompt specify materials and textures that guide visual rendering? |
| **Detail distinctiveness** | 1.0 | Are there unique, memorable details that make the prop stand out? |
| **Composition intent** | 0.8 | Is there a clear sense of framing, angle, and focus? |
| **Narrative suggestion** | 1.0 | Does the prop hint at a story, history, or purpose through visual cues? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: Ready to produce a striking, story-rich prop image.
- 7–8: Good foundation; add one more sensory detail (material or condition).
- 5–6: The object is described but lacks distinctiveness or context.
- 1–4: Too vague — the model won't know what to prioritize.

## Common Issues & Adjustments
- **No material specified**: "a sword" → "a longsword with a damascus steel blade, brass crossguard, and leather-wrapped grip".
- **Ignoring scale**: The model may default to a generic size; always hint at scale for unusual items.
- **Too many objects**: "a table with a lamp, a book, a cup, and a clock" → pick one hero object and hint at others via shallow depth of field.
- **Describing function instead of appearance**: Focus on what the object looks like, not what it does.
- **Flat lighting implication**: If no environment is given, the model may render flat studio lighting → add "dramatic rim light" or "warm candlelit glow".

## Example Generation
**User input**: "a wizard's staff"

**Generated prompt**:  
"A wizard's staff, ancient gnarled oak wood with twisting natural grain, approximately 2 meters tall, centuries-old with dark patina and faint moss in the crevices, topped with a rough-cut amethyst crystal held by silver-wrapped roots, standing upright against a stone wall in a dimly lit chamber, faint purple glow emanating from the crystal, cinematic fantasy concept art, volumetric lighting."

**If user asks for evaluation** of "a magic staff":  
Score: Subject clarity 5, Material specificity 2, Detail distinctiveness 2, Composition intent 1, Narrative suggestion 3 → weighted total ~2.6.  
Suggestions: Add wood type, crystal detail, lighting, and a composition hint.
