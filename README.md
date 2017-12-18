# dc_auto_write
파이썬 셀레니움을 이용한 dcinside 자동 글쓰기
python auto write dc inside using selenium

# Installation

From the repo directory:
```bash
git clone https://github.com/spro1/dc_auto_write
pip install -r requirements.txt
```

# config setting
Open user.conf
```bash
[dc]
id = 아이디 ex) hongildong
pw = 패스워드 ex) 1234qwer
url = http://www.dcinside.com/
login = //button[@id="lbStln"]
gall = 갤러리 주소 ex) http://gall.dcinside.com/board/write/?id=coin
save = //input[@src="http://nstatic.dcinside.com/dgn/gallery/images/btn_save.gif"]
```

# start
제목, 본문 내용 변경
edit auto_write_dc.py
```bash
driver.find_element_by_name('subject').send_keys('타이틀 제목')
driver.find_element_by_tag_name("body").send_keys("본문 내용")
```
파이썬 프로그램 시작
```bash
python auto_write_dc.py
```

# 