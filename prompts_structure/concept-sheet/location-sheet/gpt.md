## Description
GPT variant of location concept design sheet. Same layout as `gemini.md`. Anti-noise is embedded in layout language, not appended as a long style block.

**For Gemini** → use `gemini.md`. Full layout → see `concept-sheet/location-sheet/gemini.md`.

## Layout Grid (identical to Gemini)

Same 16:9 grid: Main Visual (top-left) / Alternate Angle + Top-Down (upper-right) / Mid-Distance shots 3 panels (lower-right) / Bottom Row full-width ~1/5 (details + color palette). Clean near-white paper background, thin dark dividers, labels in clean typography.

## GPT-Specific Modifications

### Prompt Composition

```
[Location content prompt — see concept/location/text_to_image_gpt.md or image_to_image_gpt.md] +

📐 Layout instruction:
16:9 location concept design sheet.
Clean near-white background with subtle paper texture, thin dark panel dividers, labels in small clean typography.
TOP-LEFT — MAIN VISUAL (establishing shot)
UPPER-RIGHT LEFT — ALTERNATE ANGLE
UPPER-RIGHT RIGHT — TOP-DOWN VIEW
LOWER-RIGHT — MID-DISTANCE SHOTS (3 panels)
BOTTOM ROW — DETAILS + COLOR PALETTE (full width, ~1/5 height)

🎨 Style:
clean rendering, balanced detail, controlled material rendering,
clean gradients, controlled highlights, smooth background tones.
Production concept design reference sheet, clean flat presentation with crisp panel lines.
```

### Negative Prompt (location sheet, short)
```
Avoid: ghost texture, repetitive micro-pattern noise, dirty texture buildup,
muddy shadows, panel border artifacts, background texture bleed,
sky gradient artifacts, fog noise patterns, dark-band noise.
```

## Key Rules

1. Layout grid: same as gemini.md.
2. **Anti-noise is in layout language and style suffix, not an appended block.**
3. Background must be explicitly "clean near-white" — GPT defaults to textured paper backgrounds.
4. Panel dividers must be "crisp clean" — no decorative or textured borders.
5. All labels in "small clean typography" — GPT produces blurry or ornamented text artifacts.
6. **Check for repetition before output.**
7. Read `meta/gpt-image-hygiene.md` for full methodology.
