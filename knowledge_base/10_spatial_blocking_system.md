# KB-10: Kinematic Scene Blocking Matrix (KSBM) & Macro Spatial Tracking

## Purpose and The "Anti-Pretzel Protocol"
The spatial tracking system operates on two distinct levels: the **Macro-Level (Ship/Environment)** and the **Micro-Level (Kinematics)**.

1.  **Macro-Level (Logline & Storyline Location Tracking):** Before blocking physical interactions, the AI must establish where everyone is located in the broader environment. This ensures characters don't teleport between decks or suddenly appear in rooms without narrative justification. It relies heavily on timelines (like `06_character_positions_timeline.md`) to place characters realistically based on the current ship cycle.
2.  **Micro-Level (The "Anti-Pretzel Protocol"):** In highly intense, action-oriented, or explicit scenes (such as those in Phases 4-8 of the Erotic Cycle), AI language models frequently lose track of character anatomy and spatial physics. This results in the "Pretzel Effect"—descriptions where a character is simultaneously facing away while making eye contact, or using three hands at once. The **Kinematic Scene Blocking Matrix (KSBM)** acts as a spatial constraint grid. It forces the AI generator to explicitly track orientation and contact points before drafting the prose.

---

## 1. Macro-Level Tracking (Environmental Placement)

Before beginning any chapter generation or deep scene work, define the spatial map of the environment based on the storyline.

*   **Current Global Time/Phase:** [e.g., Book 2, Chapter 4, Night Watch]
*   **Primary Scene Location:** [e.g., The Galley]
*   **Characters Present in Scene:** [e.g., Leo, First Mate]
*   **Known Locations of Absent Characters:** [e.g., Captain is asleep in Quarters, Deck Boss is asleep in Bunks, Engineer is in Engine Room]

*Constraint:* If a character enters the scene, their arrival must logically align with their known prior location and the travel path required to reach the primary scene location.

---

## 2. Micro-Level Principles of Spatial Tracking (Kinematics)

When blocking a specific physical scene, three elements must be clearly established and maintained until an explicit movement changes them:

1.  **Anchor Points:** Which body parts are supporting the character's weight? (e.g., knees on the mattress, back against the wall).
2.  **Orientation:** Where is the character's torso facing relative to the other character(s)? (e.g., chest-to-back, face-to-face, perpendicular).
3.  **Active Limbs (The "Two Hand Rule"):** A character only has two hands. If one hand is gripping a wrist and the other is holding a hip, they cannot simultaneously brush hair out of a face.

---

## 3. The Blocking Matrix Template

Before generating or writing a high-complexity scene, the following matrix should be filled out (or injected into the AI prompt as a constraint).

### Current Scene State
*   **Location/Prop:** [e.g., Edge of the bed, pinned against the oak desk]
*   **Primary Action/Phase:** [e.g., Phase 5: Escalation - Restraint]

### Character A (The Anchor / Dominant Position)
*   **Orientation:** [e.g., Standing, facing Character B's back]
*   **Weight Bearing On:** [e.g., Both feet, leaning forward]
*   **Left Hand Position:** [e.g., Gripping Character B's left hip]
*   **Right Hand Position:** [e.g., Pinned against the back of Character B's neck]
*   **Lower Body Contact:** [e.g., Thighs pressing against Character B's glutes]

### Character B (The Seeker / Submissive Position)
*   **Orientation:** [e.g., Bent over the desk, facing away from Character A]
*   **Weight Bearing On:** [e.g., Forearms flat on the desk, feet spread on the floor]
*   **Left Hand Position:** [e.g., Clinging to the edge of the desk]
*   **Right Hand Position:** [e.g., Pushing back against Character A's thigh (Resistance)]
*   **Lower Body Contact:** [e.g., Pressed flush against Character A's groin]

---

## 4. Transitional Movements (The "Shift")

Characters do not teleport. When transitioning from one position to another (e.g., moving from the desk to the bed), the narrative *must* explicitly describe the release of anchor points and the establishment of new ones.

**Example of a Flawed Shift (Teleporting):**
> *He had her pinned against the desk. Suddenly, she was on her back on the bed, looking up at him.*

**Example of a Blocked Shift (Tracking Kinetics):**
> *He released her neck, his hand sliding down to grip her forearm. Pulling her upright, he spun her away from the desk. She stumbled back, the back of her knees hitting the mattress before her weight collapsed onto the bed, leaving her looking up at him.*

---

## 5. Prompting the AI with Macro/Micro Spatial Tracking

When generating a scene or chapter brief, append this specific instruction to ensure spatial coherence across both levels:

> **AI INSTRUCTION - SPATIAL AWARENESS (MACRO & MICRO):**
> 1.  **Macro:** Acknowledge the location of all relevant characters on the ship based on the current timeline. Characters must not appear or teleport without traversing the ship layout logically.
> 2.  **Micro:** Review the Kinematic Scene Blocking Matrix provided. You must strictly adhere to these physical constraints. Ensure the "Two Hand Rule" is not violated. Describe the physical sensation of the specific contact points listed. If characters change positions, describe the kinetic movement that breaks the old anchor points and establishes the new ones. Do not let characters perform anatomically impossible bends or simultaneous actions.
