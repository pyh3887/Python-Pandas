#pandas : 기술적 통계와 관련된함수 NaN
from pandas import Series, DataFrame
import numpy as np


df = DataFrame([[1.4,np.nan],[7,-4.5],[np.NaN,np.NaN],[0.5,-1]],
        columns = ['one','two'])

print(df)
print(df.drop(1),'\n') # 1행지우기 
print(df.dropna(),'\n') #nan값을 지운다. 
print(df.dropna(how='any'),'\n') # nan값이 하나라도 있으면 지운다
print(df.dropna(how='all'),'\n') # 모든행의 값이 nan 이면 지운다
print(df.dropna(subset=['one']),'\n') # 특정열에 nan 이 있으면 그행을 제거한다.
print(df.fillna(0),'\n') # 평균으로 채우기 sklearn 모듈의 SimpleInputer

# 기술적 통계와 관련된 함수
print('**' * 10) 
print(df.sum(),'\n') #열단위의 합 nan은 제외  
print(df.sum(axis=0),'\n')

print(df.sum(axis=1),'\n') # 행단위의 합
print(df.mean(axis=1),'\n') # 행의 평균
print(df.mean(axis=1, skipna = True),'\n') # na포함 계산
print(df.mean(axis=1, skipna = False),'\n') # na 있을시 계산 x 

print(df.mean(axis=0, skipna= True),'\n') # nan이 있어도 계산 o (열단위)
print(df.mean(axis=0, skipna = False),'\n') #nan이 있기 때문에 계산 x 

print(df.max(),'\n')
print(df.max(axis=0),'\n') #열값중 가장 큰값
print(df.idxmax(),'\n')
print(df.idxmin(),'\n')

print(df.describe(),'\n') # 요약 통계망
print(df.info(),'\n') # 데이터프레임 구조

words = Series(['봄','여름'])
print(words.describe(),'\n')



 


