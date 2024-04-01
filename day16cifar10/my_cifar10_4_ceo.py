
from keras.utils import np_utils
from keras.datasets import cifar10
from datetime import datetime
import tensorflow as tf
import numpy as np
import cv2

before = datetime.now()

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = tf.keras.models.load_model('cifar10.h5')
model.summary()
pred = model.predict(x_test)

cnt_o=0;
cnt_n=0;

for idx, i in enumerate(x_test):
    myidx = np.argmax(pred[idx])

    goog= np.argmax(y_test[idx])

    if myidx!=goog:
        img2=cv2.imwrite("x/{}_{}_{}.png".format(myidx,goog,idx),x_test[idx]*255)


after = datetime.now()

print("after",after, "before",before)
print(after-before)
