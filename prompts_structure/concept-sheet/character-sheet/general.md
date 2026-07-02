## Description
Use this architecture when the user wants to generate a **character concept design sheet** — a single 16:9 composite image that presents the character's full-body main look alongside viewing angles, facial expressions (joy/anger/sorrow/happiness), and all clothing items, accessories, scars, and birthmarks in a structured multi-panel layout. This is the "production reference" format: a one-page design document that gives a video model everything it needs to understand the character's visual range.

## Layout Grid (16:9)

```
┌────────────────┬──────────────────────────────────────┐
│                │                                      │
│                │       VIEW VARIATIONS / 三视图        │
│                │       (upper 1/2 of right area)       │
│                │                                      │
│  MAIN VISUAL   ├──────────────────────────────────────┤
│                │                                      │
│  ~1/3 width    │       EXPRESSIONS                    │
│  ~4/5 height   │       喜怒哀乐 4 expressions          │
│                │       (lower 1/2 of right area)       │
│                │       2×2 grid, shoulder-up or face   │
│                │                                      │
├────────────────┴───┬──────────┬──────────┬───────────┤
│  Jacket/Outerwear  │ Shirt    │ Pants    │ Boots    │ Accessories │ Scars/Marks │ ...
│                    ← one horizontal row, ~1/5 height                   │
│                    number of panels = all wearable + notable body marks │
│                    more items → smaller panels, fewer → larger          │
└──────────────────────────────────────────────────────┘
```

- **Main Visual** — top-left, 1/3 width × ~4/5 height. Full-body shot of the character in default outfit, neutral/resting expression, with name/label.
- **Right Upper — View Variations** — upper half of the right area. The same character shown from 2–3 different viewing angles (front, side, back, 3/4 perspective), showing the outfit and build from multiple directions.
- **Right Lower — Expressions / 喜怒哀乐** — lower half of the right area. Four shoulder-up or face-only panels in a 2×2 grid: **喜 (joy)**, **怒 (anger)**, **哀 (sorrow)**, **乐 (happiness)**. Face-only is preferred when the user provides detailed facial feature descriptions; shoulder-up when body language matters to the emotion.
- **Bottom Row** — full width, ~1/5 height. One continuous horizontal row. Every clothing item, accessory, and notable body feature displayed individually — jacket/coat, inner shirt, pants, shoes, rings/necklaces, scars, birthmarks, tattoos, etc. More items → smaller panels; fewer items → larger panels. The AI adjusts panel sizes to fit the count.

All panels sit on a unified clean white or near-white background (e.g., `#FAFAFA` or subtle paper texture), with thin dark divider lines. Labels appear under each panel in small, clean typography.

## Prompt Structure Formula

```
[Layout instruction] + [Character identity & name] +
[Panel 1: MAIN VISUAL — full body, default outfit, neutral expression] +
[Panel 2: VIEW VARIATIONS — 2-3 different camera angles] +
[Panel 3: EXPRESSIONS — joy / anger / sorrow / happiness, shoulder-up or face] +
[Panel 4: BOTTOM ROW — all clothing items, accessories, scars, birthmarks, one horizontal row] +
[Style suffix]
```

### Formula Components

