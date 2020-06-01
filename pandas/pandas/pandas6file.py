# file 읽기

import pandas as pd

df = pd.read_csv("../testdata/ex1.csv")
print(df, type(df))
print()
df = pd.read_table('../testdata/ex1.csv',sep=',')
print(df.head(1))
print()
df = pd.read_csv('../testdata/ex2.csv', header=None)
print(df)

print()
#df = pd.read_csv('../testdata/ex2.csv',header=None, names=['a','b'])
df = pd.read_csv('../testdata/ex2.csv',header=None, names=['a','b','c','d','e'])
print(df)
print()
df = pd.read_csv('../testdata/ex2.csv',header=None, names=['a','b','c','d','e'],index_col='e') #index 칼럼으로 names
print(df)
print()
df = pd.read_table('../testdata/ex3.txt', sep='\s+', skiprows=[1,3]) #aaa,ccc 는 skip [1,3], (1,3)둘다가능 
print(df)

print()
df2 = pd.read_fwf('../testdata/data_fwt.txt',widths = (10,3,5),names=('날짜','기업명','가격'),
                  encoding='utf-8') # 10,3,5 글자로 자름
print(df2)
print('---------------------')
#chunk : 대용량의 파일인 경우에는 원하는 크기 만큼 할당해서 읽기

datas = pd.read_csv('../testdata/data_csv2.csv',header=None, chunksize=3) # chunksize 로 3개씩 짤라 데이터를 가져옴
print(datas) # TextFileReader

for p in datas:
    #print(p)
    print(p.sort_values(by=2,ascending=True)) #낮은순부터 오름차순

