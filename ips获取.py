import requests,time,re,xlwt


start_time = time.time()
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('ips')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
ab =  {'https':'http://47.96.162.28:1080'}
n = 0
for page in range(1,5):
    page_time = time.time()
    ip_url = 'http://www.superfastip.com/welcome/freeip/%d'%page
    reponse = requests.get(url = ip_url,timeout = 2,headers=headers,proxies=ab)
    res0 = reponse.text.replace('\n','').replace('\t','').replace(' ','')
    string1 = '<thclass="text-center">(.*?)</th><thclass="text-center">(.*?)</th><thclass="text-center">(.*?)</th><thclass="text-center">(.*?)</th><thclass="text-center">(.*?)</th><thclass="text-center">(.*?)</th><thclass="text-center">(.*?)</th>'
    res1 = re.compile(string1).findall(res0)[1]
    for on in range(len(res1)):
        worksheet.write(n,on,res1[on])
    n +=1
    string2 = '<td>(.*?)</td><td>(.*?)</td><!--<td>(.*?)</td>--><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>'
    res2 = re.compile(string2).findall(res0)[1:]
    for i in range(len(res2)) :
        ip = 'http://'+res2[i][0]+':'+res2[i][1]
        proxies = {'http':ip}
        url = 'https://www.baidu.com/'
        reponse = requests.get(url=url,proxies=proxies)
        if reponse.status_code == 200:
            for j in range(len(res2[i])):
                worksheet.write(i+n,j,res2[i][j])
    n += len(res2)
    workbook.save('qqips.xls')
    page__time = time.time()
    print('已导入第%d页,用时%.5f秒'%(page,page__time-page_time))
    time.sleep(3)
final_time = time.time()
time = final_time-start_time
print('成功，总用时：%.5f秒'%time)