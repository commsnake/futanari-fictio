# Master Workflow Guide

This document outlines the Master Workflow for the [Genre/Theme] Writing Repository. The primary goals of this workflow are maximum flexibility and rigorous continuity management when manual edits are introduced.

## Core Philosophy

The automated pipeline defined in this project is not a rigid rail system. The generation of erotic fiction requires nuance, tone adjustments, and frequent course corrections by the author.

Therefore, the system is designed to allow the user to **start, stop, interrupt, and resume the workflow at any given step** without losing continuity.

## 1. Flexible Execution

You do not need to execute all 10 steps of the primary pipeline (from OCR input to final Amazon metadata) in a single session.

### How to Resume Work
When returning to a project or starting a new agent session, the AI is instructed (via `AGENTS.md`) to automatically assess the state of the repository.

*   The AI will scan the directories (`story_ideas/`, `briefs/`, `drafts/`, `world_building/`, etc.).
*   It will determine the last completed artifact (e.g., if a Cast Ledger exists but no World Bible, it knows step 6 is incomplete).
*   It will prompt you with the likely next step to proceed.

You can simply tell the AI, "Resume work on Project X," and it will orient itself based on the files present.

## 2. The "Ripple Effect" Protocol (Edits & Feedback)

The most critical feature of this workflow is how it handles manual interventions. When you edit a generated output or provide feedback that alters established facts, the AI must ensure that change "ripples" backward and forward through the project's documentation to prevent continuity errors.

### How to Trigger the Protocol
You can trigger this process at any time by simply informing the AI of an edit or providing feedback:
*   *"I changed Leo's debt from $15,000 to $50,000 in chapter 1."*
*   *"I didn't like the ending of the beat sheet; let's have them arrive at a storm instead of calm waters."*
*   *"Update the style guide: we need shorter sentences during action scenes."*

### What the AI Will Do
When you provide this feedback, the AI will execute the **Ripple Effect Protocol**:

1.  **Analyze & Scope:** The AI will determine exactly what your change impacts across the four layers of continuity (Personal, Environment, Location, Story).
2.  **Identify Dependent Files:** The AI will scan the repository and find every document that is now out-of-sync due to your edit (e.g., Character Profiles, the World Bible, upcoming Chapter Briefs, Continuity Handovers).
3.  **Propose Changes (The Checkpoint):** The AI will generate a detailed list of *proposed* updates. It will tell you exactly which files it wants to change and how.
4.  **Wait for Authorization:** **The AI will not alter your files until you confirm.**
5.  **Execute the Ripple:** Once you say "Confirmed" or "Go ahead," the AI will rewrite the necessary sections in all affected documents, ensuring the project's internal logic remains perfectly consistent.

## Integrating with the Standard Pipeline

This flexible approach runs parallel to the standard 10-step pipeline outlined in the `futanari_repository_setup_guide.md`.

You might run Steps 1-5 automatically, stop the process to manually rewrite a plot point in the `story_ideas` document, trigger a Ripple Effect to update the AI's understanding, and then resume Steps 6-10 weeks later in a new session. The system will adapt to the files present in the directories.