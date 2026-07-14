## Description
GPT variant of character concept design sheet. Same layout as `gemini.md` with GPT anti-noise adaptations for the sheet rendering.

**For Gemini** → use `gemini.md`. Full layout → see `concept-sheet/character-sheet/gemini.md`.

## Layout Grid (identical to Gemini)

Same 16:9 grid: Main Visual (top-left 1/3×4/5) / View Variations (upper-right) / Expressions 2×2 (lower-right) / Bottom Row (full width ~1/5). Clean white background, thin dark dividers, labels in clean typography.

## GPT-Specific Modifications

### Full Prompt Composition

```
[Character content prompt — see concept/character/text_to_image_gpt.md] +

[📐 Layout instruction:]
16:9 character concept design sheet.
Clean near-white background with subtle paper texture, thin dark panel dividers, labels in small clean typography.
MAIN VISUAL: top-left, 1/3 width × 4/5 height, full-body in default outfit with neutral expression.
VIEW VARIATIONS: upper-right half, 2-3 angles revealing silhouette and drape.
EXPRESSIONS: lower-right half, 4 expressions in 2×2 grid, shoulder-up views.
BOTTOM ROW: full width, ~1/5 height, all clothing items laid flat + accessories + body marks, one horizontal row.

[🎨 Style suffix — GPT:]
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
clean blurred background, smooth background tones,
minimal repetitive patterns.
Layout designed as a production concept design reference sheet,
clean flat presentation with crisp panel lines, precise typography,
no background texture bleeding into panels, no residual marks between panels.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise, facial artifact marks,
panel border artifacts, background texture bleed.
```

### GPT Style Suffix Options
For character sheets, GPT works best with:

**Direction A — Clean concept art style:**
```
clean character concept design sheet, flat layout presentation,
controlled cel-style rendering with soft gradient shading,
balanced detail on key features, clean crisp panel lines,
minimal background texture, typographic labels
```

**Direction B — Realistic concept style:**
```
character concept design reference sheet,
controlled naturalistic rendering, matte skin with soft highlights,
clean material definition, minimal background, clean panel composition
```

Avoid: "photorealistic character sheet", "hyper detailed concept", "cinematic character reference" — these trigger excessive texture on GPT.

### Key Rules
1. Layout grid: same as gemini.md.
2. Every prompt must use the GPT style suffix (above) — not the Gemini one.
3. Background must be explicitly "clean near-white" — GPT defaults to textured paper backgrounds.
4. Panel dividers must be "clean crisp" — no decorative or textured borders.
5. Label typography must be "clean small" — GPT tends to add ornate or blurred text artifacts.
6. Read `meta/gpt-image-hygiene.md` for full methodology.
