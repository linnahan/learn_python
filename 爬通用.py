import urllib.request,requests



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

da = requests.get('https://wenku.baidu.com/view/c29ebdb2172ded630b1cb6b7.html')
#print(da.text)
print(da.encoding)
print(da.headers)
print(da.cookies)
print(da.apparent_encoding)