import cv2
import os
import matplotlib.pyplot as plt

# Настройка тайминга старта нарезки (в секундах)
start_time = 30  # Нарезка начинается с 10-й секунды

# Создание директории для сохранения изображений, если она не существует
output_dir = 'res/photo/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Открытие видеофайла
video = cv2.VideoCapture('res/video/0023.mp4')

# Проверка: открыт ли файл
if not video.isOpened():
    print("Ошибка: не удалось открыть видео.")
else:
    frame_rate = video.get(cv2.CAP_PROP_FPS)  # Получение fps видео
    interval = int(frame_rate * 2)  # Интервал для сохранения кадров (каждые 2 секунды)
    start_frame = int(frame_rate * start_time)  # Кадр, с которого начинается нарезка

    count = 0  # Счетчик кадров
    saved_count = 1  # Счетчик сохраненных изображений

    # Перемотка видео до кадра начала нарезки
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    while True:
        ret, frame = video.read()
        if not ret:
            break  # Выйти из цикла, если кадры закончились

        if count % interval == 0:
            # Преобразование цветового пространства
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Сохранение кадра
            filename = os.path.join(output_dir, f'screenn_{saved_count}.png')
            plt.imsave(filename, frame_rgb)
            saved_count += 1

        count += 1

    video.release()
    print(f"Сохранено {saved_count - 1} изображений.")
