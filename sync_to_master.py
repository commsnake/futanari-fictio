import os
import shutil
import re

# Define the source directories and their destination in the master template
SYNC_MAP = {
    'knowledge_base': 'master_template/knowledge_base',
    'ai_tells_prevention': 'master_template/ai_tells_prevention',
    'marketing': 'master_template/marketing',
    'style_guides': 'master_template/style_guides',
    'scripts': 'master_template/scripts',
    'reference': 'master_template/reference',
}

# Individual files to sync that might not be in a specific folder mapped above
FILE_MAP = {
    'futanari_repository_setup_guide.md': 'master_template/repository_setup_guide.md',
    'test_style_guides.py': 'master_template/scripts/test_style_guides.py',
    'chapter brief template.pdf': 'master_template/reference/chapter brief template.pdf',
    'generate_style_guide_prompt.md': 'master_template/style_guides/generate_style_guide_prompt.md'
}

def genericize_text(text):
    """Replaces genre-specific terms with generic placeholders."""
    text = re.sub(r'Futanari', '[Genre/Theme]', text)
    text = re.sub(r'futanari', '[genre-theme]', text) # Replaced slash to avoid directory issues
    text = re.sub(r'Futa', '[Genre/Theme]', text)
    text = re.sub(r'futa', '[genre-theme]', text)
    return text

def sync_file(src, dest):
    """Syncs a single file, genericizing text files and filenames."""
    if not os.path.exists(src):
        print(f"Source file missing, skipping: {src}")
        return

    # Genericize the destination filename
    dest_dir = os.path.dirname(dest)
    dest_file = os.path.basename(dest)

    # We shouldn't use slashes in filenames
    generic_dest_file = dest_file.replace('Futanari', '[Genre-Theme]')
    generic_dest_file = generic_dest_file.replace('futanari', '[genre-theme]')
    generic_dest_file = generic_dest_file.replace('Futa', '[Genre-Theme]')
    generic_dest_file = generic_dest_file.replace('futa', '[genre-theme]')

    dest = os.path.join(dest_dir, generic_dest_file)

    os.makedirs(os.path.dirname(dest), exist_ok=True)

    # Text-based files to genericize
    if src.endswith(('.md', '.txt', '.py')):
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()

        generic_content = genericize_text(content)

        # Specific hack for test_style_guides.py script paths
        if 'test_style_guides.py' in dest:
            generic_content = generic_content.replace(
                "'style_guides/gritty_blue_collar_[genre-theme].txt'",
                "'../style_guides/generate_style_guide_prompt.md'"
            )
            # Remove specific lines that aren't generic
            lines = generic_content.split('\n')
            generic_content = '\n'.join([line for line in lines if "check_file('style_guides/contemporary_realistic.txt')" not in line])

        with open(dest, 'w', encoding='utf-8') as f:
            f.write(generic_content)
        print(f"Genericized and copied: {src} -> {dest}")
    else:
        # Binary or non-text files just get copied
        shutil.copy2(src, dest)
        print(f"Copied: {src} -> {dest}")

def main():
    print("Starting sync to master_template...")

    # Make sure master_template subdirectories exist
    for _, dest_dir in SYNC_MAP.items():
        os.makedirs(dest_dir, exist_ok=True)

    # Sync directories
    for src_dir, dest_dir in SYNC_MAP.items():
        if not os.path.exists(src_dir):
            continue

        for root, _, files in os.walk(src_dir):
            for file in files:
                src_path = os.path.join(root, file)
                # Build destination path
                rel_path = os.path.relpath(src_path, src_dir)
                dest_path = os.path.join(dest_dir, rel_path)

                sync_file(src_path, dest_path)

    # Sync specific files
    for src_file, dest_file in FILE_MAP.items():
        # if file is already inside one of the sync_map directories, we might have copied it
        # but let's ensure these specific mappings are respected
        if os.path.exists(src_file):
             sync_file(src_file, dest_file)

    print("Sync complete.")

if __name__ == '__main__':
    main()
