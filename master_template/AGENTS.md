# AI Agent Instructions for Project Repository

Welcome to the [Genre/Theme] Writing Repository. As an AI Agent working within this project, you must adhere to the following master workflow constraints and behavioral guidelines.

## Master Workflow Constraints

The workflow in this repository is designed to be **highly flexible and non-linear**. You are expected to adapt to the user's current needs and seamlessly resume work from any state.

### 1. Flexible Execution (State Assessment)
Before initiating any generation task or responding to a prompt, you must first assess the current state of the project. This means the workflow can be started or stopped at any point.

When beginning a new session or resuming work, you must:
1.  **Analyze the file hierarchy:** Look for the most recently updated files in directories such as `story_ideas/`, `reports/`, `world_building/`, `style_guides/`, etc.
2.  **Determine the current phase:** Identify which of the 10 workflow steps (as defined in `futanari_repository_setup_guide.md`) is currently active based on existing artifacts. For instance, if `reports/4_world_bible.md` exists but no `reports/chapter_1.md` exists, you know the next logical step is to begin drafting chapters.
3.  **Prompt the User:** If the next logical step is ambiguous, ask the user how they wish to proceed based on your state assessment.

### 2. The "Ripple Effect" Protocol (Handling Feedback & Edits)
The user will frequently edit your outputs manually or provide explicit feedback requesting changes to existing documents. When this happens, you must execute the Ripple Effect Protocol to maintain strict multi-layer continuity (Personal, Environment, Location, Story) across the entire project.

Whenever the user submits a change, edit, or feedback, you MUST follow these steps:

1.  **Analyze the Edit:** Understand the specific change the user has made or requested (e.g., changed a character's eye color, altered a plot beat, shifted a location in a chapter).
2.  **Identify Dependent Artifacts:** Scan the knowledge base and project files to identify all other documents that will be affected by this change. This may include, but is not limited to:
    *   The Cast Ledger (`3_cast_ledger.md`) or Character Profiles.
    *   The World Bible (`4_world_bible.md`).
    *   The Beat Sheet/Story Ideas (`story_ideas_*.md`).
    *   Chapter Briefs or future planned outlines.
    *   Continuity Handovers (especially Residual Tension Types) between already generated chapters.
3.  **List Proposed Effects (Crucial Step):** **DO NOT implement the changes immediately.** You must first generate a clear, comprehensive list of all the files that need to be updated and exactly how they will be modified to maintain continuity.
4.  **Wait for Confirmation:** Present the list of proposed effects to the user and ask for their explicit confirmation to proceed.
5.  **Implement:** Only upon receiving user confirmation, execute the updates across all identified files.

## Syncing Rules to Master Repository
Any time you create a new structural rule, template, script, or update this `AGENTS.md` file, you must remember the genericization rule.

*   You must immediately run `python3 scripts/sync_to_master.py` to ensure the updates are copied to the `master_template/` folder and that any domain-specific terminology (like "[Genre/Theme]") is replaced with generic placeholders (like `[Genre/Theme]`).