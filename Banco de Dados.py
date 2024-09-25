import psycopg2

con = psycopg2.connect(host='database-1.c9o20cogif9e.sa-east-1.rds.amazonaws.com', database='inventario', user='postgres', password='123teste4')
con.autocommit = True
cur = con.cursor()
cur.execute("delete from arquivo")
con.commit()

con.close()
