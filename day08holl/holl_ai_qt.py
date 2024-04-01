import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
import tensorflow as tf
import numpy as np

form_class = uic.loadUiType("holl_ai_qt.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = tf.keras.models.load_model('hol1.h5')
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        
        mine = self.le_mine.text()
        com = ""
        pred_rf=None
        if mine=="홀":
            pred_rf=self.model.predict([[1,0]])
        else:
            pred_rf=self.model.predict([[0,1]])
        myidx = np.argmax(pred_rf)

        if myidx==1:
            com="짝"
        else:
            com="홀"
            
        self.le_com.setText(com)
        
        if com==mine:
            result = "ㅊㅊ 이김"
        else:
            result = "ㅠㅠ 짐"
        self.le_result.setText(result)
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()