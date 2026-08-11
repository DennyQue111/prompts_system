## Description

Use this architecture when generating a **single cinematic frame for Midjourney with reference images** — whether character concepts, location concepts, lighting references, or blockout layouts.

Unlike the base `midjourney.md` (text-only), this file covers the i2i workflow: how to upload reference images to Midjourney, which upload slot to use for each reference type, and how to structure the prompt when visual anchors are present.

**Pre-requisite:** Read [`meta/prompt-hygiene.md`](meta/prompt-hygiene.md) before writing any prompt. The eight cross-cutting rules and the four-question self-check apply to all platforms including Midjourney.

---

## Midjourney Reference Image Types (Web UI)

Midjourney's web interface provides three ways to use uploaded images. Each has a different effect on the output:

| Upload Slot | What It Does | Best For | Risk |
|-------------|--------------|----------|------|
| **Image Prompt** | Uses the image as a visual seed. Strongly influences composition, subject pose, color, and layout. The model treats it as "start from this image." | Previous frame variations, prop exact reproduction, specific composition you want copied | Overwhelms text instructions; locks pose and camera angle from the reference |
| **Style Reference** (`--sref`) | Extracts ONLY visual style DNA: palette, brushwork texture, light ratio, atmospheric treatment. Does NOT copy subjects, objects, or composition. | Location concept (environment palette), lighting reference, mood board | Low risk; safest reference type |
| **Omni Reference** (`--cref` / Character Reference) | Locks character identity (face, hair, body type, outfit, skin tone) while allowing new pose, camera angle, and environment. | Character concept, exact character reproduction across multiple frames | May not perfectly capture every detail; works best with a clear frontal character image |

### How to Assign Reference Images

| Reference Image Type | Upload Slot | Why |
|----------------------|-------------|-----|
| Character concept (face, body, outfit) | **Omni Reference** | Locks identity without locking pose. The character can appear in new actions and angles. |
| Location / environment concept | **Style Reference** | Adopts the environment's color palette, ground texture, sky tone, and light quality without copying specific landmarks. |
| Previous frame (same scene, new angle) | **Image Prompt** OR **Omni Reference** | Image Prompt if you want composition continuity; Omni Reference if you only want character consistency and text controls the new angle. |
| Blockout / layout / camera angle sketch | **Image Prompt** with caution | MJ is unreliable at reading spatial geometry from blockouts. Prefer describing camera angle in text and avoid uploading wireframe/blockout images. |

**Critical rule:** Do NOT upload a blockout/layout image as Image Prompt expecting exact spatial reproduction. MJ often misreads geometric relationships, converts flat intersections into overpasses, or ignores directional intent. When precise layout is required, rely on **text description of camera angle and composition** instead.

---

## How to Use Reference Images

### Method 1: Midjourney Web UI (Recommended)

The web interface at `https://www.midjourney.com/imagine` handles references automatically:

1. In the prompt box, click the **+** or image upload button.
2. Select your local reference image(s) from storage.
3. After uploading, each image appears in the prompt area with a dropdown menu in its top-right corner.
4. Click the dropdown and select the reference type:
   - **Omni Reference** — for character identity locking
   - **Style Reference** — for environment/style DNA extraction
   - **Image Prompt** — only if you want the model to start from this exact composition
5. The web UI automatically generates the URL and appends the correct parameter (`--cref`, `--sref`, or image prompt).
6. Type or paste your text prompt, set parameters, and send.

**You do NOT need to manually copy image URLs.** The web UI handles URL insertion and parameter formatting automatically.

### Method 2: Discord (Manual URL)

If using Discord instead of the web UI:
1. Drag and drop your reference image into any channel and send.
2. Right-click the uploaded image → **Copy Link**.
3. Paste the URL into your prompt in the correct position (see URL Placement Rules below).

### URL Placement Rules (Discord / Manual Only)

| Reference Type | Where the URL Goes |
|----------------|-------------------|
| Image Prompt | At the very beginning of the prompt text, before any words. `[URL] [URL] prompt text...` |
| Style Reference (`--sref`) | At the end of the prompt as a parameter: `--sref [URL]` |
| Omni Reference (`--cref`) | At the end of the prompt as a parameter: `--cref [URL]` |

Manual combination example:
```
[Image Prompt URL] prompt text... --cref [Character URL] --cw 100 --sref [Scene URL] --sw 50 --ar 16:9 --v 6.1
```

