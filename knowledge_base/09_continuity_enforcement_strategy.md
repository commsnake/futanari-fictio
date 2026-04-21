# KB-09: Continuity Enforcement Strategy

This module defines the multi-layer continuity strategy to maintain narrative consistency across long-form AI generation.

## 1. The Core Principle
AI models lack intrinsic long-term memory. Continuity must be enforced structurally through explicit state-passing mechanisms rather than relying on contextual memory windows alone.

## 2. Multi-Layer Continuity Tracking

### Layer 1: Personal (Character State)
Continuity relies on dividing character traits into immutable and mutable categories.

*   **Immutable Traits (Dynamic Character Anchors):** Kept in the `templates/character_profile_template.md`. These include:
    *   Eye color, skin tone, bone structure.
    *   Permanent scars or physical quirks (e.g., a limp).
    *   Baseline voice cadence and vocabulary rules.
*   **Mutable Traits (The Continuity Handover):** Tracked dynamically from chapter to chapter in the Universal Chapter Brief (UCB).
    *   **Physical State:** Immediate injuries (bruises, cuts), bodily fluids (sweat, blood, arousal), and clothing status (torn, missing, soiled).
    *   **Psychological State:** Current trust levels, emotional depletion (e.g., post-orgasmic vulnerability), and immediate reactions to recent trauma or climax.

### Layer 2: Environment (Setting State)
*   Tracking the physical layout of a space.
*   Note any damage done to the environment during high-intensity action or explicit scenes (e.g., broken furniture, spilled liquids).

### Layer 3: Location (Spatial State)
*   **The Anti-Pretzel Protocol:** Ensuring all character movements are anatomically possible and maintain spatial consistency within the current environment.

### Layer 4: Story (Narrative State)
*   Tracking the overarching promises made to the reader (Tone, Trope, Heat, Safety).
*   Ensuring the "Future Setup" in the UCB accurately plants objects, vocabulary, or ritual actions needed for upcoming chapters.

## 3. The Continuity Handover Process
At the end of every chapter brief generation, the author/system MUST populate Section 13 (Continuity Handover) of the UCB. This acts as the state transfer payload for the subsequent chapter's prompt.

**Example Handover:**
*   **Physical State:** They are still in the master bedroom. John's shirt is torn at the collar. Maria has a small bruise forming on her left wrist.
*   **Psychological State:** The tension has broken. Maria is in deep aftercare drop, highly vulnerable. John is protective, slightly guilty.
*   **Future Setup:** The draconian contract was left unsigned on the bedside table.

## 4. Resolving Conflicts
If a continuity error is generated (e.g., a character suddenly wearing a jacket they took off two chapters ago), the text must be manually edited. Do not attempt to have the AI "narratively justify" a clear error unless the error itself can be repurposed into a psychological tell (e.g., forgetting they took off the jacket due to shock).
