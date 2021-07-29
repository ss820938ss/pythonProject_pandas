import requests
from bs4 import BeautifulSoup

import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test = input('검색할 이름을 입력하세요 : ')

path = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path)
# driver.get('https://www.google.com')  # 구글
# driver.get('https://www.naver.com')  # 네이버
driver.get('https://www.youtube.com')  # 유튜브

# time.sleep(1)  # 구글, 네이버
time.sleep(5)  # 유튜브

# element = driver.find_element_by_name('q')  # 구글
# element = driver.find_element_by_name('query')  # 네이버
element = driver.find_element_by_id('search')  # 유튜브
time.sleep(5)  # 유튜브
element.send_keys(test, Keys.ENTER)
time.sleep(3)  # 유튜브

# image_link = driver.find_element_by_link_text('이미지')  # 구글, 네이버
# image_link.click()  # 구글, 네이버

time.sleep(1)
# 네이버용
# image_tag = driver.find_elements_by_tag_name('section> div> div> div> div> div> div> a> img')

# 구글용
# image_tag = driver.find_elements_by_tag_name('span > div > div > div > a > div > img')
image_tag = driver.find_elements_by_class_name('Q4LuWd')

time.sleep(1)

image_list = []

for i in range(len(image_tag)):
    image_list.append(image_tag[i].get_attribute('src'))
print(image_list)

for i, link in enumerate(image_list):
    urlretrieve(link, './images/{}{}.jpg'.format(test, i + 1))
