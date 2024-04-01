import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

e_id = 4

sql = f"""
    DELETE FROM 
        EMP 
    WHERE 
        e_id = {e_id}
"""
cs.execute(sql)    
print(cs.rowcount)

cs.close()
conn.commit()
conn.close()