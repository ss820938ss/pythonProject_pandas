import time
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def mainMenu():
    print('----------------------------------------')
    print('            깃허브 검색 프로그램           ')
    print('1. 모바일 창 검색  2. 전체화면 검색  3. 종료 ')
    print('----------------------------------------')


def main(search=None):
    mainMenu()

    while True:
        select = int(input("1. 모바일  2. 전체화면  3.종료"))
        if select == 1:
            MView(search)
            print(MView)

        elif select == 2:
            FView(search)
            print(FView)

        else:
            break


def MView(search):
    test = input('검색할 이름을 입력하세요 : ')

    time.sleep(2)
    path = 'C:/chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(path)
    search = driver.get('https://github.com/')

    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/button').send_keys(Keys.ENTER)
    # 깃허브에서 창 사이즈가 적으면 검색창 인식이 안되어서 메뉴바 클릭 명령 추가

    element = driver.find_element_by_name('q')
    time.sleep(2)
    element.send_keys(test, Keys.ENTER)
    time.sleep(2)


def FView(search):
    test = input('검색할 이름을 입력하세요 : ')
    path = 'C:/chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(path)
    search = driver.get('https://github.com/')

    driver.set_window_position(0, 0)
    driver.set_window_size(1500, 3000)

    element = driver.find_element_by_name('q')
    time.sleep(2)
    element.send_keys(test, Keys.ENTER)
    time.sleep(2)


if __name__ == "__main__":
    main()

# image_link = driver.find_element_by_link_text('이미지')
# image_link.click()
#
# time.sleep(3)
# #네이버용
# #image_tag = driver.find_elements_by_tag_name('section> div> div> div> div> div> div> a> img')
#
# #구글용
# #image_tag = driver.find_elements_by_tag_name('span > div > div > div > a > div > img')
# image_tag = driver.find_elements_by_class_name('Q4LuWd')
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
#     urlretrieve(link, './images/{}{}.jpg'.format(test,i+1))
#
