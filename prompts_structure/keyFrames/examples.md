# KeyFrames Example · 《复生协议》 Scene CAD

Full 9-grid keyframe prompt for CAD_0010–0090, ready to feed to Gemini.

## Reference Images

- Image 1: Xiao Wu character concept art (full color, anchors character appearance — short black hair, honest face with slightly wide rounded cheekbones, sturdy build, dark jacket unzipped to chest revealing light crew-neck T-shirt)
- Image 2: Rainy night city ring road scene concept art (full color, anchors environment — wet asphalt, sodium streetlight reflections, low skyline silhouette)

## Global Settings

### Visual Style
3D CG anime cinematic render, GANTZ:O (2016) style, Unreal Engine 5 quality, cel-shaded characters with detailed 3D face models, dark sci-fi aesthetic, Japanese CG anime film, dramatic cinematic lighting, glossy wet surfaces with raytraced reflections, 16:9 aspect ratio, high detail, cinematic quality.

Entire scene is rainy night: wet asphalt with reflective sheen, high air humidity creating soft halos around distant light sources. Cool dark tones dominate, warm orange sodium streetlights are the only warm accent in the frame. Starting from CAD_0070, Seven's cold blue arc light is introduced.

### Negative Constraints
No second person visible. No daylight or clear weather. No cyberpunk neon. No characters other than Xiao Wu. No American 2D animation style. No photorealistic live-action style. Xiao Wu's outfit is consistent across all frames: dark jacket unzipped to chest, visible light crew-neck T-shirt underneath.

---

## 9-Grid Layout

```
┌──────────────┬──────────────┬──────────────┐
│              │              │              │
│   FRAME 1    │   FRAME 2    │   FRAME 3    │
│   CAD_0010   │   CAD_0020   │   CAD_0030   │
│              │              │              │
├──────────────┼──────────────┼──────────────┤
│              │              │              │
│   FRAME 4    │   FRAME 5    │   FRAME 6    │
│   CAD_0040   │   CAD_0050   │   CAD_0060   │
│              │              │              │
├──────────────┼──────────────┼──────────────┤
│              │              │              │
│   FRAME 7    │   FRAME 8    │   FRAME 9    │
│   CAD_0070   │   CAD_0080   │   CAD_0090   │
│              │              │              │
└──────────────┴──────────────┴──────────────┘

9 frames, 3×3 grid, read left→right top→bottom. Each cell 16:9, thin black borders between cells. SHOT_ID label in small light gray text at top-left corner of each cell, non-intrusive.
```

---

## Keyframe Sequence

### FRAME 1 · CAD_0010 · Rainy Night City Extreme Wide

- **Visual Content**: Nighttime suburban ring road viewed from a high-angle overhead position. Wet asphalt uniformly reflects scattered orange sodium streetlights — each lamp casting an elongated vertical streak of light across the road surface. A single dark sedan drives alone at the center of the empty road — the car appears small in the wide frame, taillights barely two faint warm red dots. Roadside guardrails and evenly spaced utility poles converge toward a distant vanishing point. Background: low skyline silhouette — left side shows 8–12 story residential blocks with fewer than half the windows lit, right side shows 2–3 story commercial buildings with shutters closed, occasional faint neon residue. No cloud breaks reveal dark gray night sky.
- **Camera**: Wide 35mm, high-angle direct overhead, locked-off
- **Lighting & Color**: Overhead sodium streetlights cast warm orange cone-shaped light zones intersecting with cool blue reflections on wet asphalt. Frame: 70% cool dark tones, 20% warm orange streetlights and reflections, 10% distant faint city glow. Air humidity produces soft halos blurring distant lights.
- **Composition & Depth**: FG guardrails and utility poles form radial perspective leading lines → sedan centered below (roughly 15% frame height), framed by leading lines → BG skyline fades into mist at center-top. Large negative space on either side of the sedan (dark road surface) emphasizes isolation.
- **Continuity**: Scene opener — establishes spatial tone: rainy night, solitude, vast emptiness. Next frame pushes into car interior, shot size jumps from Extreme Wide to Medium Close-up.

