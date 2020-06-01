# pandas module : 고수준의 자료구조(Series , DataFrame_를 지원)

from pandas import Series
import numpy as np
from pandas.core.algorithms import value_counts

obj = Series([3,7,-5,4]) # index ' '  값 
#obj = Series((3,7,-5,4))
#obj = Series({3,7,-5,4}) # set type x

print(obj,type(obj))

print()
obj2 = Series([3,7,-5,4], index = ['a','b','c','d']) # 생성시 색인부여 가능
print(obj2, type(obj2))
print(obj2.sum(), ' ' , sum(obj2), ' ' , np.sum(obj2)) # 파이썬의 sum 은 속도가 느릴수 있음 pandas의 함수들은 numpy가 기본
print(obj2.mean(), obj2.std())
print()
print('배열값 : ', obj2.values)
print('인덱스 :' , obj2.index)

print('\n슬라이싱 ---------')
print(obj2['a']) # 임의로준 색인명
print(obj2[0]) # 실제 index
print(obj2[['a']]) # 색인과 같이 값이나옴
print(obj2[[0]])
print()
print(obj2[['a','b']])
print()
print(obj2['a':'c'])
print(obj2[2])
print(obj2[2:4])
print(obj2[[2,1]])
print(obj2 > 0)
print('a' in obj2)
print('k' in obj2)

print('dict --------------------')
names = {'mouse' : 5000 , 'keyboard': 35000, 'monitor': 550000}
print(names, type(names))
obj3 = Series(names)
print(obj3)
obj3.index = ['마우스','키보드','모니터'] # 색인 이름 바꾸기 
print(obj3)

obj3.name = '상품가격' #series에 이름을 줄수도 있다.
print(obj3)

print('-----DataFrame ---------')
from pandas import DataFrame
df = DataFrame(obj3)
print(df , type(df))

print()
data = {
    'irum' :['홍길동','신선해','공기밥','한송이','신기해'],
    'juso' :('역삼동','신길동','역삼동','역삼동','서초동'),
    'nai' : (23,25,33,20,26)
    }
print(data , type(data))

frame = DataFrame(data)  #열단위로 숫자가 같으면 됌
print(frame, type(frame))
print(frame['irum'])
print(frame.irum) #series 가 모여 dataframe을 구성 data의 irum컬럼은 객체로 생성
print(type(frame.irum))
print()
print(DataFrame(data,columns = ['juso','irum','nai'])) # 칼럼 출력 
frame2 = DataFrame(data, columns = ['irum','nai','juso','tel'], index = ['a','b','c','d','e']) # index 값 을 임의로 지정 
print(frame2)

print()
print(frame2)

print()
frame2['tel'] = '111-1111'
print(frame2)

val = Series(['222-2222','333-3333','444-4444'], index = ['b','c','e']) # 아까 생성했던 비어있는 칼럼인 tel에 값을 주는데 지정된 index 로 차례대로 값을 준다
frame2['tel'] = val
print(frame2)
print()
print(frame2.T)
print()
print(frame2.values)
print(frame2.values[0,2])
print(frame2.values[0,2])

print()
#frame3 = frame2.drop('d')
frame3 = frame2.drop('d',axis = 0) # d행 을 삭제 
print(frame3)
frame4 = frame2.drop('tel', axis =1) # tel 칼럼 열 삭제 
print(frame4)

print()
print(frame3.sort_index(axis=0 , ascending=False)) # 행단위로 정렬  ascending = false 시 내림차순
print(frame3.sort_index(axis=1 , ascending=False)) # 열단위로 정렬

print(frame3.rank(axis=0)) 

print()
print(frame3['juso'].value_counts()) #주소별 그룹핑 카운트 

print()
data = {
    'juso':['강남구 역삼동','중구 신당동','강남구 대치동'],
    'inwon':[23,25,15]
}

frame = DataFrame(data)
print(frame)
result1 = Series([x.split()[0] for x in frame.juso]) # juso 에서 구 단위로 자름 
result2 = Series((x.split()[0] for x in frame.juso)) # juso 에서 구 단위로 자름
print(result1) 
print(result2)

print(result2.value_counts()) # 구별로 데이터 카운트 출력  





























