import tensorflow as tf
import cv2
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

for idx,t in enumerate(x_train):
    img2=cv2.imwrite("img/{}/{}.png".format(y_train[idx],idx),t)
