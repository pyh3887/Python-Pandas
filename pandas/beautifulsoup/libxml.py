# 웹에서 제공되는 강남구 도서관 정보 xml 읽기

import urllib.request as req 
from bs4 import BeautifulSoup

url = 'http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/'

plainText = req.urlopen(url).read()
#print(plainText)

xmlObj = BeautifulSoup(plainText,'lxml')

libData = xmlObj.select('row')

for data in libData:
    name = data.find('lbrry_name').text
    addr = data.find('adres').text
    tel = data.find('tel_no').text
    
    