### FRAME 2 · CAD_0020 · Xiao Wu Driving, Quiet Smile

- **Visual Content**: Inside the car cabin, shot from the passenger seat angle, Xiao Wu in profile — chest up. His appearance exactly matches Image 1: short black hair neatly trimmed, honest face with slightly wide rounded cheekbones, sturdy build, dark jacket unzipped to chest revealing light crew-neck T-shirt. Left hand rests on the steering wheel — thumb hooked over the top, remaining fingers naturally relaxed. Right hand is lifted from the wheel, index and middle fingers hovering at the wheel rim, lightly tapping — the curve of his fingers shows a slow, relaxed rhythm. A quiet smile on his face — lips softly pressed together, corners slightly lifted; eyelids relaxed, lower lids slightly raised showing faint crow's feet at the corners. The unconscious expression of someone thinking about something good.
- **Camera**: Standard 50mm, eye-level with Xiao Wu, locked-off (passenger seat angle)
- **Lighting & Color**: Dashboard ambient warm light illuminates Xiao Wu's face from below — chin and lower cheekbones catch warm orange glow, bridge of nose and top of forehead remain darker. Streetlight beams through windshield intermittently sweep across his face — warm orange thin light stripe travels left to right, each pass lasting approximately 1 second. Cabin dark areas are deep gray-black (seats, rear cabin). Overall warm-dominant, cool colors exist only in the distant blurred blue-gray cityscape outside the windshield.
- **Composition & Depth**: FG left side: windshield edge with faint reflection → Xiao Wu's profile (chest up) centered-right, sharp focus → BG rear seats and headliner dissolve into soft dark shadow. Left side shows windshield and exterior night scene, right side shows Xiao Wu's face, eyeline direction rightward and slightly forward.
- **Continuity**: Cut from FRAME 1 exterior extreme wide to interior medium close-up. Space contracts from "vast and lonely" to "warm and intimate." Next frame pushes to extreme eye close-up, emotion progresses from quiet smile to "finally" look.

### FRAME 3 · CAD_0030 · Eye Extreme Close-up

- **Visual Content**: Extreme close-up of Xiao Wu's eyes — frame from upper brow ridge to below lower eyelids, lateral width contains both eyes and the bridge of the nose only. Eyes initially gaze forward at the road, then gently shift downward and to the right — eyeline direction moves from straight ahead to the lower-right passenger seat direction. Upper eyelids slightly lowered, all periocular muscles fully relaxed: brow smooth with no furrows, crow's feet naturally visible, lower eyelids gently raised. Pupils reflect a tiny streak of light from outside the windshield — a speck of warm orange-white light moving across the dark irises. This is not fear or surprise — it is the quiet certainty and softness of "finally, I'm going to do this."
- **Camera**: Macro 100mm, eye-level extreme close-up
- **Lighting & Color**: Warm orange dashboard light fills the lower eye sockets and upper cheekbones from below, creating a faint warm underlight. Streetlight sweep beam crosses both eyes from frame right — irises illuminate to light amber when hit, pupils subtly constrict. Overall warm orange + deep brown dark tones, skin cel-shaded with subtle subsurface scattering.
- **Composition & Depth**: Both eyes centered, occupying 60% of frame. Bridge of nose at lower-center frame acts as natural divider. Upper eyelashes form a natural foreground frame. Extremely shallow depth of field — only the eyes and bridge of nose in focus, brows and cheekbones in slight soft focus.
- **Continuity**: Push from FRAME 2 medium close-up to extreme close-up. Eyeline direction sets up the next frame — he is looking toward the ring box on the passenger seat. Emotional progression: quiet smile → "finally" look.

### FRAME 4 · CAD_0040 · Ring POV Close-up

