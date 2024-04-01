import os
import sys
import urllib.request
from bs4 import BeautifulSoup as bs
client_id = "wKJ87sNzIg1I8VOPG7pn"
client_secret = "QsZoc18NKC"
encText = urllib.parse.quote("장원영")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
txt = response_body.decode('utf-8')

soup = bs(txt, "xml")
items = soup.find_all("item")

for i in items:
    titles = i.find("title")
    print(titles)
    links = i.find("link")
    print(links)
    