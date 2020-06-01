# 구글 로그인하고 메일 읽어오기
from selenium import webdriver
import pandas as pd

try:
    url = "https://www.gmail.com"
    browser = webdriver.Chrome('C:/work/chromedriver')
    browser.implicitly_wait(3)
    browser.get(url);
    browser.find_element_by_id('identifierId').send_keys('leesin3153a@gmail.com')
#     browser.find_element_by_id('identifierNext').click()
    browser.find_element_by_class_name('CwaK9').click()
    browser.implicitly_wait(10)
    
    browser.find_element_by_name('password').send_keys('fltlschlrhdi')
    browser.find_element_by_id('passwordNext').click()
    browser.implicitly_wait(10)
    
    df = pd.DataFrame()     # 텅빈 데이터 프레임 생성
    
    datas1 = []
    datas2 = []
    datas3 = []
    
    subjects = browser.find_elements_by_css_selector('div.yW > span.bA4 > span.zF')
    #print('subjects : ', subjects)
    
    for subject in subjects :
        print(subject.text)
        datas1.append(subject.text)
    
    subjects1 = browser.find_elements_by_css_selector('div.y6 > span.bog > span.bqe')
    #print('subjects1 : ', subjects1)
    for subject1 in subjects1 :
        print(subject1.text)
        datas2.append(subject1.text)
    
    subjects2 = browser.find_elements_by_css_selector('span.y2')
    #print('subjects2 : ', subjects2)
    for subject2 in subjects2 :
        print(subject2.text)
        datas3.append(subject2.text)
    
    df['id'] = datas1
    df['jemok'] = datas2
#     df['naeyong'] = datas3        # 너무 길어서 짤리므로 넣지 않았습니다.
    
    print(df)
#     url = "https://datalab.naver.com/keyword/realtimeList.naver"
#     page = requests.get(url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})   # requests에서 에러메세지가 뜨면 headers 추가
#     soup = BeautifulSoup(page.text, 'lxml')
# #   print(soup)
#     title = soup.select('span.item_title')
# #   print(title)
#     print('네이버 실시간 검색어')
#     count = 0
#     for i in title:
#         count += 1
#         print(str(count) + ") " + i.string)
    

 
    print('성공')
except Exception:
    print('에러')