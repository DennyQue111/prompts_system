# prompts_system

Image & video generation prompts knowledge base. Three modules: `style-profiles` defines the visual DNA, `prompts_structure` builds specific prompts from that DNA, and `ref_skills` provides external reference methodologies.

---

## prompts_structure

The prompt engineering engine. Type-first architecture: organize by *what* you're generating, then pick the model variant.

Key directories:
- **concept/** — Content architectures for concept design sheets (character / entity / location / prop / vfx), with Gemini/GPT/Jimeng/Midjourney variants
- **performance/** — Character acting & behavior system. Upstream layer: acting master profiles, scene adaptation rules, eye life system — feeds into video sequences and shots
- **frame/** — Single cinematic frame (frameRef / look reference), t2i + i2i for Gemini/GPT/Midjourney/Jimeng
- **keyFrames/** — 3×3 grid single-image anchor for multi-shot visual consistency
- **sequence/** — Timed multi-shot pre-vis (Seedance), with @TAG reference binding, first-frame rules, spatial landmarks
- **shot/** — Single-shot video generation (Seedance)
- **storyboard/** — Multi-frame narrative sequence (Gemini / GPT)
- **world_view/** — World-building visual constitution and MJ prompts
- **meta/** — Cross-cutting quality standards (GPT anti-noise hygiene)
- **examples/** — Session walkthroughs

Entry point: `SKILL.md`.

---

## style-profiles

Drop-in visual style presets — each is a complete technical breakdown of a distinct aesthetic language, reusable across any project or prompt type.

Current profiles: made-in-abyss-technical, gantz-kny-technical, chinese-material-translucency, moebius-ligne-claire, 2d-hand-drawn-motion.

---

## ref_skills

External reference skill files from third-party workflows. **These are for study and reference only — not part of the active prompts_structure.** They provide alternative methodologies (Cinedance Higgsfield director system, Lira image prompt optimization, acting performance systems) that can inform improvements to the main prompt pipeline.

---

## How They Fit Together

```
style-profiles/          →  "What does it look like?"
    ↓
prompts_structure/       →  "How do I build the prompt?"
    ↓
Final Prompt             →  Ready for image/video generation
```

`ref_skills/` sits outside this pipeline — browse for ideas, not as production tools.
