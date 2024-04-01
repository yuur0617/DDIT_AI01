import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import QPushButton, QIcon, QMessageBox


form_class = uic.loadUiType("myomok02.ui")[0]

class myWindow(QMainWindow, form_class):

    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.flag_wb = True #흑돌, 백돌 구분
        self.flag_ing = True #게임 진행중인지?
        self.arr2D = [[0] * 10 for _ in range(10)]

        self.btn2D = [[None] * 10 for _ in range(10)]
        
        # 0.png 10x10으로 생성
        for i in range(0, 9+1):
            for j in range(0, 9+1):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                btn.setToolTip(str(i)+","+str(j)) # 이미지별 좌표숫자 저장 #setText()
                btn.clicked.connect(lambda _, i=i, j=j: self.myclick(i, j))

                self.btn2D[i][j] = btn

        self.pb.clicked.connect(self.myreset)
        
        self.myrender()
        self.show()

    #초기화
    def myreset(self):
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j] = 0
        self.myrender()
        self.flag_ing = True
        self.flag_wb = True

    # 0, 1, 2일떄 각각 빈칸, 흑돌, 백돌 변경
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.btn2D[i][j].setIcon(QIcon("0.png"))
                elif self.arr2D[i][j] == 1:
                    self.btn2D[i][j].setIcon(QIcon("1.png"))
                elif self.arr2D[i][j] == 2:
                    self.btn2D[i][j].setIcon(QIcon("2.png"))


    def myclick(self, i, j):
        if not self.flag_ing:
            return

        if self.arr2D[i][j] > 0:
            return

        stone = 1 if self.flag_wb else 2
        self.arr2D[i][j] = stone

        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        le = self.getLE(i, j, stone)
        ri = self.getRI(i, j, stone)
        ur = self.getUR(i, j, stone)
        ul = self.getUL(i, j, stone)
        dr = self.getDR(i, j, stone)
        dl = self.getDL(i, j, stone)

        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = ri + le + 1
        d4 = ul + dr + 1

        self.myrender()

        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            winner = "흑돌" if self.flag_wb else "백돌"
            QMessageBox.information(self, "게임 끝", f"게임 끝\n{winner} 승리")
            self.flag_ing = False

        self.flag_wb = not self.flag_wb

    # def get_direction(self, i, j, di, dj, stone):
    #     cnt = 0
    #     try:
    #         while True:
    #             i += di
    #             j += dj
    #             if self.arr2D[i][j] == stone:
    #                 cnt += 1
    #             else:
    #                 return cnt
    #     except IndexError:
    #         return cnt
    def getUP(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                i -= 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def getDW(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                i += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def getLE(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                j -= 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
    
    def getRI(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                j += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def getUR(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                i -= 1
                j += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def getUL(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                i -= 1
                j -= 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def getDR(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                i += 1
                j += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def getDL(self, i, j, stone):
        cnt = 0
        try :
            while(True):
                i += 1
                j -= 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
