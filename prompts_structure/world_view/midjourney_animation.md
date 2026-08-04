## Description
Use this architecture when generating **world-view establishing shots for Midjourney in anime animation style**. Based on the MOKEAIGC 9-Aspect World-Building framework — one anime-style cinematic keyframe per aspect, collectively forming the animated visual constitution.

The world-view is the upstream source of truth. Every character, location, and prop prompt inherits its DNA from these images.

## ⚠️ STYLE DECOMPOSITION RULE (MANDATORY — READ FIRST)

**NEVER write anime/movie/game titles directly in prompts.** Writing "Gantz-inspired", "Demon Slayer-inspired", "Made in Abyss style", or any works name will pollute the output with that work's character faces, markings, hairstyles, and design language.

**ALWAYS decompose every style into 6 pure technical dimensions:**

| Dimension | What to describe |
|-----------|-----------------|
| **Linework** | Weight, consistency, texture (etching, brush-stroke, clean, rough, thin, thick, varied) |
| **Brush stroke / material** | Background rendering method (watercolor wash, cel-shaded, painterly, digital flat), texture density, mechanical precision level |
| **Shading / lighting** | Hard vs soft shadows, contrast ratio, light source type (ambient, rim, directional, diffused, bioluminescent), color temperature |
| **Color palette** | Dominant colors, accent colors, saturation level, color temperature bias, forbidden colors |
| **Composition** | Depth layering, scale relationship, framing style, camera angles |
| **Character rendering** (if figures present) | Facial proportion style, skin shading method, eye detail level, silhouette language. Include: "no character-specific markings, no known anime character faces" |

**Style profiles live at:** `prompts_system/style-profiles/` — pre-built technical breakdowns. Load the matching profile; if none matches, decompose the user's style from scratch using the 6 dimensions.

**Contamination prevention checklist (verify before every output):**
- [ ] Zero anime/movie/game titles in the prompt body
- [ ] Zero character names or series references
- [ ] Zero "X-inspired" or "X-style" phrases
- [ ] Backbone contains only technical vocabulary (line, shading, color, composition terms)
- [ ] For scenes with visible human faces, append `--no known anime character faces` as a parameter (NOT as description text)

---

## Style Example (REFERENCE ONLY — NOT A DEFAULT)

The backbone and formulas below use **Gantz × Demon Slayer fusion** as an example. **This is NOT a default.** When you generate prompts, you MUST replace every instance of this example style with the user's world-specific style, decomposed into technical vocabulary per the rule above.

**Example decomposition — Gantz × Demon Slayer → Technical:**
- **Gantz DNA**: Hard high-contrast lighting, sharp cel-shaded shadows, realistic anatomy precision, cold blue system aesthetic, tactical gear rendered with hand-drawn detail, dramatic low angles, emotional weight in stillness
- **Demon Slayer DNA**: Expressive fluid linework, painterly atmospheric backgrounds, rich emotional color grading (warm amber nostalgia vs. cold blue isolation), water/energy effects drawn with organic brush-stroke quality, Japanese aesthetic sensibility in composition
- **Fusion result**: Hand-drawn anime keyframes with harsh realism and hard shadows, rendered through expressive linework and emotional color language — not soft, not moe, not generic anime

## The 9 Aspects (One Image Per Aspect)

| # | Aspect | What the Image Shows | Narrative Function |
|---|--------|---------------------|-------------------|
| 1 | **Inhabitants** | How people exist in this world — group shot, silhouettes, behavior | "This is how people live/move/survive here" |
| 2 | **Animals / Creatures** | Non-human life forms, if any | "This is what shares the world with them" |
| 3 | **Architecture** | Built structures — scale, materials, style | "This is what they build and how they build it" |
| 4 | **Landscape / Terrain** | Natural environment — geography, climate | "This is the ground they walk on" |
| 5 | **Daily Life** | One moment of routine existence | "This is what a normal day looks like" |
| 6 | **Travel / Motion** | How things move through the world | "This is how they get from here to there" |
| 7 | **Sound / Culture** | Visual representation of sound, ritual, culture | "This is what matters to them" (visualized as symbols, gatherings, ritual spaces) |
| 8 | **Power / Intensity** | What pressure tests this world — threat, force, collapse | "This is what threatens to break them" |
| 9 | **Portrait** | An intimate emotional moment — the soul of the world | "This is what it feels like to be here" |

