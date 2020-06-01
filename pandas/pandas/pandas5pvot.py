# 그룹화 , 피벗 

import numpy as np
import pandas as pd 

data = {'city':['강남','강북','강남','강북'],
        'year':[2010,2011,2012,2012],
        'pop' :[3.3,2.5,3.0,2.0]       
        }

df = pd.DataFrame(data)
print(df,'\n')

# 행 / 열 별 연산
print(df.pivot('city','year','pop'),'\n') # city , year 별 pop데이터 
print(df.pivot('year','city','pop'),'\n')
print(df.set_index(['city','year']).unstack(),'\n')
print(df.set_index(['year','city']).unstack(),'\n') 

print()
hap = df.groupby(['city']) #city를 그룹화하였음 강남 , 강북
print(hap)
print(hap.sum())
print(df.groupby(['city']).sum(),'\n')
print(df.groupby(['city','year']).mean(),'\n') #city 와 year 모두 그룹화 

print('---------------')
print(df,'\n')
print(df.pivot_table(index=['city']),'\n')
print(df.pivot_table(index=['city'],aggfunc = np.mean),'\n') # default mean
print(df.pivot_table(index=['city','year'], aggfunc=np.mean),'\n') # aggfunc 함수명
print(df.pivot_table(index=['city','year'], aggfunc=[len,np.mean]),'\n')
print(df.pivot_table(values=['pop'],index=['city']),'\n')
print(df.pivot_table(['pop'],index=['city']),'\n')
print(df.pivot_table(['pop'],index='city',aggfunc=len),'\n')
print()
print(df.pivot_table(values=['pop'],index=['year'],columns=['city']),'\n')
print(df.pivot_table(values=['pop'],index=['year'],columns=['city'],margins=True),'\n')
print(df.pivot_table(values=['pop'],index=['year'],columns=['city'],margins=True,fill_value= 0),'\n') #fill_value 로 nan값 0으로 채움


