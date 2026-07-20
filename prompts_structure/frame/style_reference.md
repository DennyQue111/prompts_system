# Style Reference — Frame Style Palette Library

> **Purpose:** A palette of visual DNA templates for frame generation across any platform (Midjourney / ComfyUI / 即梦 / 豆包). This file is a **reference library** — consult it when you need to pick a style for a project, but do not treat any single palette as a universal default.
>
> **Always verify against the project's confirmed visual direction before selecting.** For 《复生协议》, the direction is GANTZ:O 3D CG anime → use Section 2 palettes.

---

## Section 1: Film Stock Palettes (Photorealistic)

Use when the project direction is live-action/cinematic photorealism. Applies to Midjourney, Stable Diffusion, or ComfyUI photorealistic workflows.

### Film Stock & Texture

| Descriptor | Effect | Best For |
|-----------|--------|----------|
| `Kodak Vision3 500T` | Fine grain, wide latitude, natural skin tones, slight warmth in shadows | Cinematic drama, character-driven scenes |
| `Kodak Portra 400` | Soft grain, pastel-leaning, gentle contrast | Memory, nostalgia, warmth |
| `Fuji Eterna 250D` | Cool shadows, neutral palette, smooth skin | Sci-fi, clinical, modern |
| `35mm film grain` | Classic cinematic texture, organic noise | General film look |
| `16mm film grain` | Heavier grain, documentary rawness | Gritty, found-footage, realism |
| `IMAX 70mm grain` | Ultra-fine grain, epic scale, maximum detail | Landscapes, establishing shots |

### Format & Aspect Ratio

| Descriptor | Effect |
|-----------|--------|
| `IMAX 70mm` | Massive frame, microscopic detail, sweeping scale |
| `anamorphic 2.35:1` | Wide cinematic canvas, horizontal lens flares, oval bokeh |
| `16:9 digital cinema` | Clean, modern, neutral format |
| `4:3 academy ratio` | Vintage, intimate, boxed-in feel |

### Color Palette

| Descriptor | Emotional Function |
|-----------|-------------------|
| `desaturated natural tones, steel white and warm brown dominant` | Gritty realism, grounded sci-fi |
| `cold blue and deep black, high contrast` | Dread, isolation, clinical cold |
| `warm amber and gold, soft highlights` | Memory, safety, hope |
| `teal and orange, blockbuster grade` | Action, energy, mainstream cinematic |
| `monochrome near-black, faint green cast` | Cyberpunk, digital, synthetic |
| `bleached bypass, silver retention` | War, despair, harsh reality |

### Camera Language

| Descriptor | Effect | Best For |
|-----------|--------|----------|
| `documentary handheld feel` | Slight instability, human presence, immediacy | Chase, chaos, POV urgency |
| `locked-off tripod` | Absolute stillness, cold precision | Surveillance, clinical, god's-eye |
| `steadicam float` | Smooth weightless motion | Dream, afterlife, grace |
| `snorricam POV` | Subject fixed center, world moves | Disorientation, protagonist experience |
| `dolly zoom / vertigo effect` | Background compresses, foreground stays | Revelation, psychological shift |

### Film Palette Templates

Quick-start presets. Append as a suffix block to the content prompt.

**Documentary Realism:**
`Kodak Vision3 500T, IMAX 70mm grain, desaturated natural tones — steel white and warm brown dominant, documentary handheld feel`

**Cold Sci-Fi:**
`Fuji Eterna 250D, anamorphic 2.35:1, cold blue and deep black high contrast, locked-off tripod precision`

**Memory / Flashback:**
`Kodak Portra 400, 16mm film grain, warm amber and gold soft highlights, steadicam float`

**Cyberpunk:**
`anamorphic 2.35:1, monochrome near-black with faint green cast, neon accent spill, snorricam urgency`

**War / Aftermath:**
`16mm film grain, bleached bypass silver retention, desaturated earth tones, documentary handheld feel`

---

## Section 2: CG & Anime Palettes

Use when the project direction is 3D CG anime (GANTZ:O, Studio Orange) or Japanese anime film style. Works on Midjourney, ComfyUI, 即梦, 豆包.

For platforms with strict realism/person filters (即梦, 豆包), using a clearly non-photorealistic 3D CG or anime style passes different moderation paths.

### Anime Palette Templates

**GANTZ:O CG Anime:**
`3D CG anime cinematic render, GANTZ:O (2016) style, Unreal Engine 5 quality, cel-shaded characters, detailed 3D environment models, dark sci-fi aesthetic, Japanese CG anime film, dramatic cinematic lighting, glossy surfaces with raytraced reflections`

**Japanese 3D Anime Film:**
`Japanese 3D anime movie style, cel-shaded characters, smooth anime skin with subsurface scattering, detailed character models, volumetric lighting, ambient occlusion, cinematic depth`

**Studio Orange Style:**
`Studio Orange 3D anime style, dynamic camera, expressive lighting, cel-shaded characters with detailed facial animation, atmospheric depth, modern CG anime cinematography`

### Anime Style Keyword Reference (from reference.md Section 6)

| Style Keyword | Effect | Best For |
|--------------|--------|----------|
| `3D CG anime cinematic render, GANTZ:O (2016) style, Unreal Engine 5 quality` | Dark sci-fi 3D anime, glossy surfaces, dramatic lighting, cel-shaded faces on detailed 3D models | Dark sci-fi, tactical combat, death game |
| `3D CG anime film, cel-shaded characters, smooth anime skin, raytraced reflections` | Clean CG anime with subsurface scattering, ambient occlusion | Characters that need to look "not real" |
| `Japanese 3D anime movie style, detailed character models, volumetric lighting` | High-end anime film with depth and atmosphere | Emotional character moments, dramatic lighting |
| `anime concept art sheet, clean linework, cel shading, flat color blocks` | 2D anime reference sheet aesthetic | Character design sheets, turnarounds |
| `Studio Orange 3D anime style, dynamic camera, expressive lighting` | Modern 3D anime with strong cinematography | Action sequences, dramatic character intros |

---

## Usage

1. **Determine the project's visual direction** (photorealistic? CG anime? hand-drawn anime?)
2. **Pick the palette that matches** from Section 1 (film) or Section 2 (anime)
3. **Append the palette** after content components, before platform-specific parameters:

```
[Content: shot type + subject + lighting + depth + environment + camera + composition + atmosphere] +
[Style Palette: selected from this reference] +
[Platform parameters: --ar 16:9 --style raw --s XXX --v X.X for MJ, etc.]
```

### Platform Notes

- **Midjourney + Anime:** Use `--s 200–300` (anime needs more stylization than photorealism)
- **即梦 / 豆包 + Characters:** Use Section 2 CG anime palettes to avoid realism-filter flags
- **ComfyUI:** Adapt palette keywords into the positive prompt; add anime-related negative prompts for photorealistic workflows and vice versa

### ⚠️ Rules

- **Never default to a film stock palette** just because the platform is Midjourney — match the palette to the creative intent
- **Check the project's confirmed visual style** before every frameRef generation
- **One palette per project** for visual consistency — don't mix Documentary Realism and GANTZ:O in the same film