- **Visual Content**: On the passenger seat, a deep red velvet ring box sits open — lid flipped backward, velvet surface with subtle sheen. Inside the dark velvet groove, a silver ring is nestled: the band shows a clean elliptical arc with a small faceted gemstone at the top. On one facet of the gem, a tiny warm white pinpoint of light reflects — caught from a passing streetlight outside the window, briefly held on the stone's surface. The ring is centered, surrounding velvet gradually softens into bokeh blur. This is Xiao Wu's subjective POV — he is looking down at the ring, and this frame is his sightline.
- **Camera**: Macro, high-angle downward tilt (the angle of looking down at the passenger seat), Xiao Wu POV
- **Lighting & Color**: Warm orange streetlight beam sweeps across the frame — first illuminating the left side of the velvet box, then the light point lands on the gemstone facet. Overall dark palette: deep red velvet + dark gray-black cabin interior, the silver ring is the only highlight zone. Warm orange light point and silver band create subtle warm-cool micro-contrast.
- **Composition & Depth**: Ring centered, sharp focus → ring box velvet forms natural soft frame (fading into bokeh) → passenger seat and door panel beyond dissolve into fully blurred dark background. Extremely shallow depth of field, focus only on the ring and gemstone.
- **Continuity**: POV cut — from FRAME 3 Xiao Wu's eyes directly to what the eyes are looking at, creating a "seeing → seen" psychological connection. Rhythm shifts from slow calm to tender gaze. Next frame erupts into danger — this is the last moment of peace before the storm.

### FRAME 5 · CAD_0050 · Truck Barrels In

- **Visual Content**: Camera positioned inside the cabin, peering over the dark silhouette of the steering wheel and upper dashboard edge, through the windshield toward the intersection ahead. The sedan is approaching the crossing. From the right-side cross street, a massive truck shadow barrels forward — the truck's front is enormous, headlights are two blinding white circles rapidly growing larger. White light has already begun flooding the lower half of the windshield from right to left — raindrops on the glass scatter into fine light speckles. The steering wheel silhouette remains in the lower frame but has become irrelevant — everything in frame pushes toward "impact is inevitable." The traffic light at the intersection has become a blurred glow at the upper frame edge.
- **Camera**: Wide 28mm, interior over-the-shoulder (peering over steering wheel toward windshield), slight instability — mimicking Xiao Wu's body micro-movement as he registers danger
- **Lighting & Color**: Truck headlights flood white from frame right — blown-out white transitioning to warm white at closer range. Cabin interior still holds dashboard warm glow + streetlight sweep warm orange — but both warm sources are being rapidly consumed by white light. Frame upper-right zone completely blown to pure white, lower-left still retains cabin warm dark tones. Extreme contrast ratio: right pure white vs. left deep gray-black.
- **Composition & Depth**: FG steering wheel and upper dashboard edge as dark silhouette frame → MG windshield covered in rain and scattered light speckles → BG intersection with massive truck shadow + blown-out headlights. Sightline sweeps from frame left to right — natural reading direction of driver's perspective.
- **Continuity**: Rhythm rupture — from FRAME 4 tender gaze to sudden death threat. Shot size jumps from Macro to Wide 28mm, space expands from centimeters to entire intersection. Light jumps from warm to white. This is the "seeing danger" moment, next frame is "danger in your face."

### FRAME 6 · CAD_0060 · Impact Face Extreme Close-up

