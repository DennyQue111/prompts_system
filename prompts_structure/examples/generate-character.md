# Example: Generate a Character Prompt

## User Input

> Model: general (Gemini 2.5 Flash / GPT), concept – character, a detective in a steampunk trench coat

## Skill Behavior

1. Parse input: model=`general`, category=`concept`, subtype=`character`, description=`a detective in a steampunk trench coat`
2. Subtype is `character` — no ambiguity, no need to check `concept-classification.md`
3. Locate and read `concept/character/general.md`
4. Obtain the character prompt structure formula:

   ```
   [Subject] + [Appearance details] + [Outfit & accessories]
   + [Emotion / expression] + [Pose / action]
   + [Environment / background] + [Style suffix]
   ```

5. Optionally pull "steampunk" style snippet from `reference.md` (Section 3: `steampunk, Victorian industrial`)
6. Fill in the formula and compose the full prompt:

   > "A steampunk detective, mid-40s, sharp gray eyes, graying sideburns, lean build, worn brass-framed goggles pushed up on the forehead, heavy brown leather trench coat with brass buttons and gear-shaped cufflinks, utility belt with glass vials of colored liquid, calm but piercing gaze, standing with one hand resting on a brass-tipped cane, rain-slicked cobblestone alley at night, gas lamps casting warm amber pools of light, oil painting, cinematic lighting."

7. Return the composed prompt to the user.

## If User Also Asks for Evaluation

> "score this prompt: a detective"

1. Score against the character rubric:

   | Dimension | Score | Reason |
   |-----------|-------|--------|
   | Clarity | 5 | "a detective" — profession is clear, but nothing else |
   | Detail richness | 3 | No clothing, no appearance, no accessories |
   | Character consistency | 4 | A detective could look many ways; nothing anchors this one |
   | Environment relevance | 1 | No environment specified |
   | Creativity / flair | 3 | "a detective" is the most generic possible start |

2. Weighted total = (5×1.0 + 3×1.0 + 4×1.2 + 1×0.8 + 3×0.8) / 5.0 = ~3.3/10
3. Suggestions: Add clothing details, emotion, environment, and a style suffix.
