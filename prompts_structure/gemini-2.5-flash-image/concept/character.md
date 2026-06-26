
## Description
Use this architecture when the user wants to generate an image focused on **a single character** with a specific appearance, clothing, emotion, pose, and context. The structure ensures the model receives enough detail to render a coherent figure while leaving enough creative space for the AI's interpretation.

## Prompt Structure Formula
[Subject] + [Appearance details] + [Outfit & accessories] + [Emotion / expression] + [Pose / action] + [Environment / background] + [Style suffix]


### Formula Components

| Component                    | Description                                                       | Examples / Keywords                                                                                                                            |
| ---------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Subject**                  | Who or what the character is (profession, archetype, species)     | "A lone samurai", "an elven archer", "a cyberpunk detective"                                                                                   |
| **Appearance details**       | Physical traits (age, hair, skin, build, distinguishing features) | "middle-aged, scar over left eye, silver-streaked hair, lean build"                                                                            |
| **Outfit & accessories**     | Clothing, armor, accessories, weapons                             | "worn leather coat, brass goggles, utility belt with vials"                                                                                    |
| **Emotion / expression**     | Facial expression, mood                                           | "calm yet determined gaze", "melancholic smirk", "wide-eyed wonder"                                                                            |
| **Pose / action**            | Body posture, movement, activity                                  | "standing with arms crossed", "mid-dash, one hand drawing a blade", "crouched, adjusting a glowing device"                                     |
| **Environment / background** | Surrounding scene, lighting, time of day                          | "rain-slicked neon alley at night", "sunlit forest clearing", "aboard a steampunk airship"                                                     |
| **Style suffix**             | Artistic style, medium, rendering quality                         | See `reference.md` for options (e.g., "photorealistic, cinematic lighting", "anime, Studio Ghibli style", "oil painting, chiaroscuro") |

## Usage Notes for Gemini 2.5 Flash Image
- Gemini responds well to natural language; you can use full sentences or comma-separated phrases.
- The model can handle moderate complexity but may lose small details if the prompt is too long. Keep each component concise.
- Avoid contradictory emotions (e.g., "happy and sad"); choose one dominant mood and a subtle secondary one if desired.
- If a component is unspecified by the user, omit it or use a generic placeholder (e.g., "simple background").

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Clarity** | 1.0 | Is the character clearly defined? No ambiguous terms; subject and appearance are explicit. |
| **Detail richness** | 1.0 | Does the prompt include enough specifics on clothing, facial features, and accessories? |
| **Character consistency** | 1.2 | Do emotion, pose, and outfit align with the character's role/archetype? (e.g., a warrior shouldn't look bored) |
| **Environment relevance** | 0.8 | Does the background support or contrast the character meaningfully? |
| **Creativity / flair** | 0.8 | Does the prompt stand out with unexpected but fitting elements? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: Ready to produce a high-quality character image.
- 7–8: Good, but could benefit from one or two added details.
- 5–6: Core idea is there but several dimensions are weak; revise structure.
- 1–4: Likely missing critical information; rebuild the prompt.

## Common Issues & Adjustments
- **Missing subject**: Prompt starts with an environment or style; add a clear subject at the beginning.
- **Vague appearance**: "a warrior" → add "a weary Middle-Eastern warrior, sunburned skin, shoulder-length black hair, mustache".
- **Clashing emotion and pose**: "angry face, lying lazily on a couch" → adjust emotion to "bored" or pose to "clenching fists".
- **Overcrowded prompt**: Split overly long descriptions into separate prompts or move some details to environment.
- **Dead background**: "white background" → use a mood-setting phrase like "misty graveyard at dawn" unless a clean look is desired.

## Example Generation
**User input**: "a pirate queen"

**Generated prompt**:  
"A fierce pirate queen, mid-30s, long braided auburn hair, sun-kissed skin, gold hoop earrings, tricorn hat, crimson frock coat over a linen blouse, cutlass in one hand, determined smirk, standing on the bow of a galleon, storm clouds gathering on the horizon, oil painting, dramatic lighting."

**If user asks for evaluation** of "a pirate":  
Score: Clarity 3, Detail 2, Consistency 5, Environment 1, Creativity 2 → weighted total ~2.8.  
Suggestions: Add clothing details, emotion, environment, and a style suffix.
