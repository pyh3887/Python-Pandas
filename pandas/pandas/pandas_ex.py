from pandas import Series
import numpy as np
from pandas.core.frame import DataFrame


#문제1 

df = DataFrame(np.random.randn(9,4),columns = ['no1','no2','no3','no4'])
print(df,'\n')

print(df.mean(axis=0))

#문제 2



#obj2 = Series([10,20,30,40], index = ['a','b','c','d'])
print()
frame2 = DataFrame(data= [10,20,30,40], columns = ['numbers'], index = ['a','b','c','d']) # index 값 을 임의로 지정 
print(frame2)
print(frame2.loc['c'])
print(frame2.values[1,0])
print(frame2.values[2,0])
print(frame2.values[3,0])
print(frame2['numbers'].sum())
print(frame2 ** 2) #프레임 곱

val = Series(['1.5','2.5','3.5','4.5'],index = ['a','b','c','d'])
frame2['float'] = [1.5,2.5,3.5,4.5]

print(frame2)

val2 = Series(['길동','오정','팔계','오공'],index = ['d','a','b','c'])
frame2['names'] = val2

print(frame2)




