## Description
Use this architecture when the user uploads a Midjourney-generated reference image and wants to **extract a location/environment** from it, then generate a Gemini/GPT-compatible concept-location prompt that reproduces the location — preserving spatial layout, architectural character, atmosphere, and most critically, the original art style.

The core problem this solves: MJ images have a distinct rendering aesthetic that pure text-to-image prompts struggle to reproduce in other models. This structure bridges that gap by systematically deconstructing the visual DNA of the MJ reference and translating it into a prompt language that Gemini/GPT can interpret.

**Input:** MJ reference image + user instruction (e.g., "用这个风格生成第一幕的场景", "取这个环境的光影和色调", "保持这个构图但换成城市边缘的高架路")

**Output:** A location prompt in `text_to_image_general.md` format, but filled with observed (not imagined) content, plus style preservation keywords.

---

## Workflow (5 Steps)

### Step 1: Source Observation — What the Image Actually Shows

Describe ONLY what is objectively visible. Do not invent, do not embellish.

| Category | What to Observe |
|----------|----------------|
| **Geography** | Terrain type (urban/rural/mountain/coastal/industrial/void), elevation changes, natural vs built ratio, scale impression |
| **Spatial layout** | Depth planes: what's in foreground (close, detailed) → midground (main subject area) → background (depth, vanishing point). Width-to-depth ratio of the space |
| **Architecture** | Building style, era, materials, structural language (brutalist/organic/cyberpunk/vernacular/minimalist), height range, density, condition (pristine/weathered/ruined/under construction) |
| **Infrastructure** | Roads, bridges, power lines, street furniture, signage, public transport elements — what human systems are visible |
| **Time & weather** | Time of day (golden hour/midnight/overcast noon), season (if discernible), weather (clear/rain/fog/snow/haze), sky condition |
| **Light sources** | Every visible or implied light source: natural (sun/moon direction), artificial (streetlights/neon/windows/headlights/security lights), ambient (sky glow/bounce). Note color temperature and spread pattern of each |
| **Atmosphere** | Mood conveyed by the lighting and weather alone — before any narrative context. Particulate: fog/haze/rain/dust/smoke/fire embers |
| **Material palette** | Dominant surface materials visible: wet asphalt, rusted metal, smooth glass, rough concrete, polished wood, mirror surfaces, etc. How each material interacts with light |
| **Color distribution** | Background base color (% coverage) + midground accent colors + foreground detail colors. Saturation gradient across depth planes |
| **Lived-in details** | Scuffs, rust, debris, overgrowth, abandoned objects, graffiti, wear patterns — traces of use and passage of time |
| **Scale reference** | What provides the size read: human figure, vehicle, doorway, streetlight, tree |

**Rule:** If an element is obscured by shadow, depth of field blur, fog, or another object, note "not visible / obscured" — do not guess.

---

### Step 2: Style Analysis — Deconstructing the MJ Rendering Aesthetic

This is the most critical section. The MJ image has a specific rendering style that Gemini needs to approximate. Break it down into the following dimensions:

#### 2.1 Line Quality
| Aspect | Options / Examples |
|--------|-------------------|
| Line presence | Prominent visible line art / Subtle thin lines / No visible outlines |
| Line weight consistency | Uniform / Variable (thick on structural contours, thin on interior detail) |
| Line character | Clean mechanical / Expressive brush-stroke / Sketch-like / Ink-style / Architectural precision |
| Color of lines | Black / Dark brown / Colored to match adjacent area / No lines |

#### 2.2 Shading Method
| Aspect | Options / Examples |
|--------|-------------------|
| Shading type | Flat cel shading (1-2 shadow tones, hard edges) / Soft gradient shading (smooth light→dark) / Hard shadow (Gantz-style deep black shadows, sharp edge, high contrast) / Ambient occlusion only / No shading (flat color) |
| Shadow depth | Light shadows (low contrast) / Medium (naturalistic) / Deep black (8:1+ ratio) |
| Highlight style | Sharp specular (wet surface reflections) / Soft bloom / Rim light on silhouettes / No highlights |
| How light wraps surfaces | Hard light cutoff / Soft volumetric falloff / Diffuse ambient |

#### 2.3 Color Palette & Grading
| Aspect | What to Capture |
|--------|-----------------|
| Overall temperature | Cool-dominant / Warm-dominant / Neutral / Mixed temperature (warm light + cool shadows, or vice versa) |
| Saturation level | Highly saturated / Desaturated / Selective saturation (e.g., saturated neon accents against desaturated environment) |
| Color grading feel | Teal-orange blockbuster / Cold blue sci-fi / Warm nostalgic / Bleached dystopian / Natural / Monochromatic |
| Primary colors | The 2-4 dominant colors covering the largest area |
| Accent colors | Small-area high-impact colors (neon signs, glowing UI, fire, bioluminescence) |
| Shadow color | Pure black / Cool blue tint / Warm brown tint / Neutral gray |
| Highlight color | White / Warm gold / Cool cyan / Source-color-bleeding |