- **Visual Content**: Xiao Wu's face in extreme close-up — the lens seems to rush into his face in the split second before the truck hits. Eyes have snapped from the gentle softness of FRAME 3 to locked-open, wide — brows shot up, forehead showing horizontal wrinkles, pupils violently dilated filling the irises. Mouth beginning to open — lower lip already dropped, upper lip about to part, jaw muscles tensed. Truck headlight white light floods from frame right — the right half of his face (from nose bridge centerline to right ear) is completely consumed by white light, leaving only the cel-shaded highlight edge; the left half sinks into extreme deep shadow, cheekbone hollows and eye socket completely dark. This is not fear — it is the involuntary physiological response to seeing death, the single second between "seeing" and "impact" stretched to infinity.
- **Camera**: Telephoto 85mm, rush-in extreme close-up, slight Dutch angle 2–3° tilt to amplify disequilibrium
- **Lighting & Color**: Extreme split lighting — frame right 40% pure white blown-out (truck lights), left 60% deep black shadow. Dashboard warm orange completely consumed by white light. Frame reduced to three colors: white / black / deep brown-orange (skin shadow). Light forms a hard cut line at the nose bridge centerline. Right-side white light edge produces faint highlight bloom halo on skin.
- **Composition & Depth**: Face occupies 90% of frame, nose bridge centerline roughly aligns with the light dividing line. Extremely shallow depth of field — only eyes and nose bridge in focus, forehead and lips in slight soft focus. Dutch angle micro-tilt makes the face sit non-horizontally, amplifying disequilibrium and loss of control.
- **Continuity**: Cut from FRAME 5 objective danger to FRAME 6 subjective terror — two faces of the same event. Shot size from Wide to ECU, time compresses from "truck approaching" to "the second before impact." Next frame jumps directly to post-impact — what happens in between, the audience fills in.

### FRAME 7 · CAD_0070 · Overturned Car Interior

- **Visual Content**: Frame is inverted — ceiling is down, seats are up. Camera positioned in the rear seat area looking toward the front. Xiao Wu hangs upside down in the driver's seat, seatbelt diagonally cutting across his chest from lower right to upper left, his body forming a slack suspension arc — he has lost consciousness. One arm hangs limply downward from his body, fingertips nearly touching the dented ceiling liner. The air is filled with dozens of shattered glass fragments — irregular polygons of varying sizes, slowly rotating in the faint light, reflecting cold glints. The windshield has become a dense spiderweb of cracks — through the fracture center, a beam of cold streetlight enters from outside, passing through the suspended glass particles and casting tiny moving light spots across Xiao Wu's inverted body and the ceiling liner. The ceiling liner is deformed and bulging, a plastic trim panel has come loose revealing internal wiring.
- **Camera**: 24mm wide, rear-seat interior angle, frame inverted 180° (upside-down), slight instability simulating post-rollover residual tremors
- **Lighting & Color**: Cold streetlight (blue-white fluorescent temperature) enters through windshield cracks — this is the primary light source. All original interior warm ambient light has been extinguished — only this single beam of cold light and darkness remain. Suspended glass fragments act as secondary scatterers, breaking the cold beam into moving light speckles. Overall cold blue-gray + deep black. Xiao Wu's skin appears pale with a blue cast under cold light, his dark jacket and the dark gray ceiling liner nearly merge into shadow.
- **Composition & Depth**: FG right: front seat back silhouette (upper area due to inversion) → MG Xiao Wu's inverted body and dangling arm — frame core → BG (lower area, due to inversion): deformed ceiling liner and cracked spiderweb windshield. Large negative space is darkness, only the beam's path is visible. Glass fragments scattered across multiple depth planes — chaotic but layered.
- **Continuity**: Jump from FRAME 6 pre-impact instant directly to post-impact — omits the violence of the impact itself, leaving it to audience imagination. "Afterlife" cold color palette introduced, setting up Seven's entrance in the next frames.

### FRAME 8 · CAD_0080 · Ring on the Ground