**Web UI users:** Skip this section. The interface handles placement automatically after you select the reference type from the dropdown.

---

## Prompt Structure with References

Midjourney prompts are a **single continuous block of English text** — not segmented with Chinese headers, bullet points, or labeled sections. The model reads the prompt as a flat string; inserting labels like "【风格锚定】" or "核心风格锚定：" pollutes the prompt and reduces quality.

**Correct output format:** one flowing English paragraph (or several comma-separated phrases). Line breaks are allowed for human readability but do not add headers, tags, or annotations inside the prompt text.

**Recommended content order** (MJ weights the beginning of the prompt most heavily):

```
[Style Palette — MUST lead the prompt to anchor the visual DNA] +
[Shot type + camera angle + composition] +
[Subject + Action/Emotion] +
[Lighting] +
[Depth layers: foreground → midground → background] +
[Environmental dynamics: wind, particles, motion cues] +
[Environment + Atmosphere + color palette]
```

**Why style first?** Midjourney reads left-to-right with declining weight. If you describe a photorealistic human face before mentioning "2D anime," the model may already be locked into realism by the time it reaches the style instruction. Lead with `polished 2D anime key visual illustration, NO photorealistic, NO 3D render` to set the visual DNA immediately.

**Why add environmental dynamics?** Wind, dust motes, swaying grass, and hair movement do three things: (1) they make a still frame feel alive, (2) they visually connect the character to the environment through shared motion, and (3) they add atmospheric depth layers (floating particles in sunbeams create natural depth separation). In a desert/gobi setting, `a constant dry wind blows across the desert` with `hair strands blowing in the wind` and `scattered dry grass swaying` transforms a static pose into a cinematic moment.

**Camera angle locking tricks:** MJ V8 tends to "interpret" camera instructions creatively. To force compliance:
- State the angle **twice** — once near the start (after style) and once at the very end of the prompt.
- Use explicit negation inside the prompt: `extreme low angle, NOT selfie, NOT top-down, NOT eye-level`.
- Lower stylize value: `--s 100` makes MJ follow instructions more literally; `--s 200+` gives it more creative freedom to drift.
- Add unwanted angles to `--no`: `--no selfie, high angle, top-down view, overhead shot, eye-level portrait`.

**Note:** When using the Web UI with uploaded references, you do NOT manually add `--cref [URL]` or `--sref [URL]` to the text prompt. The web interface injects these automatically based on your dropdown selections. Only add standard parameters and control weights to the parameter panel or text end:
- **V6:** `--cw 100 --sw 50 --ar 16:9 --style raw --s 200 --v 6.1`
- **V7/V8:** `--sw 50 --ar 16:9 --style raw --s 200 --v 8.2` (Omni Reference no longer needs `--cw`)

### Control Weights

| Parameter | Function | Default | Recommended | V7/V8 Note |
|-----------|----------|---------|-------------|------------|
| `--cw 0–100` | Character Weight for `--cref` (V6 only). 100 = strict identity lock. 0 = only face. | 100 | 100 for exact reproduction | **Removed in V7/V8.** Omni Reference automatically applies maximum character locking without this parameter. |
| `--sw 0–1000` | Style Weight for `--sref`. Higher = stronger style influence. | 100 | 50–100 for subtle style DNA; 200–300 for strong mood adoption | Still valid in V7/V8. |

---

## Negative Constraints in Midjourney

Midjourney supports `--no` for negative prompting, but it behaves differently than GPT/Stable Diffusion negative prompts:

- `--no` tells MJ to "try to remove or reduce" the listed concepts. It is NOT a hard ban.
- MJ is generally better at understanding what you **do** want than what you **don't** want.
- Community usage varies; many experienced users prefer **positive-only prompting** and rely on precise description to steer away from unwanted elements.

### When to Use `--no`

Use `--no` sparingly for **specific concrete objects** that keep appearing despite positive description:
```
--no clouds, modern buildings, cars, text, watermark
```

### When NOT to Use `--no`

| Scenario | Better Approach |
|----------|----------------|
| Avoiding "3D render" or "photorealistic" | Describe the desired style positively in the Style Palette block instead |
| Avoiding "sketch quality" | Write `polished finished illustration, NO sketch lines` inside the main prompt |
| Avoiding clothing on upper body | Describe what IS there (`broad shoulders, defined abs visible`) rather than `--no shirt` |
| Avoiding edge glow / pasted look | Write `subject physically grounded, sharp contact shadows, no edge glow separating from background` in the main prompt |

