import requests
import re
import time


def get_one_page(url):#请求函数：获取某一网页上的所有内容
    headers = {
    'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Host' : 'weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie' : {
        '_T_WM':'63415183995',
        'SSOLoginState':'1591437079',
        'ALF':'1594029079',
        'SCF':'Apgs04sdmcVwoNsU-vSyIrb9yfpNZ47MmfLiREgoaPJNc0sfWeBNQkv3RK9rZ-7hmoy2fHg5QAWV5XII8skJHPs.',
        'SUB':'_2A25z3xdHDeRhGeNM71sY9ynEzDqIHXVRI7kPrDV6PUNbktAfLVj3kW1NTgLov0sfDd5vR9jZvFivfBA7PSYRU2dy',
        'SUBP':'0033WrSXqPxfM725Ws9jqgMF55529P9D9WW13iuryslvPGx8IX6xuWm05JpX5KMhUgL.Fo-ESh.4S0MRS0q2dJLoIE-LxKnLBoBLBoBLxK-LB.qL1heLxKML1-2L1hB_i--fiKn4iK.p',
        'SUHB':'0z1AHO9PDOrlWk',
        'MLOGIN':'1',
        'M_WEIBOCN_PARAMS':'luicode%3D20000174'
    },
    'DNT' : '1',
    'Connection' : 'keep-alive'
     }#请求头的书写，包括User-agent,Cookie等
    response = requests.get(url,headers = headers,verify=False)#利用requests.get命令获取网页html
    if response.status_code == 200:#状态为200即为爬取成功
        return response.text#返回值为html文档，传入到解析函数当中
    return None
def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    with open('test.txt','a',encoding='utf-8') as fp:
        fp.write(result)

for i in range(1,51):
    url = "https://weibo.cn/1638782947/Iy5IBEutu?type=comment&page="+str(i)
    html = get_one_page(url)
    print(html)
    print('正在爬取第 %d 页评论' % (i+1))
    parse_one_page(html)
    time.sleep(3)

content = "test.txt"

rawResults = re.findall(">.*?<",content,re.S)
firstStepResults  = []
for result in rawResults:
    #print(result)
    if ">\'][\'<"  in result:
        continue
    if ">:<"  in result:
        continue
    if ">回复<"  in result:
        continue
    if "><"  in result:
        continue
    if ">\', \'<"  in result:
        continue
    if "@"  in result:
        continue
    if "> <"  in result:
        continue
    else:
        firstStepResults.append(result)
subTextHead = re.compile(">")
subTextFoot = re.compile("<")
i = 0
for lastResult in firstStepResults:
    resultExcel1 = re.sub(subTextHead, '', lastResult)
    resultExcel = re.sub(subTextFoot, '', resultExcel1)
    print(i,resultExcel)
    i+=1
