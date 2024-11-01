import cv2
import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pytesseract
from datetime import datetime
from config import *

# Убедитесь, что путь к Tesseract указан верно
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

output_dir = 'res/photo/'  # costil
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def black_white_change(crop, threshold=165):
    # Проверяем диапазон значений, чтобы не умножать на 255, если изображение уже в нужном формате
    if crop.max() <= 1:
        crop = (crop * 255).astype(np.uint8)  # Преобразуем в диапазон от 0 до 255, если нужно

    # Если изображение уже черно-белое, пропускаем преобразование
    if len(crop.shape) == 3 and crop.shape[2] == 3:
        # Преобразуем цветное изображение в оттенки серого
        gray_crop = np.dot(crop[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
    else:
        # Если изображение уже черно-белое (1 канал), используем его как есть
        gray_crop = crop

    # Применяем пороговое значение: пиксели выше порога делаем белыми (255), ниже — черными (0)
    binary_crop = np.where(gray_crop > threshold, 255, 0).astype(np.uint8)

    # Отображаем результат, если нужно
    # plt.imshow(binary_crop, cmap='gray', vmin=0, vmax=255)
    # plt.axis('off')  # Скрываем оси для более чистого отображения
    # plt.show()  # Отображаем изображение

    return binary_crop


def del_zone(crop):
    height, width = crop.shape
    col_index = width - 1

    # Вычисляем границы средней части
    start_row = height // 4
    end_row = (3 * height) // 4

    while col_index > 0 and np.all(crop[:, col_index] >= 180):
        col_index -= 1

    # Здесь изменяем проверку только на "среднюю" часть изображения
    while col_index > 0 and np.all(crop[start_row:end_row, col_index] <= 120):
        col_index -= 1

    # Обрезаем изображение
    cropped_image = crop[:, :col_index]

    # Находим количество колонок, которое нам нужно добавить слева
    padding_width = width - col_index

    # Создаем черный паддинг
    padding = np.zeros((height, padding_width), dtype=crop.dtype)

    # Объединяем черный паддинг и обрезанное изображение
    final_image = np.hstack((padding, cropped_image))

    return final_image

    # Визуализируем результат
    # plt.figure(figsize=(10, 5))
    # plt.subplot(1, 2, 1)
    # plt.title("Original Image")
    # plt.imshow(crop, cmap='gray')
    # plt.subplot(1, 2, 2)
    # plt.title("Cropped Image")
    # plt.imshow(final_image, cmap='gray')
    # plt.show()

    # Пример использования
    # Создаем пример черно-белого изображения с черной областью слева


<<<<<<< HEAD
def process_frame(frame, save_path=None):
    # Проверка на количество каналов
    if frame.shape[2] < 3:
        raise ValueError("Ожидается как минимум три канала в изображении (RGB или RGBA).")

    # Определение размеров для сшивания изображения
    max_width = max(area.width for section in indicator_sections.values() for area in section.areas)
    total_height = sum(area.height for section in indicator_sections.values() for area in section.areas)

    # Создание пустого изображения
    stitched_image = np.ones((total_height, max_width, 4), dtype=np.uint8) * 255  # RGBA
    current_y = 0  # Координата Y для вставки

    # Обработка каждой области индикатора
    for section_key, section in indicator_sections.items():
        for area in section.areas:
            # Извлечение области из кадра
            cropped_area = frame[area.y:area.y + area.height, area.x:area.x + area.width]

            # Предполагается, что black_white_change и del_zone возвращают одноканальное изображение
            cropped_area = black_white_change(cropped_area)
            cropped_area = del_zone(cropped_area)

            # Преобразование в 3 канала и добавление альфа-канала
            cropped_area = np.stack((cropped_area,) * 3, axis=-1)
            alpha_channel = np.ones((area.height, area.width, 1), dtype=cropped_area.dtype) * 255
            cropped_area = np.concatenate((cropped_area, alpha_channel), axis=2)

            # Вставка области в сшитое изображение
            stitched_image[current_y:current_y + area.height, :area.width, :] = cropped_area
            current_y += area.height
=======
def process_frame(frame, save_path=output_dir):

    # plt.imshow(frame, cmap='gray', vmin=0, vmax=255)
    # plt.axis('off')  # Скрываем оси
    # plt.show()

    # Убедитесь, что у вас есть 3 канала
    if frame.shape[2] < 3:
        raise ValueError("Ожидается как минимум три канала в изображении (RGB или RGBA).")

    # Создание пустого изображения
    max_width = max(area[3] for area in indicator_areas)
    total_height = sum(area[4] for area in indicator_areas)

    # Обеспечение соответствия количества каналов
    stitched_image = np.ones((total_height, max_width, 4))  # RGBA

    current_y = 0  # Изменяем переменную оси на Y для вертикальной компоновки

    number_img_list = [indicator_areas[i] for i in range(len(indicator_areas)) if i % 12 in (0, 1, 2, 3, 4, 5)]

    for id, x, y, w, h, a, description in number_img_list:
        cropped_area = frame[y:y + h, x:x + w]

        # plt.imshow(cropped_area, cmap='gray', vmin=0, vmax=255)
        # plt.axis('off')  # Скрываем оси
        # plt.show()

        cropped_area = black_white_change(cropped_area)

        cropped_area = del_zone(cropped_area)

        # Предполагается, что black_white_change и del_zone возвращают одноканальное изображение
        cropped_area = np.stack((cropped_area,) * 3, axis=-1)

        alpha_channel = np.ones((h, w, 1), dtype=cropped_area.dtype) * 255
        cropped_area = np.concatenate((cropped_area, alpha_channel), axis=2)

        stitched_image[current_y:current_y + h, 0:w, :] = cropped_area
        current_y += h

    # Визуализация перед сохранением (как отладочная мера)
    # plt.imshow(stitched_image / 255.0)
    # plt.show()
>>>>>>> main

    # Обрезка изображения, если это нужно
    stitched_image = stitched_image[:, :81, :]

    # Преобразование в формат RGB для Tesseract
    stitched_image_rgb = cv2.cvtColor(stitched_image.astype(np.uint8), cv2.COLOR_RGBA2RGB)

    # Сохранение изображения
<<<<<<< HEAD
    if save_path:
        cv2.imwrite(save_path, stitched_image)

    # Распознавание текста с помощью Tesseract
=======
    cv2.imwrite('test_image.png', stitched_image)

    # Распознаём текст с помощью Tesseract
>>>>>>> main
    text = pytesseract.image_to_string(stitched_image_rgb, config='--psm 6 -c tessedit_char_whitelist=0123456789,. ')

    return text

<<<<<<< HEAD

def main():
=======
def main():

>>>>>>> main
    video_path = "res/video/0023.mp4"  # Путь к вашему видео
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть видеофайл")
        return

    try:
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        interval = int(frame_rate * 2)  # Интервал для сохранения кадров (каждые 2 секунды)
        start_time = 0  # Убедитесь, что start_time определен
        start_frame = int(frame_rate * start_time)

        count = 0  # Счетчик кадров
        saved_count = 1  # Счетчик сохраненных изображений

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        while True:
            # Считываем кадр из видеофайла
            ret, frame = cap.read()
            if not ret:
                print("Видео закончено или ошибка при чтении.")
                break

            # Преобразуем кадр в цветовое пространство RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Обрабатываем кадр
            text = process_frame(frame_rgb)

            # Если нужно смотреть видео, можно раскомментировать следующую строку
            # cv2.imshow('Video Stream', frame_rgb)

            # Увеличиваем счетчик кадров
            count += 1
            # Выводим результат и текущее время
            print(f"Обнаруженный текст: {text}")
            print(f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # Нажмите 'q' для выхода
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Закрываем все окна и освобождаем ресурсы
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
