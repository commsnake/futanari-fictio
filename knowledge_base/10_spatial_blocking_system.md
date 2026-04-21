# KB-10: Spatial Blocking & Kinematic State System

To solve the AI "pretzeling" issue (where an LLM loses track of limb placement, orientation, or environmental constraints during high-action or explicit scenes), we must introduce a **Kinematic Scene Blocking Matrix (KSBM)**.

This system adapts principles from theater blocking and 3D animation (kinematic chains) into a lightweight, text-based reference grid that an LLM can parse and strictly adhere to.

## 1. When to Use the KSBM
The KSBM is not necessary for dialogue-heavy scenes. It should be injected into the prompt *only* during:
- **Phase 4-8 of the Erotic Cycle** (Core Act through Aftercare)
- Complex action sequences or physical struggles.
- Scenes involving extreme size differences or non-standard anatomy (e.g., Futanari content).

## 2. Core Components of the KSBM
The matrix acts as a snapshot of physical reality at the start of a generation block. It defines four rigid parameters:

### A. Environment Zones
Break the immediate setting into 2-3 distinct zones.
*Example: Zone 1 (The Doorway), Zone 2 (The Desk), Zone 3 (The Center Rug).*

### B. Posture & Orientation
Define the Z-axis (verticality) and facing direction for each character.
*Options: Standing, Kneeling, Sitting, Lying (Supine/Prone), Pinned.*

### C. Points of Contact (Kinematic Links)
Explicitly map the current physical connections between entities. If a limb is assigned here, the AI cannot use it for another action without explicitly breaking the connection first.

### D. The "Free Limbs" Inventory
List what appendages are currently *not* engaged and are available for the AI to use in the generated prose.

---

## 3. The KSBM Template (Prompt Injection)

When prompting the AI for a highly choreographed scene, append this grid below the standard prompt constraints:

```markdown
### Kinematic Scene Blocking Matrix (KSBM)
**[SCENE START STATE]**

**Environment & Orientation:**
*   **Zone:** [e.g., Pressed against the bedroom door]
*   **Character A ([Name]):** [Posture: e.g., Standing, facing B, back to the door]
*   **Character B ([Name]):** [Posture: e.g., Standing, facing A, leaning inward]

**Active Points of Contact (Locked Limbs):**
*   **A's Back** <--> The Door (Pinned)
*   **B's Left Hand** <--> A's Right Jawline
*   **B's Right Hand** <--> A's Left Hip
*   **B's Right Knee** <--> Parted between A's thighs

**Free Limbs Inventory (Available for Action):**
*   **Character A:** Both arms are free (currently resting at sides).
*   **Character B:** None (Both hands and lower body engaged).

**Anatomic Constraints (Anti-Pretzel Reminder):**
*   [e.g., Character B is 6'2", Character A is 5'4". B must lean down significantly to maintain eye contact or kiss.]
```

## 4. Generative Rules for the LLM
When the KSBM is provided, the prompt must include the following rule-set to ensure compliance:

> **SPATIAL COMPLIANCE DIRECTIVE:**
> 1. **Respect the Grid:** You must generate actions originating *only* from the 'Free Limbs Inventory'.
> 2. **Explicit Disconnects:** Before a character can use a 'Locked Limb', you must describe the physical action of releasing the current Point of Contact.
> 3. **Gravitational Logic:** Maintain awareness of posture and the Anatomic Constraints (height differences, leverage). Do not generate actions that defy human joint articulation.