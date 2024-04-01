import pymysql
import numpy as np

class DaoStock:  
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectArr(self,s_name):
        sql = f"""
            SELECT * FROM stock
            WHERE 
                s_name='{s_name}'
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        arr = []
        for s in list:
            arr.append(s['price'])
        return arr
    
    def selectArrN(self,s_name):
        sql = f"""
            SELECT * FROM stock
            WHERE 
                s_name='{s_name}'
            limit 4
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        arr = []
        for s in list:
            arr.append(s['price'])
        
        return np.array(arr)
    
    def selectSNames(self):
        sql = f"""
            SELECT 
                s_name 
            FROM 
                stock 
            GROUP BY 
                s_name

        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        arr = []
        for s in list:
            arr.append(s['s_name'])
        return arr
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoStock()
    arr = de.selectSNames()
    print(arr)