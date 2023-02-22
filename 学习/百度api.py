from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = '30650709'
API_KEY = 'yD1Rq4k34QpX448QexCetQZK'
SECRET_KEY = 'bwBZAjrmGTb8yXRfQyd6ZGVSH1nRKijR'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

image = get_file_content(r'D:\gitlearn\learn_python\cache\test1.png')

# 调用通用文字识别（标准版）
res_image = client.basicGeneral(image)
# 调用通用文字识别（高精度版）
# res_image = client.basicAccurate(image)
result_list = res_image.get('words_result') # [{},{},{}]
for i in result_list:
    print(i.get('words'))



