# auto_wirte_dc.py 1.0
#
# Author : yskim
# Fork by deathmojang
# E-Mail : deathmojang __at__ gmail __dot__ com
#
# auto_write_dc.py is free software
#
# Change log
#
# 2017/12/18 - Started ver 1.0
# 2019/2/27 - Update ver 2.0 (fits to new dcinside)
#
#
#

from selenium import webdriver
import time
import configparser

# 설정파일 경로
Config = configparser.ConfigParser()
Config.read('./user.conf')

id = Config.get('dc', 'id')
pw = Config.get('dc', 'pw')
url = Config.get('dc', 'url')
gall = Config.get('dc', 'gall')
title = Config.get('dc', 'title')
content = Config.get('dc', 'content')

# 리눅스를 위한 가상 디스플레이 드라이버 로드 
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 800))  
#display.start()

# 크롬 환경 변수
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=800x600')
options.add_argument("disable-gpu")

#크롬 드라이버 로드
driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.implicitly_wait(3)

# 디시인사이드 로그인 페이지 로드
driver.get(url)

# 아이디
driver.find_element_by_name('user_id').send_keys(id)
# 패스워드
driver.find_element_by_name('pw').send_keys(pw)
# 로그인
driver.find_element_by_id('login_ok').click()

# 글을 쓰고자 하는 갤러리로 이동
driver.get(gall)
time.sleep(3)

# 제목 입력
driver.find_element_by_name('subject').send_keys(title)
# HTML으로 쓰기 방식 변경
driver.find_element_by_id("tx_switchertoggle").click();
time.sleep(1)

# 글쓰기 폼으로 진입
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))
print(driver.page_source)

#본문 입력
driver.find_element_by_tag_name("body").send_keys(content)

driver.switch_to_default_content()
#글쓰기 저장
time.sleep(3)
driver.find_element_by_xpath("//button[@class='btn_blue btn_svc write']").click()
#저장 딜레이
time.sleep(1)
#웹페이지 닫기
driver.close()

#display.sendstop()
#display.stop()
