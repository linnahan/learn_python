import requests
req=requests.get('http://www.baidu.com')
print(req)
req.encoding='utf-8'
content=req.text
print(content)
firl=open('baidu.html','w')
firl.write(content)
firl.close()