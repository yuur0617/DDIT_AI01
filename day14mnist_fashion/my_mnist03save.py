import tensorflow as tf
from tensorflow import keras
import cv2

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

print(x_train[0])
print(y_train[0])

for i in range(60000):
    cv2.imwrite("img/{}/{}.png".format(y_train[i],i), x_train[i]);
