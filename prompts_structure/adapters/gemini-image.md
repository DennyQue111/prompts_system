# Gemini Image Adapter

Use this adapter after the selected deliverable Core when the user explicitly chooses Gemini. Write the final executable prompt in English.

- Preserve the Core's subject, layout, reference boundaries, and continuity rules.
- Keep the Core's full style analysis: line quality, shading, palette, materials, proportions, lighting, and atmosphere may be expressed naturally in the prompt.
- Bind i2i references in text by role, what to copy, and what to ignore. If the reference is visibly degraded, explicitly exclude its artifacts; otherwise do not add GPT-specific anti-noise wording.
- Use natural-language aspect ratio and layout instructions; do not use Midjourney parameter syntax.
- For multi-panel sheets, name the grid, panel order, and the intended content of every panel explicitly.
