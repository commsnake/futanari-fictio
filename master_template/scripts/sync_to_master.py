import os
import shutil
import re

def genericize_text(content):
    # Genericize terms specific to this repo for the master template
    content = re.sub(r'Futanari', '[Genre/Theme]', content, flags=re.IGNORECASE)
    return content

def genericize_filename(item):
    return re.sub(r'futanari', 'genre_theme', item, flags=re.IGNORECASE)

def sync_directory(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)

        dest_item = genericize_filename(item)
        dest_path = os.path.join(dest_dir, dest_item)

        if os.path.isdir(src_path):
            sync_directory(src_path, dest_path)
        else:
            # We only process text-based files for regex replacements
            if src_path.endswith(('.md', '.py', '.txt')) and src_path != 'scripts/sync_to_master.py':
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                content = genericize_text(content)

                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                shutil.copy2(src_path, dest_path)

def sync():
    dirs_to_sync = ['knowledge_base', 'templates', 'scripts', 'ai_tells_prevention', 'marketing', 'style_guides']

    for d in dirs_to_sync:
        print(f"Syncing {d} to master_template/{d}...")
        sync_directory(d, os.path.join('master_template', d))

    print("Sync complete.")

if __name__ == '__main__':
    sync()
