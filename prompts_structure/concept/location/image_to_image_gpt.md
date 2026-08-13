## Description
Use this architecture when extracting + reproducing a location/environment from a **Midjourney reference image** for **GPT**.

GPT i2i amplifies reference image noise — compression artifacts, dark-band mud, micro-pattern noise all get aggressively rendered in the output. This architecture filters reference pollution while preserving style DNA.

**For Gemini** → use `image_to_image_gemini.md`.

## Workflow (5 Steps)

Same as Gemini: Source Observation → Style Analysis → Location Extraction → Spatial Deconstruction → Output Prompt.
Full methodology: see `concept/location/image_to_image_gemini.md`.

## GPT-Specific Modifications

### Style Analysis (Step 2) — Add noise detection
When analyzing the reference image, explicitly flag:
- **Noise regions**: dark shadow areas with banding or color noise
- **Texture overdrive zones**: surfaces with excessive micro-detail that would read as "dirty" on GPT
- **Gradient artifacts**: sky or fog areas with visible step artifacts
- **Clean zones**: areas where detail is appropriately controlled — these are the model for GPT output

### Output Prompt (Step 5)

Reference-anchored structure (NOT pure text-to-image from scratch):

```
Based on the attached reference image — [brief scene ID: "a night suburban ring road in heavy rain"] — generate a [project]. EXTEND this location from the reference, not create from scratch.

Reference content: [key features observed in reference — what's in foreground/midground/background, light sources, signs with garbled text to fix]. **Exclude all characters from the reference image — environment only, no human figures.**

Layout instruction: reference hdr_layout_instruction.md in this directory for full grid spec — 16:9 HDR 4-panel layout, 2×2 grid, equal panels, 28mm wide-angle, 90° rotation per panel. Clean near-white background with subtle paper texture, thin dark panel dividers, labels in small clean typography.

[Panel 1 (TOP-LEFT — 正面 0°): main establishing view — reproduce the reference image spatial logic + text fixes] +
[Panel 2 (TOP-RIGHT — 右侧 90°): right side view from same position, deduced from reference spatial logic] +
[Panel 3 (BOTTOM-LEFT — 背面 180°): opposite direction from same position, deduced from reference spatial logic] +
[Panel 4 (BOTTOM-RIGHT — 左侧 270°): left side view from same position, deduced from reference spatial logic] +

Style: [keywords extracted from reference — model, lighting, atmosphere — 1 line only] +

Avoid: [~10-15 scene-relevant terms only, not full methodology dump]
```

### Word Choice Guide (embed in panel descriptions, don't append as block)

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed environment | balanced spatial detail |
| micro texture on all surfaces | selective texture on near-plane architectural focus |
| highly textured rendering | controlled material rendering |
| atmospheric cinematic bokeh | clean depth of field |
| dark atmospheric scene | smooth dark tones, clean shadow falloff |
| mirror-like wet reflections | subtle controlled reflections with clean boundaries |
| chaotic rain particle spray | directional linear rain streaks |
| neon bloom / glow overdrive | soft clean glow halos centered on source |

### Scene-Specific Negative Prompt (end of prompt, short)

Tailored to scene content — never copy the full generic list. For a rainy night urban scene:
```
Avoid: garbled text, pseudo-characters, compression grain, dark-band noise,
muddy shadows, clipped highlights, crushed blacks, ghost texture,
dirty texture buildup, over-detailed distant facades,
neon glow overdrive, mirror-like reflections,
characters, human figures, people.
```

For other scene types, curate relevant terms from `meta/gpt-image-hygiene.md`.

## Key Rules

1. Use gemini.md for Steps 1-4 — identical workflow.
2. **Prompts must reference the image**: start with "Based on the attached reference image..."
3. **Clean language is in the word choice, not an appended block** — use the word choice table above while writing each panel description. The proof is in the writing, not the disclaimer.
4. **Negative prompt is scene-specific and short**: ~10-15 terms relevant to actual scene content. Never dump the full generic methodology.
5. **Never transfer reference image noise** — compression artifacts, banding, micro-pattern noise are pollution, not style.
6. **Reference background texture ≠ style** — extract only color palette, light ratio, and atmosphere from the reference background, not its noise profile.
7. **Wet/dark scenes are highest risk** — use "smooth dark tones, subtle reflections with clean boundaries" in descriptions.
8. **Check for repetition before output** — every sentence should carry new information.
9. **No characters**: Scene concept images are environment-only. If the reference image contains human figures, explicitly state "exclude all characters from the reference image, environment only." Add "characters, human figures, people" to the negative prompt. Use architectural elements for scale reference.
10. Read `meta/gpt-image-hygiene.md` for full methodology.
