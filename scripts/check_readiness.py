import argparse
import os

def check_readiness(file_path):
    print(f"Checking readiness for file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    # Critical fields required for drafting
    required_keywords = [
        "stakes",
        "flaw",
        "antagonist",
        "conflict",
        "premise"
    ]

    missing_fields = []
    for keyword in required_keywords:
        if keyword not in content:
            missing_fields.append(keyword)

    print("\n--- BBB READINESS REPORT ---")

    score = (len(required_keywords) - len(missing_fields)) / len(required_keywords) * 100
    print(f"Completeness Score: {score}%")

    if missing_fields:
        print("\nCritical Gaps (Unresolved):")
        for field in missing_fields:
            print(f"- Missing element related to: {field}")

        print("\nHANDOFF STATE: NOT_READY")
        print("Please provide the missing critical fields before proceeding to generation.")
    else:
        print("\nCritical Gaps: None")
        print("\nHANDOFF STATE: READY")
        print("The dossier is complete and ready for the Evaluation Squad.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a dossier has the critical fields required for drafting.")
    parser.add_argument("--file", required=True, help="Path to the markdown file to check.")
    args = parser.parse_args()

    check_readiness(args.file)
