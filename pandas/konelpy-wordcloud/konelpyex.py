
#문제 ) : 홍길동전(완판본)을 읽은 후에 빈도수가 높은 10위 이내 단어 출력 (내림차순)

#https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8/%ED%98%84%EB%8C%80%EC%96%B4_%ED%95%B4%EC%84%9D


import urllib 
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse
from pack1.konelpy2 import wordDict
# 문제 ) 홍길동전(완판본)을 읽은 후에 빈도 수가 10위 이내 단어 출력 (내림차순)

okt = Okt()

url = "https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8/%ED%98%84%EB%8C%80%EC%96%B4_%ED%95%B4%EC%84%9D"
page = urllib.request.urlopen(url)
#print(page)

soup = BeautifulSoup(page.read(), 'lxml')
#print(soup)
 
wordlist = []   # 명사들을 기억
for item in soup.select('#mw-content-text > div > p'):
    if item.string != None:
        #print(item.string.strip())
        ss = item.string
        wordlist += okt.nouns(ss)
 
#print('wordlist :', wordlist)
#print('wordlist 단어 수 :', str(len(wordlist)))
 
#print()
wordDict = {}   # 단어의 발생 횟수
for i in wordlist:
    if len(i) >= 2:     # 2글자 이상만 넣기
        if i in wordDict:
            wordDict[i] += 1
        else:
            wordDict[i] = 1

# print('wordDict :', wordDict)

import pandas as pd

#print()
print('---------1-------------')
df99 = pd.DataFrame([wordDict.keys(), wordDict.values()])
df99 = df99.T
df99.columns = ['단어', '빈도 수']
print(df99.sort_values(by=['빈도 수'], axis=0, ascending=False).head(10))
 
import numpy as np
 
#2
print('---------2-------------')
#print(df99[(df99['빈도 수'] >= 50) & (df99['빈도 수'] <= 100)])
abc = np.array(df99[(df99['빈도 수'] >= 50) & (df99['빈도 수'] <= 100)])
print(abc)
 
#3
print('---------3-------------')
writer = pd.ExcelWriter('hong.xlsx', engine='xlsxwriter')   # 엑셀 저장
df99.to_excel(writer, sheet_name='Sheet1')
writer.save()
 
df98 = pd.read_excel(open('hong.xlsx', 'rb'), sheet_name='Sheet1')  # 엑셀 불러오기
print(df98.head())


