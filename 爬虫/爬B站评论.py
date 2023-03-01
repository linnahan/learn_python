import requests,re,time,jsonpath
from lxml import html

session = requests.session()
params = {
  "mode": "3",
  "next": 0,
  "oid": "947853670",
  "plat": "1",
  "seek_rpid": "",
  "type": "1"
}

headers = {
'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
}
def bv2av(bv:str)->str:
    response = requests.get(url='https://api.bilibili.com/x/web-interface/view',params={'bvid':bv},headers=headers)
    av = str(response.json()['data']['aid'])
    return av
def print_blpl(n=10):
    for i in range(n):
        htm = session.get(r"https://api.bilibili.com/x/v2/reply/main?",headers = headers,params = params)
        for j in range(30):
            try:
                content = jsonpath.jsonpath(htm.json(),'$.data.replies[%d].content.message'%j)[0]
                print(content)
            except Exception as f:
                break
        print(htm.url)
        if params['next'] == 0:
            params['next'] += 2
        else:
            params['next'] += 1

if __name__ == '__main__':
    # print(bv2av('BV1Hh411k7C4'))
    params["oid"] = bv2av('BV1Kb4y1f7do')
    print_blpl()



