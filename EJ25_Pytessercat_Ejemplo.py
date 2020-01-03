import cv2
import pytesseract

imagen = cv2.imread("ejemplo pytesseeract.png")
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
texto = pytesseract.image_to_string(imagen)
print(texto)
