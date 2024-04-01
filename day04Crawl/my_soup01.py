import requests
from bs4 import BeautifulSoup as bs

res = requests.get("http://localhost:8888/HELLO_WEB_EMP/emp_list")
soup = bs(res.text, "html.parser")

trs = soup.find_all("tr")
for idx, t in enumerate(trs):
    if idx == 0:
        continue
    tds = t.find_all("td")
    print(tds[1].text, "-", tds[3].text)


