---
name: prompts-system
description: Build and execute production-ready image and video prompts for AI film projects. Use when a request involves world-building, concepts, keyframes, single shots, sequences, visual style systems, or Flux-to-MiniMax production.
---

# Prompts System

Use this skill as the routing layer for AI-film prompt work. Preserve the user's selected renderer, visual direction, project assets, and approval boundaries.

## Route the request

- For visual DNA and reusable technical style language, read the matching file in `style-profiles/`.
- For prompt construction, read the relevant architecture in `prompts_structure/`:
  - `world_view/` for a visual constitution or world-building frames.
  - `concept/` for character, entity, location, prop, or VFX concepts.
  - `frame/` or `keyFrames/` for still camera references and keyframe sets.
  - `shot/` for a continuous single video shot.
  - `sequence/` for a result containing multiple timed cuts.
- For a script outline or scene that needs shot design, read `shot-planning/SKILL.md` to plan the shots and output a shot breakdown before storyboards or media generation.
- For an actual shot-to-media run, read `prompt-execution/SKILL.md` before submitting media work.
- For a scene with generated shots or a first edit, read `editing-review/SKILL.md` to review the actual timeline and plan revisions; use `prompt-execution/SKILL.md` to produce any new or revised shots.
- For the local Flux.2 Klein → MiniMax H3 app at `D:\files\code\ai_image_video_generator`, also read `prompt-execution/references/ai-image-video-generator.md`.

## Production rules

- Treat renderer-specific limits as execution constraints, not creative defaults.
- In the local MiniMax H3 integration, every output width and height must be divisible by 32. The local app's default duration is 8 seconds only when duration is omitted; it is not a mandatory duration.
- Use a single-shot prompt for one continuous shot. Use a sequence prompt only when the requested result contains cuts.
- Inspect and approve reusable character, location, and prop anchors before generating dependent shots when continuity matters.
- Do not overwrite approved legacy assets unless the user asks to replace them.

## Reference

`README.md` is a human-facing directory map. It is not the instruction entry point.
