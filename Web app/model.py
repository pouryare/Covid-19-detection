import tensorflow as tf
import numpy as np
import cv2
import os

base = '/model'
print("\n\nTensorFlow version:", tf.__version__, "\n\n")

model = tf.keras.models.load_model(f'{base}/CovidTest.keras')

def image_pre(path):
    print(f"Processing image: {path}")
    data = np.ndarray(shape=(1, 128, 128, 1), dtype=np.float32)
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Failed to load image from {path}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (128, 128))
    data = np.array(img).reshape((-1, 128, 128, 1))/255
    return data

def predict(data):
    prediction = model.predict(data)
    return np.round(prediction[0][0])
