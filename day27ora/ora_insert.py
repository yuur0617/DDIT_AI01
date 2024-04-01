import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()

e_id = 4
e_name = 4
gen = 4
addr = 4

sql = f"""
    INSERT INTO emp (
    e_id, e_name, gen, addr
    ) VALUES (
        '{e_id}','{e_name}','{gen}','{addr}'
    )
"""
cs.execute(sql)    
print(cs.rowcount)

cs.close()
conn.commit()
conn.close()