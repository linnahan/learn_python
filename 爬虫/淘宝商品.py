import requests
import re


def getHTMLtext(url):
    try:
        r = requests.get(url,timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ift,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ift.append([title,price])
    except:
        print('aa')

def printGoodsList(ift):
    tplt = '{:4}\t{:16}\t{:8}'
    print(tplt.format('序号','商品名称','价格'))
    count = 0
    for g in ift:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '狗'
    depth = 2
    start_url = 'htt://s.taobao.com/search?q='+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLtext(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main()
