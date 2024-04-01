import pymysql

class DaoBusPath:  
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = 'SELECT * FROM bus_path'
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def insert(self, bp_name, bp_seq, sta_id, sta_name, lat, lng):
        sql = f"""
            INSERT INTO 
                bus_path (bp_name, bp_seq, sta_id, sta_name, lat, lng) 
            VALUES
                ('{bp_name}', '{bp_seq}', '{sta_id}', '{sta_name}', '{lat}', '{lng}') 
        """
        cnt = self.curs.execute(sql)    
        self.conn.commit()
        return cnt

    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoBusPath()
    list = de.selectList()
    # vo = de.select("2")
    # cnt = de.insert('1','1','1','1','1','1')
    # cnt = de.update('6', '7', '7', '7')
    # cnt = de.delete('6')
    print(list)