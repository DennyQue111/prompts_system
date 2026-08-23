## Description

GPT variant of storyboard — multi-frame narrative sequence.

**Base architecture + scene-type specializations** → see `gemini.md`. This file is a **GPT-specific overlay** only. Load `gemini.md` first for the full storyboard architecture, layout grid, prompt composition, camera & lens narrative, style suffix, scene-type specializations (action/dialogue/vfx/mixed), and general key rules.

This file covers what GPT does differently from Gemini:
1. Anti-noise word choice (GPT over-details)
2. Alternative rough pencil style (for action choreography preview)
3. Exclusion list practice (GPT responds well to explicit "no" lists)

---

## GPT Storyboard Prompt Composition

```
[Reference images — if provided, declare here. See gemini.md → Reference Image Declaration.]

[📐 Storyboard Header:]
[number of frames] storyboard, [row layout],
clean near-white background, clean thin panel borders,
minimal clean typography for labels.
PURE BLACK-AND-WHITE INK: every uninked area is solid white;
use black contour lines and sparse black hatching only;
no grayscale fills, gray wash, tonal blocks, or gradients.

[FRAME 1:]
[shot type + angle + focal length] — [description]
(pure black ink linework, white unfilled surfaces, sparse black hatching only)

[FRAME 2:]
[shot type + angle + focal length] — [description]
(pure black ink linework, white unfilled surfaces, sparse black hatching only)

[...]

All frames: consistent line density, solid white uninked surfaces,
clean panel separators, no background texture bleed,
no grayscale or tonal rendering anywhere.

[Exclusion list for this storyboard:
No timestamps. No dialogue text. No singing. No extra characters.
No enemies. No logos. No watermarks. No color. No grayscale fills.
No gray wash. No tonal blocks. No gradients. No 3D rendering.]
```

### Frame Count vs Video Duration

When the user specifies a target video duration, choose the frame count (see `gemini.md` → Frame Count vs Video Duration for the full table):

| Video Duration | Frame Count | Grid Layout |
|----------------|-------------|-------------|
| 5s | 3–4 frames | 3×1 or 2×2 |
| 10s | 5–6 frames | 3×2 |
| 15s | 6–8 frames | 3×2 or 4×2 |
| 20s | 8–10 frames | 4×2 or 5×2 |
| 30s | 10–12 frames | 4×3 or 5×3 |

Default to 6 frames (10s baseline) if no duration specified.

---

## GPT Word Choice Guide (per frame)

GPT over-details storyboard frames. Use controlled vocabulary in **each frame description** — not as an appended block.

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed sketch | pure black ink linework, white unfilled surfaces, sparse black hatching only |
| highly textured rendering | balanced detail, smooth backdrop |
| photorealistic storyboard | clean panel composition |

Do not use the standalone words `shading`, `tonal`, or `shadow fill` in clean-ink storyboard frame descriptions. GPT often interprets them as permission to paint gray areas. When form separation is needed, specify the visible mark-making directly: `variable black line weight`, `sparse black cross-hatching`, or `small isolated solid-black accents`.

---

## Alternative Style: Rough Pencil / Gesture Drawing

For action choreography preview storyboards, the default "clean ink" style may feel too finished. Use this alternative style suffix when the storyboard is an early-stage fight choreography draft:

```
rough pencil storyboard, black and white only, minimal detail,
fast gesture drawing energy, simple anatomical construction,
strong silhouette readability, lightweight and dynamic,
unfinished — like early fight choreography preview,
clean thin panel borders, solid white background
```

| Style | When to Use | Character |
|-------|------------|-----------|
| Clean ink (default) | Production-ready storyboard, dialogue scenes, VFX planning | Precise, readable, professional |
| Rough pencil / gesture | Action choreography preview, early blocking draft, movement-focused | Dynamic, energetic, unfinished |

**Anti-noise for rough pencil style:** GPT may still over-detail. Reinforce with "minimal detail, simple anatomy, fast gesture energy" in each frame description. Do NOT add the clean-ink phrase "pure black ink linework, white unfilled surfaces, sparse black hatching only" — that contradicts the rough aesthetic. Still keep the output monochrome and free of gray fills unless the user explicitly requests tonal pencil shading.

---

## Per-Storyboard Exclusion List

GPT models respond well to explicit "no" lists at the end of a prompt. Always append an exclusion list tailored to the storyboard type:

```
[Exclusion list for this storyboard:
No timestamps. No dialogue text. No singing. No extra characters.
No enemies. No logos. No watermarks. No color. No grayscale fills.
No gray wash. No tonal blocks. No gradients. No 3D rendering.]
```

For clean-ink storyboards, the exclusions above are mandatory even when a scene-type exclusion list from `gemini.md` is also used. Merge the lists; do not replace the grayscale exclusions with the shorter `No color` wording. `No color` alone is insufficient because GPT may still produce monochrome gray rendering.

Customize per scene type (scene-type rules are in `gemini.md`):
- **Action**: add "No static poses. No frozen standoffs."
- **Dialogue**: add "No action VFX. No dramatic camera angles."
- **VFX**: add "No photorealistic effects. No particle noise."
- **Mixed**: take the union of all involved types.

---

## GPT Key Rules

1. **Storyboard structure**: same as `gemini.md`.
2. **Anti-noise and pure-line enforcement are in per-frame word choice** — use "pure black ink linework, white unfilled surfaces, sparse black hatching only" in each clean-ink frame description. Do not use `clean shading`.
3. **All frames must share the same detail level** — inconsistent frame quality breaks storyboard readability.
4. **Panel borders: "clean thin lines"** — GPT decorates storyboard panel borders aggressively.
5. **Scene-type specializations** (action/dialogue/vfx/mixed): all rules are in `gemini.md` → Scene-Type Specializations. Apply them per-frame as needed.
6. **Check for repetition before output.**
7. Read `meta/gpt-image-hygiene.md` for full methodology.
8. **Rough pencil style for action preview**: use "rough pencil, gesture drawing energy" style suffix instead of "clean ink" for early-stage action choreography storyboards.
9. **Always append exclusion list**: GPT models respond well to explicit "no" lists. Customize per scene type.
10. **No dialogue text on panels**: Never write spoken lines as text on storyboard panels. Dialogue is conveyed through facial expression, body language, and lip movement only. Black text is limited to panel labels and 2–3 word action notes. See `gemini.md` → Key Rule 11.
11. **Pure black-and-white must be enforced three times for clean-ink storyboards**: once immediately after the layout header, once in each frame's rendering phrase, and once in the final exclusion list. This repetition is intentional because layout compliance is fragile, not decorative prompt duplication.
12. **Preflight visual test**: before submitting the prompt, verify that it describes every non-line region as solid white and limits dark rendering to black contours, sparse hatching, and isolated solid-black accents. If the prompt permits `shading`, `gray`, `wash`, `tone`, `gradient`, or soft filled shadows anywhere outside the exclusion list, rewrite that phrase.
