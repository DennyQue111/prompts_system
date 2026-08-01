# prompts_system

Image & video generation prompts knowledge base. Two modules work together: `style-profiles` defines the visual DNA, and `prompts_structure` builds specific prompts from that DNA.

---

## style-profiles

Drop-in visual style presets — each is a complete technical breakdown of a distinct aesthetic language, reusable across any project or prompt type.

Current profiles:

| File | Style | Key Traits |
|---|---|---|
| `made-in-abyss-technical.md` | 《来自深渊》技术拆解 | 7-dimension pure technical vocabulary, no work-name leakage, layered depth, organic fantasy |
| `gantz-kny-technical.md` | GANTZ × 鬼灭之刃融合 | Polished 2D anime key visual, cel shading, hand-drawn linework, cinematic lighting |
| `chinese-material-translucency.md` | 中国材质透光 | Material conversion (jade/porcelain/ice/glass), internal glow, minimal composition, S-curve depth |

Usage: pick a style profile → feed its technical dimensions into any prompt template from prompts_structure.

---

## prompts_structure

The prompt engineering engine. Type-first architecture: organize by *what* you're generating, then pick the model variant.

### Structure

- **concept/** — Content architectures for concept sheets (character / entity / location / prop / vfx)
- **concept-sheet/** — Layout architectures (grid, panel positions, 16:9 composition)
- **frame/** — Single cinematic frame (frameRef / look reference, t2i + i2i)
- **keyFrames/** — 3×3 grid single-image anchor for multi-shot visual consistency
- **world_view/** — World-building visual constitution (V11 orchestrator, MJ prompts, references)
- **shot/** — Single-shot video generation (Seedance)
- **sequence/** — Timed multi-shot pre-vis (Seedance)
- **storyboard/** — Multi-frame narrative sequence
- **meta/** — Cross-cutting quality standards (prompt hygiene, GPT anti-noise methodology)
- **examples/** — Session walkthroughs

### Model Variants

Dual-track Gemini/GPT with optional Midjourney, Jimeng, Seedance variants. GPT variants include anti-noise discipline (see `meta/gpt-image-hygiene.md`). Default: Gemini.

### Entry Point

`SKILL.md` — the skill definition for prompt generation. Start there.

---

## How They Fit Together

```
style-profiles/          →  "What does it look like?"
    ↓
prompts_structure/       →  "How do I build the prompt?"
    ↓
Final Prompt             →  Ready for image/video generation
```

Pick a style profile for the visual DNA, then route through prompts_structure's type-first architecture to construct the prompt.
