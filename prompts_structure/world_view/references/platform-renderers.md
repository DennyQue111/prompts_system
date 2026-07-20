# Platform Renderers

Keep the world scene platform-neutral until the final rendering step. Preserve meaning across renderers; change syntax, not the world.

Return the rendered prompts without explaining or citing platform syntax unless the user explicitly requests an explanation or audit.

## Generic

Write one clean paragraph in the user's requested language. Use positive visual description first. Add a short natural-language exclusion sentence only when it prevents a likely failure.

Do not invent platform parameters.

## Midjourney

Place parameters at the end of the prompt.

- Add `--ar [ratio]` when a ratio is known.
- Add `--sref [value]` and `--profile [value]` only when the user supplies them.
- Add a model version only when the user requests that version; otherwise use the platform default.
- Add `--hd` only when requested or when the user explicitly chooses an HD workflow compatible with the selected version and ratio.
- Use a single `--stylize` value by default. Use permutations such as `--stylize {75,125,250,500}` only when the user explicitly wants a multi-job exploration and understands that it expands into separate generations.
- Express exclusions with `--no` rather than appending a universal prose string. Keep excluded terms simple and avoid compound phrases whose tokens could be interpreted independently.
- Never output empty parameters.

Recommended order:

```text
[scene] --ar [ratio] [--sref value] [--profile value] [--stylize value] [--v value] [--hd] --no [simple exclusions]
```

Validate current platform syntax when tools or documentation are available; platform parameters are time-sensitive.

## Nano Banana

Write natural-language scene and exclusion instructions. State the chosen aspect ratio once as a generation setting rather than embedding Midjourney syntax. Do not append `--ar`, `--no`, `--sref`, `--profile`, or `--stylize`.

Use the user's requested language. Preserve English technical terms only when they add precision; do not claim English is universally superior.

## GPT Image

Write direct natural-language instructions describing composition, action, continuity anchors, light, material, and desired exclusions. State aspect ratio or orientation as a setting or plain instruction. Do not append Midjourney parameters.

Prefer concrete positive instructions over long negative lists. If exclusions matter, group them in a short final sentence such as `Avoid poster-like posing, text overlays, and unrelated futuristic materials.`
