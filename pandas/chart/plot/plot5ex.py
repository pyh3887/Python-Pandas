from django.shortcuts import render
import MySQLdb
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt 

plt.rc('font',family='malgun gothic')   #한글 깨짐 방지.
plt.rcParams['axes.unicode_minus'] = False   # -부호 깨짐 방지
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}




conn = MySQLdb.connect(**config)

cursor = conn.cursor()

sql = '''
select jikwon_no,jikwon_name,buser_name,jikwon_jik,jikwon_pay,gogek_name from jikwon left outer join buser on buser_num = buser_no join gogek on gogek_damsano = jikwon_no
'''
cursor.execute(sql)
df2 = pd.read_sql(sql,conn)

df2.columns = ('번호','이름','부서','직급','연봉','고객이름')
print()
print(df2.head(3),'\n')


jik_ysum2 = df2.groupby(['부서'])['연봉'].sum()


print(jik_ysum2,'\n')
print();print()


# 크로스 테이블

cross = pd.crosstab(df2['부서'],df2['직급'],rownames = ['True'],colnames=['pred'],margins=True) #교차표

print(cross ,'\n\n\n') 

print(df2.loc[:, ['이름', '고객이름']])





    
    
   
    
    
    
