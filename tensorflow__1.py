import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing import image

# Загрузка и предобработка данных MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Нормализация данных
train_images = train_images / 255.0
test_images = test_images / 255.0

# Создание простой модели
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели на MNIST
model.fit(train_images, train_labels, epochs=5)

# Сохранение обученной модели
model.save('mnist_model.h5')

# Загрузка и предобработка изображения для предсказания
img = image.load_img('test_3.png', target_size=(28, 28), color_mode='grayscale')
img_array = image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Создаем батч

# Предсказание
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print("Predicted label:", tf.argmax(score).numpy())
