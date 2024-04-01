import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from datetime import datetime
import tensorflow as tf
import cv2

class AIFace:  
    def __init__(self):
        self.model = tf.keras.models.load_model('face.h5')

    def getNameByImage(self, img):
        
        arr = [
            {'lbl':0,'f':'00','n':'김승연'},
            {'lbl':1,'f':'01','n':'배유림'},
            {'lbl':2,'f':'02','n':'우민규'},
            {'lbl':3,'f':'03','n':'유길상'}
        ]
    
        x_train = np.reshape(img, (-1, 32, 32, 3)) / 255 
          
        preds = self.model.predict(x_train)
        myidx = np.argmax(preds[0])
        
        return arr[myidx]['n']

if __name__ == '__main__':
    
    img = cv2.imread('pre01/03/1.png')
    
    af = AIFace()
    myname = af.getNameByImage(img)
    print("myname : ",myname)

