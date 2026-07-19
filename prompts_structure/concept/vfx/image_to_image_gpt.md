## Description

Use this architecture when generating **VFX (visual effects) concept design sheets** with GPT image models. VFX differs from entities, characters, and locations in that it is inherently dynamic — VFX elements are not static objects but phenomena that undergo form, material, and spatial transformations over time.

This file covers **image-to-image** generation where the user provides reference images (spatial layout, style reference, or existing concept art) and GPT produces a VFX concept design sheet.

**For text-to-image without reference images** → use `text_to_image_gpt.md` (if created). **For Gemini** → use `image_to_image_gemini.md`.

---

## Reference Image Handling

VFX concepts often rely on existing references for visual DNA extraction. Key distinction from entity/character references:

| Reference Type | What It Anchors | What It Does NOT Anchor |
|----------------|-----------------|------------------------|
| **Spatial layout reference** | EXACT placement, scale, and spatial relationship of the VFX element within the frame | Material, color, lighting, animation timing |
| **Style / mood reference** | Visual DNA: palette, atmosphere, light behavior, rendering style | Specific form, geometry, or composition |
| **Existing concept / entity reference** | Form logic, material properties, structural behavior | Final composition, camera angle, environment context |
| **Blockout / wireframe** | EXACT position, size, and boundary of the VFX area in frame | Style, material, animation |

**Critical rules:**
- Reference image descriptions must be minimal. State what the image is and what it anchors, but do not repeat spatial details or material descriptions that belong in the VFX content block.
- When a spatial layout reference is provided, the text prompt MUST NOT describe spatial relationships — the image is the sole authority on WHERE the VFX sits; text controls WHAT the VFX looks like and HOW it behaves.
- Avoid directional vocabulary ("横向", "对角", "右侧") when describing motion of reference-locked elements. Use "沿当前方向" or "基于参考图中已有的位置关系" instead.

---

## Prompt Formula (VFX-specific)

```
[Reference anchoring: explicit boundaries for each uploaded image] +
[VFX type / function: what does this effect do?] +
[Form & structure: geometry, layers, internal architecture] +
[Materials & textures: surface properties, light response, transparency] +
[Behavior / animation logic: how does it form, sustain, and dissolve?] +
[Scale & spatial presence: size, depth, relationship to environment] +
[Environment / context: where does it appear, what surrounds it] +
[Style suffix]
```

### VFX Content Components

| Component | Description | Key Decisions |
|-----------|-------------|---------------|
| **VFX type / function** | What is the narrative purpose? Portal? Energy burst? Dissolution? Reformation? | Portal = threshold transition. Dissolution = matter-to-energy. Reformation = energy-to-matter. |
| **Form & structure** | Geometry at each stage: formation → stable state → dissolution. Layered or monolithic? | Multi-layer VFX reads as more sophisticated: outer shell → active zone → core. |
| **Materials & textures** | Surface properties at each stage. Does the material change during the animation? | Liquid → solid = condensation. Solid → liquid = melting/dissolution. Energy = emissive/transparent. |
| **Behavior / animation logic** | How does it form? How does it sustain? How does it dissolve? What is the timing? | Formation: explosive, gradual, or triggered? Sustain: pulsing, stable, or chaotic? Dissolution: fade, collapse, or dispersal? |
| **Scale & spatial presence** | Size relative to human figures. Depth — does it occupy 3D space or is it a 2D surface effect? | Human-scale VFX = intimate. Building-scale = awe. Volumetric = immersive. Planar = decorative. |
| **Environment / context** | Where does it appear? Indoors/outdoors? Day/night? What is the background contrast? | High contrast background = VFX pops. Low contrast = VFX blends. Wet/dusty environments catch VFX light. |

---

## VFX Lifecycle States

Most VFX elements exist in three states. Define all three explicitly:

| State | Description | Prompt Keywords |
|-------|-------------|-----------------|
| **Formation** | How the VFX initiates | "cubes converge from scattered positions", "liquid surface tension breaks", "energy arcs branch outward from center" |
| **Sustain / Active** | The stable or pulsing phase | "cubes orbit in slow precise rotation", "liquid churns with deep blue electrical arcs", "core emits steady cold blue glow" |
| **Dissolution / Transition** | How the VFX ends or transforms | "cubes scatter outward in radial burst", "liquid drains inward through collapsing aperture", "energy fades to residual embers" |

**If the VFX involves matter transformation** (human → liquid → human), define the transition boundary explicitly: what is the transition point? Is it gradual (fingertips first) or instantaneous? Does the matter pool on the ground or suspend in air?

---

## GPT Anti-Noise: Pre-Writing Checklist

Define before writing (do NOT output to model):
1. Primary material at each lifecycle stage + how it responds to light: matte/glossy/translucent/emissive/metallic/rough/liquid
2. Contact shadows: between VFX and ground, between layered VFX components
3. What surfaces should be clean/flat vs detailed? (Energy surfaces are most vulnerable to dirty noise)
4. VFX-to-background boundary: crisp edge / soft glow / volumetric fade / refractive distortion
5. Animation timing: fast (explosive) vs slow (organic) — this affects blur, motion streaks, and particle behavior

## GPT Word Choice Guide

| ❌ Avoid | ✅ Use in description |
|---|---|
| ultra detailed | balanced detail |
| micro detail on all surfaces | selective detail on key structural features |
| highly textured | controlled material rendering |
| photorealistic surface | natural material rendering |
| dark atmospheric void | smooth dark tones, low texture background |
| hyper detailed energy | clean gradients, smooth light falloff |

## Negative Prompt (VFX-specific, short)

Tailor to VFX type. Example for energy/portal VFX:
```
Avoid: ghost texture, latent artifacts, repetitive micro-pattern noise,
dirty texture buildup, muddy shadows, uniform plastic gloss,
milky reflections, clipped highlights, crushed blacks,
chaotic particle soup, oversaturated bloom, wispy smoke filler.
```

---

## Key Rules

1. **VFX is dynamic — describe all three lifecycle states** (formation, sustain, dissolution) even if the concept sheet only shows one key frame.
2. **Material transformation must specify transition boundary**: what changes first, what changes last, and what the intermediate state looks like.
3. **Anti-noise is in word choice, not an appended block** — use the word choice table while writing. Negative prompt is short and scene-specific.
4. **Energy/liquid surfaces**: "smooth gradients, clean light falloff" — these surfaces are most vulnerable to dirty noise on GPT.
5. **Reference image descriptions must be minimal** — state what the image anchors, but do not repeat spatial or material details in the reference line.
6. **Avoid directional vocabulary when describing motion of reference-locked elements.**
7. **Check for repetition before output.**
8. Read `meta/gpt-image-hygiene.md` for full methodology.
