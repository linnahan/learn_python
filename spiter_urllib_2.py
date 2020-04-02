import urllib.request,re
url ='https://wenku.baidu.com/view/ab46e28c6037ee06eff9aef8941ea76e58fa4ac2.html'
html = urllib.request.urlopen(url).read().decode('utf-8','ignore')
print(html)
