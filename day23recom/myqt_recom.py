import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import tensorflow as tf
import numpy as np

form_class = uic.loadUiType("myqt_recom.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.labels = [
            {'name':'짜장', 'lbl':0, 'arr':[1,0,0,0,0] },
            {'name':'삼겹살', 'lbl':1, 'arr':[0,1,0,0,0] },
            {'name':'전복죽', 'lbl':2, 'arr':[0,0,1,0,0] },
            {'name':'킹크랩', 'lbl':3, 'arr':[0,0,0,1,0] },
            {'name':'라면', 'lbl':4, 'arr':[0,0,0,0,1] }
        ]
        self.model = tf.keras.models.load_model('recom.h5')
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def getIdxByName(self, name):
        for idx, l in enumerate(self.labels):
            if name == l['name'] : 
                return idx
        return -1
            
    def myclick(self):
        
        myname = self.le.text()
        
        idx = self.getIdxByName(myname)
        print("idx : ", idx)
        
        print(self.labels[idx]['arr'])
        
        x_rf = np.array([
            self.labels[idx]['arr']
        ])
        
        pred_rf = self.model.predict(x_rf)
        myidx = np.argmax(pred_rf)
        
        menu = self.labels[myidx]['name']
        
        self.le_recom.setText(menu)
        
        print(np.argmax(pred_rf))
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = myWindow()
    app.exec_()