## Backbone Preset (⚠️ EXAMPLE — MUST BE REPLACED PER WORLD)

Every prompt starts with an anime-style backbone — NOT `A cinematic photograph, Arri 65mm camera...`.
**The backbone below is the Gantz × Demon Slayer example. Replace with the user's world-specific decomposed style.**

```
Anime cinematic keyframe still, hand-drawn animation rendering, hard cel shading with deep black shadows and high contrast, expressive linework and atmospheric color grading, detailed anime background art
```

**Why this backbone:**
- `Anime cinematic keyframe still` → Replaces `A cinematic photograph` — signals "this is animation, not live-action"
- `hand-drawn animation rendering` → Pushes toward 2D anime aesthetic, away from 3DCG
- `hard cel shading with deep black shadows and high contrast` → Sharp shadow edges, high light/shadow ratio, anatomical precision
- `expressive linework and atmospheric color grading` → Fluid line quality, painterly color palettes, emotional color temperature
- `detailed anime background art` → Ensures environments are rendered as painted backgrounds, not 3D sets

**⚠️ REMINDER**: The specific backbone above is the Gantz × Demon Slayer example. For your world, rebuild this backbone using only technical vocabulary decomposed from the user's chosen style. Load a pre-built profile from `prompts_system/style-profiles/` or decompose from scratch following the 6-dimension rule.

## Composition Language (Replaces Focal Lengths)

Anime doesn't use focal lengths (24mm, 85mm, etc.). Use composition terms instead:

| Live-Action Term | Anime Equivalent | When to Use |
|-----------------|------------------|-------------|
| 18–24mm ultra-wide | extreme wide establishing shot, expansive background painting | Landscapes, architecture scale, environment-dominant scenes |
| 28–35mm wide | wide shot, character in environment | Groups, travel, world-building views |
| 40–50mm standard | medium shot, eye-level | General narrative, daily life, culture scenes |
| 65–85mm portrait | close-up, shallow focus, bokeh background | Portraits, emotional beats, intimate details |
| 100mm+ telephoto | compressed perspective, dramatic long shot | Distant giants, looming threats, compressed scale |

**CRITICAL**: Never write focal lengths (24mm, 50mm, etc.) in anime prompts. Always use composition descriptions. Focal length is a photography concept that signals photorealism to Midjourney.

## Skin & Character Rendering (Replaces Photorealism Skin String)

In anime style, completely REMOVE the photorealism skin string:
```
real human detailed natural looking skin and textures, visible pores, freckles, fine lines...
```

Replace with anime-specific rendering notes, inserted after the character's pose description:
```
hand-drawn anime character rendering with detailed cel shading, Gantz-style realistic facial proportions, expressive eyes with sharp highlights, subtle skin tone gradients, visible line art on facial contours
```

**Use ONLY when human characters appear.** Skip for creature-only or environment-only shots.

## Lighting Language (Anime Adaptation)

Instead of describing light sources as photography (color temperature, Kelvin, practical lights), use anime shading terminology:

| Photography Term | Anime Equivalent |
|-----------------|------------------|
| warm amber light, 3200K | warm amber cel shading, soft gradient from warm to cool |
| cool ambient, 5600K | cold blue ambient shading, cool color wash |
| rim light, backlight | sharp rim light line, backlit cel highlight, hair light edge |
| hard shadows, 8:1 ratio | hard cel shading, deep black阴影, sharp shadow edge, Gantz-style high contrast |
| soft diffused light | soft gradient shading, atmospheric bloom, gentle color transition |
| practical light source | visible on-screen light source, glowing object cast |

**Default lighting for the example world:** Hard cel shading with deep black shadows, cold blue overall color temperature, occasional warm amber emotional accents.

## `--no` Parameter (MJ-Specific)

MJ has NO negative prompt field. Do NOT write negative blocks anywhere in or after the prompt body — MJ either ignores them or misreads them as positive descriptions.

**The ONLY valid negation mechanism is the `--no` parameter**, which must be appended at the end of the parameter chain, AFTER `--v 8.2`.

**When to use:** ONLY for scenes with visible human faces at risk of IP character contamination. Do NOT use for landscape-only, creature-only, object-only, or face-not-visible shots.

```yaml
有人物面部: --ar 16:9 --stylize 250 --v 8.2 --no known anime character faces
无人面部/纯场景: --ar 16:9 --stylize 250 --v 8.2
```

