import requests
import time
import re


#爬取数据
def getHtmlText(page):
    global text
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
    url = "https://www.kanunu8.com/book2/11019/%d.html"%page
    response = requests.get(url = url,headers = headers)
    response.encoding = "gbk"
    text = response.text


#提取数据
def getText():
    global title,body
    re_title = re.compile(r'<h1>\w*\s*(.*?)<br>')
    re_body = re.compile(r'<p>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p>')
    title = re_title.findall(text)
    body = re_body.findall(text)


#保存到txt
def saveTXT():
    note = open(r"C:\Users\admin\Desktop\菊苣的初恋.txt", mode="a+")
    note.write("\n\n" + title[0] + "\n\n")
    for data in body:
        note.write("   " + data + "\n")
    note.close()

#主流程
def main():
    zpage = 0
    for page in range(199174,199201):
        getHtmlText(page = page)
        getText()
        saveTXT()
        zpage += 1
        time.sleep(4)
        print("第%d章完成"%zpage)

if __name__ == '__main__':
    main()
