import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from datetime import datetime
import tensorflow as tf
import cv2

arr = [
    {'lbl':0,'f':'00','n':'김승연'},
    {'lbl':1,'f':'01','n':'배유림'},
    {'lbl':2,'f':'02','n':'우민규'},
    {'lbl':3,'f':'03','n':'유길상'}
]


x_train = cv2.imread('185.png')
x_train = np.reshape(x_train, (-1, 32, 32, 3)) / 255
print(x_train.shape)

model = tf.keras.models.load_model('face.h5')
model.summary()

preds = model.predict(x_train)

myidx = np.argmax(preds[0])

print(arr[myidx]['n'])
    

