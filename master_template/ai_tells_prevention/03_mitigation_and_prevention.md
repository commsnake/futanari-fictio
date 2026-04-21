# Mitigation and Prevention Strategies

Preventing an AI from falling back into easily identifiable "tells" requires a multi-layered approach involving prompting techniques, system instructions, and post-generation filtering.

## 1. Prompting Techniques

### The "Negative Prompt" Blacklist
Explicitly instruct the AI on what *not* to do within the prompt itself. Do not rely solely on "write like a human." Provide the blacklist.

**Example Instruction:**
> "CRITICAL: Do NOT use any of the following words or phrases: tapestry, realm, delve, nuanced, vibrant, dynamic, compelling, testament, overarching, nestled, robust, seamless, crucial, pivotal, elevate, navigate, foster, showcase, ensure, embark, unwavering, resonate, multifaceted, symbiotic, game changer, watershed moment. Do NOT use the phrases 'It's not about X, it's about Y' or 'In conclusion'. Do NOT summarize emotions at the end of the scene."

### Enforcing "Jaggedness"
Command the AI to vary sentence structures and lengths drastically.

**Example Instruction:**
> "Write with 'jagged' rhythm. Mix very short, punchy sentences (2-5 words) with longer, descriptive ones. Avoid uniform paragraph lengths. Use fragments occasionally for dramatic effect."

### Grounding in Physical Reality (Fiction)
To prevent abstract, floaty AI prose, anchor descriptions to physical sensations.

**Example Instruction:**
> "Adhere strictly to the 'Show, Don't Tell' protocol. Do not describe a character's internal emotional state directly (e.g., 'she felt anxious'). Instead, describe their physical reaction to the emotion (e.g., 'her pulse drummed against her throat, swallowing dry'). Adhere to the 'Anti-Pretzel Protocol' to ensure physical movements are anatomically possible."

## 2. The Multi-Pass Generation Strategy

Instead of asking the AI to write a perfect final draft in one go, use a multi-pass approach:

1.  **Pass 1 (Drafting):** Generate the core narrative or argument.
2.  **Pass 2 (The "De-Fluffing" Pass):** Prompt the AI to edit its own work.
    > "Review the previous text. Remove any instances of the word 'delve', 'tapestry', or 'nuance'. Rewrite any sentences that use the 'Not X, but Y' structure. Shorten the text by 10% by removing generic transitional phrases."

## 3. Automated Post-Processing (`anti_ai_filter.py` Logic)

To guarantee that "tells" do not make it into the final output, a post-processing script should be implemented. This aligns with the pipeline outlined in the repository setup guide.

**Core Logic for `anti_ai_filter.py`:**

1.  **Regex Matching:** The script should load the blacklist from `01_overused_vocabulary.md` and use regular expressions to flag these terms in the generated markdown files.
2.  **Structural Flagging:** Use regex to identify repetitive sentence structures (e.g., `It's not about .*, it's about .*`).
3.  **Action Options:**
    *   **Audit Mode:** The script highlights the flagged terms/structures and outputs a report, requiring a human editor to rewrite them.
    *   **Automated Replacement (Risky):** The script attempts to replace simple banned words with synonyms, though this often breaks context.
    *   **Rewrite Call:** The script sends the specific flagged paragraph back to an LLM via API with the prompt: "Rewrite this paragraph to remove the AI tells, specifically the word [FLAGGED WORD], while maintaining the exact same meaning and tone."

**Implementation in the Workflow:**
The `anti_ai_filter.py` must run as the final step (Step 8) in the repository workflow, acting as a mandatory gatekeeper before a chapter is considered "finalized".