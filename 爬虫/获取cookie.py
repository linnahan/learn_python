import requests

url = 'https://www.processon.com/login'
login_email = '286933867@qq.com'
login_password = 'ZZZ05382881391'
# 创建一个session,作用会自动保存cookie
session = requests.session()
data = {
    'login_email': login_email,
    'login_password': login_password
}
# 使用session发起post请求来获取登录后的cookie,cookie已经存在session中
response = session.post(url = url,data=data)

# 用session给个人主页发送请求，因为session中已经有cookie了
index_url = 'https://www.processon.com/diagrams'
index_page = session.get(url=index_url).text
print(index_page)

import requests
from http import cookiejar

# 创建一个session,作用会自动保存cookie
session = requests.session()

# 指定cookie保存的路径
session.cookies = cookiejar.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)  # 加载cookie文件，ignore_discard = True,即使cookie被抛弃，也要保存下来
except:
    print('cookie未能加载')

def login_save_cookie():
    """
    登录并保存cookie到本地
    :return:
    """
    url = 'https://www.processon.com/login'
    login_email = '*****@qq.com'
    login_password = '****1391'
    data = {
        'login_email': login_email,
        'login_password': login_password
    }
    # 使用session发起post请求来获取登录后的cookie,cookie已经存在session中
    response = session.post(url=url, data=data)
    # 把cookie保存到文件中
    session.cookies.save()


def read_cookie():
    """
    读取cookie进入登录后的页面
    :return:
    """
    index_url = 'https://www.processon.com/diagrams'
    index_page = session.get(url=index_url).text
    print(index_page)

def login_y_n():
    """
    判断用户是否已经登录，我们这里使用的方法是：随便找一个登陆后页面的url，如果我们访问它时不发生重定向，我们就可以
    判断该用户应经登录了
    :return:
    """
    url = 'https://www.processon.com/diagrams/new#template'
    response = session.get(url = url,allow_redirects=False) # allow_redirects =False不允许重定向到登录页面
    if response != 200:
        return False
    else:
        return True

read_cookie()