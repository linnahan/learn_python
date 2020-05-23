import numpy as np

#CSV文件：有局限性，只能有效存取一维和二维数组
'''
np.save(frame, array, fmt='%.18e', delimiter=None)
frame：文件、字符串或产生器，可以是.gz或.bz2的压缩文件。
delimiter：分割字符串，默认是任何空格。
'''
#demo1：
a = np.arange(100).reshape(5,20)
np.savetxt('test.txt', a, fmt='%d', delimiter='，', encoding='utf-8')
'''
np.loadtxt(frame, dtype=np.float, delimiter=None, unpack=Flase)
dtype：数据类型，可选。
unpack：如果True，读入属性将分别写入不同变量。
'''
#demo2:
b = np.loadtxt('test.txt', dtype=np.int, delimiter='，',encoding='utf-8')
print(b)



#多维数组的存取
'''需要注意：该方法需要读取时知道存入文件时数组的维度和元素类型（可以通过元数据文件来存储额外信息）
a.tofile(frame, sep='', format='%s')
frame：文件、字符串。
sep：数据分割字符串，如果是空串，写入文件为二进制。
format：写入数据的格式。
'''
#demo3：
c = np.arange(100).reshape(5, 10, 2)
c.tofile('test.dat', sep=',', format='%d')
'''
np.fromfile(frame, dtype=float, count=1, sep='')
count：读入元素个数，-1表示读入整个文件。
'''
#demo4:
d = np.fromfile('test.dat', dtype=np.int, count=100, sep=',').reshape(5,10,2)
print(d)

'''NumPy的便捷文件存取
np.save(fname, array)或np.savez(fname, array)
frame：文件名，以.npy为扩展名，压缩扩展名为.npz
array：数组变量
'''
np.save('test.npy', c)
e = np.load('test.npy')
print(e)