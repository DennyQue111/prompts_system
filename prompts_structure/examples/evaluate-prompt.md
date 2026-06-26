# Example: Evaluate an Existing Prompt

## User Input

> Evaluate this prompt against gemini-2.5-flash-image concept character:
> "a pirate"

## Skill Behavior

1. Parse: model=`gemini-2.5-flash-image`, category=`concept`, subtype=`character`, evaluate existing prompt=`a pirate`
2. Locate and read `gemini-2.5-flash-image/concept/character.md`
3. Load the character scoring rubric (5 weighted dimensions)
4. Score each dimension:

   | Dimension | Weight | Score | Reason |
   |-----------|--------|-------|--------|
   | Clarity | 1.0 | 3 | "a pirate" — generic archetype, no specifics |
   | Detail richness | 1.0 | 2 | No clothing, no appearance, no weapon, no ship |
   | Character consistency | 1.2 | 5 | "Pirate" is an archetype — nothing contradicts it, but nothing anchors it |
   | Environment relevance | 0.8 | 1 | No environment at all |
   | Creativity / flair | 0.8 | 2 | One of the most generic prompts possible |

5. Weighted total = (3×1.0 + 2×1.0 + 5×1.2 + 1×0.8 + 2×0.8) / 5.0 = **2.8/10**

6. Interpretation: **1–4 — Likely missing critical information; rebuild the prompt.**

7. Draw suggestions from the "Common Issues & Adjustments" section:
   - **Vague appearance**: Add age, hair, skin, build
   - **Missing subject detail**: Add clothing ("tricorn hat, crimson frock coat"), weapon ("cutlass"), accessories ("gold hoop earrings")
   - **Dead background**: Add environment ("standing on the bow of a galleon, storm clouds on the horizon")
   - **No style suffix**: Add "oil painting, dramatic lighting"

8. Return the score and suggestions to the user.

## Generated Revised Prompt

> "A fierce pirate queen, mid-30s, long braided auburn hair, sun-kissed skin, gold hoop earrings, tricorn hat, crimson frock coat over a linen blouse, cutlass in one hand, determined smirk, standing on the bow of a galleon, storm clouds gathering on the horizon, oil painting, dramatic lighting."

Expected score with revision: Clarity 9, Detail 8, Consistency 9, Environment 8, Creativity 7 → weighted ~8.2/10 (Good→Ready to produce).
