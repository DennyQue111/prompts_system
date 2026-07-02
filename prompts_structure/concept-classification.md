
## Description
This guide defines the boundary lines between the four concept subtypes — **character**, **entity**, **prop**, and **location**. When the user describes a subject, consult this file to determine which architecture should be used. The goal is to prevent miscategorization (e.g., scoring a sentient sphere as if it should have clothing, or scoring a prop as if it should have emotion).

---

## Quick Decision Flow

```
Is the subject a PLACE / SETTING / SPACE?
  └─ YES → location

Does the subject have a recognizable HUMAN or HUMANOID body plan?
  (head, torso, limbs — even if stylized or partial)
  └─ YES → character

Does the subject have CONSCIOUSNESS, AGENCY, or narrative personhood?
  (It thinks, perceives, judges, protects, threatens, communicates intent)
  └─ NO → prop
  └─ YES → entity
```

---

## Detailed Classification Rules

### 1. Character — 角色（人形）

**Definition**: A being with a recognizable humanoid body plan — head, torso, limbs, face — capable of expressing emotion through facial features and body language. Clothing, armor, and accessories are part of its visual identity.

**Typical examples**:
- Human characters of any profession, era, or style
- Humanoid fantasy/sci-fi races (elves, orcs, cyborgs with human proportions)
- Anthropomorphic animals that stand, gesture, and emote like humans
- Robots/androids with clearly humanoid silhouettes

**Key signals**:
- Has a face that can express emotion
- Wears clothing or armor (or the absence of it is a deliberate choice)
- Can strike poses, perform actions with limbs
- Age, hair, skin tone, build are relevant descriptors

**Architecture directory**: `concept/character/` → read `README.md` for available model variants, then `general.md` (default).

---

### 2. Entity — 存在体 / 意识体（非人形但有意识）

**Definition**: A sentient being whose physical form does NOT follow a humanoid body plan. Its "form" and its "identity" are inseparable — the physical structure IS the character. Consciousness is communicated through non-facial signals: eye(s) embedded in non-face surfaces, light pulses, material shifts, motion patterns, geometric transformations.

**Typical examples**:
- A sentient geometric form (sphere, cube, polyhedron) with embedded sensory organs
- AI manifestations: floating holographic faces, data-clouds with awareness
- God-projections, cosmic entities, Lovecraftian presences
- Elemental beings with non-humanoid forms (a sentient flame, a living shadow)
- Alien consciousness that occupies a non-biological vessel
- Abstract "rule-keepers" and game-masters (GANTZ black sphere, Zordon energy form)
- Living machines that do not mimic the human body (a sentient starship, a conscious monolith)

**Key signals**:
- Has agency and consciousness — it's a character in the narrative
- Does NOT have a humanoid body plan — no clothes, no limbs, no human-proportioned face
- Sentience is shown through alternative cues: eye(s) on non-face surfaces, glow rhythms, reactive materials, movement patterns
- Materials/textures and form structure are the core visual descriptors (not clothing)
- Scale is critical — without a body to reference, the viewer must be told how big it is

**Boundary cases**:
| Case | Verdict | Reason |
|------|---------|--------|
| A floating giant eye | **entity** | No body, no face (an eye alone is not a face) |
| A human face emerging from a stone wall | **character** or **entity** — depends on how much body is present |
| A robot with arms, legs, and a face | **character** | Humanoid body plan |
| A robot that is a floating cube with an eye | **entity** | Non-humanoid form |
| A ghost that looks like a translucent human | **character** | Humanoid silhouette preserved |
| A ghost that is a shifting cloud of light | **entity** | No humanoid form |
| A talking sword | **entity** | Consciousness + no body |

**Architecture directory**: `concept/entity/` → read `README.md` for available model variants, then `general.md` (default).

---

### 3. Prop — 道具 / 物件（无意识）

**Definition**: An object with no inherent consciousness or agency. It may carry narrative weight (a hero's sword, a wizard's staff, a clue object), but it does not think, perceive, or act on its own. Its visual interest comes from materiality, craftsmanship, wear, and contextual placement.

**Typical examples**:
- Weapons, tools, gadgets, vehicles
- Jewelry, artifacts, relics, magical items
- Everyday objects, furniture, technology devices
- Food, plants (non-sentient), natural specimens

**Key signal — the litmus test**:
> If you remove the object from the story, does the story lose an OBJECT or lose a CHARACTER?

- Story loses an object → **prop**
- Story loses a character → **entity** or **character**

**Architecture directory**: `concept/prop/` → read `README.md` for available model variants, then `general.md` (default).

---

### 4. Location — 场景 / 环境

**Definition**: A space, setting, or environment where action takes place. The subject is the PLACE itself, not an object or being within it.

**Typical examples**:
- Landscapes (forests, deserts, mountains, oceans)
- Interiors (rooms, halls, chambers, corridors)
- Cityscapes and architecture
- Fantasy/sci-fi environments
- Abstract or dream spaces

**Architecture directory**: `concept/location/` → read `README.md` for available model variants, then `general.md` (default).

---

## Edge Cases & Tiebreakers

### When it could be entity OR prop
| Scenario | Entity if... | Prop if... |
|----------|-------------|------------|
| A strange device | It watches, responds, or shows awareness | It's inert, even if mysterious |
| A statue | Its eyes follow you / it's clearly alive | It's carved stone, no awareness implied |
| A magical gem | It pulses with awareness, chooses bearers | It's just a powerful but inert crystal |

**Tiebreaker**: Does the prompt use verbs of consciousness (stares, watches, judges, pulses with awareness, responds to...) or just descriptive adjectives? Verbs of consciousness → entity. Adjectives only → prop.

### When it could be entity OR character
**Tiebreaker**: Does it have a human face and human-proportioned body? If yes → character. If it communicates consciousness through non-humanoid features (a single eye on a sphere, a glow pattern, a geometric shift) → entity.

### When the user describes a "character" but no body details are given
Example: "a mysterious game master who sets the rules" — the user says "character" but gives no human description. Ask: does this character have a humanoid body, or is their visual form abstract/non-human? If the user doesn't know, default to the architecture that matches the visual cues they DO provide.

---

## Usage for the SKILL

When the SKILL receives a request, it should:
1. Identify which concept type is being requested (or infer from the description)
2. If unsure, **consult this classification guide**
3. If still ambiguous, ask the user: "Is this a humanoid character, a non-humanoid entity, a prop, or a location?"
4. Load the type's README, then the appropriate model variant file
5. Generate or evaluate the prompt accordingly

This file should be checked BEFORE loading any architecture file, whenever the subject type is ambiguous.
