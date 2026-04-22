import asyncio
import edge_tts
import re
import os
import sys

def clean_markdown(text):
    """Removes common markdown formatting for TTS reading."""
    # Remove bold/italic markers
    text = re.sub(r'[*_]', '', text)
    # Remove headers
    text = re.sub(r'#+\s*', '', text)
    return text

async def main(input_filepath, output_filepath, voice="en-US-ChristopherNeural"):
    if not os.path.exists(input_filepath):
        print(f"Error: {input_filepath} does not exist.")
        sys.exit(1)

    print(f"Reading from {input_filepath}...")
    with open(input_filepath, "r", encoding="utf-8") as f:
        text = f.read()

    print("Cleaning markdown formatting...")
    cleaned_text = clean_markdown(text)

    print(f"Generating audio to {output_filepath} using voice {voice}...")
    communicate = edge_tts.Communicate(cleaned_text, voice)
    await communicate.save(output_filepath)
    print(f"Audio saved to {output_filepath}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Markdown to Speech using edge-tts")
    parser.add_argument("input", help="Input markdown file path")
    parser.add_argument("output", help="Output audio file path")
    parser.add_argument("--voice", default="en-US-ChristopherNeural", help="edge-tts voice to use")
    args = parser.parse_args()

    asyncio.run(main(args.input, args.output, args.voice))
