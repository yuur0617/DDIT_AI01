import urllib.request
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pymysql

client_id = "wKJ87sNzIg1I8VOPG7pn"
client_secret = "QsZoc18NKC"
encText = urllib.parse.quote("장원영")
url = "https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
txt = response_body.decode('utf-8')

soup = bs(txt, "html.parser")

# SQLite 데이터베이스 연결 및 테이블 생성
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 현재 시간 출력
time = datetime.now().strftime('%Y%m%d-%H%M')

row_sty= soup.select('li.row_sty')
for idex, i in enumerate(row_sty):
    code = i.select_one('span.name a')['href'].split('/')[-1]
    name = i.select_one('span.name a').text.strip()
    price = i.select_one('div.st_price span.price').text

    # print(f"코드: {code}, 이름: {name}, 가격: {price}, 현재 시간: {time}")
    
    iprice = int(price.replace(',', ''))
    # 데이터베이스에 데이터 삽입
    cursor.execute('''
        INSERT INTO stock(s_name, price, s_code, ymd)
        VALUES (%s, %s, %s, %s)
    ''', (name, iprice, code, time))
    
    conn.commit()
    
print(str(idex) + "개 저장 완료")
# 데이터베이스 연결 종료
conn.close()