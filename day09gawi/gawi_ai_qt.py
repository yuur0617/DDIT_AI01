import sys
import tensorflow as tf
import numpy as np

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("gawi_ai_qt.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = tf.keras.models.load_model('gawi.h5')
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        

    def pbFunction(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        pred_rf=None
        if mine=="가위":
            pred_rf=self.model.predict([[1,0,0]])
        elif mine=="바위":
            pred_rf=self.model.predict([[0,1,0]])
        else :
            pred_rf=self.model.predict([[0,0,1]])
            
        myidx=np.argmax(pred_rf)
        
        
        if myidx==0:
            com = "가위"
        elif myidx ==1 :
            com = "바위"
        else :
            com = "보"  
        
        if com == "가위" and mine == "가위"  :  result = "비김"
        if com == "가위" and mine == "바위"  :  result = "이김"
        if com == "가위" and mine == "보"  :  result = "짐"
        
        if com == "바위" and mine == "가위"  :  result = "짐"
        if com == "바위" and mine == "바위"  :  result = "비김"
        if com == "바위" and mine == "보"  :  result = "이김"
        
        if com == "보" and mine == "가위"  :  result = "이김"
        if com == "보" and mine == "바위"  :  result = "짐"
        if com == "보" and mine == "보"  :  result = "비김"
        
        
        self.le_com.setText(com)
        self.le_result.setText(result)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()