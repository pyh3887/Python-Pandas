import sqlite3
import pandas as pd

sql = 'create table if not exists test(product varchar(10), maker varchar(10), weight real ,price integer)'

conn = sqlite3.connect(':memory:') # ram 에 db 저장

conn.execute(sql)
conn.commit()

data1 = ('마우스','삼성',12.5,5000)
data2 = ('키보드','엘지',32.5,15000)
data3 = [('모니터','삼성',4500.5,565000),('메모리','삼성',50.5,55000)]
stmt = 'insert into test values(?,?,?,?)'
conn.execute(stmt,data1)
conn.execute(stmt,data2)
conn.executemany(stmt,data3)
conn.commit()

cursor = conn.execute('select  * from test')
rows = cursor.fetchall()
#print(rows)
for a in rows:
    print(a)
    
print()
#방법 1 
df1 = pd.DataFrame(rows,columns=['product','maker','weight','price'])
print(df1)

#방법 2 #컬럼 x 
df2 = pd.read_sql('select * from test',conn)
print(df2)

cursor.close()
conn.close()


