# Futanari Writing Repository Setup Guide

Based on the established creative pipeline workflow, this document defines the requirements, directory structures, knowledge base assets, and scripts needed to set up a dedicated, automated repository for generating and organizing Futanari fiction.

---

## 1. Required Directory Structure

To maintain organization across the automated pipeline, the root repository must contain the following global directories for processing:

*   **`samples/`**: Destination for raw OCR outputs (`combined_*.md`) or Kindle scraped data.
*   **`output/`**: Destination for extracted intimate/spicy scenes (`spicy_scenes_*/extracted_scenes_*.md`).
*   **`style_guides/`**: Destination for genre analysis, trope mapping, and concrete nouns (`style_guide_*.md`, `concrete_nouns_*.txt`).
*   **`cache/`**: Destination for auto-detected subgenre and trope research data (`research_*.txt`).
*   **`story_ideas/`**: Destination for the generated 15-arc variations with stacked tropes and 14-beat Save the Cat structures (`story_ideas_*.md`).
*   **`reports/`**: The primary output directory for generated content, including the world bible (`4_world_bible.md`), cast ledger (`3_cast_ledger.md`), chapter drafts (`chapter_*.md`), and finalized prose (`chapter_*_final_final.md`).
*   **`reference/`**: Destination for reference materials.
*   **`marketing/`**: Destination for KDP marketing briefs and title drafts.
*   **`world_building/`**: Destination for the project world bibles.
*   **`templates/`**: Destination for chapter and character profile templates.
*   **`scripts/`**: Destination for python scripts used in generation.
*   **`ai_tells_prevention/`**: Destination for AI tell prevention blacklists and protocols.
*   **`knowledge_base/`**: Destination for all KB guidelines.
*   **`master_template/`**: Destination for genre-agnostic version of the AI writing system.

### Individual Project Structure
Once a story idea is selected and generated, it should be organized into its own dedicated project folder (e.g., `My_Futanari_Story_Book1/`) containing:
*   `chapters/` (Finalized chapter markdown files)
*   `research/` (Seed specifications and research text)
*   `style_guide/` (Specific style guide for the book)
*   `story_ideas/` (The selected beat sheet and synopsis)
*   `bible/` (The specific cast ledger and world bible)
*   `data/` (Extracted scenes and concrete nouns)

---

## 2. Knowledge Base (KB) Requirements

The core of the procedural generation relies on a strictly defined knowledge base. A dedicated `knowledge_base/` directory must be present, containing the following core documents tailored to the Futanari genre:

1.  **`01_narrative_architecture.md` (KB-01)**
    *   *Purpose:* Defines the 8-phase erotic cycle (Hook → Lead-In → Dynamic Shift → Core Act → Escalation → Climax → Melt → Aftercare).
    *   *Requirement:* Must include H-KIS intensity levels (1-5) and a Heat Ladder tailored to the specific pacing of Futanari romance/erotica.
2.  **`02_lexicon_and_prose_rules.md` (KB-02)**
    *   *Purpose:* Defines the anatomical lexicon specific to the genre.
    *   *Requirement:* Must include specific Futanari anatomical terminology, banned terms, prose style protocols, and strict instructions on AI tell avoidance.
3.  **`03_psychology_and_dynamics.md` (KB-03)**
    *   *Purpose:* Outlines character psychology and power dynamics.
    *   *Requirement:* Must define the Anchor/Seeker dyad model, Authority Gaps (Competence, Emotional, Physical), and Vulnerability Triggers, which are highly relevant in Futanari "Reveal" and "Transformation" tropes.
4.  **`04_spice_trope_library.md` (KB-04)**
    *   *Purpose:* A library of Spice trope IDs (e.g., VOY-01 to SYM-10).
    *   *Requirement:* Must include a usage guide for scene generation, specifically adapted to include common Futanari tropes (Size Difference, Secret Futa, Breeding, Forced Proximity).
