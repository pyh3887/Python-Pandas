#BBQ 사이트 자료 읽고 메뉴와 가격 출력, 가격 평균, 표준편차
import urllib.request as req
import bs4

bbqurl = "https://www.bbq.co.kr/menu/menuList.asp"
bbq = req.urlopen(bbqurl)
print(bbq)

soup = bs4.BeautifulSoup(bbq,'lxml')
data1 = soup.select('div.box > div.info > p.name')  #메뉴명
data2 = soup.select('div.box > div.info > p.pay')    #가격

name = []
pay = []

for a in data1:
    name.append(a.text)
    
print(name)

for b in data2:
    pay.append(int(b.text.replace(',','').replace('원',''))) #문자를 숫자만 남기게 하기 위해서 대체
    
print(pay)

data = {'name':name,'pay':pay}
from pandas import DataFrame
df = DataFrame(data)
print(df)

print('-------------------------')

bbqurl = "https://www.bbq.co.kr/menu/menuList.asp"
bbq = req.urlopen(bbqurl)
print(bbq)

soup = bs4.BeautifulSoup(bbq,'lxml')

datas = []
info = soup.select('div.info')  #메뉴명



for i in info:
    tempPrice = i.select('p.pay')[0].text
    price = ''
    for j in tempPrice:
        try:
            int(j)
            price += j # 1 19 190 ...
            #print(price)
        except:
            pass
    datas += [[i.select('p.name')[0].text,int(price)]]

df2 = DataFrame(datas,columns=['메뉴','가격'])
print(df2.head())    
print('가격평균 :', df2['가격'].mean())
print('가격평균 :', df2['가격'].std())

    
            
            
    
    






