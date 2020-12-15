from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
from numpy.matlib import rand
from numpy.random.mtrand import randint
from pygame import image

#随机字母：
def rndChar():
    return chr(random.randint(65,90))

#随机颜色1：
def rndColor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2：
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#图片大小240*60：
width = 60*4
height = 60
image = Image.new('RGB', (width, height), (155,155,155))

#创建Font对象：
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

#创建Draw对象：
draw = ImageDraw.Draw(image)

#填充每个像素：
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor1())

#输出文字：
for i in range(4):
    draw.text((60 * i + 10 , 10), rndChar(), fill = rndColor2(), font = font)
    
#模糊处理：
image = image.filter(ImageFilter.BLUR)
image.save('test.jpg',  'jpeg')
print('生成成功！')
