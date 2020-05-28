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


'''NumPy的随机数函数子库
np.random的随机数函数（1）
rand(d0,d1,...,dn) 根据d0-dn创建随机数组，浮点数，[0,1)，均匀分布
randn(d0,d1,...,dn) 根据d0-dn创建随机数组，标准正态分布
randint(low[,high,shape]) 根据shape创建随机数组或整数数组，范围是[low,high)
seed(s) 随机数种子，s是给定的种子值
'''
#demo:
a1 = np.random.rand(3,4,5)
a2 = np.random.randn(3,4,5)
a3 = np.random.randint(100,200,(3,4))
'''
np.random的随机数函数（2）
shuffle(a) 根据数组a的第1轴进行随排列，改变数组x
permutation(a) 根据数组a的第1轴产生一个新的乱序数组，不改变数组x
choice(a[,size,replace,p]) 从一维数组a中以概率p抽取元素，形成size形状新数组replace表示是否可以重用元素，默认值为False
'''
np.random.shuffle(a3)
b1 = np.random.permutation(a3)
b2 = np.random.choice(np.random.randint(100,200,(8,)), (3,2), replace=False)
'''
np.random的随机数函数（3）
uniform(low,high,size) 产生均匀分布的数组，low起始值，high结束值，size形状
normal(loc,scale,size) 产生具有正态分布的数组，loc均值，scale标准差，size形状
poisson(lam,size) 产生具有泊松分布的数组，lam随机事件发生率，size形状
'''
u = np.random.uniform(0,10,(3,4))
n = np.random.normal(10,5,(3,4))

'''NumPy的统计函数
np.random的统计函数（1）
sum(a,axis=None) 根据给定轴axis计算数组a相关元素之和，axis整数或元组
mean(a,axis=None) 根据给定轴axis计算数组a相关元素的期望，axis整数或元组
average(a,axis=None,weights=None) 根据给定轴axis计算数组a相关元素的加权平均值，weights权重
std(a,axis=None) 根据给定轴axis计算数组a相关元素的标准差
var(a,axis=None) 根据给定轴axis计算数组a相关元素的方差
'''                                         #axis表示按照哪个维度的计算
aa = np.arange(15).reshape(3,5)
np.sum(a)
np.mean(a,axis=1)
np.mean(a,axis=0)
np.average(a,axis=0,weights=[10,5,1])        #2*10+7*5+12*1/(10+5+1)=4.1875
np.std(a)
np.var(a)
'''
np.random的统计函数（2）
min(a) max(a) 计算数组a中元素的最小值、最大值
argmin(a) argmax(a) 计算数组a中元素最小值、最大值的降一维后下标（位置）
unravel_index(index,shape) 根据shape将一维下标index转换成多维下标
ptp(a) 计算数组a中最大值和最小值之差
median(a) 计算数组a中元素的中位数（中值）
'''
np.unravel_index(np.argmax(b),b.shape)
'''
np.random的梯度函数
np.gradient(f) 计算数组f中元素的梯度，当f为多维时，返回每个维度梯度
梯度：连续值之间的变化率，即斜度。
demo：XY坐标轴连续三个X坐标对应的Y轴值：a，b，c，其中，b的梯度是：(c-a)/2
'''