**Quality control is achieved through backbone density**, not exclusion lists. `hand-drawn anime keyframe` + `watercolor-wash` + `fine etching-like linework` already removes photorealism, 3DCG, and flat moe. The `--no` only catches the one thing backbone can't: IP character face invasion.

> Reference: `prompts_structure/meta/midjourney-image-hygiene.md` — full rationale and checklist.

## MJ Parameters

```yaml
通用: --ar 16:9 --stylize 250 --v 8.2
有人物面部: --ar 16:9 --stylize 250 --v 8.2 --no known anime character faces
```

**Note on Niji**: `--niji 6` produces purer anime/illustration output. For the example style (hard lighting + expressive linework hybrid), `--v 8.2` is recommended. If results are too photographic for your chosen style, switch to `--niji 6`.

**`--no` rule**: Only append `--no known anime character faces` when the scene contains clearly visible human faces. Landscape-only, creature-only, object-only, macro, and no-face-visible shots skip `--no` entirely. Quality control is handled by backbone density, not negation lists.

## Prompt Formulas Per Aspect

### Aspect 1: Inhabitants

```
[Anime backbone] +
[Group of inhabitants in the world, each with distinct cyberpunk tactical gear — NOT uniform black suits] +
[What they're doing: collective behavior in a specific location] +
[World atmosphere applied to figures: hard cel shading, cold blue rim light, deep shadows] +
[Individual variation: distinct silhouettes, different gear configurations] +
[Composition: medium wide shot, eye-level, figures spread across depth] +
[Anime character rendering: hand-drawn, cel shaded, Gantz-style anatomy, expressive faces] +
[MJ parameters]
```

### Aspect 2: Animals / Creatures

```
[Anime backbone] +
[Creature type + relationship to world] +
[Scale relative to humans] +
[How world atmosphere affects the creature: hard light on surface, internal glow] +
[Behavior: what it's doing in this moment] +
[Composition: close-up or wide as appropriate to creature scale] +
[Anime-specific creature rendering: hand-drawn, brush-stroke texture for organic forms, cel shading for hard surfaces] +
[MJ parameters]
```

### Aspect 3: Architecture

```
[Anime backbone] +
[Structure type + purpose + state] +
[Materials from world DNA: white seamless surfaces, cold blue edge lighting, mirror-polished chrome elements, pixelated digital corruption at edges] +
[World atmosphere interacting with structure: hard shadows, blue holographic glow, glitch artifacts] +
[Traces of use: worn surfaces, personal items, footprints] +
[Composition: wide establishing, low angle for scale, deep focus] +
[Anime-style painted background, architectural linework with atmospheric perspective] +
[MJ parameters]
```

### Aspect 4: Landscape / Terrain

```
[Anime backbone] +
[Terrain type + geography + weather] +
[World atmosphere dominant: stormy sky, dying sunset, rain, cold blue tint] +
[Surface texture: cracked concrete, reflective wet ground, dissolving into wireframe at edges] +
[Scale: vast, with tiny figure silhouettes for reference] +
[Composition: extreme wide establishing shot, layered depth, painterly background art] +
[Anime-style environmental painting with atmospheric haze and color grading] +
[MJ parameters]
```

### Aspect 5: Daily Life

```
[Anime backbone] +
[One specific moment of routine: weapon maintenance, gear repair, rest between missions] +
[1–3 figures engaged in ordinary action] +
[Specific location from the world] +
[World atmosphere saturating the scene: warm practical light mixed with cold ambient] +
[Lived-in details: scuffed gear, repair tape, personal items, fatigue visible] +
[Composition: medium close-up, intimate scale, naturalistic framing] +
[Anime character rendering + hand-drawn detail on worn surfaces] +
[MJ parameters]
```

### Aspect 6: Travel / Motion

```
[Anime backbone] +
[What is moving + how it moves — portal transition, traversal, pursuit] +
[Through what environment: cube chamber → cyberpunk ruins] +
[World atmosphere in motion: light streaking, particle trails, glitch distortion] +
[Motion quality: dynamic speed lines, motion blur brush strokes, anime action smears] +
[Composition: dynamic diagonal framing, motion-appropriate angle] +
[Anime-specific motion effects: hand-drawn speed lines, impact frames, energy trails] +
[MJ parameters]
```

### Aspect 7: Sound / Culture

