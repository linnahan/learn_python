import requests,re
from lxml import html


params = {
  "type": "1",
  "oid": "964811855",
  "pid": "947853670",
  "segment_index": "1",
  "pull_mode": "1",
  "ps": "0",
  "pe": "120000"
}

headers = {
'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
}
def bv2av(bv:str)->tuple:
    response = requests.get(url='https://api.bilibili.com/x/web-interface/view',params={'bvid':bv},headers=headers)
    oid = str(response.json()['data']['cid'])
    pid = str(response.json()['data']['aid'])
    return oid,pid
def print_blpl():
    htm = requests.get(r"https://api.bilibili.com/x/v2/dm/web/seg.so?",headers = headers,params = params)
    content_list = re.findall(r"[\u4e00-\u9fef]{2,}", htm.text)
    # print(htm.text)
    print(content_list)
    print(len(content_list))
def html_bv(url):
    a = re.search('/(BV.*?)/',url)
    return a.group(1)

if __name__ == '__main__':
    # print(bv2av('BV1Xt411v7wB'))
    params["oid"],params["pid"] = bv2av('BV1Kb4y1f7do')
    print_blpl()
    '''输入视频网址获取弹幕'''
    # params["oid"],params["pid"] = bv2av(html_bv(input("输入视频网址获取弹幕")))
    # print_blpl()



