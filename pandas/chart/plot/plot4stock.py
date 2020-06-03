import pandas as pd
from pandas_datareader import data

#종목 읽기

kosdaq = pd.read_pickle('./kosdaq.pickle')
kospi = pd.read_pickle('./kospi.pickle')

print(kosdaq.head(),'\n')
print(kospi.head(),'\n')


#Yahoo 에서 읽기 

start_date = '2019-01-01'
tickers = ['003380.KQ','251270.KS'] # 제일 홀딩스 , 넷마블 게임즈

holding_df = data.get_data_yahoo(tickers[0], start_date)
print(holding_df.head(3),'\n')
net_df = data.get_data_yahoo(tickers[1], start_date) #넷마블 게임즈 코스피
print(net_df.head(3),'\n')

# file 로 저장 

holding_df.to_csv('./holding.csv')
net_df.to_csv('./net.csv')

holding_df.to_pickle('./holding.pickle')
net_df.to_excel('./net.xls')

with open('./holding.csv',mode = 'r') as f:
    print(f.read(),'\n')

print()    
print(pd.read_csv('./net.csv'))
print()
import matplotlib.pyplot as plt 
#plt.plot(holding_df)
#plt.show() 

#plt.plot(net_df)
#plt.show()

import numpy as np
# pandas가 plot 기능-------------------
np.random.seed(0)

df = pd.DataFrame(np.random.randn(10,3), index = pd.date_range('1/1/2000',periods=10), columns = ['a','b','c'])

print(df,'\n')

#df.plot(kind = 'bar') # 'box' ,,,
df[:5].plot.bar(rot = 15)  #pandas 의 plot 메소드
plt.title('test')
plt.show()







    

    
    
    
    
    






