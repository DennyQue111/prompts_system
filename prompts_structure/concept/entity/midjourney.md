## Description
Use this architecture when generating a **single-image entity design prompt for Midjourney**. For sentient non-humanoid beings (AI manifestations, god-projections, alien consciousness, elemental beings), this produces one cinematic frame that captures the entity's form, material nature, and sentience — optimized for MJ's strength in textures, lighting, and atmosphere.

Unlike `general.md` (multi-panel concept sheet), this is a single image. The challenge: convey consciousness, scale, and material nature in ONE frame.

## Core Principles

1. **Material contrast carries identity.** MJ excels at texture. Layer interior vs exterior material tension (magma inside obsidian, light inside shadow, liquid inside crystal) — the tension IS the design.
2. **Scale needs a reference.** An entity floating in void has no scale. Include something human-scale (a figure, a doorway, a hand reaching) or use lens compression to imply size.
3. **Sentience = behavior, not just glow.** A blinking light is a machine. A surface that ripples toward the viewer is alive. MJ needs behavioral language — verbs, not adjectives — to render sentience.
4. **World-view materials must saturate the entity.** If the world runs on "cold blue light and mirror surfaces," the entity should be made of the world's materials or a deliberate inversion of them.

## Prompt Content Formula

```
[Entity type + narrative role] +
[World-view material injection] +
[Physical form: geometry, layers, structure] +
[Materials & textures: interior vs exterior tension] +
[Scale reference: comparison object or lens compression] +
[Sentience behavior: how it shows it's alive] +
[Environment grounding: where it exists] +
[Camera & composition] +
[MJ style parameters]
```

## World-View to Entity Injection

Entities should be made of the world's visual DNA — or its deliberate opposite:

| World attribute → Entity | Example |
|--------------------------|---------|
| Cold blue light everywhere | Entity is either made of cold blue crystal, OR it's the only warm amber presence |
| Rain never stops | Entity either absorbs rain into its surface, OR water evaporates before touching it |
| Mirror surfaces reflect everything | Entity either is a perfect mirror, OR it's the only matte-black object |
| Death game arena | Entity appears as a floating scoreboard, a judgment throne, a pulsing rules-engine |

## MJ-Specific Parameters

Same base as character: `--ar 16:9 --style raw --s 150 --q 2 --v 6.1`

For scale shots: `--ar 3:2` (more vertical room for vertical entities)
For giant beings: `--ar 16:9` with telephoto lens language (100–135mm compressed)

## Usage Notes
- **Material contrast is MJ's superpower.** Spend most of your descriptive budget on what the entity is MADE of and how those materials interact.
- **Sentience needs verbs.** "It glows" → "Its surface pulses with a slow heartbeat rhythm, brightening every 3 seconds." Write behavior as time-unfolding.
- **Scale reference is mandatory.** Without it, the entity could be fist-sized or city-sized. Use a human figure, architecture, or focal length.
- **Entity personality-to-visual applies** (see `general.md` for translation table): ancient → geological layering; hungry → surfaces ripple toward viewer; broken → internal light flickers irregularly.
