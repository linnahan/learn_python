import os
from PIL import Image
import numpy as np



# 改变图片像素
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

# 图片二值化
def binaryImage(file):   
    img = Image.open(file)
    img2 = img.convert('1') # 图像二值化
    img2.save('niu2.png')
    arr = np.array(img2)
    print(arr)
    return arr

# 打印图片01点阵
def printBin(arr):
    for i in range(height):
        for j in range(width):
            if arr[i, j] == True:
                print('0', end='')
            else:
                print('1', end='')
        print()

# 拼接图片
def head2char(workspace, user, self, arr):
    folder = "{}\\{}".format(workspace,user)
    os.chdir(folder)   # 将工作路径转移至头像文件夹
    imgList = os.listdir(folder)     # 获取文件夹内头像列表
    numImages = len(imgList)    # 获取头像图片个数
    n=0     # 变量n用于循环遍历头像图片，即当所需图片大于头像总数时，循环使用头像图片
    color = '#FFFFFF'
    '''初始化颜色列表，用于背景着色：FFFACD黄色 #F0FFFF白  #BFEFFF 蓝  #b7facd青色
     #ffe7cc浅橙色  #fbccff浅紫色 #d1ffb8淡绿 #febec0淡红 #E0EEE0灰'''
    os.chdir(folder)    # 工作路径转到头像所在文件夹
    canvas = Image.new('RGB', (width*eachSize, height*eachSize), color)  # 建一块画布
    for i in range(height):    # 每个点阵中的点用一张100*100的头像来填充
        for j in range(width):
            if arr[i, j] == False:      # 点阵信息为1，即代表此处要显示头像来组字
                xHead = n % numImages    # 循环读取头像图片
                try:
                    img = Image.open(imgList[xHead])  # 打开图片
                except IOError:
                    print("有1位朋友的头像读取失败，已使用本人头像替代")  # 有些人没设置头像，就会有异常
                    img = Image.open(self)
                finally:
                    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)  # 调整图片
                    canvas.paste(img, ((j % width) * eachSize, i * eachSize))  # 拼接图片
                n= (n+1) % numImages     # 调整n以读取后续图片
    os.chdir(workspace)
    canvas.save('result.jpg', quality=10)      # quality代表图片质量，1-100
    
    
if __name__ == '__main__':
    file_in = 'niu1.png'
    width = 35*4
    height = 26*4
    file_out = 'niu1.out.png'
    file = file_out
    workspace = os.getcwd()
    user = 'xinsuanna'
    self = 'xinsuanna.jpg'
    eachSize = 100   # 设置头像裁剪后尺寸
    produceImage(file_in, width, height, file_out)
    print('像素改变成功')
    arr = binaryImage(file)
    printBin(arr)
    head2char(workspace, user, self, arr)
    print('succeed')



