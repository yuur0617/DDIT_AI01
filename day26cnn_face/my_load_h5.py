from time import time
import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
import tensorflow as tf


x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)


model = tf.keras.models.load_model('face.h5')
model.summary()

preds= model.predict(x_train)

for idx,p in enumerate(preds):
    print(idx,np.argmax(p))









