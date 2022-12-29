from  bs4 import BeautifulSoup
import requests


ml_url = "https://book.qidian.com/info/1032766396/#Catalog"
header = {
    "Host": "book.qidian.com",
    "Referer": "book.qidian.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}
HtmlPage = requests.get(url=ml_url, headers = header)
HtmlPage.encoding = "utf-8"
print(HtmlPage.request.headers)
print(HtmlPage.text)
