from lxml import html
import csv

def write_to_csv(dict_list):
    with  open(r'D:\gitlearn\learn_python\data\b.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=["类型","小说标题","小说链接","作者","作者首页"])
        writer.writeheader()
        writer.writerows(dict_list)


with open(r"D:\gitlearn\learn_python\data\a.html", "r", encoding="gbk") as f:
    scoure = f.read()
    dict_list = []
    htm = html.fromstring(scoure)  # 整个HTML页面
    htm_block = htm.xpath('//div[@class = "line index-body-nr-left clearfix"][2]/div') # 要提起数据的一大块[]
    for style_block in htm_block: # 一整个类型的数据
        style = style_block.xpath('h2/text()')  # 类型
        style_on = (''.join(style)).strip()
        urlandtext = style_block.xpath('ul/li')   # 类型下的数据
        for onea in urlandtext: # 单个小说完整数据
            a = onea.xpath('a') # 提取a标签
            url = a[0].get('href')   # 小说链接
            title = a[0].text   # 小说标题
            aurl = a[1].get('href')    # 作者链接
            autor = a[1].text  # 作者名字
            dict = {"类型":style_on ,"小说标题":title ,"小说链接":url ,"作者":autor ,"作者首页":aurl }
            dict_list.append(dict)
            write_to_csv(dict_list)



