import os
import argparse
import re

TIMELINE_DIR = "world_building/longliner_story_bible/timelines"

def get_state(book, chapter):
    """
    Parses existing timelines to extract current state for a given Book and Chapter.
    """
    state = {
        "book": book,
        "chapter": chapter,
        "sea_conditions": "Unknown",
        "character_positions": {}
    }

    sea_timeline_path = os.path.join(TIMELINE_DIR, "00_overarching_timeline_and_sea_conditions.md")
    positions_timeline_path = os.path.join(TIMELINE_DIR, "06_character_positions_timeline.md")

    # Parse Sea Conditions
    if os.path.exists(sea_timeline_path):
        with open(sea_timeline_path, 'r') as f:
            content = f.read()
            # Find the section for the specific book
            book_section = re.search(rf"## Book {book} Breakdown:(.*?)(?=## Book |$)", content, re.DOTALL)
            if book_section:
                # Find the row for the chapter
                rows = re.findall(r"\|(.*?)\|(.*?)\|(.*?)\|", book_section.group(1))
                for row in rows:
                    chapters_range = row[0].strip().replace("**", "")
                    if "-" in chapters_range:
                        try:
                            start, end = map(int, chapters_range.split("-"))
                            if start <= int(chapter) <= end:
                                state["sea_conditions"] = row[2].strip()
                                break
                        except ValueError:
                            pass
                    elif chapters_range == str(chapter):
                        state["sea_conditions"] = row[2].strip()
                        break

    # Parse Character Positions
    if os.path.exists(positions_timeline_path):
        with open(positions_timeline_path, 'r') as f:
            content = f.read()
            book_section = re.search(rf"### Book {book}:(.*?)(?=### Book |$)", content, re.DOTALL)
            if book_section:
                rows = re.findall(r"\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|", book_section.group(1))
                for row in rows:
                    # Skip header/separator rows
                    if '---' in row[0] or 'Chapter' in row[0]:
                        continue

                    chapters_range = row[0].strip().replace("**", "")
                    match = False
                    if "-" in chapters_range:
                        try:
                            start, end = map(int, chapters_range.split("-"))
                            if start <= int(chapter) <= end:
                                match = True
                        except ValueError:
                            pass
                    elif chapters_range == str(chapter):
                        match = True

                    if match:
                        state["character_positions"] = {
                            "Context": row[1].strip(),
                            "Captain": row[2].strip(),
                            "First Mate": row[3].strip(),
                            "Engineer": row[4].strip(),
                            "Deck Boss": row[5].strip(),
                            "Deckhand": row[6].strip(),
                            "Leo": row[7].strip()
                        }
                        break
    return state

def create_timeline(name, template="standard"):
    """
    Scaffolds a new timeline document.
    """
    os.makedirs(TIMELINE_DIR, exist_ok=True)

    # Simple numbering scheme for new files
    existing_files = [f for f in os.listdir(TIMELINE_DIR) if f.endswith('.md')]
    highest_num = 0
    for f in existing_files:
        try:
            num = int(f.split('_')[0])
            if num > highest_num:
                highest_num = num
        except ValueError:
            pass

    new_num = highest_num + 1
    new_filename = f"{new_num:02d}_{name.lower().replace(' ', '_')}.md"
    new_filepath = os.path.join(TIMELINE_DIR, new_filename)

    with open(new_filepath, 'w') as f:
        f.write(f"# {new_num:02d}. {name}\n\n")
        f.write("This timeline tracks [Entity] across the overarching Book/Chapter structure.\n\n")
        f.write("## Book 1\n| Chapter | State |\n| :--- | :--- |\n| 1 | ... |\n\n")
        f.write("## Book 2\n| Chapter | State |\n| :--- | :--- |\n| 1 | ... |\n\n")
        f.write("## Book 3\n| Chapter | State |\n| :--- | :--- |\n| 1 | ... |\n")

    print(f"Created new timeline: {new_filepath}")
    return new_filepath

def main():
    parser = argparse.ArgumentParser(description="Timeline Manager System")
    subparsers = parser.add_subparsers(dest="command")

    # get-state command
    get_parser = subparsers.add_parser("get-state", help="Get timeline state for a specific book and chapter")
    get_parser.add_argument("book", type=str, help="Book number")
    get_parser.add_argument("chapter", type=str, help="Chapter number")

    # create command
    create_parser = subparsers.add_parser("create", help="Create a new timeline document")
    create_parser.add_argument("name", type=str, help="Name of the new timeline")

    args = parser.parse_args()

    if args.command == "get-state":
        state = get_state(args.book, args.chapter)
        print(f"--- Timeline State for Book {args.book}, Chapter {args.chapter} ---")
        print(f"Sea Conditions: {state['sea_conditions']}")
        if state['character_positions']:
            print("Character Positions:")
            for char, pos in state['character_positions'].items():
                print(f"  - {char}: {pos}")
        else:
            print("Character Positions: Unknown")

    elif args.command == "create":
        create_timeline(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
