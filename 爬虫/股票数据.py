import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHtmlText(url,code='utf-8'):
    try:
        data = requests.get(url,timeout=10)
        data.raise_for_status()
        data.encoding = data.apparent_encoding
        return data.text
    except:
        return ''

def getStockList(lst,stockURL):
    html = getHtmlText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][zh]\d{6}',href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHtmlText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find_all('div',attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'bets.name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count += 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count += 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end='')
            #traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    output_file = 'BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

if __name__ == '__main__':
    main()