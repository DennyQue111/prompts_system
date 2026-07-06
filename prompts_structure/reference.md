## Description
This is the cross-category style reference library. Each section provides reusable style snippets that can be appended to the end of any prompt across all concept types (character, entity, location, prop). Pick the style that best matches the creative vision requested by the user.

Currently applies to: Gemini 2.5 Flash Image, GPT image models.

---

## Section 1: Artistic Medium & Tradition

| Style Keyword                    | Effect Description                                                        | Best For                                 |
| -------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| `oil painting, impasto texture`  | Rich brush strokes, thick paint, classical fine-art look                  | Fantasy, historical, dramatic portraits  |
| `watercolor, soft washes`        | Delicate, translucent layers, gentle color transitions                    | Ethereal scenes, nature, dream sequences |
| `ink wash painting, sumi-e`      | Bold ink strokes, negative space, East Asian aesthetic                    | Martial arts, zen landscapes, calligraphy |
| `pencil sketch, charcoal`        | Monochrome, textured, unfinished feel                                     | Concept exploration, moody studies       |
| `digital painting, smooth render`| Clean, polished, modern concept-art finish                                | Sci-fi, game art, character sheets       |
| `gouache, matte opacity`         | Flat color blocks, poster-like, mid-century illustration                  | Graphic novel, editorial illustration    |

## Section 2: Rendering & Quality

| Style Keyword                                    | Effect Description                                                       | Best For                                 |
| ------------------------------------------------ | ------------------------------------------------------------------------ | ---------------------------------------- |
| `photorealistic, 8K, DSLR`                       | Hyper-real, lens-accurate detail and texture                             | Props, real-world objects, product shots |
| `cinematic lighting, anamorphic lens`             | Film-like depth, lens flares, 2.35:1 widescreen feel                     | Characters, epic locations               |
| `concept art, key shot, artstation`               | Polished game/film concept art with strong silhouette and rim light       | Any concept piece                        |
| `matte painting, epic scale`                      | Expansive, highly detailed backgrounds with atmospheric depth             | Locations, establishing shots            |
| `macro photography, shallow depth of field`       | Extreme close-up, blurred background, fine texture emphasis              | Props, details                           |
| `studio lighting, product photography`            | Clean, evenly lit, catalog-ready look                                    | Props, neutral reference images          |

## Section 3: Aesthetic Movements & Vibes

| Style Keyword                               | Effect Description                                                      | Best For                                  |
| ------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------- |
| `cyberpunk, neon noir`                      | High-contrast neon, rain, chrome, dystopian                             | Sci-fi characters, futuristic locations   |
| `steampunk, Victorian industrial`           | Brass, gears, leather, steam, sepia tones                               | Retro-futuristic props, characters        |
| `Ghibli style, lush and whimsical`          | Soft, painterly, nature-infused, warm                                   | Fantasy locations, gentle characters      |
| `film noir, black and white, chiaroscuro`   | Stark shadows, venetian blinds, moody                                   | Detective characters, suspense locations  |
| `vaporwave, retro synthwave`                | Purple/pink gradients, grid lines, sunset, 80s chrome                   | Stylized locations, album-art characters  |
| `dark fantasy, grimdark`                    | Desaturated, oppressive, gothic, harsh                                  | Dark lords, haunted locations             |
| `solarpunk, bright eco-futurism`            | Green overgrowth, clean tech, warm sun, hopeful                         | Utopian locations, nature-tech hybrids    |
| `baroque, dramatic chiaroscuro`             | Deep shadows, golden highlights, theatrical                             | Historical characters, opulent interiors  |

## Section 4: Color Palettes

| Style Keyword                    | Palette Description                                       |
| -------------------------------- | --------------------------------------------------------- |
| `monochromatic blue, cold tones` | Single-hue blue range, icy, clinical, melancholic         |
| `warm amber and gold`            | Sunset tones, firelit, cozy, magical                      |
| `desaturated, muted earth tones` | Washed-out greens and browns, gritty, grounded            |
| `neon pink and cyan`             | High-contrast synthwave, vibrant, electric                |
| `pastel, soft and airy`          | Light pinks, lavenders, baby blues, gentle and dreamy     |
| `high contrast, deep blacks`     | Crushed shadows, bright highlights, dramatic tension      |

## Section 5: Camera & Lens Reference

