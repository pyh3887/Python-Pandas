#웹에서 제공되는 강남구 도서관 정보 json 읽기

import urllib.request as req 
import json

url = 'http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/'

plainText = req.urlopen(url).read().decode()
print(plainText)
print(type(plainText)) #class str
jsonData = json.loads(plainText) #json decoding
print(type(jsonData)) #class dict

print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])

# get()
libData = jsonData.get('SeoulLibraryTime').get('row')
print(libData)

print('----------')

for ele in libData:
    name = ele.get('LBRRY_NAME')
    addr = ele.get('ADRES')
    tel = ele.get('TEL_NO')
    print(name + "\t" + tel + '\t' + addr)
    
    
