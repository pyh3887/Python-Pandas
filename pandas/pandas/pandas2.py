# pandas 기능 

from pandas import Series, DataFrame 

# 재색인 ------------

data = Series([1,3,2], index = (1,4,2))
print(data)

data2 = data.reindex((1,2,4)) #index를 새로 지정
print(data2)

# 재색인하며 값 채우기 -------------- 
data3 = data2.reindex((1,2,3,4,5))
print(data3)

print()
data3 = data2.reindex([1,2,3,4,5],fill_value = 777) # 비어있는 NaN 을 777로 채움
print(data3) 

print('------')
data3 = data2.reindex([1,2,3,4,5], method = 'ffill') # NaN 을 앞의 값으로 대체함 
print(data3)
data3 = data2.reindex([1,2,3,4,5], method = 'pad')
print(data3)

print('-----')

data3 = data2.reindex([1,2,3,4,5], method = 'bfill') # NaN 을 뒤의 값으로 대체함 index 5 다음값은 없으므로 NaN이나옴 
print(data3)
data3 = data2.reindex([1,2,3,4,5], method = 'backfill')
print(data3)

print('^^^' * 10)

import numpy as np

df = DataFrame(np.arange(12).reshape(4,3),index = ['1월','2월','3월','4월'], columns = ['강남','강북','서초'])
print(df)
print()
print(df['강남'] > 3) # df 데이터프레임이 강남이면서 3봐 큰
print()
print(df[df['강남'] > 3]) 

print()
print(df<3)
df[df<3] = 0
print(df)

print('※ DataFrame 슬라이싱 관련 메소드 ---')

#loc : 라벨지원, iloc: 숫자지원 
print(df.loc['3월',])
print(df.loc['3월', :])

print(df.loc[:'2월']) # 2월이하행 출력
print(df.loc[:'2월',['서초']]) #2월이하행 중 서초 열 출력
print(df.loc[:'2월',['서초','강남']]) #2월이하행 중 서초 강남 열 출력

print()
print(df)
print(df.iloc[2])
print(df.iloc[2,:])
print(df.iloc[:3]) #3행 미만
print(df.iloc[:3,2])
print(df.iloc[:3,1:3])

print('\n\n산술연산----------------')
s1 = Series([1,2,3], index = ['a','b','c'])
s2 = Series([4,5,6,7], index = ['a','b','d','c'])
print(s1)
print(s2)

print(s1+s2)  
print(s1.add(s2)) #프레임 합 (index에 맞춰 더한다)
print(s1 * s2) #프레임 곱

print()
df1 = DataFrame(np.arange(9.).reshape(3,3), columns = list('kbs'), index=['서울','인천','수원'])
print(df1)
df2 =DataFrame(np.arange(12.).reshape(4,3), columns = list('kbs'), index=['서울','인천','수원','일산'])
print(df2)

print()
print(df1 + df2)
print(df1.mul(df2))
print(df1.mul(df2, fill_value = 0))

print()
seri = df1.iloc[0]
print(seri)
print(df1 - seri) #브로드 캐스팅




