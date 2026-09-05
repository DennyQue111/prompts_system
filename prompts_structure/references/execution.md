# From architecture to generated media

Read for a stage requesting real media. This skill composes prompts; the host supplies model execution. Keep three decisions separate: content route, renderer/model, and tool/provider.

## Discover the executor

1. Inspect the host's available skills and tools for the selected modality and model. Use its tool discovery mechanism if capabilities are deferred. Do not declare a renderer unavailable solely because it is absent from the first visible tool list.
2. For GPT images, use the host's image-generation skill when present (commonly `imagegen`) and its built-in GPT image tool by default. Preserve this library's content, layout, and reference constraints when applying the execution skill. Follow its current schema rather than copying argument names from this file.
3. For Seedance or a named alternative, use a provider skill/tool only if it actually offers that model and required input mode. A video provider's presence alone does not prove Seedance availability. Read its current model selection, reference upload, duration, and output instructions.
4. No matching skill is required if a compatible tool is directly available. If neither exists, return the composed prompt with the missing capability and input mapping. Identify this as a prompt ready for rendering, not finished media. Do not fabricate a callable skill or tool name.

Model-family aliases select the prompt architecture, not an exact engine version. Preserve explicit versions; when the user names only a family, use the tool's supported default within that family. Follow the host's execution requirements for CLI/API fallbacks.

## Compile the prompt and bind references

- Read layout/base instructions locally and replace template placeholders with a complete executable prompt. Never submit “read simple_layout_instruction.md” or an unresolved `[project]` as an instruction to an image generator.
- Inspect referenced local images with the host image viewer before describing them. Text extraction or a filename alone does not reveal visual content.
- Keep one mapping from user identity/role to attachment, path, or upload handle. A name such as `人物A` can label an unnamed subject; it is not a fabricated filename.
- Actually pass each reference through the tool's supported image fields or upload workflow. Writing `@image filename.png` in text does not upload a file.
- Convert logical `@image`/`@TAG` references to the provider's supported syntax when required, preserving the role mapping. Bind character sheets to appearance, location sheets to space, and keyframes to shot composition. A character sheet's white background does not become the scene; its separate views do not become separate people.
- Never submit a whole multi-panel concept sheet as the literal first frame unless the user wants that grid animated. Use reference mode; if only a first-frame tool is available, prepare a suitable single frame when consistent with the requested workflow, disclosing the added step.
- Keep model-input prompts free of route notices, methodology, review tables, and unrelated project metadata. Retain functional reference labels, timing, and panel instructions.

## Execute and deliver

- Infer ordinary unspecified parameters using the selected architecture and tool's supported defaults. Preserve user duration, aspect ratio, count, and content. Template limits are working conventions; confirm actual tool limits from its schema/documentation. If an explicit requirement cannot be met, explain that limitation rather than silently shortening the result.
- A concept sheet is one image with multiple views; separately requested character and location sheets are separate deliverables. Generate only requested stages and necessary dependencies.
- If a tool returns a pending job, retain its job ID and use its status/wait mechanism. Poll that job rather than submitting the same generation again. Use the host's follow-up mechanism when a job must continue beyond this turn.
- When a stage completes, inspect the artifact where supported: intended subject, layout, retained identity, and—for video—shot scope, duration, and reference consistency. Report checks that could not be performed accurately.
- Feed successful outputs into dependent stages using actual returned paths/handles. If a dependency fails, complete independent requested outputs and report the blocked stage; do not pretend later stages ran.
- Deliver the generated image/video preview or real output link/path. A job ID means submitted/pending, not completed. On failure return the error summary, finished outputs, and ready-to-run prompt as appropriate.

## Continuation and portable use

“再来一张/只改镜头运动/改成竖版” refers to the active artifact and preserves its route, model, source mapping, and unaffected requirements. “这次用 Gemini” overrides that stage; “以后所有图片用 Gemini” establishes a continuing image preference until changed. Separate image/video preferences so a video choice does not alter later image defaults.

Distribute the entire `prompts_structure/` folder, or install it under the host's skill directory convention using the declared name `prompts-structure`. The host must load its entrypoint and have access to its referenced files. `agents/openai.yaml` is optional host metadata; other agents can follow `SKILL.md`. Automatic discovery and renderer access are capabilities of the receiving host, not provided by this folder.
