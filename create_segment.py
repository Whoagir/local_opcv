import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import numpy as np
from config import *

# Данные индикаторных областей: [id, top, bottom, width, height, rotation, description]


# Путь к снимкам
_fmask = r"res/photo/screenn_11.png"
image_files = glob.glob(_fmask, recursive=True)  # Получение списка файлов

# Настройка отображения
fig, ax = plt.subplots(1, 1, figsize=(10, 5))

# Чтение и обработка изображения
_img = mpimg.imread(image_files[0])  # Чтение первого изображения

# Нормализация изображения в диапазоне [0, 1]
_img = np.clip(_img, 0, 1) if _img.dtype.kind == 'f' else np.clip(_img, 0, 255) / 255.0

# Добавление индикаторных областей
for section_key, section in indicator_sections.items():
    for area in section.areas:
        ax.add_patch(
            Rectangle(
                (area.x, area.y), area.width, area.height,
                edgecolor="#f00", facecolor="blue", fill=False, lw=1
            )
        )

ax.imshow(_img)
plt.show()