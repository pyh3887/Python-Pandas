
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(df)


bins = [1, 20, 35, 60, 150] 

labels = ["소년", "청년", "장년", "노년"]
df["Age_cat"] = pd.cut(df["Age"], bins, labels=labels)

print(df)
data = df.pivot_table(values=['Survived'],index=['Sex','Age_cat'],columns=['Pclass'])
print(data,'\n')

# 4-1) human.csv 파일을 읽어 아래와 같이 처리하시오.  
    
# - NA삭제 

df1 = pd.read_csv('../testdata/human.csv') #skipinitialspace = True
print(df1)

df1 = df1[~df1[' Group'].isin([' NA'])]

print(df1,'\n') 
# - 두개컬럼 추출 
columns_df = df1[[' Career', ' Score']]

print(columns_df,'\n')

# - 평균구하기
print(columns_df.mean(),'\n')


# 4-2)tips.csv 파일을 읽어 아래와 같이 처리하시오.

    

  
df2 = pd.read_csv('../testdata/tips.csv')
print(df2,'\n')
print(df2.describe(),'\n')
print('-------')
print(df2[0:3])
print('-------\n')
print(df2['smoker'].value_counts(),'\n') #구간별 갯수를 카운트함
print(df2['day'].unique())

   

   