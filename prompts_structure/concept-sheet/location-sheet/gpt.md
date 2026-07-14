## Description
GPT variant of location concept design sheet. Same layout as `gemini.md` with GPT anti-noise adaptations.

**For Gemini** → use `gemini.md`. Full layout → see `concept-sheet/location-sheet/gemini.md`.

## Layout Grid (identical to Gemini)

Same 16:9 grid: Main Visual (wide establishing shot top-left) / Alternate Angle + Top-down (upper-right) / Mid-distance details 3 panels (lower-right) / Bottom Row (full width ~1/5, environment details + color palette). Clean white background, thin dark dividers, labels.

## GPT-Specific Modifications

### Full Prompt Composition

```
[Location content prompt — see concept/location/text_to_image_gpt.md] +

[📐 Layout instruction:]
16:9 location concept design sheet.
Clean near-white background with subtle paper texture, thin dark panel dividers, labels in small clean typography.
MAIN VISUAL: top-left establishing shot, [spatial composition from content].
ALTERNATE ANGLE: upper-right left panel.
TOP-DOWN VIEW: upper-right right panel.
MID-DISTANCE SHOTS: lower-right, 3 panels.
BOTTOM ROW: full width, ~1/5 height, environment detail macro shots + color palette reference.

[🎨 Style suffix — GPT:]
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
smooth background tones, clean depth of field,
smooth dark tones with readable shadow detail,
minimal repetitive patterns.
Production location concept design reference sheet,
clean flat presentation with crisp panel lines,
no sky gradient artifacts, no background texture bleed into panels.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, milky reflections,
clipped highlights, crushed blacks, dark-band noise,
sky gradient artifacts, fog noise patterns,
panel border artifacts, background texture bleed.
```

### GPT Style Suffix Options
**Direction A — Clean concept art:**
```
clean location concept design sheet, flat layout presentation,
controlled environmental rendering, balanced spatial detail,
clean crisp panel lines, minimal background texture
```

**Direction B — Cinematic reference:**
```
location concept design reference sheet,
controlled cinematic rendering, clean atmosphere with smooth light falloff,
clean material definition on architectural surfaces,
clean panel composition with smooth background
```

Avoid: "cinematic location concept", "photorealistic environment sheet", "hyper detailed scene" — triggers excessive texture noise on GPT.

### Key Rules
1. Layout grid: same as gemini.md.
2. Every prompt must use GPT style suffix (above).
3. **Panel dividers must be "clean crisp"** — GPT decorates borders with noise.
4. **Color palette panel must be "clean flat swatches"** — GPT adds texture to color blocks.
5. **Sky/atmosphere in panels must be "smooth gradients"** — highest-risk area for GPT artifacts.
6. Read `meta/gpt-image-hygiene.md` for full methodology.
