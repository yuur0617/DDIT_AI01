import cx_Oracle 

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cur = conn.cursor()

sql = """
    select 
        e_id, e_name, gen, addr
    from
        emp
"""
rs = cur.execute(sql)

rows = cur.fetchall()

print(rows)

cur.close()
conn.close()