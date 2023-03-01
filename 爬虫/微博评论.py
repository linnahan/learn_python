import requests,re,time,jsonpath
from lxml import html

session = requests.session()
params = {
  "is_reload": "1",
  "id": "4873807821015602",
  "is_show_bulletin": "2",
  "is_mix": "0",
  "count": "10",
  "uid": "7735105675"
}
headers = {
'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
}
for i in range(10):
    htm = session.get(r"https://weibo.com/ajax/statuses/buildComments?",headers = headers,params = params)
    max_id = jsonpath.jsonpath(htm.json(),'$.max_id')[0]
    text_raw = jsonpath.jsonpath(htm.json(),'$..text_raw')
    print(max_id)
    print(text_raw)
    print(htm.url)
    if str(max_id) == '0':
        break
    # params['count'] = '20'
    params['max_id'] = str(max_id)

# print(htm.text)


