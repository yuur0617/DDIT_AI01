import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from day15Crawl.dao_bus_path import DaoBusPath
import time


form_class = uic.loadUiType("my_deajeon_all.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.dbp = DaoBusPath()
        self.bp_names = []
        self.cnt = 0
        self.driver = webdriver.Firefox()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.pb_all.clicked.connect(self.my_busall)
        self.pb_macro.clicked.connect(self.my_macro)
        self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
        self.my_busall()
        
    def my_macro(self):
        for idx,bp_name in enumerate(self.bp_names): 
            ul = self.driver.find_element(By.CSS_SELECTOR,"ul[class='route']")
            lis = ul.find_elements(By.CSS_SELECTOR,"li")
            
            lis[self.cnt].click()
            time.sleep(2)
            self.myclick()
            time.sleep(2)
        


        
    def my_busall(self):
        ul = self.driver.find_element(By.CSS_SELECTOR,"ul[class='route']")
        marks = ul.find_elements(By.CSS_SELECTOR,"mark")
        strongs = ul.find_elements(By.CSS_SELECTOR,"strong")
        self.bp_names.clear()
        for idx,mark in enumerate(marks):
            bp_name = "{}{}".format(mark.text,strongs[idx].text)
            self.bp_names.append(bp_name)
            print(idx,bp_name)
        print("self.bp_names",self.bp_names,len(self.bp_names))
                      
    def myclick(self):              
        spans = self.driver.find_elements(By.CSS_SELECTOR,"span[class='st_id']")

        for idx,s in enumerate(spans):

            myparent = s.find_element(By.XPATH, '..')
            sp2 = myparent.find_elements(By.CSS_SELECTOR,"span[class='st_name']")
            
            bus_id = s.text
            bus_name = sp2[0].text
            
            ip = myparent.find_elements(By.CSS_SELECTOR,"input")[0]
            txt = ip.get_attribute('value')
            
            myjson=json.loads(txt)
            lat = myjson['gpsLati']
            lng = myjson['gpsLong']
            cnt = self.dbp.insert(self.bp_names[self.cnt], idx, bus_id, bus_name, lat, lng)
            print(self.bp_names[self.cnt], idx, bus_id, bus_name, lat, lng,cnt)
        self.cnt += 1
        self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
