import argparse
import os

def evaluate_dossier(file_path):
    print(f"Evaluating file: {file_path}")
    print("Simulating Dossier Evaluation Squad...\n")

    # Read file content for basic keyword checks
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    # Basic keyword checks
    has_structure = any(word in content for word in ["act", "beat", "spine", "chapter"])
    has_character = any(word in content for word in ["protagonist", "flaw", "want", "need", "character"])
    has_world = any(word in content for word in ["world", "location", "setting", "rules"])
    has_pacing = any(word in content for word in ["escalation", "stakes", "climax", "tension"])
    has_market = any(word in content for word in ["genre", "tropes", "audience", "market"])

    # Simulate scores based on keywords
    atlas_score = 8 if has_structure else 3
    psych_score = 9 if has_character else 4
    nova_score = 7 if has_world else 3
    tempo_score = 8 if has_pacing else 2
    niche_score = 9 if has_market else 4

    print("--- 1. ATLAS (Structure & Causality) ---")
    print(f"Score: {atlas_score}/10")
    print(f"Verdict: {'Solid' if atlas_score >= 7 else 'STOP. Missing structural elements.'}")
    print("\n--- 2. PSYCH (Character Logic) ---")
    print(f"Score: {psych_score}/10")
    print(f"Verdict: {'Greenlight' if psych_score >= 9 else 'STOP. Missing character depth.'}")
    print("\n--- 3. NOVA (World Integrity) ---")
    print(f"Score: {nova_score}/10")
    print(f"Verdict: {'Solid' if nova_score >= 7 else 'STOP. Missing world rules.'}")
    print("\n--- 4. TEMPO (Pacing Architecture) ---")
    print(f"Score: {tempo_score}/10")
    print(f"Verdict: {'Solid' if tempo_score >= 7 else 'STOP. Missing pacing cues.'}")
    print("\n--- 5. NICHE (Market/Genre Alignment) ---")
    print(f"Score: {niche_score}/10")
    print(f"Verdict: {'Greenlight' if niche_score >= 9 else 'STOP. Missing genre alignment.'}")

    print("\n--- CONSENSUS SUMMARY ---")
    scores = [atlas_score, psych_score, nova_score, tempo_score, niche_score]
    lowest_score = min(scores)

    if lowest_score <= 4:
        print("\nFOUNDATION VERDICT: STOP - REPAIR LOOP REQUIRED.")
        print("One or more personas scored 4 or below. Drafting is blocked.")
        print("Next Steps: Address the missing elements flagged by the evaluation squad.")
    elif lowest_score <= 6:
        print("\nFOUNDATION VERDICT: CAUTION.")
        print("Drafting can proceed, but review the flagged areas for improvement.")
    else:
        print("\nFOUNDATION VERDICT: GREENLIGHT.")
        print("All personas approve. Drafting may proceed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a story dossier or outline using the Dossier Evaluation Squad personas.")
    parser.add_argument("--file", required=True, help="Path to the markdown file to evaluate.")
    args = parser.parse_args()

    evaluate_dossier(args.file)
