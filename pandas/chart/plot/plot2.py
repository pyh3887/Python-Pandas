# 시각화 
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font',family='malgun gothic')   #한글 깨짐 방지.
plt.rcParams['axes.unicode_minus'] = False   # -부호 깨짐 방지
#===============================================================================
# fig = plt.figure()    #차트 영역에 대한 객체 선언
# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)
# 
# ax1.hist(np.random.randn(10), bins = 20,alpha = 0.2)
# ax2.plot(np.random.randn(10))
# plt.show()
#===============================================================================

#막대 그래프
#===============================================================================
data = [50,80,100,75,90]   #width
# plt.bar(range(len(data)),data)  #height
# plt.show()
# 
# errdata = np.random.rand(len(data))
# plt.barh(range(len(data)),data,alpha = 0.5,xerr = errdata)  #horizontal  xerr: 편차,에러값,신뢰구간 ... 
# plt.show()
#===============================================================================

#원형
#===============================================================================
# plt.pie(data,explode=(0,0,0.1,0,0), colors=['yellow','red','blue'])
# plt.title('원형')
# plt.show()
#===============================================================================

#박스 plot
#===============================================================================
# plt.boxplot(data)
# plt.show()
#===============================================================================

#버블차트
#===============================================================================
# n = 30
# np.random.seed(1)
# x = np.random.rand(n)
# y = np.random.rand(n)
# color = np.random.rand(n)
# scale = np.pi * (20 * np.random.rand(n))**2
# plt.scatter(x, y ,s = scale, c=color)
# plt.show()
#===============================================================================

import pandas as pd
df = pd.DataFrame(np.random.randn(100,4), index=pd.date_range('1/1/2000',periods=100),columns = list('ABCD'))
#print(df)
df = df.cumsum()
print(df.head())
plt.plot(df)
plt.show()











