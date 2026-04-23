import re
import os
import argparse
import subprocess
import json

def validate_path(path, base_dir=None):
    """
    Validates that the path is within the base directory to prevent path traversal.
    Defaults to the repository root as the base directory.
    Uses realpath to resolve symlinks and commonpath to prevent sibling directory bypasses.
    """
    if base_dir is None:
        # Assume repo root is the parent of the scripts directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    real_path = os.path.realpath(path)
    real_base = os.path.realpath(base_dir)

    if os.path.commonpath([real_path, real_base]) != real_base:
        raise ValueError(f"Access denied: {path} is outside of {base_dir}")
    return real_path

def load_knowledge_base(kb_path):
    kb_data = {}
    if not os.path.exists(kb_path):
        print(f"Warning: Knowledge base path {kb_path} not found.")
        return kb_data

    for root, dirs, files in os.walk(kb_path):
        for file in files:
            if file.endswith(".md") or file.endswith(".txt"):
                filepath = os.path.join(root, file)
                # Use filename as a rough key, without extension
                key = os.path.splitext(file)[0].lower()
                # For character profiles, remove '_profile'
                if key.endswith('_profile'):
                    key = key.replace('_profile', '')

                with open(filepath, 'r') as f:
                    kb_data[key] = f.read()
    return kb_data

def find_entities_in_prompt(prompt_text, kb_keys):
    found_keys = []
    lower_prompt = prompt_text.lower()
    for key in kb_keys:
        # Simple string match. For robustness, regex with word boundaries could be used.
        if re.search(r'\b' + re.escape(key) + r'\b', lower_prompt):
            found_keys.append(key)
    return found_keys

def extract_book_chapter_from_filename(filename):
    """Attempt to extract Book and Chapter numbers from the filename."""
    match = re.search(r'book(\d+).*?chapter(\d+)', filename.lower())
    if match:
        return match.group(1), match.group(2)
    return None, None

def get_timeline_context(book, chapter):
    """Calls timeline_manager.py to get the timeline state."""
    try:
        # Assuming timeline_manager.py is in the same directory as codex_injector.py
        manager_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'timeline_manager.py')
        result = subprocess.run(
            ['python3', manager_path, 'get-state', book, chapter],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to fetch timeline state. {e.stderr}")
        return ""
    except FileNotFoundError:
        print("Warning: timeline_manager.py not found.")
        return ""

def inject_codex(prompt_file, kb_path, output_file):
    try:
        prompt_file = validate_path(prompt_file)
        kb_path = validate_path(kb_path)
        output_file = validate_path(output_file)
    except ValueError as e:
        print(f"Security Error: {e}")
        return False

    if not os.path.exists(prompt_file):
        print(f"Error: Prompt file {prompt_file} not found.")
        return False

    with open(prompt_file, 'r') as f:
        prompt_text = f.read()

    injected_prompt = prompt_text

    # Extract Timeline Data
    book, chapter = extract_book_chapter_from_filename(os.path.basename(prompt_file))
    if book and chapter:
        print(f"Detected Book {book}, Chapter {chapter}. Injecting Timeline Data...")
        timeline_context = get_timeline_context(book, chapter)
        if timeline_context:
            injected_prompt += "\n\n### Injected Timeline & Macro-Spatial Context ###\n"
            injected_prompt += timeline_context

    kb_data = load_knowledge_base(kb_path)
    if not kb_data:
        return False

    found_entities = find_entities_in_prompt(prompt_text, kb_data.keys())

    if not found_entities:
        print("No dynamic entities found in prompt.")
    else:
        print(f"Found entities: {', '.join(found_entities)}")
        injected_prompt += "\n\n### Injected Codex Context ###\n"
        for entity in found_entities:
            injected_prompt += f"\n--- Context for: {entity} ---\n"
            # Just take the first 1000 characters to avoid massive context bloat
            injected_prompt += kb_data[entity][:1000] + "...\n"

    with open(output_file, 'w') as f:
        f.write(injected_prompt)

    print(f"Injected prompt saved to {output_file}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Inject Codex/KB info into prompts dynamically.")
    parser.add_argument("prompt_file", help="Path to the draft prompt or chapter brief")
    parser.add_argument("--kb_path", default="templates/character_profiles", help="Path to the directory containing character profiles or world bible elements")
    parser.add_argument("--output", default="output/injected_prompt.md", help="Output file path")

    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    inject_codex(args.prompt_file, args.kb_path, args.output)

if __name__ == "__main__":
    main()
