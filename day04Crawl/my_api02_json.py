import urllib.request
import json

client_id = "wKJ87sNzIg1I8VOPG7pn"
client_secret = "QsZoc18NKC"
encText = urllib.parse.quote("장원영")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
txt = response_body.decode('utf-8')

datas = json.loads(txt)
list = datas["items"]
for i in list:
    print("title:"+i["title"], end="\t")
    print("link:"+i["link"])

