
## Description
Use this architecture when the user wants to generate an image of **a sentient, non-humanoid entity** — a being that possesses consciousness, agency, or narrative presence but does not conform to the humanoid body plan. This includes AI manifestations, god-projections, alien consciousness, elemental beings, abstract sentient constructs, and any character whose "form" is inseparable from its identity. The structure prioritizes the entity's physical construction, material composition, and the visual signals that communicate its sentience to the viewer.

**Not for**: humanoid characters with clothes and limbs → use `character.md`.  
**Not for**: inert objects without consciousness → use `prop.md`.

## Prompt Structure Formula
[Subject / Entity type] + [Physical form & structure] + [Materials & textures] + [Scale & spatial presence] + [Sentience indicators] + [Behavior / agency] + [Environment / context] + [Style suffix]

### Formula Components

| Component                         | Description                                                       | Examples / Keywords                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Subject / Entity type**         | What kind of conscious being this is (narrative role optional)    | "A sentient black sphere, a game-master entity", "a fractal energy being, guardian of the threshold", "a floating AI eye" |
| **Physical form & structure**     | Geometry, layers, internal vs external, how it's built            | "a perfect sphere built inside-out: magma core encased in obsidian", "a shifting cloud of hexagonal glass shards", "a single giant eye in a void" |
| **Materials & textures**          | What it is made of, surface quality, translucency, reflectivity   | "polished obsidian like frozen black oil", "liquid mercury with rippling surface", "translucent crystalline with inner light" |
| **Scale & spatial presence**      | Size relative to known references, how it occupies space          | "30cm diameter, personal scale", "towering 5 meters tall, dwarfing the viewer", "fills the entire horizon"               |
| **Sentience indicators**          | Visual cues that tell the viewer this thing is aware, alive       | "a single realistic human eye embedded at center, blinking slowly", "pulsing veins of golden light like a heartbeat", "the surface ripples in response to sound" |
| **Behavior / agency**             | What the entity is doing or capable of doing in the frame         | "staring with cold dispassionate intelligence, appraising the viewer", "rotating slowly, scanning the room", "emitting rhythmic pulses of dim warm light" |
| **Environment / context**         | Surrounding space, how it interacts with setting                  | "hanging silently in pitch black void", "floating above an ancient altar in a temple", "emerging from a rift in reality" |
| **Style suffix**                  | Artistic style, rendering quality                                 | See `reference.md` (e.g., "cinematic, hyperrealistic, 8K", "dark fantasy concept art", "surrealist, dreamlike") |

## Usage Notes for Gemini 2.5 Flash Image
- Entities thrive on material contrast — the tension between interior and exterior (magma inside obsidian, light inside shadow) is visually compelling.
- Sentience indicators are the make-or-break component. Without them, the entity reads as a prop. An eye, a glow rhythm, a responsive surface — these are what separate a dead object from a living presence.
- Gemini handles geometric precision well (spheres, crystals, floating structures) — lean into precise form descriptions.
- If the entity has human-like features (an eye, a voice-source, a face-like pattern), describe how they integrate with the non-human form.
- Scale anchors matter enormously for non-human forms. Without a body to reference, the viewer needs you to say whether this thing is palm-sized or building-sized.
- Behavior/agency can be static (staring, hovering) or dynamic (pulsing, rotating, blinking) — pick one clear behavior signal.

## Scoring Rubric (for evaluating user prompts)

Score each dimension 0–10 (0 = missing, 10 = excellent).

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Entity identity** | 1.0 | Is the entity type and narrative role immediately identifiable? |
| **Form distinctiveness** | 1.0 | Is the physical form unique, memorable, and well-structured in description? |
| **Material/texture specificity** | 1.2 | Does the prompt specify materials, surfaces, and optical qualities that guide rendering? |
| **Sentience communication** | 1.2 | Can the viewer perceive consciousness/awareness/aliveness from the visual description? |
| **Narrative presence** | 0.6 | Does the entity suggest a story role — guardian, judge, oracle, observer, gatekeeper? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

### Score interpretation
- 9–10: The entity feels alive, visually striking, and narratively charged.
- 7–8: Strong visual identity but sentience or narrative role could be sharper.
- 5–6: Core concept exists but reads more like a prop than a conscious being.
- 1–4: Ambiguous — viewer won't know they're looking at a sentient entity.

## Common Issues & Adjustments
- **Entity confused with prop**: If the prompt describes only materials and form but gives no signal of consciousness → it's a prop. Add an eye, a glow, a movement, a reactive surface.
- **No scale anchor**: "floating in space" gives the model no size reference → add a measurement or a comparison object.
- **Over-describing function**: "a being that controls the rules of the game" → describe what it looks like and how it behaves visually, not its metaphysical powers.
- **Humanoid leakage**: If the entity starts growing arms, legs, or clothing → consider switching to `character.md` or clarify that it remains non-humanoid.
- **Sentience clichés**: Not everything needs a glowing eye. Consider: pulsating lights, drifting motion, surface undulation, harmonic resonance, shifting patterns, responding to an unseen observer.
- **Environment overpowers entity**: A complex background can swallow a subtle entity → use minimal or void backgrounds when the entity's form is the primary subject.

## Example Generation
**User input**: "a game-master entity like GANTZ's black sphere, but unique"

**Generated prompt**:  
"A sentient black sphere, a rule-enforcing game-master entity, 30cm in diameter — personal scale, intimate and unnerving. Built inside-out: a core of volcanic rock and flowing magma glows with dark red heat, molten lava creeping through cracks. The interior is completely encased in a thick smooth layer of polished obsidian — richly glossy like frozen black oil — thick enough that the internal lava is visible only as blurred silhouettes beneath the surface, like an insect preserved in amber but in black glass. A single large organic realistic human eye occupies roughly one third of the sphere's surface, embedded seamlessly at center — its pupil is deep black, staring with cold dispassionate intelligence as if appraising the viewer. Around the very edge of the black pupil, a thin ring of fine golden-yellow light lines encircles it like a thread of fire — golden at the center, fading to dark red at the edges. In 3 or 4 scattered spots, dim warm light pulses through the obsidian from deep within, like a slow heartbeat. The surface is mirror-glossy, reflecting a suggestion of the environment while the inner glow creates a layered double-image. No tendrils, no wires, no mechanical parts, no limbs. The eye blinks slowly. Hanging silently in pitch black void. Cinematic, hyperrealistic, 8K, Gantz-inspired but unique."

**If user asks for evaluation** of "a magic floating ball with an eye":  
Score: Entity identity 4, Form distinctiveness 2, Material/texture 1, Sentience communication 3, Narrative presence 2 → weighted total ~2.5.  
Suggestions: Specify materials (what is the ball made of?), how the eye integrates, what makes it feel alive beyond just "having an eye", and what its narrative role is.
