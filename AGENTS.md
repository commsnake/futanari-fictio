# Agent Guidelines

Welcome, AI Agent! This repository follows a strict procedural pipeline for generating fiction. When working within this repository, you must adhere to the following rules.

## 1. The Master Template Synchronization Rule

We maintain a `master_template/` directory that contains a generic, genre-agnostic version of this writing system (rules, structure, templates, code, etc.).

**Crucial Instruction:** Whenever you are asked to apply a new system, create a new rule, add a template, or write code for the primary repository structure, you **MUST** ensure those changes are synchronized to the `master_template/` directory.

To do this:
1. Make your required changes, additions, or modifications to the primary directories (e.g., `knowledge_base/`, `marketing/`, `style_guides/`, `ai_tells_prevention/`, etc.).
2. Once your changes are complete, you MUST run the synchronization script from the repository root:
   ```bash
   python3 sync_to_master.py
   ```
3. This script will automatically copy the updated files to the `master_template/` directory and replace any genre-specific terms (like "Futanari") with the generic placeholder `[Genre/Theme]`.
4. Verify that the script ran successfully and the files in `master_template/` reflect your additions in a generalized format.

## 2. General Operations
- Obey all constraints defined within the `knowledge_base/` and `ai_tells_prevention/` directories when generating narrative content.
- Ensure all narrative outputs adhere to the Anti-Pretzel protocol (physically possible movements) and continuity rules.
