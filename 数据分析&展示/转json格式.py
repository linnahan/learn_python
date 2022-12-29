"""
GET /info/1033675720/ HTTP/1.1
Host: book.qidian.com
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://book.qidian.com/info/1033675720/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _yep_uuid=b028a1d6-7027-b63f-b9e8-9ee9d800cf0d; e1=%7B%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G16%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; newstatisticUUID=1670240725_7916634439; Hm_lvt_f00f67093ce2f38f215010b699629083=1670240727; _csrfToken=oRZYlDqSMma3l728635TGtyRY1nzNS0b0cYkFoRF; fu=1230339736; _gid=GA1.2.1525549018.1670240727; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; Cc2838679FS=5tVstI3UcKiDWxQISra.CfmbrzBEWmjByCHXa21ess6.8eu.pr3NfziWW3Y9zn6BV3vFiwnJMeex4W2yXzplSla; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=1032766396%7C695742597%7C0; rcr=1032766396; navWelfareTime=1670301265158; bc=1032766396; traffic_utm_referer=https%3A//www.baidu.com/link%3Furl%3DfkWFyMYWtYaF2oTlJpyU2ZGB-tclAn5ntXjnQMR5Zee%26wd%3D%26eqid%3Ddd90f71b000106f300000006638ecb15; _gat_gtag_UA_199934072_2=1; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; _ga=GA1.1.1471425084.1670240727; Hm_lpvt_f00f67093ce2f38f215010b699629083=1670302515; Cc2838679FT=63g4hWKiinulqqqDlyQvowa6r0ywBq2dGqu03adb3L5zhj2QF3gr74HJFdX91occwcf69OBm0td9ENJeHtxZ3YZ97SruJjfyBbqifW3xaBBfp12NXW4XjCjPStIIFLQmrq7ac_dqXsijstUWUEHGjl1X2WbdwWSRIKJ5z_hMOf610CJ6.GQxf3__C.xMjVs6JcpDHDTDKpJeDeJr3VWHp76Hk9X9ln4RvxWYERUTu3dwDgYobQm2ZKBi4dVTyy95XpmOOXYTScwTjTmpNmyDamJzoPztLuw_Wkt1DxTAXspBuhRSWmBQuGJKEd_z0qebgDn1UBcfZ0nj3MySwcScEon; _ga_FZMMH98S83=GS1.1.1670301262.3.1.1670302516.0.0.0; _ga_PFYW0QLV3P=GS1.1.1670301262.3.1.1670302516.0.0.0
"""
import re

a = open(r"C:\Users\admin\Desktop\666.txt", mode= "r+")
text = a.read()
rec = re.compile("(.*):\s*(.*)\n")
lbHeader = rec.findall(text)
header = {}
for i in lbHeader:
    header[i[0]] = i[1]
print(header)

a.close()