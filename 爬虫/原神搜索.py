import requests,jsonpath
from urllib import parse
from selenium import webdriver

def ll():
    session = requests.session()
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    answer = parse.quote(input("搜索："))
    reponse1 = session.get(
        f'https://bbs-api.miyoushe.com/post/wapi/searchPosts?gids=2&keyword={answer}&size=10',
        headers=headers)
    js1_data = reponse1.json()
    n = 1
    title_list = jsonpath.jsonpath(js1_data,'$..subject')
    postid_list = jsonpath.jsonpath(js1_data,'$..post_id')
    content_list = jsonpath.jsonpath(js1_data,'$..content')
    global url_list
    url_list = []
    for i in title_list:
        url = f"https://www.miyoushe.com/ys/article/{postid_list[n-1]}"
        url_list.append(url)
        print(f"{n}、{i}----------{url}\n{content_list[n-1]}")
        n += 1
def dd():
    while True:
        ans = input("输入编号打开网页：")
        if ans == '':
            break
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url_list[int(ans)-1])

if __name__ == '__main__':
     ll()
     dd()

