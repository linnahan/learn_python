import urllib.request,requests,re



'''opener=urllib.request.build_opener()
ua=('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36")
opener.addheaders=[ua]
urllib.request.install_opener(opener)
url='https://wenku.baidu.com/view/c29ebdb2172ded630b1cb6b7.html'
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
file = open('this.html','w+',encoding='utf-8')
file.write(data)
file.close()
print('finished')'''



da = requests.request('get','https://wenku.baidu.com/view/51a9f39ec381e53a580216fc700abb68a882ad2d.html')
#print(da.text)
print(da.encoding)
print(da.headers)
print(da.cookies)
print(da.apparent_encoding)
import re


string = '<p(.*?)</p>'
corvent = re.compile(string).findall(da.text)
print(type(corvent))
try:
    bb = '\n'.join(corvent)
    print(bb)
except:
    print('hh')