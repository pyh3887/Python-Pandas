import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
data = urllib.request.urlopen(url).read()
#print(data.decode('utf-8'))

soup = BeautifulSoup(data,'lxml') #xml 파일 파싱
#print(soup)

title = soup.find('title').string #title attribute 의 값을 저장

#print(title)
#print(soup.find('wf'))
city = soup.findAll('city') #city attribute 의 값들을 저장
#print(city)

cityDatas = []

for c in city:
    #print(c.string)
    cityDatas.append(c.string) #cityDatas 에 city의 값들을 집어넣어준다
    
df = pd.DataFrame()
df['city'] = cityDatas
print(df.head(3))
tmef = soup.select_one('location > province + city + data > tmef') 
print(tmef)

tempMins = soup.select('location > province + city + data > tmn')
tempDatas = []

for t in tempMins:
    print(t.string)

df['tempMins'] = tempMins
df.columns = ['지역','최저기온']

print(df.head(3))
print(df[0:3])

print(df.tail(2))
print(df[-2:len(df)])


#파일로 저장 
df.to_csv('날씨.csv' , index = False)

print('iloc,loc-------------')

print(df.iloc[0], type(df.iloc[0]))

print(df.iloc[0:2], type(df.iloc[0:2]))
print(df.iloc[0:2,:], type(df.iloc[0:2,:]))
print()
print(df.iloc[0:2,0:1])
print(df.iloc[0:2,0:2])
print()
print(df['지역'][0:2] , type(df['지역'][0:2]))
print(df['지역'][:2])
print(df.지역[:2])

#print(df[:])
#print(df)

print('---------')
print(df.loc[1:3]) # print(df.loc['a':'c'])
print(df[1:4])
print(df.loc[[1,3]])
print(df.loc[:,'지역']) # 전체행의 지역열

print()
print(df.loc[1:3,['최저기온','지역']])
print(df.loc[:,'지역'][1:4]) 

print('-------------')
print(df.info())
print(df)
df = df.astype({'최저기온':'int'})
print(df['최저기온'].mean())
print(df['최저기온'].describe())
print()
#print(df['최저기온'] >= 19)
print(df.loc[df['최저기온']>=19])
print(df.loc[(df['최저기온']>= 18) & (df['최저기온'] < 20)]) #and : &  or:| 
print(df.loc[df['최지ㅓ기온']>=19,['최저기온'][0:3]])
print()
print(df.sort_values(['최저기온'],ascending=True))











