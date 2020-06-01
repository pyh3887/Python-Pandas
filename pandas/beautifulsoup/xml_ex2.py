# 기상청 날씨정보 xml 자료읽기 
import urllib.request 
import xml.etree.ElementTree as etree
from openpyxl.xml.functions import localname


try:
    webdata = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml') #web xml 가지고오기
    webxml = webdata.read() # xml문서 읽기
    #print(webxml
    webxml = webxml.decode('utf-8') 
    print(webxml)
    webdata.close()
    
    with open('myweather.xml',mode= 'w', encoding='utf-8') as f:
        f.write(webxml) #웹에서 가져온 xml을 파일로 저장 
    
except Exception as e :
    print('err' , e)
    
xmlfile = etree.parse('myweather.xml')
print(xmlfile)

root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
child = root.findall('{current}weather')
child = root.findall(root[0].tag)
print(child)

for i in child:
    y = i.get('year')
    m = i.get('month')
    d = i.get('day')
    h = i.get('hour')
    print(y + '년' + m + '월' + d + '일' + h + "시 현재") 

datas = []

for ch in root:
    #print(ch.tag) {current} weather
    for i in ch:
        #print(i.tag) # {current}local...
        localName = i.text #데이터 텍스트
        #print(localName)
        ta = i.get('ta') # 데이서 속성 온도
        desc = i.get('desc') # 데이터 속성 날씨
        datas += [[localName,ta,desc]]
        
print(datas)


from pandas import DataFrame 
df = DataFrame(datas,columns = ['지역','온도','상태'])
print(df.head(3)) # 첨부터세개
print(df.tail(3)) # 끝에서 세개

print('웹자료 읽어 바로 출력')
import urllib.request

webdata2 = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
xmlFile = etree.parse(webdata2)
root = xmlFile.getroot()

ndate = list(root[0].attrib.values())
print(ndate)
print(ndate[0] + '년' + ndate[1] + '월' + ndate[2] + '일' + ndate[3] + '시')

for child in root:
    for subChild in child:
        print(subChild.text + ':' + subChild.attrib.get('ta'))


# 웹 이미지 읽기 
imgUrl = 'http://i.011st.com/ex_t/R/400x400/1/85/0/src/pd/20/1/0/3/5/6/5/EGavw/1387103565_B.jpg'
saveName = 'myimage.jpg'
urllib.request.urlretrieve(imgUrl,saveName) #이미지 주소 복사후 jpg 파일로 저장하기  

    


