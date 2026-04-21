import random
import os

def generate_height():
    feet = random.randint(4, 6)
    inches = random.randint(0, 11)
    if feet == 4:
        inches = random.randint(8, 11)
    return f"{feet}'{inches}\""

def generate_build():
    builds = [
        "Lean and muscular", "Soft and curvy", "Broad-shouldered",
        "Petite and lithe", "Thick and sturdy", "Athletic and toned",
        "Willowy and graceful", "Stocky and powerful"
    ]
    return random.choice(builds)

def generate_breast_size():
    bands = [30, 32, 34, 36, 38, 40, 42]
    cups = ["AA", "A", "B", "C", "D", "DD", "E", "F", "G"]
    band = random.choice(bands)
    cup = random.choice(cups)
    return f"{band}{cup}"

def generate_penis_size():
    length = round(random.uniform(5.0, 10.0), 1)
    girth_descriptors = ["slender", "average girth", "thick", "heavy", "incredibly thick"]
    girth = random.choice(girth_descriptors)
    return f"{length} inches, {girth}"

def generate_face_hair_eyes():
    hair_colors = ["black", "blonde", "brown", "red", "auburn", "silver"]
    hair_styles = ["messy", "neatly combed", "long and flowing", "short crop", "braided"]
    eye_colors = ["blue", "green", "brown", "hazel", "grey"]

    hair = f"{random.choice(hair_styles)} {random.choice(hair_colors)} hair"
    eyes = f"piercing {random.choice(eye_colors)} eyes"

    return f"{hair}, {eyes}"

def generate_character_profile(name, role, archetype, gender_config, ethnicity, birthplace):
    height = generate_height()
    build = generate_build()

    # Logic for Futanari/Erotica context
    if gender_config.lower() in ["female", "futanari"]:
        breast_size = generate_breast_size()
    else:
        breast_size = "N/A (Flat/Pecs)"

    if gender_config.lower() in ["male", "futanari"]:
        penis_size = generate_penis_size()
    else:
        penis_size = "N/A"

    face_hair_eyes = generate_face_hair_eyes()

    template = f"""# Character Profile: {name}

## 1. Core Concept & Role
* **Role:** {role}
* **Archetype:** {archetype}
* **Gender Configuration:** {gender_config}
* **Background/Ethnicity:** {ethnicity}
* **Place of Birth/Home:** {birthplace}

## 2. Immutable Physical Traits (Dynamic Anchor)
> **AI INSTRUCTION ON ANATOMY & MEASUREMENTS:**
> The exact measurements below (Breast Size, Penis Size, etc.) are strictly for your internal reference to accurately guide sensory and physical descriptions (e.g., determining if a character is "heavy", "thick", "petite", or "imposing"). **Do NOT explicitly state the exact numerical measurements (inches, cup sizes) in the generated prose**, with the exception of height. Instead, use evocative, 'Show, Don't Tell' descriptions of how their body moves and interacts with the environment or other characters.

* **Height:** {height}
* **Build/Body Type:** {build}
* **Breast Size:** {breast_size} *(Internal Reference Only)*
* **Penis Size:** {penis_size} *(Internal Reference Only - If applicable)*
* **Face/Hair/Eyes:** {face_hair_eyes}
* **Distinctive Marks:** [To be filled by author]

## 3. Voice & Dialogue Anchor (Show, Don't Tell)
* **Speech Rhythm:** [To be filled by author]
* **Voice Samples:**
    * *Sample 1 (Calm):* "[To be filled by author]"
    * *Sample 2 (Angry/Tense):* "[To be filled by author]"
    * *Sample 3 (Intimate/Aroused):* "[To be filled by author]"

## 4. Conflict & Reaction Style
* **Conflict Style:** [To be filled by author]
* **Resistance Style:** [To be filled by author]

## 5. Psychological Baseline (CDP Alignment)
* **Core Wound:** [To be filled by author]
* **False Belief:** [To be filled by author]
* **Vulnerability Trigger:** [To be filled by author]
"""
    return template

if __name__ == "__main__":
    regions = [
        {
            "ethnicity": "Irish-American",
            "birthplace": "South Boston, Massachusetts",
            "names": ["Declan", "Liam", "Connor", "Fiona", "Maeve", "Siobhan", "Sean", "Aidan", "Nora"]
        },
        {
            "ethnicity": "Italian-American",
            "birthplace": "Brooklyn, New York",
            "names": ["Marco", "Giovanni", "Luca", "Sofia", "Isabella", "Carmela", "Enzo", "Mateo", "Lucia"]
        },
        {
            "ethnicity": "Mexican-American",
            "birthplace": "San Diego, California",
            "names": ["Mateo", "Santiago", "Diego", "Valeria", "Camila", "Sofia", "Alejandro", "Javier", "Elena"]
        },
        {
            "ethnicity": "African-American",
            "birthplace": "Atlanta, Georgia",
            "names": ["Marcus", "Jamal", "Trey", "Aaliyah", "Nia", "Kiara", "DeShawn", "Jasmine", "Malik"]
        },
        {
            "ethnicity": "Japanese-American",
            "birthplace": "Honolulu, Hawaii",
            "names": ["Kenji", "Hiroshi", "Takeshi", "Yuki", "Sakura", "Hana", "Ren", "Kai", "Mei"]
        },
        {
            "ethnicity": "Vietnamese-American",
            "birthplace": "Houston, Texas",
            "names": ["Minh", "Tuan", "Duc", "Mai", "Linh", "Thuy", "Hoang", "An", "Lan"]
        },
        {
            "ethnicity": "Greek-American",
            "birthplace": "Astoria, Queens, New York",
            "names": ["Nikos", "Dimitri", "Costa", "Eleni", "Maria", "Athena", "Yianni", "Sofia", "Andreas"]
        },
        {
            "ethnicity": "Scandinavian-American",
            "birthplace": "Minneapolis, Minnesota",
            "names": ["Lars", "Erik", "Sven", "Freja", "Ingrid", "Astrid", "Bjorn", "Leif", "Kirsten"]
        }
    ]

    roles = ["Protagonist", "Anchor", "Seeker", "Antagonist"]
    archetypes = ["The Stoic", "The Rebel", "The Caregiver", "The Explorer"]
    gender_configs = ["Futanari", "Female", "Male"]

    region = random.choice(regions)
    name = random.choice(region["names"])
    ethnicity = region["ethnicity"]
    birthplace = region["birthplace"]

    role = random.choice(roles)
    archetype = random.choice(archetypes)
    gender_config = random.choice(gender_configs)

    profile = generate_character_profile(name, role, archetype, gender_config, ethnicity, birthplace)

    os.makedirs("templates/character_profiles", exist_ok=True)
    filename = f"templates/character_profiles/{name.lower()}_profile.md"

    with open(filename, "w") as f:
        f.write(profile)

    print(f"Generated character profile for {name} ({gender_config}) at {filename}")
