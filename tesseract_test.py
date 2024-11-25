import cv2
import numpy as np
import logging
import pytesseract
<<<<<<< HEAD

from config import indicator_sections

pytesseract.pytesseract.tesseract_cmd = r'D:\)\tesseract.exe'
=======
from config import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
>>>>>>> main

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


<<<<<<< HEAD
# def black_white_change(crop, base_threshold=165, threshold_adjustment_factor=1.0, brightness_range=(63, 78),
#                        brightness_reduction_factor=1.5):
#     # Преобразование изображения в оттенки серого
#     gray_crop = np.dot(crop[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
#
#     # Вычисление медианы, средней и стандартной яркости
#     mean_brightness = np.mean(gray_crop)
#     median_brightness = np.median(gray_crop)
#     std_brightness = np.std(gray_crop)
#
#     # Коррекция яркости, если она выходит за пределы диапазона
#     lower_bound, upper_bound = brightness_range
#     if mean_brightness < lower_bound or mean_brightness > upper_bound:
#         target_brightness = (lower_bound + upper_bound) / 2
#         scale_factor = target_brightness / median_brightness
#         if median_brightness > upper_bound:
#             scale_factor /= brightness_reduction_factor
#         gray_crop = np.clip(gray_crop * scale_factor, 0, 255).astype(np.uint8)
#
#     # Перерасчет яркости после коррекции
#     adjusted_mean_brightness = np.mean(gray_crop)
#     adjusted_median_brightness = np.median(gray_crop)
#
#     # Вычисление порога с учетом медианы и дисперсии
#     dynamic_threshold = (base_threshold +
#                          threshold_adjustment_factor * (adjusted_mean_brightness - 128) +
#                          0.25 * (std_brightness - 64))
#     dynamic_threshold = np.clip(dynamic_threshold, 120, 180)
#
#     # Пороговая фильтрация
#     binary_crop = np.where(gray_crop > dynamic_threshold, 255, 0).astype(np.uint8)
#
#     return binary_crop


# def black_white_change(crop, base_threshold=165, target_brightness=128, target_contrast=64):
#     """
#     Преобразует изображение в черно-белый формат с усиленной стабилизацией,
#     чтобы числа в логе оставались одинаковыми.
#
#     Параметры:
#     - crop: Входное изображение, которое будет преобразовано.
#     - base_threshold: Фиксированный порог для черно-белой конверсии.
#     - target_brightness: Целевое значение яркости для нормализации.
#     - target_contrast: Целевое значение контраста для стабилизации.
#     """
#
#     # Преобразование изображения в оттенки серого с использованием стандартных коэффициентов
#     gray_crop = np.dot(crop[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
#
#     # Вычисление текущей средней яркости и стандартного отклонения
#     mean_brightness = np.mean(gray_crop)
#     std_brightness = np.std(gray_crop)
#
#     # Нормализация контраста
#     contrast_scale = target_contrast / (std_brightness if std_brightness != 0 else 1)
#     gray_crop = np.clip((gray_crop - mean_brightness) * contrast_scale + target_brightness, 0, 255).astype(np.uint8)
#
#     # Применение фиксированного порога
#     binary_crop = np.where(gray_crop > base_threshold, 255, 0).astype(np.uint8)
#
#     return binary_crop
=======
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
>>>>>>> main


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
<<<<<<< HEAD
    max_width = max(area.width for section in indicator_sections.values() for area in section.areas)
    total_height = sum(area.height for section in indicator_sections.values() for area in section.areas)

    # Create empty image for final result
    stitched_image = np.ones((total_height, max_width, 4), dtype=np.uint8) * 255
    current_y = 0

    for section_key, section in indicator_sections.items():
        for area in section.areas:
            cropped_area = frame[area.y:area.y + area.height, area.x:area.x + area.width]
            cropped_area = black_white_change(cropped_area)
            cropped_area = del_zone(cropped_area)

            if len(cropped_area.shape) == 2 or cropped_area.shape[2] == 1:
                cropped_area = np.stack((cropped_area,) * 3, axis=-1)
            elif cropped_area.shape[2] == 2:
                cropped_area = cv2.cvtColor(cropped_area, cv2.COLOR_GRAY2RGB)

            alpha_channel = np.ones((area.height, area.width), dtype=np.uint8) * 255
            cropped_area = np.dstack((cropped_area, alpha_channel))

            stitched_image[current_y:current_y + area.height, :area.width, :] = cropped_area
            current_y += area.height

    stitched_image = stitched_image[:, :81, :]
    stitched_image_rgb = cv2.cvtColor(stitched_image, cv2.COLOR_RGBA2RGB)

    # Save processed image
    cv2.imwrite('test_image.png', stitched_image)

    # OCR text recognition
=======
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
>>>>>>> main
    text = pytesseract.image_to_string(stitched_image_rgb,
                                       config='--psm 6 -c tessedit_char_whitelist=0123456789,. -c textord_noise_normratio=0.9')

    return text


def main():
<<<<<<< HEAD
    video_path = "res/video/C0023.mp4"
    cap = cv2.VideoCapture(video_path)

=======
    video_path = "res/video/0023.mp4"
    cap = cv2.VideoCapture(video_path)
    # cap = cv2.VideoCapture(0) # видео поток
>>>>>>> main
    if not cap.isOpened():
        print("Ошибка: Не удалось открыть видеофайл")
        return

    try:
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
<<<<<<< HEAD
        start_time = 0
=======
        start_time = 0  # ?
>>>>>>> main
        start_frame = int(frame_rate * start_time)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Видео закончено или ошибка при чтении.")
                break

<<<<<<< HEAD
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            text = process_frame(frame_rgb)
            text = ''.join(text).replace("\n", ",")
=======
            # cv2.imshow('Video Stream', frame_rgb)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            text = process_frame(frame_rgb)
            text = ''.join(text).replace("\n", ",")
            # parts = text.split(',')
            # standardized_parts = [part.rjust(5) for part in parts]
            # standardized_text = ','.join(standardized_parts)

>>>>>>> main
            logging.info(f"Обнаруженный текст: {text}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
