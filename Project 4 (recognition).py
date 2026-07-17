"""Basic Text Recognition (OCR) with pytesseract:
Demonstrates using a pre-trained AI model for text recognition using a pre-trained model (Google's Tesseract OCR engine, trained
on huge volumes of text/character image data)

NOTICE:install the tesseract OCR engine from the web after that, you then run this command in cmd "pip install pytesseract pillow".
do this before running and debugging and the program should work
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def load_image(image_path):
    """Load an image file for OCR processing."""
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find image: {image_path}")


def recognize_text(img):
    """Run OCR on the image and return the extracted text."""
    text = pytesseract.image_to_string(img)
    return text.strip()


def get_detailed_data(img):
    """
    Get word-level recognition details: each detected word plus
    its confidence score (0-100) and position on the image.
    """
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    results = []
    for i in range(len(data["text"])):
        word = data["text"][i].strip()
        conf = int(data["conf"][i])

        # Skip empty detections and low-confidence noise
        if word and conf > 0:
            results.append({
                "word": word,
                "confidence": conf,
                "position": (data["left"][i], data["top"][i]),
            })

    return results


def display_results(full_text, word_data):
    """Print the OCR output clearly."""
    print("=" * 50)
    print("OCR RESULTS")
    print("=" * 50)

    print("\nFull recognized text:")
    print("-" * 50)
    print(full_text if full_text else "(no text detected)")
    print("-" * 50)

    print(f"\nWords detected: {len(word_data)}\n")
    for item in word_data:
        print(f"  '{item['word']}'  "
              f"(confidence: {item['confidence']}%, "
              f"position: {item['position']})")

    print("=" * 50)


def main():
    image_path = "sample_text.png"   # replace with your own image path

    img = load_image(image_path)
    full_text = recognize_text(img)
    word_data = get_detailed_data(img)

    display_results(full_text, word_data)


if __name__ == "__main__":
    main()


"""
SETUP NOTES (Windows)
----------------------
pytesseract needs the actual Tesseract OCR engine installed separately:

1. Download the Windows installer from:
   https://github.com/UB-Mannheim/tesseract/wiki
   (grab the latest .exe, e.g. tesseract-ocr-w64-setup-x.x.x.exe)

2. Run the installer. Note the install path — usually:
   C:\\Program Files\\Tesseract-OCR\\

3. In this script, uncomment the line near the top and set it to
   your install path:
   pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

4. Install the Python packages:
   pip install pytesseract pillow

5. Run the script:
   python ocr_recognition.py
"""