#### 2.4 Material & Texture Rendering
| Material | How It's Rendered |
|----------|-------------------|
| Concrete/stone | Rough matte with visible grain / Smooth polished / Weathered with cracks |
| Metal | Mirror chrome / Brushed matte / Rusted oxidized / Anodized colored / Wet reflection |
| Glass | Clear transparent / Tinted / Frosted / Cracked / Mirror-reflective |
| Asphalt/ground | Rough with visible aggregate / Smooth worn / Wet and reflective / Cracked with weeds |
| Water | Still mirror / Rippled reflection / Rain-streaked / Murky / Bioluminescent |
| Vegetation | Detailed individual leaves / Painterly masses / Overgrown wild / Manicured |
| Fabric/canvas | Woven texture visible / Worn and frayed / Clean and taut |
| Sky/atmosphere | Clear gradient / Cloud layer detail / Fog density / Light pollution glow / Stars |

#### 2.5 Composition & Camera Language
| Aspect | What to Capture |
|--------|-----------------|
| Focal length impression | Wide-angle (expanded depth, strong foreground) / Normal (~50mm) / Telephoto (compressed depth) |
| Camera angle | Eye-level / Low angle (awe, scale) / High angle (vulnerability, overview) / Dutch tilt |
| Depth of field | Shallow (bokeh in bg/fg) / Deep (everything sharp) / Selective focus |
| Composition rule | Rule of thirds / Symmetrical / Leading lines / Frame within a frame / Diagonal dynamic |
| Aspect ratio feel | Cinematic 16:9 / Vertical / Square / Ultra-wide |

#### 2.6 Atmosphere & Environmental FX
| Aspect | What to Capture |
|--------|-----------------|
| Particulate | Fog density / Haze color / Rain intensity / Snow / Dust motes / Ember float / Light rays (god rays) |
| Volumetric lighting | Visible light beams / Light cone scatter / Atmospheric density |
| Lens effects | Lens flare / Chromatic aberration / Bloom / Vignette / Film grain |

**Style Preservation Keywords (compile from above analysis):**
After filling 2.1–2.6, distill the analysis into a compact keyword string like:
```
[line quality keyword], [shading keyword], [color grading keyword], [material keyword], [camera keyword], [atmosphere keyword], [overall style category keyword]
```

This string will be prepended to the final Gemini prompt to anchor the style.

---

### Step 3: Location Extraction — Isolate the Target

Define exactly WHAT environment is being extracted from the image:

1. **Target specification**: Which location? (full establishing shot / specific building / street level / interior / etc.)
2. **Exclusions**: What is NOT the location? (characters/creatures, narrative action, UI overlays, specific props that belong to a character rather than the environment)
3. **User content override**: If the user wants the reference's style but a DIFFERENT location content ("用这个风格画废弃的游乐场"), separate style (from reference) from content (from user instruction)
4. **Contradiction resolution**: If the user asks for something that conflicts with the reference's physical logic (e.g., "keep the neon cyberpunk lighting but make it a medieval village"), flag the tension but proceed with user's content + reference's color/light logic where possible

---

### Step 4: Spatial Deconstruction — Separating Geography from Style

Unlike characters, locations don't have "front/side/back views" — they have **spatial layers** and **alternate angles**. Deconstruct the reference's space and plan reconstruction for the target location.

#### Spatial Layer Map
```
Foreground (closest to camera):
- Observed elements: [list directly visible foreground objects/textures]
- Depth function: [frame within frame? Blocking element? Scale reference?]
- Dominant material & light quality: [...]

Midground (main subject zone):
- Observed elements: [list the core location features]
- Focal anchor: [the ONE thing the eye is drawn to — a building, a light source, a landmark]
- Dominant material & light quality: [...]

Background (depth / vanishing point):
- Observed elements: [buildings, skyline, mountains, sky, horizon]
- Depth treatment: [atmospheric perspective? Sharp detail? Silhouette?]
- Dominant material & light quality: [...]
```

#### Alternate Angles (if generating a multi-panel sheet)
```
Alternate angle 1 — Low angle from [position]:
[How the location reads from a different vantage — what changes?]

Alternate angle 2 — Top-down overview:
[Bird's-eye spatial relationships — layout, zoning, traffic flow]

Mid-distance details (2-3 panels):
[Key location features that tell environmental story — a broken sign, an empty bus stop, a streetlight with one LED dead]
```

