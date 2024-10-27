import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Загрузка модели
model = load_model('mnist_model.h5')

# Загрузка изображения
img = cv2.imread('test_2.png', cv2.IMREAD_GRAYSCALE)

# Применение бинаризации для выделения цифр
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

# Нахождение контуров (предположительно, что контуры – это цифры)
contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Обход каждого контура и распознание цифры внутри него
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    digit_img = img[y:y+h, x:x+w]
    digit_img = cv2.resize(digit_img, (28, 28))
    digit_img = digit_img / 255.0
    digit_img = digit_img.reshape(1, 28, 28, 1)

    # Предсказание модели
    predictions = model.predict(digit_img)
    score = tf.nn.softmax(predictions[0])
    predicted_label = tf.argmax(score).numpy()

    # Отображение предсказанных цифр
    print("Predicted label:", predicted_label)

    # Отображение изображения цифры (для проверки)
    cv2.imshow(f'Digit {predicted_label}', digit_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
