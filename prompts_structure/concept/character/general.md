## Description
Use this architecture when the user wants to generate an image of **a humanoid character** — a being with a recognizable head, torso, limbs, and face, capable of expressing emotion through facial features and body language. The generated image is always a multi-panel concept design sheet (16:9) that presents the character's full visual range as a video production reference.

**Not for**: non-humanoid sentient entities → use `entity`.

## Core Principle: Show, Don't Tell

AI models don't understand abstract personality words. "He is loyal" produces nothing. "He unconsciously positions his body half a step in front of his teammates" produces an image. **Every personality trait must be translated into a visible physical cue before it enters the prompt.** This is the most important rule in this architecture.

### Personality-to-Visual Translation Table

When the user describes a character's personality, translate it:

| Inner Trait (don't write) | Visual Translation (write this instead) |
|---------------------------|----------------------------------------|
| Loyal / protective | Stands slightly in front of teammates, body angled toward them, arm half-extended as a shield |
| Stubborn / single-minded | Direct unwavering gaze, no unnecessary micro-expressions, moves slowly and deliberately, mouth often slightly open in concentration |
| Slow / dim-witted | Reaction delayed by half a beat, head tilts slightly when processing words, blinks infrequently |
| Brutally strong | Thick neck and shoulders, large rough hands, knuckles with calluses, unconsciously clenches fists |
| Gentle / soft-hearted | Fingers relaxed and half-curled, touches objects with careful fingertips, shoulders slightly rounded inward |
| Battle-hardened | Old scars on knuckles, dirt embedded under fingernails, holds objects with the side of the grip rather than fingertips |
| Loyal but with a soft core | Massive frame curled up in a corner sleeping, giant fingers delicately holding something tiny, full-body scars but using the gentlest strength to hold a child |

## What the Image Must Include

This architecture defines **what content goes into each panel** of the character concept image. The final image is a single 16:9 composite with the following panels:

| Panel Area | Content | Detail Level |
|------------|---------|--------------|
| **Main Visual** | Full-body, default outfit, neutral expression, standing posture | Richest description — every visual signal: face, hair, build, body language as personality manifestation, outfit from outer to inner to shoes, accessories, posture, hand state |
| **View Variations** | 2–3 camera angles of the same default appearance | Each angle: what's newly visible (back view → hair rear, jacket back, shoulder width; side → profile, build thickness, clothing drape) |
| **Expressions / 喜怒哀乐** | 4 shoulder-up or face-only panels: 喜 (joy), 怒 (anger), 哀 (sorrow), 乐 (happiness) | Each: emotion label + key facial changes (brow position, eye shape, mouth, wrinkles/tension) |
| **Wardrobe & Body Marks** | All clothing items, accessories, scars, birthmarks — each in its own panel, one horizontal row | Clothing laid flat or on ghost mannequin. Scars/birthmarks as cropped body close-ups. More items → smaller panels. |

## Prompt Content Formula

For the main visual description, structure the text as:

[Subject: name + age + role] + [Facial features: shape, proportions, expression] + [Hair] + [Build / physique] + [Personality-to-Visual: body language + hand state + signature gesture] + [Outfit: outer → inner → bottom → shoes] + [Accessories & body marks] + [Posture / stance — now enriched with personality cues] + [Style suffix]

### Content Components

| Component | Description | What to Cover |
|-----------|-------------|---------------|
| **Subject** | Who this character is | Name, age, profession/role, pre-death identity if relevant (e.g., "programmer before entering the death game"), one-line archetype |
| **Facial features** | Face shape, proportions, key impression | Face width, jawline, cheekbones, nose, mouth, overall "feel" (honest, sharp, gentle, etc.), any distinguishing marks |
| **Hair** | Hairstyle, color, maintenance level | Length, cut style, color, how it falls, tidiness, any battle-wear changes |
| **Build / physique** | Body type, height, frame | Height, build type, shoulder width, arm/leg thickness, the "silhouette" — **contrast between face and body is a major memorability tool** (e.g., honest office-worker face on a massive frame) |
| **Personality-to-Visual** | ★ NEW — Translate inner character into visible physical cues | See translation table above. Must cover: (1) body language — how they stand/sit/walk, (2) hand state — calluses/scars/grip style/resting position, (3) signature gesture — one recurring micro-action that acts as a visual signature (rubbing a ring-less finger, tilting head when confused), (4) contrast shot idea — one visual contradiction that reveals hidden depth (giant hand holding something tiny, scarred face breaking into a childlike smile) |
| **Outfit** | Clothing from outer to inner to bottom to shoes | Each layer's cut, color, fabric, function. **Write the "prototype" not just the description** — "combat suit adapted from a wedding tuxedo" is ten times more distinctive than "black tactical suit". The viewer should see the original garment underneath the combat adaptation |
| **Accessories & body marks** | Rings, necklaces, scars, birthmarks, tattoos | Visibility rules (e.g., "ring appears as translucent glimmer for split-second only"), scar location and appearance. These are story artifacts — mention their origin in one phrase if it adds visual context |
| **Posture / stance** | How the character stands/holds themselves | Now enriched by Personality-to-Visual — the stance should directly manifest the translated personality cues. Don't write "alert"; write "weight on the balls of his feet, shoulders squared but not tense, head slightly angled as if listening for something" |
| **Style suffix** | Artistic style | From `../../reference.md`: e.g., "cinematic character concept sheet, photorealistic 8K, game production character design reference" |

## Usage Notes
- **Personality-first**: Before writing any physical description, scan the user's character for personality traits and translate them into the 4 dimensions of Personality-to-Visual. These visual cues should then saturate the main visual description — in the hands, the stance, the way the clothes hang on the body.
- The main visual description is the anchor — it occupies ~1/3 width × ~4/5 height and gets the richest paragraph.
- Expression panels must show **clear contrast**: joy (eye crinkle + smile) vs anger (brow down + jaw tight) vs sorrow (inner brows up + unfocused eyes) vs happiness (wide relaxed smile + bright eyes). Avoid "same face, slightly different mouth."
- When the user describes expressions that connect to personality (e.g., "his anger is quiet and cold, not explosive"), reflect that in the expression descriptions — don't default to generic anger.
- Always scan the user's character description for **hidden wearable items and body marks** (rings, scars, birthmarks, tattoos) and include them in the wardrobe row.
- If the character has multiple outfit variants or battle-damage stages, pick the default/earliest state for the main visual and note variants can be separate sheets.
- **The prototype-writing rule**: "combat-adapted [original garment]" always beats "black tactical [garment]". A character who died in a wedding suit and now wears it as combat armor is instantly more memorable than one in generic tactical gear.

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Character identity** | 1.0 | Does the sheet communicate who this character is, their build, face, and overall vibe at a glance? |
| **Detail coverage** | 1.2 | Are facial features, hair, build, outfit, accessories, and body marks all covered? |
| **Personality visualization** | 1.0 | ★ NEW — Are personality traits translated into visible body language, hand state, and signature gestures? Or are they left as abstract adjectives? |
| **View completeness** | 0.8 | Do the viewing angles reveal meaningful silhouette/drape information? |
| **Expression range** | 1.0 | Are 喜怒哀乐 visually distinct? Can the viewer tell each emotion apart? |
| **Wardrobe & marks inventory** | 1.0 | Are all wearable items, scars, and birthmarks accounted for and individually displayed? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: Production-ready. A video model has everything it needs, including the character's soul visible in their body.
- 7–8: Strong core; one zone could use more items, contrast, or personality-to-visual translation.
- 5–6: Zones blur together, personality is still abstract adjectives, or some clothing/marks are missing.
- 1–4: Reads more like a generic portrait than a character reference sheet.

## Common Issues & Adjustments
- **Personality left as adjectives**: "he is loyal and stubborn" → translate EVERY trait: "stands with body unconsciously angled to shield teammates, gaze direct and unflinching, moves with deliberate slowness, no wasted micro-expressions."
- **Missing subject**: Prompt starts with environment or style → add the character as the clear subject.
- **Vague face**: "a warrior" → add face shape, proportions, and the honest/sharp/gentle impression.
- **Clashing build and face**: The user describes a massive body but forgets to mention it → always link build and face in the main visual as contrast if notable. This contrast IS the memorability.
- **Generic outfit**: "black tactical suit" → ask: what did this person wear when they died? What prototype garment was adapted into combat gear? The dead person's last outfit is the best starting point.
- **Expressions too subtle**: Video model references need CLEAR facial changes. Don't be subtle.
- **Wardrobe row missing items**: Scan the full character description for rings, scars, birthmarks, tattoos.
- **No signature gesture**: After describing the character, ask: "what does this character do with their hands when they're thinking/waiting/nervous?" Add one micro-action.

## Image Structure
For the **layout grid, panel positions, and 16:9 composition**, see:
→ **`concept-sheet/character-sheet/general.md`**

That file defines:
- Exact panel positions (main visual top-left 1/3×4/5, view variations upper-right, expressions lower-right 2×2, wardrobe row bottom full-width)
- How to write the full combined prompt with layout instructions + panel content
- Detailed example generation
- Sheet-specific scoring and common issues

The agent workflow is: read this file for **what** content to generate → read the corresponding sheet file for **how** to compose the image → combine both into the final prompt.
