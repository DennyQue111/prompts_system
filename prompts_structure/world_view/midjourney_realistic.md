## Description
Use this architecture when generating **world-view establishing shots for Midjourney**. Based on the MOKEAIGC 9-Aspect World-Building framework, this produces one cinematic still per aspect — collectively forming a "visual constitution" that defines the project's look before any character or location is designed.

The world-view is the upstream source of truth. Every character, location, and prop prompt inherits its DNA from these images.

## The 9 Aspects (One Image Per Aspect)

| # | Aspect | What the Image Shows | Narrative Function |
|---|--------|---------------------|-------------------|
| 1 | **World Concept** | The world in one establishing shot — overall atmosphere, light, mood | "This is what the world feels like" |
| 2 | **Inhabitants** | How people exist in this world — group shot, silhouettes, behavior | "This is how people live/move/survive here" |
| 3 | **Animals / Creatures** | Non-human life forms, if any | "This is what shares the world with them" |
| 4 | **Architecture** | Built structures — scale, materials, style | "This is what they build and how they build it" |
| 5 | **Landscape / Terrain** | Natural environment — geography, climate | "This is the ground they walk on" |
| 6 | **Daily Life** | One moment of routine existence | "This is what a normal day looks like" |
| 7 | **Travel / Motion** | How things move through the world | "This is how they get from here to there" |
| 8 | **Sound / Culture** | Visual representation of sound, ritual, culture | "This is what matters to them" (visualized as symbols, gatherings, ritual spaces) |
| 9 | **Power / Authority** | Who or what holds power — visual hierarchy | "This is who controls this world" |

## Aspect 1: World Concept

The master establishing shot. One image that captures the world's core visual identity.

**Prompt Formula:**
```
[World name + one-line concept] +
[Atmosphere: light temperature, weather, color palette] +
[Scale: vastness or claustrophobia] +
[Dominant visual element: the one thing that defines this world] +
[Texture of the world: what surfaces are made of] +
[Camera: wide establishing, 18–28mm, cinematic] +
[MJ parameters]
```

**Example concept:** "零渊挽歌 — a gray arena suspended between life and death, bathed in cold blue light, rain never stops, mirror surfaces everywhere"

## Aspect 2: Inhabitants

Not individual characters, but how people exist as a collective. Group composition that shows behavior, scale relationships, and the human condition in this world.

**Prompt Formula:**
```
[Group of inhabitants in the world] +
[What they're doing: a moment of collective behavior] +
[World atmosphere applied to the figures: light on skin, rain on clothing] +
[Uniform element: what they all share visually] +
[Individual variation: what makes each silhouette distinct] +
[Camera: 35mm wide, eye-level or slightly elevated, cinematic] +
[MJ parameters]
```

## Aspect 3: Animals / Creatures

Non-human life. If the world has no creatures, this aspect can be skipped or replaced with "absence of life" as a visual statement.

**Prompt Formula:**
```
[Creature type + relationship to world] +
[Scale relative to humans] +
[How world atmosphere affects the creature: light, rain, surface interaction] +
[Behavior: what it's doing in this moment] +
[Camera: appropriate to creature scale — 50mm for human-scale, 100mm+ for distant giants] +
[MJ parameters]
```

## Aspect 4: Architecture

What they build, how they build it, what it says about their values.

**Prompt Formula:**
```
[Structure type + purpose] +
[Scale: human-sized, monumental, ruined] +
[Materials: from world DNA — mirror surfaces, rain-etched concrete, cold blue metal] +
[State: pristine, decaying, battle-damaged, overgrown] +
[World atmosphere interacting with the structure: rain on surfaces, light through gaps] +
[Camera: 24mm wide for scale, 35mm for detail, low angle for awe] +
[MJ parameters]
```

## Aspect 5: Landscape / Terrain

The ground they walk on. Natural geography shaped by the world's logic.

**Prompt Formula:**
```
[Terrain type + geography] +
[World atmosphere dominant: weather, light, time of day] +
[Surface texture: what the ground is made of, how it reflects/absorbs world light] +
[Scale: vast or confined] +
[Traces of inhabitants: paths, debris, structures in distance] +
[Camera: 18–24mm ultra-wide to 135mm compressed telephoto, depending on desired scale] +
[MJ parameters]
```

## Aspect 6: Daily Life

One frozen moment of routine existence. This is the most "human" aspect — it grounds the world in lived experience.

**Prompt Formula:**
```
[One specific moment of daily routine] +
[Who: 1–3 figures engaged in an ordinary action] +
[Where: a specific location type from the world] +
[World atmosphere saturating the scene] +
[Lived-in details: worn surfaces, personal items, traces of use] +
[Camera: 35–50mm, eye-level, naturalistic — document the moment, don't stage it] +
[MJ parameters]
```

## Aspect 7: Travel / Motion

How things move through this world. Can be people, vehicles, light, or abstract movement patterns.

**Prompt Formula:**
```
[What is moving + how it moves] +
[Through what environment] +
[World atmosphere in motion: rain trailing, light streaking, surfaces reflecting movement] +
[Motion quality: slow/cinematic, urgent, drifting, mechanical] +
[Camera: motion-appropriate — 24mm for sweeping, 85mm for tracking, long exposure implication] +
[MJ parameters]
```

## Aspect 8: Sound / Culture (Visualized)

Sound can't be rendered, but its visual traces can. This aspect shows rituals, symbols, gatherings, marks — the visual evidence of culture and meaning.

**Prompt Formula:**
```
[Cultural element: ritual, symbol, gathering, mark-making] +
[Where it appears in the world: carved into walls, projected as light, worn on bodies] +
[World atmosphere interaction] +
[The visual language of this culture: geometric, organic, luminous, scarred] +
[Camera: appropriate to the scale of the cultural element — macro for marks, wide for gatherings] +
[MJ parameters]
```

## Aspect 9: Power / Authority

Who or what controls this world. Visual hierarchy made explicit — the system that judges, the arena that watches.

**Prompt Formula:**
```
[Source of power/authority in the world] +
[How power is visualized: a structure, a light source, a looming presence, an eye] +
[Scale relationship: how small humans look against it] +
[World atmosphere centered on the power source: does light come FROM it or fall ON it?] +
[Camera: low angle for submission, high angle for surveillance, 24mm for looming scale] +
[MJ parameters]
```

## MJ Parameters for World-View Shots

Default per aspect:
- Establishing shots (1, 4, 5): `--ar 16:9 --style raw --s 200 --q 2 --v 6.1`
- Human-scale shots (2, 6, 7): `--ar 16:9 --style raw --s 150 --q 2 --v 6.1`
- Detail shots (3, 8, 9): `--ar 16:9 --style raw --s 100 --q 2 --v 6.1`

Higher stylization for atmosphere, lower for clean reference.

## Usage Notes
- **The 9 aspects form a complete visual constitution.** Generate all 9 before designing any individual character, location, or prop. Everything downstream inherits from these.
- **Aspects 1–5 are mandatory.** Aspects 6–9 can be adjusted or skipped depending on the project's needs, but the first 5 establish the fundamental visual DNA.
- **Consistency is the goal.** After generating, compare all 9 images. They should feel like stills from the SAME film. If one aspect drifts in color temperature or material language, regenerate.
- **The world-view document IS your prompt source.** If the project has a written world-view (like `零渊挽歌_世界观_MJ.md`), pull atmosphere keywords, color temperatures, and material descriptions directly from it.
- **CG anime fallback:** If the project targets Chinese platforms, use Section 6 CG anime styles from `reference.md` across all 9 aspects for consistency.
