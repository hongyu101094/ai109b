from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
img = Image.open('test2.png')
text = pytesseract.image_to_string(img, lang='eng')
print(text)
