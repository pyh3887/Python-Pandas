# 신문 사이트에서 검색 단어 입력후 해당 단어 기사들 정보 읽어 워드 클라우드 출력

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote


#keyword = input('검색어 입력:')
keyword = '코로나'
print(quote(keyword))

targetUrl = 'https://www.donga.com/news/search?query=' + quote(keyword)

print(targetUrl)
searchData = urllib.request.urlopen(targetUrl)
soup = BeautifulSoup(searchData,'lxml',from_encoding='utf-8')
#print(soup)

msg = ''

for title in soup.find_all('p','tit'): #p 태그의 class tit 중 a 태그 찾기
    title_link = title.select('a')
    #print(title_link)
    article_url = title_link[0]['href']
    #print(article_url) 
   
    
    source_article = urllib.request.urlopen(article_url) # 각 a tag의 기사 내용 읽기 
    soup = BeautifulSoup(source_article,'lxml',from_encoding='utf-8')
    contents = soup.select('div.article_txt')
    for imsi in contents :
        item = str(imsi.find_all(text=True)) #text만 읽기
        #print(item)
        msg = msg + item
      
print(msg)

print()

from konlpy.tag import Okt
from collections import Counter

nlp = Okt()
nouns = nlp.nouns(msg)
result = []
for imsi in nouns:
    if len(imsi) > 1: #2자 이상
        result.append(imsi) 
        

print(result[:10]) 

count = Counter(result) # 명사 카운트 세기
#tag = print(count)

tag = count.most_common(50)

import pytagcloud

taglist = pytagcloud.make_tags(tag,maxsize=100) #cloud 

print(taglist[:5])
pytagcloud.create_tag_image(taglist,'morph4word.png',size=(1000,600), fontname='malgun', rectangular=False) 

#저장된 이미지 읽기 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

img = mpimg.imread('morph4word.png')
plt.imshow(img)
plt.show()

import webbrowser
webbrowser.open('morph4word.png')
        

     
        
        






 

    
     
    
    
    

    