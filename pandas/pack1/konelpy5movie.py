from bs4 import BeautifulSoup
import requests 
from konlpy.tag import Okt
from collections import Counter 
import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
okt = Okt()

def movie_scrap(url):
    result = [] 
    for p in range(10):
        r = requests.get(url + '&page=' + str(p))
        soup = BeautifulSoup(r.content,'lxml',from_encoding='ms949')
        #print(soup)
        title = soup.find_all('td',{'class':'title'})
        
        #print(title)
        sub_result = [] 
        for i in range(len(title)) :            
            sub_result.append(title[i].text
                              .replace('\r','')
                              .replace('\n','')
                              .replace('\t','')
                              .replace('\신고','')
                              .replace('-','')
                              .replace('...','')      #필요없는값 제거      
                              .replace('?','')  
                              .replace('여곡성','')
                              .replace('고양이의 보은','')
                              .replace('날씨의 아이','')
                              .replace('알 포인트','')
                              .replace('코코','')  
                              .replace('영화','')                    
                              )            
        result = result + sub_result
    return(''.join(result))

yeogoksung = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171750&target=after')

rpoin = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37261&target=after')

nalci = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=181114&target=after')

coco = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=151728&target=after')

catmovie = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37073&target=after')

movies = [yeogoksung,rpoin,nalci,catmovie,coco]

print(movies)

words_basket = []

for mov in movies:
    words = okt.pos(mov)
    for word in words:
        if(word[1] in ['Noun','Adjective'] and len(word[0])>= 2): # 명사 또는 형용사인 자료
            words_basket.append(word[0])

print(words_basket)
print(Counter(words_basket).most_common(50))

