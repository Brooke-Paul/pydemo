from urllib import request
from bs4 import BeautifulSoup

# BeautifulSoup 的简单使用

req = request.urlopen("https://category.vip.com/search-1-0-1.html?q=3|95878")
html = req.read().decode("utf-8")

btfs = BeautifulSoup(html, "html.parser")
print(btfs)
imghtml = btfs.find_all("a")
myList = []
print(imghtml)
for i in imghtml:
    # a = i.img['data-original']
    #
    a = i.img
    if a:
        myList.append(a.get("data-original"))


print(myList)

