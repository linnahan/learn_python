import urllib.request



opener=urllib.request.build_opener()
ua=('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36")
opener.addheaders=[ua]
urllib.request.install_opener(opener)
url='http://www.gkstk.com/wenku/1939665.html'
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
#print(data)
file = open('this.md','w+',encoding='utf-8')
file.write(data)
file.close()
print('finished')
