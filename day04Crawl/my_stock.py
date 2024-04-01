import requests
from bs4 import BeautifulSoup as bs
import datetime
from day04Crawl.daostock import DaoStock
import time

print("1")
time.sleep(5)

ds = DaoStock()

now = datetime.datetime.now()
ymd = now.strftime("%Y%m%d_%H%M") #시간

res = requests.get("https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry")

soup = bs(res.text, "html.parser")

names = soup.select(".st_name")
for idx, n in enumerate(names):
    s_name = n.text.strip() #이름
    s_code = n.select("a")[0]['href'].split('/')[3] #코드
    price = n.parent.select(".price")[0].text.replace(",", "") #가격
    cnt = ds.insert(s_name, price, s_code, ymd)
    print(idx, cnt, s_name, s_code, price, ymd)
    
    
