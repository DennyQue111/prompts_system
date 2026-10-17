# Entity Concept Design Sheet — Layout Instruction

## Layout Strategy (16:9 default)

Use one clean 16:9 sheet as a design master by default, but adapt the zones to the entity. The layout exists to make identity, form, and continuity easy to understand—not to fill a fixed checklist. Start by deciding which morphology or state is most important to the story, then allocate enough image area for it to read clearly.

Choose a layout pattern:

- **Fixed-form entity:** one dominant primary view; add only useful angle views, structure details, and a scale cue.
- **Multi-form / transforming entity:** give each story-critical form a clearly readable panel or zone. If transformation order matters, add a short left-to-right progression strip. Keep shared identity markers visible and consistent across forms.
- **Swarm / abstract entity:** prioritize the overall silhouette, how it is composed, one or two alternate configurations, and any visual signals that communicate awareness or emotion.

These patterns can be combined when the entity needs it. Omit redundant views and optional states; do not shrink a key form just to include every possible close-up.

## Optional Layout Grid (16:9)

```
┌────────────────┬──────────────────────────────────────┐
│                │                                      │
│                │       VIEW VARIATIONS / 三视图        │
│                │       (upper 1/2 of right area)       │
│                │                                      │
│  MAIN VISUAL   ├──────────────────────────────────────┤
│                │                                      │
│  ~1/3 width    │       DETAIL CLOSE-UPS               │
│  ~4/5 height   │       (lower 1/2 of right area)      │
│                │       AI-determined flexible grid     │
│                │       panel size adapts to count      │
│                │                                      │
├────────────────┴───┬──────────┬──────────┬───────────┤
│  Form Variation A  │ Form B   │ Form C   │ Emotion A │ Emotion B │ Emotion C │ ...
│                    ← forms first →         ← emotions →
│                         ~1/5 height, one horizontal row                       │
└─────────────────────────────────────────────────────┘
```

## Optional Panel Definitions

- **PRIMARY FORM / MAIN VISUAL** — give the most story-relevant form the largest area. Usually this is the default form; for a transformation-driven entity, a combat or alternate form may be equally important and deserve its own large panel. Include a short name/label only when it helps identify the design.

- **VIEW VARIATIONS** — use 2–3 angles of the same form only when they reveal useful 3D structure or continuity. These are views, not different morphologies.

- **STRUCTURE / DETAIL CLOSE-UPS** — show only signature components such as a core, sensory area, internal pattern, material boundary, or scale cue. Arrange panels flexibly; fewer useful details should receive larger panels.

- **FORM / STATE STRIP** — optional. Use for story-critical form changes or clearly different visual states. A short horizontal progression works when order matters. Emotion panels are optional and should show the same morphology with only the relevant visible signal changed; do not add them merely to fill space.

## Background & Dividers

All panels sit on a unified clean white or near-white background with thin dark divider lines. Labels appear under each panel in small, clean typography.

## Modular Prompt Composition

```
[Layout instruction: 16:9 entity design sheet; name the selected zones and panel order] +
[Entity identity and visible sentience cue] +
[Primary form or story-critical forms — describe silhouette, scale, materials, and behavior] +
[Optional useful views of the same form] +
[Optional structure details and scale reference] +
[Optional form/state progression, in narrative order if relevant] +
[Shared identity markers repeated consistently across forms] +
[Style and rendering controls]
```

## Key Rules

1. **Layout first, then visual priorities**: State the canvas, selected zones, and reading order before describing panel contents.
2. **Give key forms enough area**: A story-critical alternate form is not a tiny footnote. Multi-form entities may need co-primary panels.
3. **Views show angles, not forms**: Keep camera angle changes distinct from actual morphology changes.
4. **Repeat invariants across forms**: Describe the shared core, markings, or material pattern so the model visibly links the forms as one entity.
5. **Use state panels selectively**: Include emotion states only when they change visible features; keep the underlying morphology stable.
6. **Keep the sheet legible**: Prefer fewer larger details over a crowded grid. Use short labels only when they help identify a form or component.
7. **Unified clean background**: A white or near-white sheet background keeps the entity readable; add environmental context only when needed for scale or behavior.
