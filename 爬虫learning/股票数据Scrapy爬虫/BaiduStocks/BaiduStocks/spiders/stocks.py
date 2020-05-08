# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stock'
    start_urls = ['http://http://quote.eastmoney.com/center/gridlist.html#hs_a_board']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][zh]\d{6}',href)[0]
                url = 'http://gupiao.baidu.com/stock/'+stock+'.html'
                yield scrapy.Request(url,callback=self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>',keyList[i])[0][1,-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>',valueList[i])[0][0,-5]
            except:
                val = '--'
            infoDict[key] = val
        infoDict.update(
            {'股票名称':re.findall('\s.*\(',name)[0].spilt()[0] + re.findall('\>.*\<',name)[0][1,-1]}
        )
        yield infoDict