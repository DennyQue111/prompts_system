# Spatial Topology and Shot Visibility

Use this reference for spatially constrained `frame`, `storyboard`, and `keyFrames` prompts: intersections, alleys, doors, rooms, corridors, vehicles, multiple characters, screen direction, or any shot that must connect to another camera angle.

## Core distinction

Never treat **world topology** and **what the current camera can see** as the same description.

- **World topology**: what connects to what in the scene, independent of camera. Example: one narrow alley is perpendicular to a continuous main lane.
- **Shot visibility**: what that topology projects into this frame from this camera. Example: from far back and nearly parallel to the facade, the alley reads only as a dark opening; its floor and interior walls are fully occluded.

A correct map can still produce a wrong frame when the prompt describes the topology but fails to describe its visible projection.

## Spatial preflight

Before writing the render prompt, make a compact internal spatial ledger:

1. **Fixed topology** — paths, walls, openings, connections, dead ends, relative widths.
2. **Camera transform** — camera position, height, orientation, lens, and viewing axis.
3. **Occlusion** — which wall, corner, object, or character hides each off-axis space.
4. **Visible projection** — silhouettes, openings, floor patches, wall faces, and vanishing points actually visible in frame.
5. **Forbidden projection** — spatial evidence that would imply a different topology, such as a second road vanishing point or visible alley floor.

Do not send the abstract ledger unchanged to the renderer. Compile it into concise, visible evidence.

## Visibility contract

For every important opening, intersection, doorway, or corridor, explicitly resolve:

- Is the opening visible at all?
- Is only its mouth/silhouette visible, or is the interior visible?
- Which near edge occludes the interior?
- Is any floor inside visible?
- Does it create a second vanishing point?
- How wide is it in frame relative to the main path or facade?

If the intended shot sees only an opening, say positively what occupies the pixels: `a narrow dark vertical opening in the continuous facade, with the near corner wall covering the interior; the main road retains one vanishing point.` Do not add phrases such as `show the first few metres inside`.

## Reference authority without contradiction

Classify each reference before prompting:

- **Exact shot/blockout from the intended camera**: authority for projected composition and occlusion. Text may identify semantic roles and visible/invisible boundaries, but must not move geometry.
- **Plan, map, orthographic diagram, or multi-view layout**: authority for world topology only. It is not proof of what a perspective camera can see. Derive the current shot visibility from camera position.
- **Location concept or unrelated camera view**: environment/style/architecture reference, not exact spatial authority.
- **Previous accepted frame**: continuity authority for the features explicitly being preserved.

Do not upload a full multi-view sheet as direct composition authority when only one panel applies. Crop or isolate the relevant view whenever possible. Avoid combining references whose camera viewpoints imply different projections unless their roles are explicitly separated.

When an exact camera-matched blockout conflicts with prose, repair the prose. When only a map or multi-view sheet exists, text must state the current camera's visible projection; the map alone is insufficient for image models.

## Vocabulary traps

Topology labels such as `T-junction`, `branch`, `cross street`, `side road`, `right-angle alley`, and arrows are not enough. Image models may expand them into a familiar wide intersection. Pair any necessary topology label with measurable visible evidence, or omit the label when it activates the wrong composition.

Prefer:

- one visible road vanishing point
- continuous storefront silhouette
- doorway-width dark opening
- near corner wall occludes the passage interior
- no visible interior floor plane

Use short negative constraints only for high-risk topology failures that cannot be expressed positively. Do not repeat a prior failed image in detail.

## Frame rule

For a single frame, optimize for the **visibility contract**, not for explaining the whole set. The prompt must be drawable from the current camera only. If exact topology remains fragile, prefer this order:

1. use or create a camera-matched blockout;
2. isolate the relevant location reference panel;
3. edit a validated background locally;
4. use unconstrained regeneration only when the above are unavailable.

## Storyboard rule

For a storyboard, define one shared spatial ledger before the panel descriptions. Each panel then states only its camera transform and resulting visible projection.

Track across panels:

- stable landmarks and path connectivity;
- character positions and facing directions in world space;
- screen-left/screen-right movement and eyelines;
- which openings are visible or occluded from each angle;
- entry/exit edges and the 180-degree line;
- the number and direction of visible vanishing points.

Never copy the same intersection description into every panel. A location can contain an alley while one panel shows only its mouth, another looks from inside it, and a third does not show it at all. Add a re-establishing wide panel after a major axis change when spatial comprehension matters.

## Final spatial check

Before rendering, answer:

1. Could an artist draw a top-down map from the fixed topology?
2. Could the same artist draw this exact frame without inventing unseen space?
3. Does every visible floor plane and vanishing point belong to the intended camera view?
4. Would any visible opening accidentally read as a second road or room?
5. For a sequence, can every character and camera position be placed consistently on one shared map?

If any answer is uncertain, fix the spatial ledger or create a camera-matched blockout before generation.