| Component | Description | Key Info to Include |
|-----------|-------------|---------------------|
| **Layout instruction** | The grid specification | `16:9 character concept design sheet`, `main visual top-left 1/3 width and 4/5 height`, `right area split into upper half (view variations) and lower half (expressions: joy anger sorrow happiness in 2×2 grid)`, `bottom row full width 1/5 height: all clothing items, accessories, scars, and birthmarks displayed individually in one horizontal row`, `clean white background with thin dark panel dividers` |
| **Character identity & name** | Who this is | Character name, age, role/faction, a one-line archetype tag (e.g., "SHEN YE — 28, Office Worker turned Death Game Survivor") |
| **Panel 1: Main visual** | Full body, default outfit, neutral face, richest description | Complete visual description — facial features, hair, build/body type, full outfit from outer to inner to shoes, any visible accessories, default expression, standing posture. This is the largest rendered area; the richest description lives here. |
| **Panel 2: View variations** | 2–3 camera angles of the same default appearance | Each angle: (a) perspective label (front, back, side, 3/4), (b) what's visible from that angle — back view shows hair rear detail and jacket back design, side view shows profile and build thickness. Keep each ~1–2 sentences. |
| **Panel 3: Expressions** | 喜/怒/哀/乐, 2×2 grid, shoulder-up or face-only | Each expression: (a) the emotion label, (b) key facial changes — eyebrow position, eye shape, mouth, any wrinkles or tension areas, (c) how the eyes specifically change (e.g., "eyes crinkle at corners" for joy, "brows drawn down and together" for anger). Face detail from the character's facial description should be referenced here. |
| **Panel 4: Bottom row** | All wearable items + body marks, one row, AI-scaled | Each item in its own panel — coat/jacket, shirt, pants, shoes, ring, necklace, scar close-up, birthmark location. For clothing: show the item laid flat or on a mannequin fragment. For marks: a cropped body close-up with the mark visible. More items → smaller panels, fewer items → larger panels. |
| **Style suffix** | Rendering quality, art style | `cinematic character concept sheet`, `photorealistic 8K`, `game production character design reference`, aesthetic tag |

## Usage Notes
- **Layout first**: The grid instruction must come first. Go macro (zones) → micro (panel contents).
- **Main visual is the anchor**: ~4/5 height × 1/3 width is the hero panel. This paragraph should contain every visual signal the model needs to render the character accurately.
- **View variations are about silhouette and drape**: Side and back views reveal how the clothing hangs on the build, how the hair falls from behind, how thick the body reads in profile. These are production-critical details for a video model.
- **Expression panels must show clear facial contrast**: Joy (eyes crinkle, mouth corners up) vs Anger (brows down, jaw tight, nostrils flare) vs Sorrow (inner brows raised, mouth slightly open, eyes unfocused) vs Happiness (wide warm smile, eyes relaxed). Avoid "same face, slightly different mouth."
- **Bottom row = inventory display**: Think of it as the character's equipment screen. Each item gets its own panel. Clothing items can be shown laid flat or on a ghost mannequin. Scars and birthmarks should be cropped body close-ups with the mark clearly visible.
- **Item count drives panel size**: 4 items → fewer items (e.g., jacket + shirt + pants + boots) gets spacious panels. 8 items (adding ring, necklace, scar, birthmark) gets narrower panels. Tell the AI: "panel width adjusts to fit count."

## Scoring Rubric

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Layout clarity** | 1.2 | Is the grid structure clearly described — main visual, right halves, bottom inventory row? |
| **Character identity** | 1.0 | Does the sheet communicate who this character is, their build, face, and overall vibe at a glance? |
| **View coverage** | 1.0 | Are the viewing angles meaningful and do they reveal silhouette/drape information? |
| **Expression range** | 1.0 | Are 喜怒哀乐 visually distinct? Can the viewer tell joy from happiness, anger from sorrow? |
| **Wardrobe & marks completeness** | 0.8 | Are all clothing items, accessories, scars, and birthmarks accounted for and individually displayed? |

Total score = (sum of weighted scores) / (sum of weights) → 0–10.

## Common Issues & Adjustments
- **Expressions too subtle**: Video model references need CLEAR facial changes. Joy = visible smile + eye crinkle. Anger = visible brow furrow + jaw tension. Don't be subtle.
- **Bottom row missing items**: The user may describe a ring, scar, or birthmark in body text. Always scan for these and include them in the bottom row.
- **View variations bland**: If all 3 angles look the same, the panels waste space. Back view must show something the front doesn't — hair rear detail, jacket back seam, shoulder blade width.
- **Too many bottom-row items**: If the count exceeds 6, suggest grouping (e.g., "accessories" as one panel showing ring + necklace together) or trimming non-essential items.
- **Name label missing**: Include the character name visible near the main visual panel.

## Example Generation
**User input**: "Shen Ye, 28, office worker in a death game. Wide honest face, short black hair, Ma Dong-seok build, wears combat-adapted wedding suit with silver ring that flashes briefly. Has a faint childhood scar on his left forearm."

