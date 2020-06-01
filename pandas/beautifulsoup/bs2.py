# HTML / XML 전용 처리 모듈 : Beautiful Soup

from bs4 import BeautifulSoup

html_data = '''
<html><body>
<h1>뷰티풀 라이프</h1>
<p>웹페이지 분석</p>
<p>원하는 자료 추출</p>
</body></html>
'''

print(html_data,type(html_data)) # type string 
soup = BeautifulSoup(html_data,'html.parser')
print(soup,type(soup)) # type beautifulsoup

h1 = soup.html.body.h1 # h1태그 
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling #두번째 p2
print(h1,' ', h1.string)
print(p1,' ',p1.string)
print(p2,' ',p2.string)

print('**' * 10)
html_data2 = '''
<html><body>
<h1 id = "title" >뷰티풀 라이프</h1>
<p>웹페이지 분석</p>
<p id='my'>원하는 자료 추출</p>
</body></html>
'''

soup2 = BeautifulSoup(html_data2,'lxml')
print(soup2)
print(soup2.p)
print(soup2.p.string)
print(soup2.find('p'),soup2.find('p').string) # find('태그명')태그 ,값 ,find('태그명').string 태그명의 값
print(soup2.find('p', id='my'), soup2.find('p',id='my').string) #id를 이용해 찾기
print(soup2.find(id='title').string)
print(soup2.find(id='my').string)

print('------------------------')
html_data3 = '''
<html><body>
<h1 id = "title" >뷰티풀 라이프</h1>
<p>웹페이지 분석</p>
<p id='my'>원하는 자료 추출</p>
<div>
 <a href='http://www.naver.com'>naver</a>
 <a href = 'http://daum.com'>daum</a>
</div>
</body></html>
'''
soup3 = BeautifulSoup(html_data3,'lxml')
#print(soup3)
#print(soup3.prettify()) html 태그만
print(soup3.find('a'))
print(soup3.find('a').string)
print(soup3.find(['a']))
print(soup3.find_all(['a'])) #a 태그 모두찾기
print(soup3.findAll(['a']))
links = soup3.find_all('a')

for i in links :
    href = i.attrs['href'] # a태그의 href 주소값얻기
    text = i.string #a태그의 값 모두 얻기
    print(href,' ', text)    
    
print(soup3.find_all('p'))
print(soup3.find_all(['p','h1']))

aa = soup3.find_all(string=['뷰티풀 라이프','원하는 자료 추출','웹페이지 분석']) # 값으로 찾기
print(aa)
print('정규 표현식 가능')
import re 
links2 = soup3.find_all(href=re.compile(r'^ht')) #정규표현식 사용
print(links2)

for h in links2:
    print(h.attrs['href'])
    
print('\n\n CSS selector 이용 --------------')

html_data4 = """
<html><body>
<div id ='hello'>
 <a href='http://naver.com'>naver</a>
 <span>
     <i>
       <a href='http://www.asia.com'>asia</a>
     </i>
     <a href='http://www.korea.com'>korea</a>
 </span>
 <ul class = 'world'>
  <li>안녕</li>
  <li>반가워</li>
 </ul>
 <ul class = 'kbs'>
  <li>good</li>
  <li>nice</li>
 </ul>
</div>

<div id='kbs'>
 <b>나는 b </b>
 <a href='http://www.mbc.com'>mbc</a>
</div>
</body></html>
"""

soup4 = BeautifulSoup(html_data4,'lxml')
a = soup4.select_one('div#kbs a') # div 아래에 a 태그가 있으면 (css 선택자)
print('a : ', a)

b = soup4.select_one('div#hello ul')
print(b,'\n')

c = soup4.select_one('div#hello a').string
print(b,'\n')

d = soup4.select_one('div#hello span > a').string
print(d,'\n')

e = soup4.select_one('div#hello span > i > a').string
print(e,'\n')

g = soup4.select_one('div#hello ul.world')
print(g,'\n')




