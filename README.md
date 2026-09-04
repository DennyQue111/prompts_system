# prompts_system

Image & video generation prompts knowledge base. Three modules: `style-profiles` defines the visual DNA, `prompts_structure` builds specific prompts from that DNA, and `ref_skills` provides external reference methodologies.

---

## prompts_structure

The prompt engineering engine. It first infers *what* the user wants from natural language and attached references, then selects the matching type, source mode, and model variant. Image generation defaults to GPT; video generation defaults to Seedance. Explicit model choices always override these defaults.

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

Entry point: `SKILL.md`. The skill is execution-oriented: when the user asks to generate media, the agent should assemble the prompt internally and call an available compatible renderer instead of requiring the user to name a template.

---

## style-profiles

Drop-in visual style presets — each is a complete technical breakdown of a distinct aesthetic language, reusable across any project or prompt type.

Current profiles: made-in-abyss-technical, gantz-kny-technical, chinese-material-translucency, moebius-ligne-claire, 2d-hand-drawn-motion.

---

## project-structure

Universal file structure & naming conventions for AI short-film projects. **Generic by design** — any new script project (复生协议, 孢子纪元, or future) initializes its directories per this skill. Contains:
- `SKILL.md` — generic directory skeleton, naming conventions (`{Name}_{type}_{model}_v{N}`), workflow pipeline, model routing
- `references/复生协议_案例.md` — ★ concrete reference implementation (real project with naming details & pitfalls)
- `references/复生协议_full-tree.md` — auto-generated full file tree (332 entries)
- `scripts/generate_tree.py` — regenerate the full-tree for any project

Usage: tell an agent "按 project-structure skill 的结构来" when starting a new project.

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

`project-structure/` is orthogonal — it answers "where does the file go?" and applies to the whole pipeline. `ref_skills/` sits outside this pipeline — browse for ideas, not as production tools.
