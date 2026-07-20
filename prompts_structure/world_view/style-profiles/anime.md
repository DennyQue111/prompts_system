# Anime Cinematic Style Profile

Overlay this profile when the user requests an anime animation, hand-drawn cinematic, or Gantz × Demon Slayer fusion aesthetic. Applies to all nine aspects.

## Style Fusion: Gantz × Kimetsu no Yaiba

- **Gantz DNA**: Hard high-contrast lighting, sharp cel-shaded shadows, realistic anatomy precision, cold blue system aesthetic, tactical gear rendered with hand-drawn detail, dramatic low angles, emotional weight in stillness
- **Demon Slayer DNA**: Expressive fluid linework, painterly atmospheric backgrounds, rich emotional color grading (warm amber nostalgia vs. cold blue isolation), water/energy effects drawn with organic brush-stroke quality, Japanese aesthetic sensibility in composition
- **Fusion result**: Hand-drawn anime keyframes with Gantz's harsh realism and hard shadows, rendered through Demon Slayer's expressive linework and emotional color language — not soft, not moe, not generic anime

## Capture Profile

```yaml
capture_medium_or_emulation: hand-drawn animation cel, anime keyframe still
lens_character: none — composition driven, not focal-length driven
aperture_or_depth_of_field_intent: shallow focus for emotional close-ups, deep focus for establishing shots — described as composition, not aperture
framing_device: 16:9 anime cinematic frame
motion_trace_in_still: speed lines, impact frames, brush-stroke motion trails
```

## Backbone Preset

Prepend to every prompt when this profile is active. Replaces any photographic backbone:

```
Anime cinematic keyframe still, hand-drawn animation rendering, Gantz-inspired hard cel shading with deep black shadows and high contrast, Kimetsu no Yaiba-inspired expressive linework and atmospheric color grading, detailed anime background art
```

**Component breakdown for understanding** (not to be included in prompt):
- `Anime cinematic keyframe still` → Signals "this is animation, not live-action"
- `hand-drawn animation rendering` → Pushes toward 2D anime aesthetic, away from 3DCG
- `Gantz-inspired hard cel shading with deep black shadows and high contrast` → Sharp shadow edges, high light/shadow ratio, anatomical precision
- `Kimetsu no Yaiba-inspired expressive linework and atmospheric color grading` → Fluid line quality, painterly color palettes, emotional color temperature
- `detailed anime background art` → Environments as painted backgrounds, not 3D sets

## Composition Language

**CRITICAL**: Never write focal lengths (24mm, 50mm, etc.) in anime prompts. Focal length is a photography concept that signals photorealism. Use composition descriptions instead:

| Live-Action Term | Anime Equivalent | When to Use |
|-----------------|------------------|-------------|
| 18–24mm ultra-wide | extreme wide establishing shot, expansive background painting | Landscapes, architecture scale, environment-dominant |
| 28–35mm wide | wide shot, character in environment | Groups, travel, world-building views |
| 40–50mm standard | medium shot, eye-level | General narrative, daily life, culture scenes |
| 65–85mm portrait | close-up, shallow focus, bokeh background | Portraits, emotional beats, intimate details |
| 100mm+ telephoto | compressed perspective, dramatic long shot | Distant giants, looming threats, compressed scale |

## Character Rendering (Replaces Skin Detail)

When a human character appears, append after the character's pose description. Completely replaces all photographic skin language:

```
hand-drawn anime character rendering with detailed cel shading, Gantz-style realistic facial proportions, expressive eyes with sharp highlights, subtle skin tone gradients, visible line art on facial contours
```

Skip for creature-only or environment-only shots.

## Lighting Language

Use anime shading terminology instead of photographic color temperature or Kelvin values:

| Photography Term | Anime Equivalent |
|-----------------|------------------|
| warm amber light, 3200K | warm amber cel shading, soft gradient from warm to cool |
| cool ambient, 5600K | cold blue ambient shading, cool color wash |
| rim light, backlight | sharp rim light line, backlit cel highlight, hair light edge |
| hard shadows, 8:1 ratio | hard cel shading, deep black shadows, sharp shadow edge, Gantz-style high contrast |
| soft diffused light | soft gradient shading, atmospheric bloom, gentle color transition |
| practical light source | visible on-screen light source, glowing object cast |

**Default lighting**: Hard cel shading with deep black shadows (Gantz), cold blue overall color temperature, occasional warm amber emotional accents (Demon Slayer).

## Negative Prompts

```
no photorealism, no photographic film grain, no live-action, no 3DCG render, no realistic human skin texture, no photographic lens blur, no flat moe anime style, no generic isekai anime, no chibi proportions
```

## MJ Parameters

```
--ar 16:9 --stylize 250 --v 8.1 --hd
```

**Note on Niji**: `--niji 6` produces purer anime/illustration output. For Gantz × Demon Slayer fusion, `--v 8.1` is recommended — it better handles the hybrid of hard realism (Gantz) and expressive anime (Demon Slayer). If results are too photographic, switch to `--niji 6`.
