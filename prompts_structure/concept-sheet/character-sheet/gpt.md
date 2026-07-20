## Description
GPT variant of character concept design sheet. Same layout as `gemini.md`. Anti-noise is embedded in layout language, not appended as a long style block.

**For Gemini** → use `gemini.md`. Full layout → see `concept-sheet/character-sheet/gemini.md`.

## Layout Grid (identical to Gemini)

Same 16:9 grid: Main Visual (top-left 1/3×4/5) / View Variations (upper-right) / Expressions 2×2 (lower-right) / Bottom Row (full width ~1/5). Clean white background, thin dark dividers, labels in clean typography.

## GPT-Specific Modifications

### Prompt Composition

```
[Character content prompt — see concept/character/text_to_image_gpt.md] +

📐 Layout instruction:
16:9 character concept design sheet.
Clean near-white background with subtle paper texture, thin dark panel dividers, labels in small clean typography.
MAIN VISUAL: top-left, 1/3 width × 4/5 height, full-body in default outfit with neutral expression.
VIEW VARIATIONS: upper-right half, 2-3 angles revealing silhouette and drape.
EXPRESSIONS: lower-right half, 4 expressions in 2×2 grid, shoulder-up views.
BOTTOM ROW: full width, ~1/5 height, all clothing items laid flat + accessories + body marks, one horizontal row.

🎨 Style:
clean rendering, balanced detail, controlled material rendering,
clean gradients, controlled highlights, smooth background tones.
Production concept design reference sheet, clean flat presentation with crisp panel lines.
```

### GPT Style Suffix Options

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

### Negative Prompt (character sheet, short)
```
Avoid: ghost texture, repetitive micro-pattern noise, dirty texture buildup,
muddy shadows, uniform plastic gloss, waxy skin, dirty pore noise,
panel border artifacts, background texture bleed.
```

## Key Rules

1. Layout grid: same as gemini.md.
2. **Anti-noise is in layout language and style suffix, not an appended block** — style suffix is short (~4 lines) and negative prompt is scene-specific.
3. Background must be explicitly "clean near-white" — GPT defaults to textured paper backgrounds.
4. Panel dividers must be "clean crisp" — no decorative or textured borders.
5. Label typography must be "clean small" — GPT tends to add ornate or blurred text artifacts.
6. **Check for repetition before output.**
7. Read `meta/gpt-image-hygiene.md` for full methodology.