| Style Keyword                                   | Effect                                                  |
| ----------------------------------------------- | ------------------------------------------------------- |
| `wide angle lens, deep depth of field`          | Expansive scene, everything in focus                    |
| `telephoto lens, compressed perspective`        | Distant subject, flattened space, cinematic             |
| `tilt-shift, miniature effect`                  | Toy-like, selective focus, whimsical                    |
| `fisheye lens, distorted`                       | Exaggerated perspective, immersive, surreal             |
| `dutch angle, off-kilter`                       | Uneasy, dynamic tension                                 |
| `overhead flat lay, top-down`                   | Bird's eye, organized composition (great for props)     |

### Lens Focal Length Quick Reference (from MOKEAIGC V9)

When writing prompts for image models that understand lens terminology, include a specific focal length for stronger composition control:

| Focal Length | Visual Characteristic | Best For |
|-------------|----------------------|----------|
| `18-24mm` (ultra-wide) | Strong perspective exaggeration, stretched edges, dramatic depth | Epic landscapes, narrow interiors, environment-dominating-subject shots |
| `28-35mm` (wide) | Environmental storytelling, natural presence, slight perspective | Architecture panoramas, group/migration shots, documentary-style daily life |
| `40-50mm` (standard) | Near-human-eye, neutral perspective | General narrative shots, single character with environment, balanced mid-shots |
| `65-85mm` (medium telephoto) | Mild compression, pleasing bokeh, subject separation from background | Portraits, facial close-ups, intimate single-character, shallow-DOF emotional shots |
| `100-135mm` (telephoto) | Strong compression, very shallow DOF | Distant subject close-ups, compressing giant objects with people, isolation details |
| `135mm+` (super-telephoto) | Extreme compression and blur | Distant giants pulled close, layered silhouette compression |

**Mapping to concept types (default starting points):**

| Concept Type | Default Focal Length | Rationale |
|-------------|---------------------|-----------|
| Character main visual | `50mm` or `85mm` | Natural presence or flattering portrait compression |
| Character expressions | `85mm` | Tight face shots, soft background separation |
| Entity (sentient being) | `24-35mm` or `100mm+` | Either sweeping wide for scale, or tight telephoto for detail |
| Location (environment) | `18-28mm` or `135mm` | Ultra-wide for scale, or super-telephoto for compressed distant features |
| Prop (object) | `50mm` or `85mm` | Neutral reference or dramatic hero shot |

---

## Section 6: CG & Anime Styles (ComfyUI / 即梦 / 豆包 Compatible)

For platforms with strict realism/person filters (即梦, 豆包), using a clearly non-photorealistic 3D CG or anime style passes different moderation paths:

| Style Keyword | Effect Description | Best For |
|--------------|-------------------|----------|
| `3D CG anime cinematic render, GANTZ:O (2016) style, Unreal Engine 5 quality` | Dark sci-fi 3D anime, glossy surfaces, dramatic lighting, cel-shaded faces on detailed 3D models | Dark sci-fi, tactical combat, death game settings |
| `3D CG anime film, cel-shaded characters, smooth anime skin, raytraced reflections` | Clean CG anime look with subsurface scattering on skin, ambient occlusion | Characters that need to look intentionally "not real" |
| `Japanese 3D anime movie style, detailed character models, volumetric lighting` | High-end anime film look with depth and atmosphere | Emotional character moments, dramatic lighting scenes |
| `anime concept art sheet, clean linework, cel shading, flat color blocks` | 2D anime reference sheet aesthetic | Character design sheets, turnarounds |
| `Studio Orange 3D anime style, dynamic camera, expressive lighting` | Modern 3D anime (Beastars, Land of the Lustrous) with strong cinematography | Action sequences, dramatic character introductions |

**When to use Section 6 over Section 1-2:**
- The target platform is 即梦 or 豆包 (strict human realism filters)
- The project direction is intentionally 3D CG anime (like GANTZ:O) rather than photorealistic
- The user wants to avoid deepfake/escalation flags on Chinese AI image platforms

---

## Usage Tips
- **Layer styles**: Combine a medium, a quality, and a vibe for richer results.  
  Example: `oil painting, cinematic lighting, dark fantasy` — each layer adds dimension without redundancy.
- **Don't overstack**: 2–3 style keywords are usually enough. Four or more can confuse the model.
- **Match the subject**: Gritty styles suit props and dark locations; soft styles suit ethereal characters.
- **Test variations**: When evaluating which model to use for a project, generate the same prompt with different style suffixes to compare outputs.
