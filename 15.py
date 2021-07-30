import requests
from bs4 import BeautifulSoup

import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test = input('검색할 이름을 입력하세요 : ')

path = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://unsplash.com/')

time.sleep(1)

element = driver.find_element_by_name('searchKeyword')
element.send_keys(test, Keys.ENTER)

# image_link = driver.find_element_by_link_text('이미지')  # 구글, 네이버
# image_link.click()  # 구글, 네이버


# 구글용
# image_tag = driver.find_elements_by_tag_name('span > div > div > div > a > div > img')
# num = 10,000,000
# x = driver.find_elements_by_class_name('xLon9')

# 이미지 상세창 접속
time.sleep(5)
driver.find_element_by_class_name('_2Mc8_').send_keys(Keys.ENTER)

# 조회수 찾아내기(안되고있음 ....너무안되고있음...주소전혀못찾고있음...)
req = requests.get('https://unsplash.com/photos/{}')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

view = soup.select('')

result = soup.find_all('td', 'title')
for i in range(len(result)):
    print('{:2} 위 : {}'.format(i + 1, result[i].get_text().strip()))

# 이미지 상세창 닫기
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button').send_keys(Keys.ENTER)


# image_tag = driver.find_elements_by_class_name('oCCRx')
# #  뷰 클래스 코드 xLon9 / oCCRx _2Mc8_ / /html/body/div[4]/div/div/div[4]/div/div/div[1]/div[4]/div[1]/div[1]/span
#
# time.sleep(1)
#
# image_list = []
#
# for i in range(len(image_tag)):
#     image_list.append(image_tag[i].get_attribute('src'))
# print(image_list)
#
# for i, link in enumerate(image_list):
#     urlretrieve(link, './images/{}{}.jpg'.format(test, i + 1))
