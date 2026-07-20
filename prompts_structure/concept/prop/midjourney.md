## Description
Use this architecture when generating a **single-image prop prompt for Midjourney**. Produces one detailed frame of a narrative object (weapon, tool, artifact, vehicle, everyday item) — optimized for MJ's strength in material rendering, surface detail, and dramatic lighting.

Unlike `general.md` (multi-panel prop sheet), this is a single hero shot of the object, often in context rather than on a neutral background.

## Core Principles

1. **Props carry story.** Every object in a death-game setting has a history — who used it, how it was modified, what it's been through. Show that history in the wear and modification.
2. **Materiality > function.** MJ renders surfaces better than mechanisms. Describe what the prop is made of and how light interacts with it, not how it works.
3. **Context grounds the prop.** A weapon floating in void is generic. A weapon lying in a rain puddle reflecting cold blue light IS the world.
4. **World-view materials must be visible in the prop.** If the world has "mirror surfaces everywhere," the prop should have a mirrored component or the notable absence of one.

## Prompt Content Formula

```
[Prop type + narrative significance] +
[World-view material injection: materials from world DNA] +
[Physical form: shape, size, construction logic] +
[Materials & surfaces: optical properties, wear, texture] +
[Story marks: modifications, damage, previous owner traces] +
[Context & environment: where it sits, what surrounds it] +
[Camera & composition: distance, angle, lighting] +
[MJ style parameters]
```

### Content Components

| Component | Description | Story Integration |
|-----------|-------------|-------------------|
| **Prop type** | What it is + why it matters narratively | "The wedding ring that glimmers for half a second when he teleports" > "a ring" |
| **Material injection** | Materials drawn from world DNA | Props should feel manufactured from the world's substance — cold blue metal, mirrored surfaces, rain-etched |
| **Physical form** | Shape, size, construction | Object size relative to hand/body — a key that fills a palm vs one that's fingernail-sized |
| **Materials & surfaces** | Optical properties, texture, wear | MJ keywords: "rain-slicked," "blood-rusted," "mirror-polished," "scratched matte," "oily iridescent" |
| **Story marks** | Damage, modifications, owner traces | Dried blood in the grip grooves, initials scratched into the barrel, one edge chipped from a specific impact — tell the prop's history in 2–3 marks |
| **Context** | Where the prop is and what light hits it | A blade on wet concrete reflecting cold blue emergency lights. A locket half-buried in mirror shards. Context = world DNA visible on the prop. |
| **Camera & composition** | Distance, angle, lighting | Default: 85mm macro for hero shots, 50mm for in-context. Shallow DOF for focus, deep DOF for texture reading |

## MJ-Specific Parameters

Default: `--ar 16:9 --style raw --s 100 --q 2 --v 6.1`

- Lower stylization (`--s 50–100`) for clean reference prop shots
- `--s 150–200` for atmospheric in-context prop shots
- `--ar 1:1` for square catalog-style prop reference
- `--ar 3:2` for vertical objects (swords, staffs)

## Usage Notes
- **Every prop needs a story mark.** Without at least one scar, modification, or owner trace, the prop is a catalog image, not a narrative object.
- **Material words over function words.** "Blade with rain-etched surface catching cold blue light" beats "a combat knife with serrated edge."
- **The prop inherits the world's lighting.** Don't light the prop independently — it should be in the same cold blue / rain-soaked environment as everything else.
- **Scale through context.** If the prop's size matters, place it near a hand, a puddle, a doorway — something that gives scale.
