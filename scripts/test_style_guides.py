import re

def check_file(filepath):
    # Using stems/roots where appropriate to catch plurals/participles
    # e.g., 'delv' catches delve, delves, delving
    # 'tapestr' catches tapestry, tapestries
    tells = ['delv', 'tapestr', 'testament', 'delicate dance', 'intertwined',
             'crescendo', 'symphon', 'palpable', 'myriad', 'journey',
             'intricat', 'leverag', 'optimiz', 'optimis', 'facilitat', 'furthermore', 'moreover']

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

        # Added re.DOTALL so .*? matches across line breaks until it hits a period
        # Note: Fixed the regex pattern string from the issue to just have \.
        content = re.sub(r'Banned AI Tells:.*?\.', '', content, flags=re.IGNORECASE | re.DOTALL)

        content = content.lower()
        found = []

        for tell in tells:
            # Using \b to start at a word boundary, but allowing word characters \w* after the stem
            if re.search(r'\b' + tell + r'\w*\b', content):
                found.append(tell)

        if found:
            print(f"FAILED: {filepath} contains banned tells: {found}")
            return False
        else:
            print(f"PASSED: {filepath} is clean.")
            return True

if __name__ == '__main__':
    check_file('style_guides/gritty_blue_collar_futanari.txt')
    check_file('style_guides/contemporary_realistic.txt')
