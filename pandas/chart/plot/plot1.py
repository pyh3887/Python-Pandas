#시각화 
import numpy as np 
import matplotlib.pyplot as plt 

plt.rc('font', family = 'malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

x = ['서울','인천','수원'] # list , tuple 가능 . set 불가
y = [5,3,7]
#plt.plot(x,y)
#plt.xlim([-1,3])
#plt.ylim([0,10])
#plt.yticks(list(range(0,11,3)))
#plt.show()

print()
data = np.arange(1,11,2)
#print(data)
#plt.plot(data) # y측값 만 줌 
#x = [0,1,2,3,4]
#for a,b in zip(x,data):
#    plt.text(a,b,str(b))
    
#plt.show()
#plt.plot(data)
#plt.plot(data,data,c = 'r')
#plt.show()

x= np.arange(10)
y = np.sin(x)
print(x,y)
#plt.plot(x,y)
#plt.plot(x,y ,'bo')
#plt.plot(y, 'r+')
#plt.plot(x,y,'g--',linewidth=3 , markersize=10) # -- 파선 -실선  :점선  / c ='색' lw = '선두께' marker='마커종류' ms='마커크기;
#plt.show()

#Hold: 하나의 차트 영역에 복수의 plot 그림을 겹쳐 출력

x = np.arange(0,np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
#plt.plot(x,y_sin,'r')
#plt.plot(x,y_cos,'b')
#plt.xlabel('x축')
#plt.ylabel('y축')
#plt.title('hold 기능')
#plt.legend(['sine','cosine'])

#plt.show() 

# subplot : figure 를 여러대로 나눔
#plt.subplot(2,1,1)
#plt.plot(x,y_sin)
#plt.title('Sine')
#plt.subplot(2,1,2)
#plt.plot(x,y_cos)
#plt.title('코사인')

#plt.show()

irum = ['a','b','c','d','e']
kor = [80,55,78,88,90]
eng = [100,75,48,88,60]

plt.plot(irum,kor,'ro-')
plt.plot(irum,eng,'bs-')
plt.ylim([0,100]) #y최소값 최대값
plt.title('시험 점수')
plt.legend(['국어','영어'],loc = 4) # 범례
plt.grid(True) # 차트 가로줄 세로줄
fig = plt.gcf() #차트를 이미지로 저장 준비
plt.show()

fig.savefig('aaa.png')

from matplotlib.pyplot import imread

img = imread('aaa.png')
plt.imshow(img)
plt.show








    


