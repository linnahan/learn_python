import urllib.request,re,random
import progress_bar

def urlag():
    uapools=[
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",#360
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",#谷歌
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",#火狐
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",#火狐
]
    thisua=random.choice(uapools)
    opener=urllib.request.build_opener()
    ua=('User-Agent',thisua)
    opener.addheaders=[ua]
    urllib.request.install_opener(opener)
    #print('当前使用User-Agent：',thisua)
n = 0
xiaohua=open('xiaohua.txt','w')
for i in range(6500,7000):
    urlag()
    try:
        url='http://xiaodiaodaya.cn/article/view.aspx?id=%d'%i
        data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
        string='<!--listS-->(.*?)<!--listE-->'
        neirong=re.compile(string,re.S).findall(data)
        a=neirong[0].replace('<br/><br/>','\n')
        b=a.replace('<br/>', ' ')
        xiaohua.writelines(b)
        xiaohua.write('\n')
        n+=1
        #print('成功第%d个'%n)
    except:
        pass
    progress_bar.progress_bar(500)

xiaohua.close()
print('总共成功访问了%d次'%n)
