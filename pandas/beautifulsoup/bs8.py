#naver 영화 사이트 순위 읽기
from bs4 import BeautifulSoup

# 방법1 
import urllib.request
url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data,'lxml')
#print(soup)
#print(soup.select('div.tit3'))
#print(soup.select('div[class=tit3]'))

for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip()) #좌우 공백자르기

print()
#방법2 
import requests

#data = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
#print(data.status_code, ' ' , data.encoding)
#datas = data.text
#print(datas)

datas = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn').text
soup = BeautifulSoup(datas,'lxml')

print(soup)
#m_list = soup.findAll('div','tit3')
m_list = soup.findAll('div',{'class':'tit3'})
print(m_list)

#참고 
title = 'abcdefg'
print(title[title.find('b'):title.find('f')]) #bcde

#-------------- 

for i in m_list:
    #print(i)
    title = i.findAll('a')
    print(str(title)[str(title).find('title="')+7:str(title).find('">')])


print('순위 표시 -----')
count = 1

for i in m_list:
    title = i.find('a')
    print(str(count)+ "위:" + title.string)
    count += 1















