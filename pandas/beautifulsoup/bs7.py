# 웹문서 일부 읽은 후 파일로 저장
from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = 'https://finance.naver.com/marketindex/'

data = req.urlopen(url)
print(data)

soup = BeautifulSoup(data,'html.parser')

price = soup.select_one('div.head_info > span.value').string

print('미국USD',price)

#t = datetime.date.today()
t = datetime.datetime.now()
print(t)

fname = t.strftime('%Y-%m-%d-%H-%M-%S')+'.txt'
print(fname)

with open(fname, 'w' , encoding='utf-8') as f:
    f.write(price)