import os
import argparse
import glob
import re

def analyze_text(text):
    """
    Analyzes extracted text to build a basic style guide.
    This is a foundational analyzer that extracts nouns, detects common sentence lengths,
    and builds a template. In a full implementation, this could call an LLM.
    """
    analysis = {}

    # 1. Very basic Concrete Noun Extraction (words > 4 letters, capitalized, or frequent)
    # This is a naive implementation; NLP libraries like spaCy would be better here.
    words = re.findall(r'\b[A-Za-z]+\b', text.lower())
    word_counts = {}
    for w in words:
        if len(w) > 4: # Ignore small common words
            word_counts[w] = word_counts.get(w, 0) + 1

    # Sort by frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    analysis['top_nouns_and_verbs'] = [w[0] for w in sorted_words[:50]]

    # 2. Sentence Length Variance (Burstiness)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]

    if sentences:
        lengths = [len(s.split()) for s in sentences]
        avg_len = sum(lengths) / len(lengths)
        analysis['avg_sentence_length'] = round(avg_len, 1)
        analysis['max_sentence_length'] = max(lengths)
        analysis['min_sentence_length'] = min(lengths)
    else:
         analysis['avg_sentence_length'] = 0
         analysis['max_sentence_length'] = 0
         analysis['min_sentence_length'] = 0

    return analysis

def build_style_guide(analysis, output_file):
    """Formats the analysis into a Markdown style guide document."""

    content = f"""# Auto-Generated Style Guide

This style guide was procedurally generated from OCR text samples.

## 1. Prose Burstiness & Rhythm
* **Average Sentence Length:** {analysis.get('avg_sentence_length', 0)} words
* **Variance Range:** {analysis.get('min_sentence_length', 0)} to {analysis.get('max_sentence_length', 0)} words

*Goal:* Ensure the LLM matches this rhythm when generating prose. Mix short, punchy sentences with longer descriptive ones.

## 2. Concrete Lexicon (Extracted)
The following frequently used words define the tone and texture of the source material. Prioritize using these or similar concrete terms:

{', '.join(analysis.get('top_nouns_and_verbs', []))}

## 3. Tropes & Subgenre (Manual Review Required)
Based on the text, manually define the applicable tropes and subgenres below:
* **Trope 1:** [To be filled]
* **Trope 2:** [To be filled]
* **Tone:** [e.g., Gritty, ethereal, high-tension]

## 4. Anti-AI Filtering
Remember to cross-reference this generated vocabulary with the active AI Blacklist to ensure no common AI tells (e.g., "intricate", "leverage") have slipped into the stylistic baseline.
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Style guide generated and saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Build a style guide from OCR text samples.")
    parser.add_argument("--input", default="samples/combined_ocr_output.md", help="Path to the combined OCR text file.")
    parser.add_argument("--output", default="style_guides/generated_style_guide.md", help="Path to save the generated style guide.")

    args = parser.parse_args()

    if not os.path.exists(args.input):
         print(f"Error: Input file {args.input} not found.")
         print("Please run ocr_with_structure.py first to generate the combined text sample.")
         return

    with open(args.input, 'r', encoding='utf-8') as f:
        text = f.read()

    print("Analyzing text...")
    analysis = analyze_text(text)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    build_style_guide(analysis, args.output)

if __name__ == "__main__":
    main()
