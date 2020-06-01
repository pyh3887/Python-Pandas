# 웹문서를 읽어 형태소 분석

import urllib 
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse

okt = Okt()

#para = '이순신'
para = parse.quote('이순신')
url = 'https://ko.wikipedia.org/wiki/' + para #인코딩해주어야함

page = urllib.request.urlopen(url)

#print(page)

soup = BeautifulSoup(page.read(),'lxml')
#print(soup)
#mw-content-text > div > p

wordlist = [] #명사들을 기억
for item in soup.select('#mw-content-text > div > p'):
    if item.string != None:
        #print(item.string.strip())
        ss = item.string
        wordlist += okt.nouns(ss) #명사 담기
        
print('wordlist :', wordlist ) #명사들을 출력
print('wordlist 단어수 :' + str(len(wordlist))) #명사의 갯수 출력

print()
wordDict = {} # 단어의 발생횟수
for i in wordlist:
    if i in wordDict:
        wordDict[i] += 1 #그단어가 만약 있을경우 +1 
    else:
        wordDict[i] = 1 # 처음나올 경우 초기값 1 
        
print('wordDict :', wordDict)        

# 중복없이 단어 보기 
setData = set(wordlist) # set 타입은 중복허용 x 
print('중복없이 단어 보기' , setData)
print('중복없이 단어 수' , len(setData))

print()
import pandas as pd 
woList = pd.Series(wordlist) # series 에 담기
print(woList[:3]) # 3행까지
print(woList.value_counts()[:5]) #단어별 횟수 구하기 pandas

print()
df1 = pd.DataFrame(wordlist , columns = ['단어'])
print(df1.head(3))
print()
df2 = pd.DataFrame([wordDict.keys(),wordDict.values()])
#print(df2)
df2 = df2.T
df2.columns = ['단어','빈도수']
print(df2.head())
print(df2.info())

#file로 저장
df2.to_csv('이순신.csv',sep=',',index=False) #csv 파일로 저장

df3 = pd.read_csv('이순신.csv') #저장된 csv 파일을 읽기 
print(df3.head(3))












      