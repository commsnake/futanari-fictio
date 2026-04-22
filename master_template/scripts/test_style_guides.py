import re

# Using stems/roots where appropriate to catch plurals/participles
# e.g., 'delv' catches delve, delves, delving
# 'tapestr' catches tapestry, tapestries
TELLS = ['delv', 'tapestr', 'testament', 'delicate dance', 'intertwined',
         'crescendo', 'symphon', 'palpable', 'myriad', 'journey']

# Combine into a single regex with alternation
# We use a capturing group around the stems to identify which one matched.
TELLS_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(tell) for tell in TELLS) + r')\w*\b', re.IGNORECASE)
BANNED_CLEANUP_PATTERN = re.compile(r'Banned AI Tells:.*?\.', re.IGNORECASE | re.DOTALL)

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

        # Remove the "Banned AI Tells" section to avoid false positives
        content = BANNED_CLEANUP_PATTERN.sub('', content)

        content = content.lower()

        # findall returns the content of the capturing group (the stem) for each match.
        # We use set() to get unique stems and sort them for consistent output.
        found = sorted(list(set(TELLS_PATTERN.findall(content))))

        if found:
            print(f"FAILED: {filepath} contains banned tells: {found}")
            return False
        else:
            print(f"PASSED: {filepath} is clean.")
            return True

if __name__ == '__main__':
    check_file('style_guides/gritty_blue_collar_futanari.txt')
    check_file('style_guides/contemporary_realistic.txt')
