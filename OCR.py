from PIL import Image
import pytesseract
# Set the path to the Tesseract executable (update this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def perform_ocr(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)

    return text


if __name__ == "__main__":
    # Replace 'path/to/your/image.png' with the actual path to your image file
    image_path = r'C:\SUREKHA/News.png'

    result = perform_ocr(image_path)

    print("OCR Result:")
    print(result)
