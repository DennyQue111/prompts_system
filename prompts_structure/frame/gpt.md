## Description
GPT variant of single-frame cinematic still (frameRef / look reference). Same structure as `gemini.md` with GPT anti-noise.

**For Gemini** → use `gemini.md`. Full frame architecture → see `frame/gemini.md`.

## GPT-Specific Modifications

### Prompt Formula (augmented)
```
[Subject + Action/Emotion] + [Composition + Focal length] +
[Lighting: source + color temp + ratio] +
[Material-light definition: primary surface + how it responds to light] +
[Atmosphere + color palette] +
[🧹 GPT Clean-Render Layer] +
[Style suffix]
```

### Material-Light Definition (REQUIRED for single frames)
Single frames have no context — the model has nothing to infer. Define explicitly:
1. Main surface material: what is the dominant visible surface?
2. Light response: matte/satin/glossy/wet/mirror?
3. Where are the contact shadows? (under chin, at collar, at object contact points, on ground plane)
4. What's in the background? Must specify texture level control.

### Clean Rendering Block (append to every prompt)
```
clean rendering, balanced detail, realistic detail only,
natural texture only, controlled material rendering,
clean gradients, controlled highlights,
[background: clean smooth background OR clean depth of field with smooth falloff],
minimal repetitive patterns.

Avoid: ghost texture, latent artifacts, hidden watermark-like marks,
repetitive micro-pattern noise, low-contrast residual textures,
dirty texture buildup, pasted-on texture, muddy shadows,
noisy bokeh, dirty AO halos, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks.
```

### GPT Style Suffix (single frames)
Single cinematic frames should avoid elaborate camera-brand language on GPT:
```
16:9 cinematic still, [time of day], [light source description],
controlled color grading, clean atmosphere, smooth highlight rolloff
```

### Key Rules
1. **Frame composition**: same as gemini.md.
2. **Every prompt must carry the Clean Rendering Block.**
3. **Background must be explicitly controlled**: "clean smooth background" OR "clean shallow depth of field" — never left implied.
4. **Faces in single frames**: "natural facial planes, matte skin with soft specular highlights" — single-frame face rendering on GPT is the highest-risk area for dirty pore noise.
5. **Dark/atmospheric frames**: add "smooth dark tones with readable shadow detail."
6. Read `meta/gpt-image-hygiene.md` for full methodology.
