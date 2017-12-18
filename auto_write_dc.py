# auto_wirte_dc.py 1.0
#
# Author : yskim
# E-Mail : bookstation __at__ naver __dot__ com
#
# auto_write_dc.py is free software
#
# Change log
#
# 2017/12/18 - Started ver 1.0
#
#

from selenium import webdriver
import time
import configparser

Config = configparser.ConfigParser()
# 설정파일 경로
Config.read('./user.conf')
url = Config.get('dc', 'url')
id = Config.get('dc', 'id')
pw = Config.get('dc', 'pw')
login_button = Config.get('dc', 'login')
gall = Config.get('dc', 'gall')

#크롬드라이버 경로
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)

driver.get(url)

# 아이디
driver.find_element_by_name('user_id').send_keys(id)
# 패스워드
driver.find_element_by_name('password').send_keys(pw)

driver.find_element_by_id('login_ok').click()

driver.get(gall)
# 제목 입력
driver.find_element_by_name('subject').send_keys('타이틀 제목')

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))
print(driver.page_source)

#본문 입력
driver.find_element_by_tag_name("body").send_keys("본문 내용")

driver.switch_to_default_content()
#글쓰기 저장
driver.find_element_by_xpath("//input[@src='http://nstatic.dcinside.com/dgn/gallery/images/btn_save.gif']").click()
#저장 딜레이
time.sleep(1)
#웹페이지 닫
driver.close()
