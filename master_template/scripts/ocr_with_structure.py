import os
import argparse
import glob
try:
    from PIL import Image
    import pytesseract
except ImportError:
    print("Error: Missing required libraries. Please install them using:")
    print("pip install Pillow pytesseract")
    print("You may also need to install the tesseract-ocr system package.")
    exit(1)

def perform_ocr(image_path):
    """Extracts text from an image using pytesseract."""
    try:
        print(f"Processing image: {image_path}")
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ""

def process_directory(input_dir, output_dir):
    """Processes all images in a directory and combines their text."""
    os.makedirs(output_dir, exist_ok=True)

    # Supported image formats
    image_extensions = ('*.png', '*.jpg', '*.jpeg', '*.webp', '*.bmp', '*.tiff')
    image_files = []

    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(input_dir, ext)))

    image_files.sort() # Ensure chronological order if named sequentially

    if not image_files:
        print(f"No images found in {input_dir}.")
        return

    combined_text = ""
    for i, file_path in enumerate(image_files):
        extracted = perform_ocr(file_path)
        if extracted:
            combined_text += f"\n\n--- Source: {os.path.basename(file_path)} ---\n\n"
            combined_text += extracted

    output_file = os.path.join(output_dir, "combined_ocr_output.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# OCR Extracted Content\n\n")
        f.write(combined_text)

    print(f"\nSuccess! Extracted text from {len(image_files)} images and saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from images for the creative pipeline.")
    parser.add_argument("--input", default="samples/images", help="Directory containing source images.")
    parser.add_argument("--output", default="samples", help="Directory to save the OCR markdown output.")

    args = parser.parse_args()

    # Create input dir if it doesn't exist to avoid errors for users just starting
    os.makedirs(args.input, exist_ok=True)

    process_directory(args.input, args.output)

if __name__ == "__main__":
    main()