**Generated prompt**:  
```
16:9 character concept design sheet layout. The canvas has a clean white background with subtle paper-like texture and thin dark grid lines dividing the panels.

The top-left MAIN VISUAL panel occupies roughly one-third width and four-fifths height. It shows Shen Ye — 28, ordinary office worker turned death game survivor — full body standing in a neutral upright posture, relaxed but alert. Wide-set face with rounded cheekbones, a soft jawline, well-proportioned features that are pleasant but not striking — the honest, dependable face of an everyday man. Short black hair cleanly faded at the sides with a bit of length on top, bangs falling naturally across his forehead without covering the eyebrows. His build is surprisingly massive — roughly 182cm, broad-shouldered and thick-armed with a naturally thick powerful frame, the contrast between his honest ordinary face and his heavily built body striking and memorable. He wears a combat-adapted wedding suit: a deep charcoal suit jacket silhouette made from matte tactical fabric with subtle dark woven texture, the suit lapel preserved but the collar raised into a closed high-neck design, a white dress shirt collar peeking at the throat. Dark gray trousers with a visible crease line in the same tactical fabric. Black boots in a clean dress-shoe toe profile. The outfit is clean and intact. His expression is calm and neutral — the default resting face of a man who has accepted his situation. Small clean dark label text near the panel reads "SHEN YE — Default."

The right UPPER HALF contains VIEW VARIATIONS — 3 angles. FRONT VIEW: the full front as described in main visual. BACK VIEW: the jacket's back shows a clean center seam and subtle shoulder yoke detail in the tactical fabric, his short hair cleanly faded at the nape, the broad span of his shoulders and back emphasized from this angle, trousers with the crease line visible down the back of each leg. SIDE VIEW: his profile reveals the thickness of his build — deep chest, thick arms hanging with natural weight, the high-neck collar framing his jaw, the suit silhouette following his frame closely, the trouser crease running sharply down the side.

The right LOWER HALF contains EXPRESSIONS — 4 panels in a 2×2 grid, shoulder-up. Panel A — 喜 JOY: a warm genuine smile, eyes crinkling slightly at the corners, brows relaxed, the honest face becoming warm and approachable, a rare softening of his usually guarded expression. Panel B — 怒 ANGER: brows drawn sharply down and together, jaw clenched tight with visible muscle tension at the temples, eyes narrowed and intense, nostrils slightly flared, the dependable face turned hard and dangerous. Panel C — 哀 SORROW: inner brows raised and drawn together, eyes unfocused and staring through rather than at, mouth slightly parted, a quiet devastated stillness, the honest face vulnerable and raw. Panel D — 乐 HAPPINESS: a wide relaxed smile, eyes bright and fully engaged, the slight crinkle at the outer corners, an unguarded moment of genuine lightness, the face of someone who has briefly forgotten the weight he carries.

The BOTTOM ROW spans the full width at roughly one-fifth height — one horizontal line showing all wearable items and body marks, panel width adjusting to fit count. Panel 1 — JACKET: the charcoal tactical suit jacket laid flat, showing the high-neck collar, the suit lapel structure, the subtle dark woven texture of the matte combat fabric, the clean front closure. Panel 2 — SHIRT: the white tactical-fabric dress shirt laid flat, showing the classic collar and button placket, the fabric's micro-stretch weave visible up close. Panel 3 — TROUSERS: the dark gray tactical trousers laid flat, showing the sharp crease line, the elastic combat fabric texture, the suit-style waistband. Panel 4 — BOOTS: the black tactical boots, showing the clean dress-shoe toe profile and the combat-grade sole. Panel 5 — RING: a close-up of the plain silver ring, shown as a faint translucent glimmer as it appears for only a split second — a ghost of the proposal that never happened. Panel 6 — SCAR: a cropped close-up of the left forearm, showing a faint thin childhood scar running diagonally near the wrist.

Cinematic character concept sheet, photorealistic 8K, game production character design reference, Gantz-inspired tone.
```
