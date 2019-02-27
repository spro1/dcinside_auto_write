# dc_auto_write
파이썬 셀레니움을 이용한 DC인사이드 자동 글쓰기

automated DCinside web articles writer by using selenium in python


# version
python3.x, windows10

or

python3.x & linux (tested in debian, ubuntu)


# Installation

For windows:

From the repo directory:
```bash
git clone https://github.com/deathmojang/dc_auto_write
pip install -r requirements.txt
```

For linux
```bash
git clone https://github.com/deathmojang/dc_auto_write
pip install selenium configparser setuptools pyvirtual PyVirtualDisplay
```
get and install google-chrome-stable package from https://www.chrome.com

download chrome webdriver from https://chromedriver.chromium.org/downloads and put it in the git directory


# config setting
Open user.conf
```bash
[dc]
id = 아이디 ex) hongildong
pw = 패스워드 ex) 1234qwer
url = http://www.dcinside.com/
gall = 갤러리 주소 ex) http://gall.dcinside.com/board/write/?id=teamfortress2
title = 제목 ex) "서버 열었다"
content = 내용 (html로 작성) ex) "<p>들어와라</p>"
```

# start
파이썬 프로그램 시작
```bash
python3 auto_write_dc.py
```

# 
