import re

def check_file(filepath):
    # 'just' and 'very' are allowed as part of words (like 'violently' has 'very' in 'ery' - actually it doesn't but grep matched 'Every')
    tells = ['delve', 'tapestry', 'testament', 'delicate dance', 'intertwined', 'crescendo', 'symphony', 'palpable', 'myriad', 'journey']
    with open(filepath, 'r') as f:
        content = f.read()

        # We should exclude the Banned AI Tells list section from this check
        content = re.sub(r'Banned AI Tells:.*?\.', '', content, flags=re.IGNORECASE)

        content = content.lower()
        found = []
        for tell in tells:
            if re.search(r'\b' + tell + r'\b', content):
                found.append(tell)

        if found:
            print(f"FAILED: {filepath} contains banned tells: {found}")
            return False
        else:
            print(f"PASSED: {filepath} is clean.")
            return True

check_file('style_guides/gritty_blue_collar_futanari.txt')
check_file('style_guides/contemporary_realistic.txt')
