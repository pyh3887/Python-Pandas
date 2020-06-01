# file 로 저장
import pandas as pd 

items = {'apple':{'count':10,'price':1500}}
df = pd.DataFrame(items)
print(df,'\n')

df.to_csv('result1.csv',sep=',')
df.to_csv('result2.csv', sep=',', index = False) # 색인 제외
df.to_csv('result2.csv', sep=',', index = False , header=False) # 색인 제외,헤더제외

data = df.T
print(data,'\n')

data.to_csv('result4.csv', sep=',' , index = False, header= True)
redata = pd.read_csv('result4.csv')
print(redata,'\n')

print('-----------excel-------------')
df2 = pd.DataFrame({'data':[1,2,3,4,5]})
print(df2)
writer = pd.ExcelWriter('good.xlsx', engine='xlsxwriter') #엑셀파일 읽기 
df2.to_excel(writer,sheet_name= 'Sheet1')
writer.save()
print('저장성공')

exf = pd.ExcelFile('good.xlsx')
print(exf.sheet_names) # 시트 이름 읽기
df3 = exf.parse('Sheet1') # 파싱 
print(df3)

print()
df4 = pd.read_excel(open('good.xlsx','rb'))
df4 = pd.read_excel(open('good.xlsx','rb'),sheet_name = 'Sheet1') # 판다스의 엑셀 read 
print(df4)



  

