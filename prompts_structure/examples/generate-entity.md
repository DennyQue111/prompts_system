# Example: Generate an Entity Prompt

## User Input

> Model: general (Gemini 2.5 Flash / GPT), concept – entity, a sentient black sphere with an eye, game-master

## Skill Behavior

1. Parse input: model=`general`, category=`concept`, subtype=`entity`, description=`a sentient black sphere with an eye, game-master`
2. Subtype is `entity` — check `concept-classification.md` to confirm:
   - Not a location (it's a being, not a space)
   - No humanoid body plan (no head, torso, limbs, face)
   - Has consciousness and narrative role (sentient, game-master) → **entity** ✓
3. Locate and read `concept/entity/general.md`
4. Obtain the entity prompt structure formula:

   ```
   [Subject / Entity type] + [Physical form & structure] + [Materials & textures]
   + [Scale & spatial presence] + [Sentience indicators] + [Behavior / agency]
   + [Environment / context] + [Style suffix]
   ```

5. Fill in the formula and compose the full prompt:

   > "A sentient black sphere, a rule-enforcing game-master entity, 30cm in diameter — personal scale, intimate and unnerving. Built inside-out: a core of volcanic rock and flowing magma glows with dark red heat, molten lava creeping through cracks. The interior is completely encased in a thick smooth layer of polished obsidian — richly glossy like frozen black oil — thick enough that the internal lava is visible only as blurred silhouettes beneath the surface, like an insect preserved in amber but in black glass. A single large organic realistic human eye occupies roughly one third of the sphere's surface, embedded seamlessly at center — its pupil is deep black, staring with cold dispassionate intelligence as if appraising the viewer. Around the very edge of the black pupil, a thin ring of fine golden-yellow light lines encircles it like a thread of fire — golden at the center, fading to dark red at the edges. In 3 or 4 scattered spots, dim warm light pulses through the obsidian from deep within, like a slow heartbeat. No tendrils, no wires, no mechanical parts, no limbs. The eye blinks slowly. Hanging silently in pitch black void. Cinematic, hyperrealistic, 8K, Gantz-inspired but unique."

6. Return the composed prompt to the user.

## Why Entity, Not Character or Prop

This example is the exact case that motivated creating the `entity` subtype:

| | character | entity | prop |
|---|----------|--------|------|
| Has consciousness? | ✓ | ✓ | ✗ |
| Humanoid body? | ✓ | ✗ | ✗ |
| Has clothing? | ✓ | ✗ | ✗ |
| Materials define it? | — | ✓ | ✓ |
| Acts / behaves? | ✓ (poses) | ✓ (stares, blinks, pulses) | ✗ |

The sphere is a **character in the narrative** (it sets rules, it watches, it judges), but its visual form breaks every assumption of the `character` architecture. Using `entity` ensures the scoring rubric evaluates what matters — material rendering, sentience communication — rather than penalizing the absence of clothing and poses.
