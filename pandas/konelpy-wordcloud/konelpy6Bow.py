# BOW(Bag of word) : 문서가 가지는 모든 단어 , 문맥 , 순서를 무시하고 일괄적으로 단어에 대해 빈도수를 부여해 feature vectr 화를 함 
# cout 기반과 TF-IDF 기반으로 나뉜다. 
# CountVectorizer : 문서를 토큰 리스트화 , 각 문서에서 토큰의 출현빈도를 카운트  ,BOW 인코딩 벡터를 만듬
# 

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

count_vec = CountVectorizer(analyzer='word', min_df= 1 ) # 건수를 이용한 벡터생성

contents = ['How to format my hard disk' , 'Hard disk format format problems']
aa = count_vec.fit_transform(contents)
print(aa)

print(count_vec.get_feature_names()) 
print(aa.toarray())
 
print()
tfidf_vec = TfidfVectorizer(analyzer='word', min_df=1)
bb= tfidf_vec.fit_transform(contents) # 가중치 포함
print(bb)
print(tfidf_vec.get_feature_names())
