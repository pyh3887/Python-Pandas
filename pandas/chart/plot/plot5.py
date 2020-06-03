# 교차 테이블 작성 : 행과 열로 구성되는 교차표 . 변수간 의미의 차이 

import pandas as pd 

ytrue = pd.Series([2,0,2,2,0,1,1,2,0])
ypred = pd.Series([2,1,1,2,0,1,0,1,0])

kbs = pd.crosstab(ytrue,ypred,rownames = ['True'],colnames=['pred'],margins=True) #교차표 
print(kbs)
print('예측 정확도:' ,(2+1+2)/9)

print('--------------')

des = pd.read_csv('../testdata/descriptive.csv')
print(des.info(),'\n')
print(des.head(3),'\n')

data = des[['resident','gender','level','pass']]
print(data[:3],type(data),'\n')

table = pd.crosstab(data.resident,data.gender)
print(table,'\n')

table2 = pd.crosstab([data.resident,data.gender],data.level)
print(table2,'\n')