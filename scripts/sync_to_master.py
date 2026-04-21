import os
import shutil
import re

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def sync_file(src_path, dest_path):
    print(f"Syncing {src_path} to {dest_path}")
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace domain-specific terms with generic placeholders
    # In this case, we replace "Futanari", "futanari", "Futa", "futa"
    content = re.sub(r'\bFutanari\b', '[Genre/Theme]', content)
    content = re.sub(r'\bfutanari\b', '[genre/theme]', content)
    content = re.sub(r'\bFuta\b', '[Genre/Theme]', content)
    content = re.sub(r'\bfuta\b', '[genre/theme]', content)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_dirs_to_sync = ['scripts', 'knowledge_base', 'ai_tells_prevention', 'marketing', 'reference', 'style_guides', 'templates']
    root_files_to_sync = ['AGENTS.md', 'master_workflow.md']

    master_template_dir = 'master_template'

    for file_name in root_files_to_sync:
        if os.path.exists(file_name):
            sync_file(file_name, os.path.join(master_template_dir, file_name))

    for dir_name in root_dirs_to_sync:
        src_dir = dir_name
        if not os.path.exists(src_dir):
            continue

        dest_dir = os.path.join(master_template_dir, dir_name)
        ensure_dir(dest_dir)

        for root, dirs, files in os.walk(src_dir):
            # Calculate relative path to maintain subdirectories
            rel_path = os.path.relpath(root, src_dir)

            # Ensure subdirectory exists in master_template
            if rel_path != '.':
                current_dest_dir = os.path.join(dest_dir, rel_path)
                ensure_dir(current_dest_dir)
            else:
                current_dest_dir = dest_dir

            for file in files:
                # Skip pycache or hidden files
                if file.startswith('.') or '__pycache__' in root:
                    continue

                src_file = os.path.join(root, file)
                dest_file = os.path.join(current_dest_dir, file)

                sync_file(src_file, dest_file)

if __name__ == "__main__":
    main()
