from PIL import Image, ImageEnhance
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open('test_1.png')

# Преобразование в черно-белый
bw_image = image.convert("L")

# Повышение контрастности
enhancer_contrast = ImageEnhance.Contrast(bw_image)
contrast_image = enhancer_contrast.enhance(2)  # Вы можете регулировать значение

# Повышение резкости
enhancer_sharpness = ImageEnhance.Sharpness(contrast_image)
sharp_image = enhancer_sharpness.enhance(2)  # Вы можете регулировать значение

#Повышенние резкости изображения:
enhancer1 = ImageEnhance.Sharpness(image)
factor1 = 0.01 #чем меньше, тем больше резкость
im_s_1 = enhancer1.enhance(factor1)

text = pytesseract.image_to_string(im_s_1, config='--psm 6 -c tessedit_char_whitelist=0123456789,. ').split('\n')
print(text)
