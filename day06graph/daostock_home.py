import pymysql

class DaoStock:  
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def select(self,s_name):
        sql = f"""
            SELECT * FROM stock
            WHERE 
                s_name='{s_name}'
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoStock()
    list = de.select('삼성전자')
    print(list)