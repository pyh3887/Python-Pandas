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

#print(words_basket)
#print(Counter(words_basket).most_common(50)) #참고로 빈도수 높은 단어 확인


movies = [m.replace('ㅋㅋㅋㅋ',"") for m in movies] # 해당단어 잘라내기
movies = [m.replace('이런',"") for m in movies] # 해당단어 잘라내기 
movies = [m.replace('있었고',"") for m in movies] # 해당단어 잘라내기  
print(movies,len(movies))

print('------------------------')
def word_separate(movies):
    result = []
    for mov in movies:
        words = okt.pos(mov)
        one_result = []
        for word in words:
            if(word[1] in ['Noun','Adjective'] and len(word[0]) >= 2):
                one_result.append(word[0])
        result.append(' '.join(one_result))
    return result
    
word_list = word_separate(movies)
print(word_list)

print('----------------------------------------')

# 토큰 생성 후 벡터화 

# 1 : CountVectorizer
count = CountVectorizer(min_df= 2)
print(count)

cou_dtm = count.fit_transform(word_list).toarray()
print(cou_dtm)
cou_dtm_df = pd.DataFrame(cou_dtm, columns= count.get_feature_names() , index= ['yeogoksung','rpoin','nalci','catmovie','coco'])

print(cou_dtm_df) # 단어별 빈도 수

print('^^^' * 20)

# 2 : CountVectorizer()

idf_maker = TfidfVectorizer(min_df = 2 )
tfidf_dtm = idf_maker.fit_transform(word_list).toarray()
tfidf_dtm_df = pd.DataFrame(tfidf_dtm, columns = count.get_feature_names(), index = ['yeogoksung','rpoin','nalci','catmovie','coco'])  
print(tfidf_dtm_df) #단어들의 중요도를 알 수 있는 가중치로 출력

# 코사인 유사도를 이용해 단어의 유사성 출력 
def cosin_func(doc1,doc2):
    bunja = sum(doc1 * doc2)
    bunmo = (sum(doc1 ** 2) * sum(doc2 ** 2)) ** 0.5
    return bunja/bunmo

res = np.zeros((5,5))
print(res)



print(res)

for i in range(5):
    for j in range(5):
        res[i,j] = cosin_func(tfidf_dtm_df.iloc[i], tfidf_dtm_df.iloc[j].values)

df = pd.DataFrame(res, index= ['yeogoksung','rpoin','nalci','catmovie','coco'] , columns = ['yeogoksung','rpoin','nalci','catmovie','coco'])

print(df)

                
                
                
        
        
        
        






 
