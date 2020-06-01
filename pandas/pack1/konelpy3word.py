# 웹 뉴스 정보로 워드 임베딩 하여 유사 단어 파악하기 


from konlpy.tag import Okt 
import pandas as pd 

okt = Okt()

# daum news 

with open('daumnews.txt', mode = 'r', encoding='utf8') as f :
    #print(f.read())
    lines = f.read().split('\n') #줄단위로 자르기
    
    print(len(lines))
    
wordDic = {}

for line in lines: 
    datas = okt.pos(line)
    #print(datas)
    for word in datas:
        if word[1] == 'Noun': 
            #print(word[0])
            #print(word[0] in wordDic)
            if not(word[0] in wordDic): # dictionry 안에 같은값이 있을경우 0
                wordDic[word[0]]= 0 
            wordDic[word[0]] += 1 
print(wordDic) 

keys = sorted(wordDic.items(), key= lambda x:x[1], reverse=True) #단어의 갯수가 많은순부터 내림차순 정렬
print(keys)

# df 에 담기 

wordList = []
countList = []

for word, count in keys[:20]:
    wordList.append(word)
    countList.append(count)
 
#print(wordList)
#print(countList)

df = pd.DataFrame()

df['word'] = wordList
df['count'] = countList

print(df.head(3))

print('-------------------------------------------')

results = []
with open('daumnews.txt',mode='r',encoding='utf8') as fr : 
    lines = fr.read().split('\n')
    
    for line in lines:
        datas = okt.pos(line,stem = True)
        #print(datas)
        imsi = [] 
        for word in datas: 
            #print(word)
            if word[1] in ['Noun'] : #명사말고 제외
                imsi.append(word[0])            
            
                
        imsi2 = (" ".join(imsi)).strip()
        results.append(imsi2)
                
#print(results)


#file 로 저장
fileName = 'daumnews2.txt'
with open(fileName,mode='w',encoding ='utf8') as fw:
    fw.write('\n'.join(results))
    print('저장성공')

# word embeddig  중 Word2vec

from gensim.models import word2vec

#간단한 예 -----
sentence = [['python','language','program','computer','say']]
model = word2vec.Word2Vec(sentence , min_count= 1)
print(model.wv.most_similar('python')) # 절대 값 1 에 가까울수록 친밀


print()
# 저장된 문서 daumnews2.txt 를 읽어 유사 단어 파악 
genObj = word2vec.LineSentence(fileName)
print(genObj) # word2vec.LineSentence object
model = word2vec.Word2Vec(genObj, size = 100 , window = 10, min_count=2 , sg=1) # sg=1 분석방법론은 skip-Gram 사용
print(model)
model.init_sims(replace=True) #필요 없는 메모리 해제


# 모델 저장 후 사용 
try: 
    model.save('daum_model.model')
    
except Exception as e:
    print('err :', e)

# 모델 읽기
model = word2vec.Word2Vec.load('daum_model.model')

#단어별 유사도 확인
print(model.wv.most_similar(positive='마스크'))
print(model.wv.most_similar(positive=['마스크'],topn=3))
print(model.wv.most_similar(positive=['마스크','차단'],negative=['가격']))



        

        
        
        
    
    
    
    












