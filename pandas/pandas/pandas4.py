# 행 열 이동 , 중복제거 , 구간 단위 설정
import pandas as pd
import numpy as np

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3),index=['대전','서울'], columns = ['2017','2018','2019'])

print(df)
print()

df_row = df.stack() #인덱스 기준 데이터 쌓음
print(df_row,'\n')

df_col = df_row.unstack() #컬럼기준 데이털르 쌓음 
print(df_col,'\n')

print()
data = {'data1':['a'] * 4, 'data2':[1,1,2,2]}
print(data)
df2 = pd.DataFrame(data)
print(df2)
result = df2.drop_duplicates()
print(result)

#연속 데이터 범주화
print()
price = [10.3,5.5,7.8,3.6]

cut = [3,7,9,11] # 구간 기준값

result_cut = pd.cut(price,cut) #cut 으로 인해 3개의 구간이 생김 3~7 , 7~9 , 9~11

print(result_cut,'\n')
print(pd.value_counts(result_cut)) #구간별 갯수를 카운트함

print('---------------')
datas = pd.Series(np.arange(1,1001))
print(datas,'\n')
result_cut2 = pd.qcut(datas,3)
print(result_cut2,'\n') # 1에서 1000 기준 3개의 구간으로 나뉘게됌
print(pd.value_counts(result_cut2))
print('----------------')

# merge dataframe 합치기 

df1 = pd.DataFrame({'data1':range(7),'key':['b','b','a','c','a','a','b']})
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df1,'\n')
print(df2,'\n')
print(pd.merge(df1,df2,on='key'),'\n') #공통 칼럼인 key를 기준으로 inner join
print(pd.merge(df1,df2,on='key', how ='inner'),'\n')
print(pd.merge(df1,df2,on='key', how ='outer'),'\n') # outer join
print(pd.merge(df1,df2,on='key', how ='left'),'\n') # left join
print(pd.merge(df1,df2,on='key', how ='right'),'\n') # right join


print('공통칼럼이 없는경우----')
df3 = pd.DataFrame({'key2': ['a','b','d'],'data2':range(3)})  
print(pd.merge(df1,df3,left_on='key',right_on='key2'))

print()
print(pd.concat([df1,df2],axis=0),'\n') #두개의 데이터프레임 이어붙이기

print('np의 array 자료 이어 붙이기')
arr1 = np.arange(6).reshape(2,3)
arr2 = np.arange(4,10).reshape(2,3)
print(arr1,'\n')
print(arr2,'\n')
arrs1 = np.concatenate([arr1,arr2], axis=0) #행단위 이어붙이기
print(arrs1,'\n')
arrs2 = np.concatenate([arr1,arr2], axis=1) #열단위 이어붙이기
print(arrs2,'\n')




















