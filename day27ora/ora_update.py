import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

e_id = 4
e_name = 5
gen = 5
addr = 5

sql = f"""
    UPDATE 
        EMP 
    SET 
        e_name = {e_name}, gen = {gen}, addr = {addr}
    WHERE 
        e_id = {e_id}
"""
cs.execute(sql)    
print(cs.rowcount)

cs.close()
conn.commit()
conn.close()