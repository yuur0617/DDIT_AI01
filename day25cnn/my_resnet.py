import tensorflow.keras as keras
import cv2
import numpy as np
from day25cnn.imagelabel import ImageLabel


il = ImageLabel()

img = cv2.imread('cd.jpg')
img = cv2.resize(img, (224,224))
img_input = np.reshape(img,(-1,224,224,3))

print(img.shape)

model = keras.applications.resnet.ResNet50()
model.summary()



pred = model.predict(img_input)
idx1 = np.argmax(pred[0])
pred[0][idx1]=0
idx2 = np.argmax(pred[0])
pred[0][idx2]=0
idx3 = np.argmax(pred[0])
pred[0][idx3]=0
idx4 = np.argmax(pred[0])
pred[0][idx4]=0
idx5 = np.argmax(pred[0])

print(il.label[idx1])
print(il.label[idx2])
print(il.label[idx3])
print(il.label[idx4])
print(il.label[idx5])

