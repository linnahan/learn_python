import requests
from lxml import html

session = requests.session()
cookies = {
    '_yep_uuid': '5eba0ed3-9777-ffcf-ca6d-fd6f558678bd',
    'e2': '%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D',
    'e1': '%7B%22pid%22%3A%22qd_P_read%22%2C%22eid%22%3A%22qd_R120%22%2C%22l1%22%3A3%7D',
    'newstatisticUUID': '1670240725_7916634439',
    '_csrfToken': 'oRZYlDqSMma3l728635TGtyRY1nzNS0b0cYkFoRF',
    'fu': '1230339736',
    'qdrs': '0%7C3%7C0%7C0%7C1',
    'showSectionCommentGuide': '1',
    'qdgd': '1',
    'traffic_utm_referer': 'https%3A//www.baidu.com/link%3Furl%3DYJe2_m3VW-k8DLLS7I9DUImBX3nYeFSD3Gv0Fe_VL47%26wd%3D%26eqid%3Dc78f2bde0000154d0000000663ec8923',
    'Hm_lvt_f00f67093ce2f38f215010b699629083': '1676445994',
    '_gid': 'GA1.2.2001193042.1676445994',
    'pageOps': '1',
    'navWelfareTime': '1676446011110',
    'rcr': '1033071585%2C1032766396',
    'bc': '1033071585',
    '_gat_gtag_UA_199934072_2': '1',
    'lrbc': '1033071585%7C701338724%7C0%2C1032766396%7C695742597%7C0',
    'Hm_lpvt_f00f67093ce2f38f215010b699629083': '1676446341',
    '_ga_PFYW0QLV3P': 'GS1.1.1676445993.7.1.1676446341.0.0.0',
    '_ga': 'GA1.1.1471425084.1670240727',
    '_ga_FZMMH98S83': 'GS1.1.1676445993.7.1.1676446341.0.0.0',
}
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://read.qidian.com/chapter/mkAh-cQVP0w3LbtcZNMchg2/-5cDWlYbdIzM5j8_3RRvhw2/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
 }


def get_text(url = 'https://read.qidian.com/chapter/f8NdeY_56CIJiWg6PYdjVg2/z8czHbrYkCTwrjbX3WA1AA2/'):
    try:
        response = session.get(url,
            cookies=cookies,
            headers=headers,)
        htm = html.fromstring(response.text)
        next_url = 'https:' + htm.xpath('//*[@id="j_chapterNext"]/@href')[0]
        text = htm.xpath('//div[@class="main-text-wrap "]')
        title = text[0].xpath('div/h3/span[@class="content-wrap"]/text()')[0]
        content_list = text[0].xpath('div[@class="read-content j_readContent"]/p/text()')
        with open(r'D:\gitlearn\learn_python\cache\aaa.txt','a+',encoding='utf-8') as f:
            f.write(title + "\n")
            f.writelines('\n'.join(content_list))
        global n
        n += 1
        print(f"第{n}章完成")
        get_text(url=next_url)
    except Exception as f:
        print(f)
if __name__ == '__main__':
    n = 0
    get_text()
'''在get_text里面输入小说第一章的url即可爬取任何小说'''

