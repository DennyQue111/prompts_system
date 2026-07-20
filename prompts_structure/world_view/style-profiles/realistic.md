# Realistic Cinematic Style Profile

Overlay this profile when the user requests a live-action, photographic, or realistic cinematic world-view rendering. Applies to all nine aspects.

## Capture Profile

```yaml
capture_medium_or_emulation: photographic film emulation
lens_character: Cooke anamorphic, smooth roll-off, organic bokeh
aperture_or_depth_of_field_intent: shallow when subject is human-scale, deep for landscapes
framing_device: 16:9 letterbox cinematic
motion_trace_in_still: natural motion blur, no shutter artifacts
```

## Backbone Preset

Prepend to every prompt when this profile is active:

```
A cinematic photograph, shot on an Arri 65mm camera with Cooke anamorphic lenses, analog film stock, natural film grain, cinema-grade color grading
```

Replaces V11's adaptive `capture_profile`. Only apply when user explicitly selects this style or when photographic realism is clearly the intent.

## Focal Length Conventions

Use explicit focal length references. Select based on aspect type:

| Aspect Type | Default Focal Length | When to Use |
|-------------|---------------------|-------------|
| Establishing (Landscape, Architecture) | 18–28mm | Vast scale, environment-dominant |
| Human-scale (Daily Life, Inhabitants) | 35–50mm | Natural perspective, eye-level |
| Detail / Intimate (Portrait, Culture) | 65–85mm | Shallow focus, emotional compression |
| Distant scale (Creatures, Power) | 100–135mm | Compression, looming threat |

Express as: `shot on a 24mm wide lens` / `shot on a 50mm standard lens` / `shot on an 85mm portrait lens`.

## Skin & Human Texture

When a human face is clearly visible at close range, append after the character description:

```
real human detailed natural looking skin and textures, visible pores, freckles, fine lines, natural skin imperfections, subtle facial peach fuzz, authentic human skin characteristics
```

Skip for distant figures, silhouettes, masks, non-human beings, or faces that cannot resolve that detail.

## Lighting Language

Use photographic terminology (color temperature, light source type, light ratios):

| Concept | Phrasing |
|---------|----------|
| Warm interior light | warm amber light, 3200K color temperature, tungsten practical |
| Cool daylight/ambient | cool ambient light, 5600K, overcast sky soft fill |
| Rim / backlight | rim light, backlit edge, hair light separation |
| Hard shadows | hard shadows, 8:1 contrast ratio, chiaroscuro lighting |
| Soft diffused light | soft diffused window light, overcast flat fill, 2:1 contrast |
| Practical source | practical light source in frame, motivated single-source |

**Default for world-view**: dramatic cinematic lighting with motivated sources, 3-point lighting language where appropriate.

## Negative Prompts

```
no clean digital sharpness, no CGI look, no poster composition, no centered portrait, no black bars, no letterbox, no 3D render aesthetic
```

## MJ Parameters

Default per aspect:

- Establishing (Landscape, Architecture): `--ar 16:9 --style raw --s 200 --q 2 --v 6.1`
- Human-scale (Daily Life, Inhabitants, Travel): `--ar 16:9 --style raw --s 150 --q 2 --v 6.1`
- Detail (Creatures, Culture, Portrait, Power): `--ar 16:9 --style raw --s 100 --q 2 --v 6.1`

Higher stylization for atmosphere, lower for clean reference.
