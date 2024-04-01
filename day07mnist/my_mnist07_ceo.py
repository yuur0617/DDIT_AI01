import tensorflow as tf
import numpy as np
import cv2
from tensorflow import keras

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_test_ori = x_test

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = tf.keras.models.load_model('first.h5')
model.summary()
pred = model.predict(x_test)
cnt_o=0;
cnt_n=0;

for idx, i in enumerate(x_test):
    myidx = np.argmax(pred[idx])
    goog=y_test[idx]
    if myidx!=goog:
        img2=cv2.imwrite("x/{}_{}_{}.png".format(idx,myidx,goog),x_test[idx]*255)
        

