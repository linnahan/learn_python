import urllib.request,re
for a in range(20):
    try:
        url='http://xiaodiaodaya.cn/article/view.aspx?id=6953'
        data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
        string ='<title>(.*?)</title>'
        biaoti=re.compile(string,re.S).findall(data)
        print(data)
    except:
        print('done')