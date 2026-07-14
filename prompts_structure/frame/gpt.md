## Description
GPT variant of single-frame cinematic still (frameRef / look reference). Same structure as `gemini.md`. Anti-noise is embedded in word choice.

**For Gemini** → use `gemini.md`. Full frame architecture → see `frame/gemini.md`.

## Prompt Formula (augmented)

```
[Subject + Action/Emotion] + [Composition + Focal length] +
[Lighting: source + color temp + ratio] +
[Atmosphere + color palette] +
[Style suffix]
```

## GPT Anti-Noise: Pre-Writing Checklist

Single frames have no context — the model has nothing to infer. Define explicitly:
1. Main surface material: what is the dominant visible surface?
2. Light response: matte/satin/glossy/wet/mirror?
3. Where are the contact shadows? (under chin, at collar, at object contact points, on ground plane)
4. What's in the background? Must specify texture level control.

## GPT Word Choice Guide

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed, 8K, hyper detailed | balanced detail |
| micro detail everywhere | selective detail on key surfaces |
| highly textured | controlled material rendering |
| photorealistic skin pores | natural facial planes, matte skin with soft specular highlights |
| cinematic bokeh | clean depth of field with smooth falloff |
| dark atmospheric background | smooth dark tones, clean shadow falloff |

## GPT Style Suffix (single frames)

Avoid elaborate camera-brand language on GPT:
```
16:9 cinematic still, [time of day], [light source description],
controlled color grading, clean atmosphere, smooth highlight rolloff
```

## Negative Prompt (frame-specific, short)

Tailor to frame content. Example for a character frame:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
waxy skin, dirty pore noise.
```

## Key Rules

1. **Frame composition**: same as gemini.md.
2. **Anti-noise is in word choice, not an appended block** — use the word choice table while writing. Negative prompt is short and scene-specific.
3. **Background must be explicitly controlled**: "clean smooth background" OR "clean shallow depth of field" — never left implied.
4. **Faces in single frames**: "natural facial planes, matte skin with soft specular highlights" — highest-risk area for dirty pore noise on GPT.
5. **Dark/atmospheric frames**: add "smooth dark tones with readable shadow detail."
6. **Check for repetition before output.**
7. Read `meta/gpt-image-hygiene.md` for full methodology.
