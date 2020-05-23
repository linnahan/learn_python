import numpy as np

'''ndarray数组的创建方法

（1）从Python中的列表、元组等类型创建ndarray数组
x = np.array(list/tuple, dtype = )
（2）使用Numpy中函数创建ndarray数组，如：arange、ones、zeros、full、eye等
还有ones_like、zeros_like、full_like等
y = np.ones((2, 5, 5))
（3）使用Numpy中其他函数创建ndarray数组，如：linspace、concatenate
a = np.linspace(1, 10, 4)
b = np.concatenate((a, b))
'''

'''ndarray数组的维度变换

.reshape(shape) 不改变数组元素，返回一个shape形状的数组，原数组不变
.resize(shape) 与.reshape()功能一致，但修改原数组
.swapaxes(ax1,ax2) 将数组n个维度中两个维度进行调换
.flatten() 对数组进行降维，返回折叠后的一维数组，原数组不变
a = np.arange(24).reshape((2,3,4)) 

ndarray数组的类型变换
new_a = a.astype(new_type)

ndarray数组向列表的转换
a.tolist()
'''

'''ndarray数组的操作：数组的索引和切片
索引：获取数组中特定位置元素的过程
切片：获取数组元素子集的过程
一维数组与列表操作相似：
索引：a[0] 切片：a[1 :10 :2]
多维数组的索引：(每个维度一个索引值，逗号分割)
a[-1, -2, -3]
多维数组的切片：
a[:, 1, -3] ---选取一个维度用
a[:, 1:3, :] ---每一个维度切片方法与一维数组相同
a[:, :, ::2] ---每个维度可以使用步长跳跃切片
'''

'''ndarray数组的运算
数组与标量之间的运算
数组与标量之间的运算作用于数组的每一个元素
a = a / a.mean() ---计算a与元素平均值的商

NumPy一元函数
对ndarray中的数据执行元素级运算的函数
np.abs(x) np.fabs(x) ---计算数组各元素的绝对值
np.sqrt(x) ---计算数组各元素的平方根
np.square(x) ---计算数组各元素的平方
np.log(x) np.log10(x) np.log2(x) ---计算数组各元素的自然对数、10底对数和2底对数
np.ceil(x) np.floor(x) ---计算数组各元素的ceiling值或floor值
np.rint(x) ---计算数组各元素的四舍五入值
np.modf(x) ---将数组各元素的小数和整数部分以两个独立数组形式返回
np.cos(x) np.cosh(x) & np.sin(x) np.sinh(x) & np.tan(x) np.tanh(x) ---计算数组各元素的普通型和双曲型三角函数
np.exp(x) ---计算数组各元素的指数值
np.sign(x) ---计算数组各元素的符号值，1(+)，0，-1(-)

NumPy二元函数
+-*/**    两个数组各元素进行对应运算
np.maximum(x,y) np.fmax() & np.minimum(x,y) np.fmin()    元素级的最大值/最小值计算
np.mod(x,y)      元素级的模运算
np.copysign(x,y)     将数组y中各元素值的符号赋值给数组x对应元素
> < >= <= == !=      算术比较，产生布尔型数组
'''