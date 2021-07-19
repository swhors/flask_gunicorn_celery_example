import psycopg2

class M1(object):
    

conn = psycopg2.connect(host='localhost', dbname='weonseo', user='weonseo', port='5432') # db에 접속

cur = conn.cursor()

cur.execute("select * from m1")

datas = cur.fetchall()

for data in datas:
    print(data)
cur.close()
conn.close()
