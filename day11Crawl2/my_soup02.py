import requests
from bs4 import BeautifulSoup as bs

res = requests.get("http://localhost:8888/MVVM_EMP/emp.html")
res.encoding = 'utf-8'
soup = bs(res.text, "html.parser")
# print(soup)

trs = soup.select("tr")

# print(trs)
for idx,tr in enumerate(trs):
    if idx == 0:
        continue
    tds = tr.select("td")
    print(tds)