import argparse
import os

def generate_blurb(title, tropes, subgenre):
    blurb = f"**{title}**\n\n"
    blurb += f"A thrilling {subgenre} romance featuring: {', '.join(tropes)}.\n\n"
    blurb += "[Placeholder for dynamic summary generated from manuscript beats]\n\n"
    blurb += "Warning: This book contains explicit content, consensual non-consent elements, and is intended for mature audiences 18+ only."
    return blurb

def generate_keywords(tropes, subgenre):
    keywords = [subgenre.lower(), "romance", "steamy", "explicit", "erotica"]
    for trope in tropes:
        keywords.append(trope.lower().replace(" ", " "))
    return keywords[:7] # Amazon KDP allows 7 keyword slots

def main():
    parser = argparse.ArgumentParser(description="Generate KDP metadata (blurb, keywords, etc.)")
    parser.add_argument("--title", required=True, help="Title of the book")
    parser.add_argument("--subgenre", required=True, help="Primary subgenre")
    parser.add_argument("--tropes", nargs='+', required=True, help="List of primary tropes")
    parser.add_argument("--output", default="marketing/metadata_draft.md", help="Output file path")

    args = parser.parse_args()

    blurb = generate_blurb(args.title, args.tropes, args.subgenre)
    keywords = generate_keywords(args.tropes, args.subgenre)

    metadata = f"# KDP Metadata for: {args.title}\n\n"
    metadata += "## Generated Blurb\n"
    metadata += blurb + "\n\n"
    metadata += "## Amazon KDP Keywords (Max 7)\n"
    for i, kw in enumerate(keywords):
        metadata += f"{i+1}. {kw}\n"

    metadata += "\n## A+ Content Suggestions\n"
    metadata += "*   **Header Image:** 970 x 250 px - High contrast, featuring a mood-setting background (e.g., stormy seas for a longliner story) and the book title in bold typography.\n"
    metadata += "*   **Standard 3 Image & Text Module:** Three 300 x 300 px images highlighting specific character traits or tropes (e.g., 'Alpha Futanari', 'Blue Collar Romance', 'Size Difference').\n"
    metadata += "*   **Standard Product Description Text:** A stylized version of the blurb with bolded key phrases.\n"

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        f.write(metadata)

    print(f"Generated KDP metadata at {args.output}")

if __name__ == "__main__":
    main()
