import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import QPushButton, QIcon, QMessageBox
from idlelib.debugobj import myrepr


form_class = uic.loadUiType("myomok03_20.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                               
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],  
                               
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]                
                                                             
            ]
        self.pb2D = []
        self.flag_wb = True
        self.flag_ing = True
        
        
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        
        for i in range(20):
            line = []
            for j in range(20):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                btn.clicked.connect(self.myclick)
                btn.setToolTip("{},{}".format(i,j))
                line.append(btn)
            self.pb2D.append(line)
            
        self.show()
        self.myrender()
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
        
    def myclick(self):
        
        if not self.flag_ing:
            return 
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",");
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j]>0:
            return
        
        stone = 0
        if self.flag_wb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        le = self.getLE(i, j, stone)
        ri = self.getRI(i, j, stone)
        ur = self.getUR(i, j, stone)
        ul = self.getUL(i, j, stone)
        dr = self.getDR(i, j, stone)
        dl = self.getDL(i, j, stone)
        
        d1 = up + dw + 1;
        d2 = ur + dl + 1;
        d3 = ri + le + 1;
        d4 = ul + dr + 1;
        
        self.myrender()
        
        if d1==5 or d2==5 or d3 ==5 or d4 == 5:
            if self.flag_wb:
                QMessageBox.about(self, '오목', '흑돌승리')
            else:
                QMessageBox.about(self, '오목', '백돌승리')
                
            self.flag_ing = False
            
        self.flag_wb = not self.flag_wb
        
    def getUP(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def getDW(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getLE(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getRI(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    
    def myreset(self):
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
        self.myrender()
        self.flag_ing = True
        self.flag_wb = True

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainClass()
    myWindow.show()
    app.exec_()
    