- **Visual Content**: Wet asphalt surface, ultra-low angle hugging the ground. A silver ring lies on its side — one arc of the band touches the rough road surface, the ring caught at the threshold between decelerating roll and topple: center of mass shifting, slowly tipping left, finally settling flat — the band's faceted top facing up. Extremely shallow fresh scratch marks sit beside the ring on the water film. Around it, scattered fine glass shards — irregular tiny translucent particles catching sporadic white reflections from distant streetlights. A thin stream of dark liquid extends from the upper-left of frame toward the ring — the front edge now 2–3 cm away, not yet touching. The road surface water film reflects a blurred orange glow from above.
- **Camera**: Macro, ground-level (flat on the ground), locked-off
- **Lighting & Color**: A distant tilted streetlight casts cold fluorescent light from above — blue-white cold light is the primary source, road water film reflects cold blue sheen. The silver ring reads as cool-tone metal under cold light. The dark liquid is near-black, only its edges catch faint cold light reflection. Scattered orange residue light comes from a still-flickering distant headlight or streetlight — creating tiny warm highlight points on glass shards. Overall cold blue-gray + deep black, sparse warm orange highlight dots. The cold dark palette telegraphs: death has already happened.
- **Composition & Depth**: Ring centered, occupying 30% of frame → surrounding glass shards and road water film form midground texture → upper-right dissolves into out-of-focus darkness. Extremely shallow depth of field — only the ring and glass shards within 2–3 cm in focus. The dark liquid entering from upper-left forms a natural sightline leading line toward the ring.
- **Continuity**: From FRAME 7 chaotic interior panorama to ground-level macro — space compresses from cubic meters to centimeters. The ring is the last "living" object seen before the crash and Seven's target — it appears as an independent subject for the first time across all 8 frames, the emotional anchor. Next frame: Zero tears through from the upper-mid frame — same ground plane, dimension ripped open.

### FRAME 9 · CAD_0090 · Zero Descends

- **Visual Content**: 14mm ground-level upward angle. FG: the overturned sedan's undercarriage wreckage — twisted metal frame structure, a broken exhaust pipe tip dripping dark liquid. MG: shattered glass and metal debris scattered across the wet road surface. Upper-mid frame: space is torn open — a perfect geometric rift with sharp irregular fracture edges, interior is pure black void. Seven (cube cluster) is extruding its lower half from the rift — dozens of mirror-black cubes ranging from fist-sized to grain-sized, edges emitting hairline cold blue light. Electric arcs jump and conduct between adjacent cubes — fine blue-white currents continuously flowing, cubes constantly rearranging their positions, like living black crystal pouring down from the fissure. Below the rift, several cubes have already landed on the road surface, emitting faint cold blue light rings at contact points — like digital snowflakes. Only Seven's lower portion is visible (above the rift is obscured), maintaining mystery and oppressive presence. Cube surfaces reflect the road's cold light — each face a tiny distorted mirror.
- **Camera**: 14mm ultra-wide, ground-level upward angle (shooting up from the road surface), locked-off
- **Lighting & Color**: Cold blue arc light is the only new light source — fine bright blue-white jumping across pure black void. Existing scene light: distant tilted streetlight cold white fluorescence continues illuminating the road. Seven's cube cold blue light and streetlight cold white merge into a unified cold palette — frame 90% cold blue-gray + deep black, 10% arc blue-white highlight. Cube mirror reflections bounce road cold light back, creating dancing light points. The entire frame has a single temperature: cold.
- **Composition & Depth**: FG undercarriage wreckage as massive silhouette occupying lower 40% of frame (distorted by 14mm ultra-wide) → MG road surface debris → Upper-MG rift and Seven's cubes are the focal point → BG (above rift) pure black void. The 14mm distortion makes the FG wreckage appear abnormally huge, Seven's rift pushed back in perspective — creating the oppressive sense that "something vast is descending." The rift's irregular geometric edges are further stretched by the ultra-wide perspective.
- **Continuity**: Scene closer. From FRAME 8 ring macro → FRAME 9 ultra-wide ground shot, space explodes from centimeters to full scene, introducing the supernatural element. Cold blue arc light unifies with all previous frames' cool palette but is distinct — this is "afterworld" light, not rainy night streetlight. The 9 frames complete a full arc: warm human world → crash → death → supernatural arrival.
