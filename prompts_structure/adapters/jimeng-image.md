# Jimeng Image Adapter

Use this adapter after a Core only when the user explicitly chooses Jimeng image generation and the selected deliverable is supported by the route. Compile the final prompt into concise Chinese modules.

## Platform controls

- The prompt must fit the platform's approximately 2,000-character limit. Preserve layout, subject identity, and required panel/cut descriptions before optional atmosphere or material detail.
- Bind the uploaded reference through the appropriate similarity mode: character identity 75–90%; style 30–50%; composition/layout 50–65%. State in text what to lock and what not to copy.
- Use one short `@image` declaration per reference as a project-side boundary statement; actual image attachment and similarity settings remain platform actions.
- When the reference already locks style, omit a duplicate style block. Add a style block only for an intentional style change or missing visual constraint.
- Use a Chinese negative list of 5–8 terms only for recurring failures not already excluded in the positive prompt.

## Output controls

- State the layout before the content. Use short labelled modules such as `【Layout 布局】`, `【主体】`, `【镜头与构图】`, `【风格锚定】`, and `【反向提示词】` only when needed.
- For Storyboards, default to no more than six panels and lock black-and-white line art in the style description, reference declaration, and negative list.
- For character and location concept sheets, preserve the Core's panel grammar exactly; do not simplify a sheet into a single illustration.
