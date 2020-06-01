# BBQ 사이트 자로 읽고 메뉴와 가격 출력 .가격평균, 표준편차

import urllib.request as req
import bs4

car = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
car = req.urlopen(car)

#listCont > div.wrap-thumb-list > ul > li:nth-child(1) > div > div.mode-cell.title > p > a

soup = bs4.BeautifulSoup(car,'lxml')

info = soup.select('div#listCont > div.wrap-thumb-list > ul > li > div')  #메뉴명
carname = soup.select('div#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.title > p > a')  #메뉴명
data1 = soup.select('div#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.year > span')
data2 = soup.select('div#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.fuel > span')
data3 = soup.select('div#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.km > span')
price = soup.select('div#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.price > b > em')    #가격


name = []
pay = []
cardata = []

from pandas import DataFrame

for i in info:
    name = i.select('div.mode-cell.title > p > a')[0].text
    data1 = i.select('div.mode-cell.year > span')[0].text
    data2 = i.select('div.mode-cell.fuel > span')[0].text
    data3 = i.select('div.mode-cell.km > span')[0].text
    price = i.select('div.mode-cell.price > b > em')[0].text
    corprice = ''
    for j in price:
        try:
            int(j)
            corprice += j # 1 19 190 ...
            #print(price)
            
        except:
            pass
        
    cardata += [[name,int(corprice),data1,data2,data3]]


df2 = DataFrame(cardata,columns=['이름','가격','연식','타입','주행'])

print(df2)
print('가격평균 :', df2['가격'].mean())
   