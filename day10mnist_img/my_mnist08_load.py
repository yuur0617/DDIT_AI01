import tensorflow as tf
import numpy as np
import cv2

img = cv2.imread('9_2.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_28 = cv2.resize(img_gray, (28,28))

x_test1 = np.reshape(img_gray_28, (1, 28, 28, 1))/255

x_test1_rev = 1-x_test1

print(x_test1_rev)

model = tf.keras.models.load_model('first.h5')
model.summary()

pred = model.predict(x_test1_rev)
print(pred)


