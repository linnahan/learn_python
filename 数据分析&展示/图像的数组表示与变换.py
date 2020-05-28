from PIL import Image
import numpy as np


a = np.array(Image.open('test.jpg').convert('L'))
print(a.shape,a.dtype)       #打印宽度、高度和像素RGB值
#b = 255 - a
#b = (100/255)*a + 150       #区间变换
b = 255 * (a/255)**2        #像素平方
im = Image.fromarray(b.astype('uint8'))
im.save('test1.jpg')