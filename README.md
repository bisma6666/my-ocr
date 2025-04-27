# Simple OCR Project

This is a simple OCR (Optical Character Recognition) project made in Python using Pytesseract and Pillow.

## Setup Instructions

1. Install Python 3.x from [https://python.org](https://python.org)

2. Install required Python libraries:
    ```
    pip install -r requirements.txt
    ```

3. Install Tesseract OCR:
    - Download from: https://github.com/tesseract-ocr/tesseract
    - Install it and remember the install path (e.g., `C:\Program Files\Tesseract-OCR`).

4. Update `pytesseract.pytesseract.tesseract_cmd` in `main.py` to your install path if different.

5. Place an image named `sample.png` in the same folder.

6. Run the project:
    ```
    python main.py
    ```

7. The extracted text will be printed and also saved into `ocr_output.txt`.

---

## Notes

- Works with .png, .jpg images.
- You can replace `sample.png` with your own image.
# my-ocr