### Recommended Approach for This Project

**Prefer positive description over `NO` exclusion.** Empirical testing shows that Midjourney often misinterprets negative terms or gives them unintended weight. Instead of `NO photorealistic, NO 3D render`, rely on strong positive style anchoring at the very beginning of the prompt: `polished 2D anime key visual illustration, finished digital painting with traditional media texture, clean confident ink outlines`.

If the output still drifts toward realism, add exclusions sparingly and only after positive anchoring has failed:
```
... polished 2D anime key visual illustration ...
```

Reserve `--no` for the parameter line only when specific concrete objects keep appearing:
```
--no text, watermark, border, modern buildings, amusement park rides
```

---

## Default Parameters for i2i Frames

### V6
```
--ar 16:9 --style raw --s 200 --q 2 --v 6.1
```

### V7 / V8
```
--ar 16:9 --style raw --s 200 --q 2 --v 8.2
```

For anime-style projects, `--s 200` gives enough stylization without drifting into abstraction. Use `--s 100` for literal reproduction when the reference already contains the exact composition you want.

**V7/V8 changes:**
- `--cref` / Omni Reference no longer requires `--cw`. Character identity locking is automatic at maximum strength when the image is set to Omni Reference.
- `--sref` / Style Reference still supports `--sw` for weight control.

---

## Example Workflow (Web UI)

**User provides:**
1. `xiaowu_character_concept.png` → Character identity
2. `gobi_location_concept.png` → Environment style
3. `camera_angle_blockout.png` → Camera intent (do NOT upload to MJ)

**Step 1:** Open https://www.midjourney.com/imagine

**Step 2:** Click the **+** upload button, select images 1 and 2 from local storage.

**Step 3:** Set reference types from the dropdown on each uploaded image:
- `xiaowu_character_concept.png` → **Omni Reference**
- `gobi_location_concept.png` → **Style Reference**

**Step 4:** Do NOT upload the blockout. Describe the camera angle in the text prompt instead.

**Step 5:** Paste the text prompt into the input box. The web UI automatically injects `--cref` and `--sref` URLs. Add control weights and parameters as needed.

**Final text to paste:**
```
Extreme low angle from ground level beside the legs, looking upward, muscular young man with angular jawline and dark messy short hair lying on coarse gravel ground, propping upper body on one elbow, other hand rubbing eyes, slow groggy movement just woken up, broad shoulders thick chest well-defined abs, black athletic shorts, half-lidded sleepy eyes, disoriented empty gaze, harsh midday sun from above, high contrast, warm sunlight carving sharp sculptural shadows across muscles, cool blue sky reflection in shadows, foreground coarse gravel ground flat unbroken, midground torso and face center-upper frame, background vast deep blue sky with massive black mirror cube hovering above, distant barren hills, far horizon massive canyon rifts as dark linear gashes, polished 2D anime key visual illustration, finished digital painting with traditional media texture, clean confident ink outlines with varied line weight, flat cel-shading blended with expressive painterly brushwork, mature anime character design, NO sketch quality, NO 3D render, NO photorealistic shading, NO plastic gloss
```

**Parameters to set (V8):**
```
--sw 50 --ar 16:9 --style raw --s 200 --q 2 --v 8.2 --no text, watermark, border, amusement park buildings, cloudy sky
```

> V7/V8 的 Omni Reference 已不需要 `--cw` 参数，上传并设为 Omni Reference 后自动以最大权重锁定角色身份。

---

## Key Rules

1. **Omni Reference for characters, Style Reference for environments.** Image Prompt only when you want the model to start from an existing composition.
2. **Never upload blockouts/layouts as Image Prompt expecting exact spatial reproduction.** Describe camera angle and composition in text.
3. **Positive description beats negative exclusion in MJ.** Describe what you want, not what you don't want.
4. **Use `--no` only for persistent unwanted concrete objects** (text, watermarks, specific buildings), not for style bans.
5. **Omni Reference auto-locks character identity in V7/V8** — no `--cw` parameter needed. In V6 only, use `--cw 100` for strict identity lock.
6. **Style Weight `--sw 50–100`** for subtle environmental palette adoption. Raise to 200+ only if the style reference is the dominant creative driver.
