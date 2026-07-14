## Description
GPT variant of entity concept design sheet. Same layout as `gemini.md`. Anti-noise is embedded in layout language, not appended as a long style block.

**For Gemini** → use `gemini.md`. Full layout → see `concept-sheet/entity-sheet/gemini.md`.

## Layout Grid (identical to Gemini)

Same 16:9 grid: Main Visual (top-left 1/3×4/5) / View Variations (upper-right) / Detail Close-ups (lower-right, AI-determined flexible grid) / Bottom Row (full width ~1/5, form variations → emotion states). Clean white background, thin dark dividers, labels.

## GPT-Specific Modifications

### Prompt Composition

```
[Entity content prompt — see concept/entity/gpt.md] +

📐 Layout instruction:
16:9 entity concept design sheet.
Clean near-white background, thin clean panel dividers, labels in small clean typography.
MAIN VISUAL: top-left, 1/3 width × 4/5 height, entity in default form with label.
VIEW VARIATIONS: upper-right half, 2-3 angles showing three-dimensionality.
DETAIL CLOSE-UPS: lower-right half, critical component close-ups, AI-determined flexible grid.
BOTTOM ROW: full width, ~1/5 height, form variations first (left) then emotion states (right).

🎨 Style:
clean rendering, balanced detail, controlled material rendering,
clean gradients, controlled highlights, smooth background tones,
clean crisp panel lines, no decorative border artifacts.
Entity concept design reference sheet, clean flat presentation with sharp typography.
```

### GPT Style Suffix Options

**Abstract/energy entities:**
```
clean entity concept design sheet, controlled rendering,
smooth gradients, clean light falloff, crisp panel lines,
minimal background, flat clean swatches for bottom row
```

**Material-based entities:**
```
entity concept design reference sheet,
controlled material rendering, clean surface definition,
balanced structural detail, clean panel composition,
smooth background tones
```

Avoid: "atmospheric void background", "dark dramatic entity sheet" — triggers muddy gradient artifacts on GPT.

### Negative Prompt (entity sheet, short)
```
Avoid: ghost texture, repetitive micro-pattern noise, dirty texture buildup,
muddy shadows, uniform plastic gloss, panel border artifacts,
background texture bleed, fuzzy typography, ghost typography duplicates.
```

## Key Rules

1. Layout grid: same as gemini.md.
2. **Anti-noise is in layout language and style suffix, not an appended block** — style suffix is short (~5 lines) and negative prompt is scene-specific.
3. **Abstract/energy/material entities**: "smooth gradients, clean light falloff" — energy effects are most vulnerable to noise on GPT.
4. **Panel backgrounds between entity and sheet**: "clean separation" — no gradient blending into sheet background.
5. **Labels/typography**: must specify "clean sharp" — GPT generates blurry or doubled text artifacts.
6. **Check for repetition before output.**
7. Read `meta/gpt-image-hygiene.md` for full methodology.
