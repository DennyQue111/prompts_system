# GPT Image Adapter

Use this adapter after the selected deliverable Core. GPT is the default image renderer when the user does not name a model. Write the final executable prompt in English.

## Rendering controls

- Preserve the Core's subject, layout, reference boundaries, and continuity rules. Do not redesign the deliverable.
- Treat compression grain, banding, muddy shadows, repeated micro-patterns, dirty pore detail, and watermark-like artifacts in references as pollution, never as style.
- Describe materials with controlled, selective detail: `clean material separation`, `natural facial planes`, `subtle skin texture`, `smooth gradients`, `clean light falloff`, `controlled wear patterns`, `subtle reflections with clean boundaries`.
- Avoid `ultra detailed`, `8K`, `hyper detailed`, `micro detail everywhere`, `photorealistic skin pores`, and elaborate camera-brand language.
- Add one short, scene-specific English `Avoid:` list only when it prevents a real likely failure. Keep it roughly 10–15 terms; do not append a generic wall of negatives.

## Reference and sheet controls

- For i2i, bind each reference by role and state what it locks and what it must not transfer.
- For design sheets, say that panel dividers, labels, and empty background areas are crisp, clean, and undecorated.
- For KeyFrames, state each internal cinematic frame is 16:9 landscape and has clean, undecorated separators.
- For Storyboards, enforce either `pure black ink linework, white unfilled surfaces, sparse black hatching only` or the user-selected rough-pencil alternative. Explicitly exclude gray fills, color, text, timestamps, logos, and watermarks.

## Recovery

If GPT produces a dirty result, regenerate from the Core plus this adapter. Do not repeatedly i2i-repair the same dirty output.
