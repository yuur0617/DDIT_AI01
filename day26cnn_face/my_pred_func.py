from time import time
import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
import tensorflow as tf
import cv2


def getNameByImage(img):

    arr = [
        {'lbl':0,'f':'00','n':'김승연'},
        {'lbl':1,'f':'01','n':'배유림'},
        {'lbl':2,'f':'02','n':'우민규'},
        {'lbl':3,'f':'03','n':'유길상'}
    ]
    
    x_train = np.reshape(img,(-1,32, 32, 3))/255
    model = tf.keras.models.load_model('face.h5')
    model.summary()
    
    preds= model.predict(x_train)
    myidx = np.argmax(preds[0])
    return arr[myidx]['n']



img = cv2.imread('pre01/01/0.png')
myname = getNameByImage(img)
print(myname)





