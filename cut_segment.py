import time
<<<<<<< HEAD
=======

>>>>>>> main
from PIL import Image, ImageEnhance
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from config import *


<<<<<<< HEAD
# Функция для преобразования изображения в черно-белый формат
def black_white_change(crop, base_threshold=165, threshold_adjustment_factor=1.0, brightness_range=(63, 78),
                       brightness_reduction_factor=1.5):
=======
def black_white_change(crop, threshold=165):
>>>>>>> main
    plt.imshow(crop, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')  # Скрываем оси
    plt.show()

    crop = (crop * 255).astype(np.uint8)  # Преобразуем в диапазон от 0 до 255
    gray_crop = np.dot(crop[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)  # Преобразуем в оттенки серого

    # Применяем порог: если пиксель больше порога, делаем его белым (255), иначе черным (0)
<<<<<<< HEAD
    binary_crop = np.where(gray_crop > base_threshold, 255, 0).astype(np.uint8)
=======
    binary_crop = np.where(gray_crop > threshold, 255, 0).astype(np.uint8)
>>>>>>> main

    # Отображаем изображение
    plt.imshow(binary_crop, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')  # Скрываем оси
    plt.show()  # Отображаем изображение, если нужно

    return binary_crop


<<<<<<< HEAD
# Функция для удаления ненужных зон из изображения
=======
>>>>>>> main
def del_zone(crop):
    height, width = crop.shape
    col_index = width - 1

    # Вычисляем границы средней части
    start_row = height // 4
    end_row = (3 * height) // 4

<<<<<<< HEAD
    # Находим последний ненужный столбец
=======
>>>>>>> main
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

<<<<<<< HEAD

# Путь к снимкам
_fmask = r"res/photo/screenn_1.png"
=======
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




# Путь к снимкам
_fmask = r"res/photo/screen_1.png"
>>>>>>> main
image_files = glob.glob(_fmask, recursive=True)

# Чтение и обработка изображения
_img = mpimg.imread(image_files[0])

<<<<<<< HEAD
=======
# plt.imshow(_img, cmap='gray', vmin=0, vmax=255)
# plt.axis('off')  # Скрываем оси
# plt.show()

>>>>>>> main
# Определение числа каналов
num_channels = _img.shape[2] if _img.ndim > 2 else 1

if num_channels < 3:
    raise ValueError("Ожидается как минимум три канала в изображении (RGB или RGBA).")

# Создание пустого изображения
<<<<<<< HEAD
max_width = max(area.width for section in indicator_sections.values() for area in section.areas)
total_height = sum(area.height for section in indicator_sections.values() for area in section.areas)
=======
max_width = max(area[3] for area in indicator_areas)
total_height = sum(area[4] for area in indicator_areas)
>>>>>>> main

# Обеспечение соответствия количества каналов
stitched_image = np.ones((total_height, max_width, 4))  # RGBA

current_y = 0  # Изменяем переменную оси на Y для вертикальной компоновки

<<<<<<< HEAD
# Извлекаем области индикаторов из секции
for section_key, section in indicator_sections.items():
    for area in section.areas:
        cropped_area = _img[area.y:area.y + area.height,
                       area.x:area.x + area.width]  # Обрезаем изображение по заданным координатам

        cropped_area = black_white_change(cropped_area)  # Преобразуем в черно-белый формат

        cropped_area = del_zone(cropped_area)  # Удаляем ненужные зоны

        cropped_area = np.stack((cropped_area,) * 3, axis=-1)  # Создаем 3 канала для цветного изображения

        alpha_channel = np.ones((area.height, area.width, 1), dtype=cropped_area.dtype) * 255  # Создаем альфа-канал
        cropped_area = np.concatenate((cropped_area, alpha_channel), axis=2)  # Объединяем каналы

        stitched_image[current_y:current_y + area.height,
        0:area.width] = cropped_area  # Добавляем обрезанное изображение в итоговое
        current_y += area.height  # Увеличиваем Y для следующего изображения
=======
number_img_list = [indicator_areas[i] for i in range(len(indicator_areas)) if i % 12 in (0, 1, 2, 3, 4, 5)]

for id, x, y, w, h, a, description in number_img_list:
    cropped_area = _img[y:y + h, x:x + w]

    cropped_area = black_white_change(cropped_area)

    cropped_area = del_zone(cropped_area)

    cropped_area = np.stack((cropped_area,) * 3, axis=-1)

    alpha_channel = np.ones((h, w, 1), dtype=cropped_area.dtype) * 255
    cropped_area = np.concatenate((cropped_area, alpha_channel), axis=2)

    stitched_image[current_y:current_y + h, 0:w] = cropped_area
    current_y += h
>>>>>>> main

# Визуализация перед сохранением (как отладочная мера)
plt.imshow(stitched_image / 255.0)
plt.show()

<<<<<<< HEAD
# Обрезаем итоговое изображение до нужной ширины
stitched_image = stitched_image[:, :81]

=======
#32
stitched_image = stitched_image[:, :81]
>>>>>>> main
# Нормализация и сохранение
stitched_image_normalized = stitched_image / 255.0
plt.imsave('test_1.png', stitched_image_normalized)
