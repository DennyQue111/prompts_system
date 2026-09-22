Use this adapter after the selected deliverable Core when the user explicitly chooses **Flux** or a local open-source Flux workflow. Write the final executable prompt in English unless the host tool requires another language.

## Core behavior

- Preserve the Core's subject, layout, reference boundaries, and continuity rules. Do not redesign the deliverable.
- Flux is more literal and less forgiving than GPT/Gemini. Convert abstract intent into **visible evidence**: body mechanics, camera placement, clothing construction, material response, background structure, light direction, and what is or is not visible in frame.
- Keep prompts concrete. Replace vague phrases such as `mysterious atmosphere`, `strange laughter in darkness`, or `cinematic tension` with drawable evidence such as fog density, doorway silhouettes, partial faces, hand position, lamp glow, lens choice, and screen-space relationships.
- Prefer positive visible instructions first. Use short negative clauses only for high-risk failures such as duplicate people, extra limbs, or accidental text overlays.

## Flux prompt discipline

1. **State layout first when the deliverable is a sheet.** Repeat panel count, panel order, aspect ratio, and divider/background rules in plain language.
2. **Describe every important panel explicitly.** Flux often drops or merges panels when the prompt says only `character sheet` or `three-view reference`.
3. **Name the subject count clearly.** If the image must contain one person only, say `one single character only, no duplicate characters, no second figure`.
4. **Describe the shot geometry.** For frame and keyframe work, specify framing, lens, camera height, view direction, and what occupies foreground, midground, and background.
5. **Spell out material and lighting cues.** Flux responds better when cloth, leather, metal, grime, blood, skin, fog, and lamp light are described concretely.
6. **Convert emotion into posture.** Instead of only `nervous`, say `shoulders slightly raised, jaw held tight, hand paused mid-action`.

## Reference handling

- Use one image as the **identity anchor** when face/clothing consistency is the priority.
- Use a separate image as the **layout or shot anchor** only when composition must be preserved.
- Do not use a multi-view character sheet as direct single-frame composition authority unless the output itself is that sheet. Flux may interpret multiple views as multiple people in one scene.
- When a multi-panel concept sheet exists, derive or generate a separate single-character anchor before frame or video generation if identity stability matters.

## Recommended deliverable adjustments

- For Flux character concept sheets intended for downstream video, prefer a simpler layout with fewer, larger panels over dense production sheets.
- For Flux frame/keyframe prompts, describe the scene more fully than you would for GPT image generation. Do not assume Flux will infer missing environment details from style shorthand alone.
- For spatially constrained shots, keep topology rules in `../meta/spatial-continuity.md`, then express the final visible projection in denser plain language for Flux.

## Failure patterns to watch

- Multi-view sheet turns into multiple characters inside one scene.
- Background horror cues become literal extra people or faces because the prompt leaves the darkness semantically open.
- Clothing and body proportions drift when the prompt says only `same character as reference` without restating the core identifying features.
- Dense sheet layouts collapse into one hero portrait when panel instructions are too short.