**Rule for spatial deduction:** If the user wants the reference's STYLE but a DIFFERENT location's CONTENT, replace the geography/architecture with the target location while preserving the spatial composition logic (foreground→midground→background depth structure, camera angle, focal length feel) from the reference.

---

### Step 5: Gemini Output Prompt

The final prompt, formatted for Gemini/GPT image generation. Follow the layout from `concept-sheet/location-sheet/general.md` but fill ALL content from Steps 1-4 observations and inferences.

```
[Style preservation keywords from Step 2.6] +

[Layout instruction: 16:9 location concept design sheet, clean white background...] +

TOP-LEFT — MAIN VISUAL (establishing shot):
[Location type + narrative function] +
[Atmosphere injection: from Step 1 atmosphere + Step 2.6 atmospheric FX] +
[Spatial composition: from Step 4 spatial layer map — foreground → midground → background] +
[Architecture & materials: from Step 1 architecture + material palette, textured by Step 2.4 material rendering] +
[Lived-in details: from Step 1] +
[Scale reference: from Step 1]

UPPER-RIGHT LEFT — ALTERNATE ANGLE:
[Step 4 alternate angle 1]

UPPER-RIGHT RIGHT — TOP-DOWN VIEW:
[Step 4 alternate angle 2]

LOWER-RIGHT — MID-DISTANCE SHOTS (3 panels):
[Step 4 mid-distance details — location storytelling through objects and wear]

BOTTOM ROW — DETAILS + COLOR PALETTE (full width, ~1/5 height):
[Step 1 lived-in details as macro close-ups] +
Color Palette: [Step 2.3 primary + accent colors distilled to hex descriptions]

[Style suffix with Step 2 keywords]
```

---

## Key Rules

1. **Observe, don't invent.** If a building's interior is not visible through windows, write "interior: not visible." Do not guess what's inside.
2. **Style analysis is mandatory.** A location prompt without style keywords will produce Gemini's default aesthetic, which will NOT match the MJ reference. Always complete Step 2 fully.
3. **Separate geography from style.** The reference image's spatial layout is content. Its color, light, and texture treatment is style. When the user asks for "this style but a different location," replace the geography but keep the visual DNA.
4. **Respect user content override.** If the user says "apply this style to a suburban ring road at midnight," the scene geography and architecture come from the user's description. The rendering style comes from Step 2 analysis of the reference.
5. **Light source logic must transfer.** If the reference is lit by neon signs from below, the generated location must also derive its lighting logic from in-scene sources, not generic ambient fill. The language of light is the strongest style signal.
6. **Weather and atmosphere are style, not content.** Rain, fog, time of day, particulate — these are transferable style elements. A user asking "this style but my location" almost always means "keep the weather and atmosphere too."
7. **No artistic reinterpretation.** The purpose is reproduction, not improvement. If the MJ image has fog that's a bit too thick, describe the fog — don't "fix" it.

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Style analysis skipped → Gemini output looks generic | Always complete Step 2 — the style keywords are what make the reproduction possible |
| User's target location described too vaguely | Ask for specifics: time of day, weather, architectural style, key landmarks — otherwise the model defaults |
| Light source logic not transferred | The reference's lighting language (neon underlight, god rays through windows, sodium streetlight pools) must be explicitly described, not summarized as "dramatic lighting" |
| Weather discarded as "content" | Rain, fog, time of day, and atmospheric conditions are style transfer elements unless user explicitly says otherwise |
| Material palette ignored | "Wet asphalt with mirror streaks" vs "dry dusty concrete" — this IS the style difference. Always describe surface material + light interaction in the output prompt |
| Spatial depth flattened | If the reference has strong 3-plane depth (foreground silhouette → midground subject → background vanishing point), the output must replicate this depth structure |

---

## Usage Notes

- **When to use this**: User uploads a reference image (MJ or other) and asks to extract/reproduce a location environment from it, or apply its visual style to a project location.
- **When to use `text_to_image_general.md` instead**: User describes a location from imagination/script — no reference image provided.
- **When to use `midjourney.md`**: User wants a single-shot atmospheric location image generated directly in Midjourney.
- **Sheet layout**: Always pair with `concept-sheet/location-sheet/general.md` for the multi-panel grid specification.
- **Scale is critical in locations**: Always include at least one scale reference element (human figure, vehicle, doorway) in the output prompt. Environments without scale cues feel like miniature dioramas.
- **For interior locations**: Add ceiling height, room dimensions, and contained/spacious feel to Step 4's spatial layer map.
