import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("myomok01.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.lbl.mousePressEvent = self.mylblclick
        self.show()

    def myclick(self):
        self.pb.setIcon(QtGui.QIcon("1.png"))

    # def mylblclick(self, event):
    #     self.lbl.setPixmap(QtGui.QPixmap("1.png"))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
