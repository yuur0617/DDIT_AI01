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
    
    def insert(self, s_name, price, s_code, ymd):
        sql = f"""
            INSERT INTO 
                stock(s_name, price, s_code, ymd) 
            VALUES
                ('{s_name}', '{price}', '{s_code}', '{ymd}') 
        """
        cnt = self.curs.execute(sql)    
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoStock()
    cnt = de.insert(1, 1, 1, 1)
    print(cnt)