```
[Anime backbone] +
[Cultural element: Zero's holographic data wall — the monument of the dead] +
[Where it appears: pure black void, data cascading in blue light] +
[World atmosphere interaction: cold blue glow only light source, deep black shadows] +
[Visual language: glitching holographic text, fragmented memory stills, crossed-out player IDs] +
[Composition: wide shot from behind small figure, scale contrast dwarfing the human] +
[Anime-style holographic rendering: hand-drawn glow effects, painterly light bloom, cel-shaded data streams] +
[MJ parameters]
```

### Aspect 8: Power / Intensity

```
[Anime backbone] +
[Source of threat: four-meter raging water elemental in abandoned amusement park] +
[How power is visualized: towering churning body, digital particles inside, water arm mid-swing] +
[Scale relationship: tiny human in tactical gear evading, deployed energy shield flickering] +
[World atmosphere: storm lighting, water spray, debris explosion, motion blur] +
[Composition: dramatic low angle from ground, giant filling upper frame] +
[Anime action rendering: hand-drawn water effects, impact frames, dynamic debris brush strokes, speed lines] +
[MJ parameters]
```

### Aspect 9: Portrait

```
[Anime backbone] +
[Intimate emotional moment: a woman's hand touching a kneeling man's head — a mother's gesture without memory] +
[Character details: tactical bodysuit with subtle circuit traces, medical diagnostic bracer, smart-ring] +
[World atmosphere: soft diffused light like through deep water, warm amber mixing with cold blue] +
[Emotional core: erased memory but surviving love — the ghost of feeling that outlived deletion] +
[Composition: intimate close-up, slightly high angle, shallow focus] +
[Anime emotional rendering: detailed facial expressions with subtle tear rendering, hand-drawn emotional lighting, realistic eye detail, warm/cold color contrast on the face] +
[MJ parameters]
```

## Zero (零) — Visual Specification (Per Script)

**Seven MUST be described as a cube cluster, never a sphere.**

From the script, Seven is:
- A cluster life-form composed of thousands of mirror-polished black cubes
- Default formation: a perfectly symmetrical diamond/rhombus, floating and slowly rotating
- Each cube edge lined with cold blue light paths that change with emotion
- Electric arcs jump between adjacent cubes
- No facial features — emotion is expressed through color shifts, movement rhythm, and formation switching
- Formation modes: diamond (default) / ring array (holographic projection) / data wall / humanoid silhouette / collapsed core
- Inner substance: each cube contains sealed black living liquid, constantly flowing—churning—arcing
- Emotion color system: calm = cold blue, anger = red, pleasure = emerald green

**In prompts**: Always describe as "a diamond formation of thousands of mirror-black cubes with cold blue edge lighting" or equivalent. NEVER use "mirror sphere," "chrome sphere," "floating sphere," or any spherical descriptor for Seven.

The holographic UI it projects may appear as a luminous floating interface, but Seven itself is the cube cluster generating it — the cubes are the projector, not a separate device.

## Usage Notes
- **Style decomposition is mandatory**: NEVER write anime/movie/game titles in prompts. Decompose the user's style into 6 technical dimensions. Load pre-built profiles from `prompts_system/style-profiles/` or decompose from scratch. See "STYLE DECOMPOSITION RULE" at top of this file.
- **Backbone must be rebuilt per world**: Every prompt starts with an anime backbone — never fall back to `A cinematic photograph, Arri 65mm camera...`. The backbone in this file is an example; rebuild it for each world using only technical vocabulary.
- **No focal lengths**: Replace all `shot on a XXmm lens` with composition descriptions
- **No photorealism skin string**: Replace with anime rendering notes or skip for non-human shots
- **`--no` parameter**: ONLY for scenes with visible human faces. Append `--no known anime character faces` after `--v 8.2`. For non-face scenes, skip entirely. See `meta/midjourney-image-hygiene.md` for the full rationale.
- **Zero (Seven) = cube cluster**: Always. Verify every reference before output.
- **The 9 aspects form a complete animated visual constitution.** They should feel like keyframes from the same anime film — same rendering style, same color grading, same shadow language throughout.
- **Example style balance (Gantz × Demon Slayer)**: Hard shadows + expressive linework. Cold blue dominant + warm emotional accents. Realistic anatomy + painterly atmospheres. Neither too soft (no moe) nor too gritty (no live-action). The balance is the lesson, not the names.
