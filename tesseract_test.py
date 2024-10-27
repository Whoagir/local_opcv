import cv2
import numpy as np
import logging
import pytesseract
from config import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def black_white_change(crop, base_threshold=165, threshold_adjustment_factor=1.0, brightness_range=(63, 78),
                       brightness_reduction_factor=1.5):
    # Преобразование изображения в градации серого
    gray_crop = np.dot(crop[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

    # Вычисление средней и стандартной яркости
    mean_brightness = np.mean(gray_crop)
    std_brightness = np.std(gray_crop)

    # Коррекция яркости, если она находится за пределами заданного диапазона
    if mean_brightness < brightness_range[0] or mean_brightness > brightness_range[1]:
        avg_brightness = 0.5 * (brightness_range[0] + brightness_range[1])
        scale_factor = avg_brightness / mean_brightness
        if mean_brightness > brightness_range[1]:
            scale_factor /= brightness_reduction_factor
        gray_crop = np.clip(gray_crop * scale_factor, 0, 255).astype(np.uint8)
        mean_brightness = np.mean(gray_crop)

    # Определение динамического порога
    dynamic_threshold = base_threshold + threshold_adjustment_factor * (mean_brightness - 128) + (
            std_brightness - 64) * 0.3
    dynamic_threshold = np.clip(dynamic_threshold, 100, 200)

    # Применение пороговой фильтрации
    binary_crop = np.where(gray_crop > dynamic_threshold, 255, 0).astype(np.uint8)

    return binary_crop


def del_zone(crop):
    height, width = crop.shape
    col_index = width - 1

    start_row = height // 4
    end_row = (3 * height) // 4

    while col_index > 0 and np.all(crop[:, col_index] >= 180):
        col_index -= 1

    while col_index > 0 and np.all(crop[start_row:end_row, col_index] <= 120):
        col_index -= 1

    cropped_image = crop[:, :col_index]
    padding_width = width - col_index
    padding = np.zeros((height, padding_width), dtype=crop.dtype)
    final_image = np.hstack((padding, cropped_image))

    return final_image


def process_frame(frame):
    # Предварительное вычисление максимальной ширины и общей высоты
    max_width = max(area[3] for area in indicator_areas)
    total_height = sum(area[4] for area in indicator_areas)

    # Создание пустого изображения с альфа-каналом
    stitched_image = np.ones((total_height, max_width, 4), dtype=np.uint8) * 255
    current_y = 0

    # Фильтрация областей
    number_img_list = [area for area in indicator_areas if area[0] % 12 in (0, 1, 2, 3, 4, 5)]

    for id, x, y, w, h, a, description in number_img_list:
        cropped_area = frame[y:y + h, x:x + w]
        cropped_area = black_white_change(cropped_area)

        cropped_area = del_zone(cropped_area)

        # Проверка числа каналов и преобразование в три канала, если это необходимо
        if len(cropped_area.shape) == 2 or cropped_area.shape[2] == 1:
            cropped_area = np.stack((cropped_area,) * 3, axis=-1)
        elif cropped_area.shape[2] == 2:
            cropped_area = cv2.cvtColor(cropped_area, cv2.COLOR_GRAY2RGB)

        # Добавление альфа-канала
        cropped_area = np.dstack((cropped_area, np.ones((h, w), dtype=np.uint8) * 255))

        # Помещение обрабатываемой области в итоговое изображение
        stitched_image[current_y:current_y + h, :w, :] = cropped_area
        current_y += h

    # Обрезка изображения на необходимую ширину
    stitched_image = stitched_image[:, :81, :]
    stitched_image_rgb = cv2.cvtColor(stitched_image, cv2.COLOR_RGBA2RGB)

    # Сохранение изображения
    cv2.imwrite('test_image.png', stitched_image)

    # Распознавание текста
    text = pytesseract.image_to_string(stitched_image_rgb,
                                       config='--psm 6 -c tessedit_char_whitelist=0123456789,. -c textord_noise_normratio=0.9')

    return text


def main():
    video_path = "res/video/0023.mp4"
    cap = cv2.VideoCapture(video_path)
    # cap = cv2.VideoCapture(0) # видео поток
    if not cap.isOpened():
        print("Ошибка: Не удалось открыть видеофайл")
        return

    try:
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        start_time = 0  # ?
        start_frame = int(frame_rate * start_time)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Видео закончено или ошибка при чтении.")
                break

            # cv2.imshow('Video Stream', frame_rgb)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            text = process_frame(frame_rgb)
            text = ''.join(text).replace("\n", ",")
            # parts = text.split(',')
            # standardized_parts = [part.rjust(5) for part in parts]
            # standardized_text = ','.join(standardized_parts)

            logging.info(f"Обнаруженный текст: {text}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
