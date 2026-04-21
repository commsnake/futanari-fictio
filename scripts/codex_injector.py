import re
import os
import argparse

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

def inject_codex(prompt_file, kb_path, output_file):
    if not os.path.exists(prompt_file):
        print(f"Error: Prompt file {prompt_file} not found.")
        return False

    with open(prompt_file, 'r') as f:
        prompt_text = f.read()

    kb_data = load_knowledge_base(kb_path)
    if not kb_data:
        return False

    found_entities = find_entities_in_prompt(prompt_text, kb_data.keys())

    if not found_entities:
        print("No dynamic entities found in prompt.")
        injected_prompt = prompt_text
    else:
        print(f"Found entities: {', '.join(found_entities)}")
        injected_prompt = prompt_text + "\n\n### Injected Codex Context ###\n"
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
