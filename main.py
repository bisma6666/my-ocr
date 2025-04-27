from PIL import Image
import pytesseract

# Path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update if different

# Open an image file
img = Image.open('sample.png')  # Make sure sample.png is in the same folder

# Run OCR
text = pytesseract.image_to_string(img)

# Print extracted text
print(text)

# Optional: Save output to a text file
with open('ocr_output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
