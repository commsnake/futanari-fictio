# Agent Instructions

## Synchronization Requirement
This repository utilizes a `master_template/` directory which acts as a genre-agnostic version of the AI writing system.

**Rule:** Any new rules, templates, or code added to the main repository (specifically in `knowledge_base/`, `templates/`, `scripts/`, `ai_tells_prevention/`, or `marketing/`) MUST be synchronized to the master template folder.

To do this, you must run the following script after making your changes:
`python3 scripts/sync_to_master.py`

This script will automatically copy your changes and genericize domain-specific terms (like "Futanari") into placeholders like `[Genre/Theme]`.
