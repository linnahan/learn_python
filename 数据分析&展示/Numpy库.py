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

ndarray数组的类型变换
new_a = a.astype(new_type)

ndarray数组向列表的转换
a.tolist()
'''

'''ndarray数组的操作：数组的索引和切片
索引：获取数组中特定位置元素的过程
切片：获取数组元素子集的过程

一维数组与列表操作相似：
a[0] a[1 :10 :2]
多维数组的索引：(每个)
a = np.arange(24).reshape((2,3,4))
a[-1, -2, -3]
'''