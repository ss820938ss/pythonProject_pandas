import time
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('해당 프로그램은 네이버 사전을 기반으로 제작되었습니다.')
test = input('검색할 단어를 입력하세요 >>> ')

path = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://dict.naver.com/')

time.sleep(1)

element = driver.find_element_by_name('dicQuery')
element.send_keys(test, Keys.ENTER)

time.sleep(1)