5.  **`05_common_sex_positions.md` (KB-05)**
    *   *Purpose:* Standard sexual positions used.
6.  **`06_advanced_positions.md` (KB-06)**
    *   *Purpose:* Advanced sexual positions used.
7.  **`07_world_lore_and_biology.md` (KB-07)**
    *   *Purpose:* Lore on world building and biology.
8.  **`08_brand_and_copyright_guidelines.md` (KB-08)**
    *   *Purpose:* Enforces brand, trademark, and copyright rules. Relying on Nominative Fair Use but restricting brands from illegal/negative context.
9.  **`09_continuity_enforcement_strategy.md` (KB-09)**
    *   *Purpose:* Enforces multi-layer continuity strategy tracking immutable/mutable traits and mandatory Continuity Handover.
10. **`10_spatial_blocking_system.md` (KB-10)**
    *   *Purpose:* Outlines the Kinematic Scene Blocking Matrix (KSBM) for the Anti-Pretzel spatial physics checks.
11. **`11_futanari_on_male_mechanics.md` (KB-11)**
    *   *Purpose:* Establishes instructions and adaptations for Futanari-on-Male anal sex. Focuses on mechanics and sensory contrast.

---

## 3. Core Pipeline Scripts & Tools

The repository requires a suite of Python scripts to automate the creative pipeline. These scripts must be located in the root directory (or managed via a dedicated skills agent):

| Script | Layer | Purpose | KB Used |
| :--- | :---: | :--- | :---: |
| `ocr_with_structure.py` / `kindle_scraper.py` | 1 | Inputs source material via screenshots or direct Kindle app capture. | - |
| `spicy_editor.py` | 1 | Extracts spicy scenes and keywords from the input text. | - |
| `style_guide_builder.py` | 1 | Analyzes genre, voice, and tropes to build a cohesive style guide. | - |
| `research_scraper.py` | 1 | Auto-detects subgenres (specifically flagging Futanari) and builds the research cache. | - |
| `generate_story_ideas.py` | 1 | Uses the research cache to output 15 story arcs featuring stacked tropes, 14-beat Save the Cat structures, and open threads for sequels. | - |
| `bible_synthesizer.py` | 2 | Generates the `3_cast_ledger.md` and `4_world_bible.md` based on the selected story idea. | KB-03, KB-04 |
| `prose_drafter.py` / `prose_prompt_generator.py`| 3 | Generates chapter prose (or prompts for external AI generation) based on the arcs and bibles. | KB-01, KB-02 |
| `character_generator.py` | 4 | Procedurally generates character profiles and standardizes via templates. | - |
| `sync_to_master.py` | 4 | Synchronizes any new rules, templates, or code added to the main repository to the master template folder. | - |
| `test_style_guides.py` | 4 | Validates text files. | - |

*(Note: The previously mentioned `anti_ai_filter.py` script is missing. AI tell checks must currently be performed manually via regex/grep or `test_style_guides.py`.)*

---

## 4. The 8-Step Workflow Summary

To fully utilize the repository, the following workflow is executed:

1.  **Input:** Capture raw text using `ocr_with_structure.py` or `kindle_scraper.py`.
2.  **Extraction:** Run `spicy_editor.py` to isolate intimate scenes.
3.  **Style Analysis:** Run `style_guide_builder.py` to establish the tone.
4.  **Research & Subgenre Detection:** Run `research_scraper.py` to categorize the tropes and confirm the Futanari subgenre.
5.  **Story Generation:** Run `generate_story_ideas.py` to create multiple 14-beat arcs.
6.  **World Building:** Run `bible_synthesizer.py` to solidify characters and settings.
7.  **Drafting:** Generate the prose using internal LLMs or by passing outputs from `prose_prompt_generator.py` to an external AI session to bypass explicit content filters.
8.  **Refinement:** Run manual regex/grep or `test_style_guides.py` to polish the final chapter files.
