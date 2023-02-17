
def get_headers(raw_header):
    """
    通过原生请求头获取请求头字典
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    """
    return dict(line.split(": ", 1) for line in raw_header.split(";") if line != '')

def get_cookies(raw_cookie):
    """
    通过原生cookie获取cookie字段
    :param cookie_raw: {str} 浏览器原始cookie
    :return: {dict} cookies
    """
    return dict(line.split("=", 1) for line in raw_cookie.split("; "))


if __name__ == '__main__':
    raw_header = '''
Host: www.baidu.com
Connection: keep-alive
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.baidu.com/s?wd=fiddler%E6%8F%90%E5%8F%96%E8%AF%B7%E6%B1%82%E5%A4%B4&rsv_spt=1&rsv_iqid=0xc1f47d110000a2a3&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=fiddler%25E6%258F%2590%25E5%258F%2596%25E5%25A4%25B4&rsv_t=4dbe1pHQPCz%2Fx6UmbqLg0VvzZ1zxUfqifegoZoJKkA3fRkRsMWgzlDajT5xwaqD4nJeP&rsv_btype=t&inputT=7545&rsv_sug3=42&rsv_sug1=29&rsv_sug7=100&rsv_pq=b08d81f6000082ca&rsv_sug4=8721
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BIDUPSID=8C0BD16C3A21164A6D891753020F3907; PSTM=1665802318; BAIDUID=8C0BD16C3A21164A985CFB3C9BC07682:FG=1; BD_UPN=12314753; newlogin=1; BDUSS=EprZXplRnhud0N5UkgwYUFkaGpQbDRiZjF-U35kTFduYVpvZERmZFdYTjQ0QTVrSVFBQUFBJCQAAAAAAAAAAAEAAACpuAFRzdqy29PDu6fD-wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhT52N4U-djU; BDUSS_BFESS=EprZXplRnhud0N5UkgwYUFkaGpQbDRiZjF-U35kTFduYVpvZERmZFdYTjQ0QTVrSVFBQUFBJCQAAAAAAAAAAAEAAACpuAFRzdqy29PDu6fD-wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhT52N4U-djU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=6; ZD_ENTRY=baidu; BAIDUID_BFESS=8C0BD16C3A21164A985CFB3C9BC07682:FG=1; FPTOKEN=9XkvW2XKW9d4TeG2Th7v6mBZEDty45a+YgghzL3fBQzGH0qHXYJfCqkTqcr2e8GBm8kMQGJbZ/8JlyOpGh0pKd1P+uumi9XBwexedY9Q+uqyzfAJjXgl8/tJBvOmI/YYGRKJvMcpZ6YbuskltAJSD/IJHXqasb6G4OGS/643WLfIgNdgRPjdDmw/+QUUAUxELTVavY2abRQPhGdyj/4J9ENRVCqpkdbnX96RA3Zp8xePKuZCNuOSbnLwO3/+fVdHzOsOUzcAqffPKDHGtcQ9qvTQme6BmraNfm601GuXjtDsrjDGDkWD/bI148gCKAyMLI23pLrJJfC99KR3iLfvELyKEANGzrF2CV8ZSepCZTqI2QRz5Q/wUECUkTMMSFsydAdaYtgcP+Pwjl7roYh+bg==|TJhzEJ4UoCkncjJHm7inJC8yWcOn9HVswSBz2mpAhMY=|10|218bacf40a6eafee9508698938fe3215; BD_HOME=1; BA_HECTOR=2k0h0400al80ah0k0k210hvg1huu9s71k; ZFY=KkpJAzye9nMSMcgBH:AwxyYcAI2aDVyCVjiK6XhPyt:Bs:C; __bid_n=1865e33c632c6bf5324207; ab_sr=1.0.1_YjgxNjViOWE5MDUzMDA2YTRlYTA2NTE2MGEyMjY0YTU0MmQyM2U0N2QyNDI2ZjJlMDc2ZTAzYWViNGU4ZTk0OTk0YWE5OTRkNzY4YzQxNGMxOGYzOWY4ZTBhZWMyNWYxMzlhOWI5ZTJhZGJmY2I3MDFjMmFiZmEzYjdhMDdlZGYwMGM4YzZmMDJlYWUwNmRkYmQ3OGZjMzczYmVkZTVmMjIzMTU2ODk4YTY4NmQzYjlhNzkxNDJjYzEyYThhMThl; H_PS_PSSID=; COOKIE_SESSION=9537_0_8_9_7_7_1_0_8_6_0_0_25601_0_3_0_1676623502_0_1676623499%7C9%231565731_53_1670565657%7C9; baikeVisitId=67c5ddac-1adb-453c-a402-18f73b67867a; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_645EC=e834rmPTuztfm4CVn%2BMXMVZoVJmVfL1VfMInYNU%2BkaM3kvJqUwA1jcAUBcNHTNuNxtpO
'''
    raw_cookie = ''''''
    print(get_headers(raw_header))
    print(get_cookies(raw_cookie))

