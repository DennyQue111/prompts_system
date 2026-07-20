# Output Formats

## Compact mode — default

Use this unless the user requests expanded production detail.

```markdown
# [Poetic World Name]

Platform: [generic or named platform]  
Aspect ratio: [ratio]  
Assumptions: [only important inferred choices]

## World concept

[2–3 sentences]

## Continuity anchors

- Environment: [...]
- Inhabitants and body covering: [...]
- Materials and architecture: [...]
- Ecology and recurring symbol: [...]
- Palette and lighting: [...]
- Forbidden drift: [...]

## 1. Inhabitants / 居民

Visual intention: [one concise Chinese sentence, or the user's requested language]

Prompt:  
[one self-contained platform-ready prompt]

...continue through the requested aspects...
```

Do not duplicate separate camera and lighting fields when the full prompt already contains them.

## Production mode — on request

Use when the user asks for full bilingual prompts, separated production controls, or a detailed prompt pack.

```markdown
## [Aspect]

World note: [brief visual function]

Camera:
- EN: [position, distance, focal length, depth-of-field intent, framing]
- 中文: [equivalent content]

Lighting:
- EN: [source, direction, contrast, temperature, atmospheric interaction]
- 中文: [equivalent content]

English Prompt:  
[self-contained platform-ready prompt]

中文提示词：  
[semantically equivalent prompt]
```

Keep functional platform parameters unchanged in the translated version only when the user genuinely needs two directly executable copies. Otherwise show parameters once to avoid accidental duplicate jobs.

## Planning-only mode

When the user wants visual development before prompt writing, output only:

- World concept.
- Continuity bible.
- Nine-row aspect matrix.
- Open creative decisions.

Do not generate final platform prompts until requested.

## Subset behavior

Default to all nine aspects. If the user names a subset, produce exactly that subset in canonical order unless they specify another order. Do not pad the output back to nine.

