import re
import argparse
import sys
import os

def load_blacklist(filepath):
    blacklist = []
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        return blacklist

    with open(filepath, 'r') as f:
        content = f.read()

    # Extract words/phrases from markdown lists (lines starting with * **)
    matches = re.findall(r'^\*\s+\*\*([^*]+)\*\*', content, re.MULTILINE)
    for match in matches:
        # Clean up the term (remove e.g. parenthetical examples if any made it in, though the regex mostly grabs the bolded part)
        term = match.strip()
        blacklist.append(term)

    # Also find phrases in quotes in specific sections
    quoted_matches = re.findall(r'\*\*\"([^\"]+)\"\*\*', content)
    for match in quoted_matches:
        term = match.strip()
        blacklist.append(term)

    return [t.lower() for t in blacklist]

def analyze_file(filepath, blacklist):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r') as f:
        text = f.read()

    lines = text.split('\n')

    findings = []

    # 1. Overused Vocabulary (Blacklist)
    for term in blacklist:
        # Create a boundary-safe regex, escaping special characters
        escaped_term = re.escape(term)
        # Using word boundaries for alphabetic strings
        pattern = r'\b' + escaped_term + r'\b' if re.search(r'\w$', term) else escaped_term

        for i, line in enumerate(lines):
            matches = re.finditer(pattern, line.lower())
            for match in matches:
                findings.append({
                    'type': 'vocabulary',
                    'term': term,
                    'line': i + 1,
                    'context': line.strip()[:100] # Provide snippet
                })

    # 2. Structural Patterns
    # "X vs Y" or "Not X, but Y"
    pattern_not_but = re.compile(r'(not\s+[^,]+,\s*but\s+[^.]+)', re.IGNORECASE)
    for i, line in enumerate(lines):
        matches = re.finditer(pattern_not_but, line)
        for match in matches:
            findings.append({
                'type': 'structural',
                'term': "Not X, but Y pattern",
                'line': i + 1,
                'context': line.strip()[:100]
            })

    # Summaries (In conclusion, ultimately)
    summary_patterns = [
        re.compile(r'\bin conclusion\b', re.IGNORECASE),
        re.compile(r'\bultimately\b', re.IGNORECASE),
        re.compile(r'\bas they looked at each other\b', re.IGNORECASE)
    ]
    for pattern in summary_patterns:
        for i, line in enumerate(lines):
            matches = re.finditer(pattern, line)
            for match in matches:
                findings.append({
                    'type': 'summary',
                    'term': "Summary conclusion pattern",
                    'line': i + 1,
                    'context': line.strip()[:100]
                })

    return findings

def print_report(findings):
    if not findings:
        print("No AI tells found. Good job!")
        return

    print(f"Found {len(findings)} potential AI tells:")
    print("-" * 50)
    for f in sorted(findings, key=lambda x: x['line']):
        print(f"Line {f['line']}: [{f['type'].upper()}] '{f['term']}'")
        print(f"  Context: {f['context']}")
    print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description="Analyze text for AI tells.")
    parser.add_argument("file", help="Path to the markdown file to analyze")
    parser.add_argument("--blacklist", default="ai_tells_prevention/01_overused_vocabulary.md",
                        help="Path to the blacklist markdown file")

    args = parser.parse_args()

    blacklist = load_blacklist(args.blacklist)
    if not blacklist:
        print("Could not load blacklist. Exiting.")
        sys.exit(1)

    findings = analyze_file(args.file, blacklist)
    print_report(findings)

if __name__ == "__main__":
    main()
