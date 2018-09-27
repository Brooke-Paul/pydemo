from urllib import request
import json

requ = request.urlopen("http://www.baidu.com")

# print(requ.read().decode('utf-8')) 设置返回值编码集

currentPageNumber = 1
pageMaxSize = 200


# 获取分页数据，每页设置条数2000条
def getdata(currentpage):
    url = "https://kekai.g2work.com/personajax/listPersonInfoByOrgInfo.json?pageMaxSize=2000&_hidden_currentPageNumber="
    url = url + str(currentpage)
    print(url)
    reque = request.Request(url)
    reque.add_header("cookie",
                     "SEEYON_ESN_COMPANY_DOMAIN=; loginFail=; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; uid=0; dajiaID=4852571270373198836_1537887482692; SEEYON_ESN_COMPANY_ID=892485852779041661148774; JSESSIONID=0FF30E793B477EC309BEB82651AF22A8")
    response = request.urlopen(reque)

    test = response.read().decode('utf-8')
    jsonobject = json.loads(test)

    for key in jsonobject:
        if key == "_page_info":  # 获取分页参数
            totalPageSize = jsonobject[key]["totalPageSize"]
            print("总页数:::" + str(totalPageSize))
            print("当前第:::" + str(currentpage) + ":::页")
    while totalPageSize > currentpage:
        currentpage += 1
        getdata(currentpage)
    else:
        print("Good bye!")


if __name__ == "__main__":
    getdata(currentPageNumber)
