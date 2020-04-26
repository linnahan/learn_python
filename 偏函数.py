#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
print(int('010101011111',base = 2))   #麻烦

import functools
int2 = functools.partial(int,base = 2)
'''不需要自己定义
def int2(x, base=2):
    return int(x, base)'''

print(int2('11110100000'))


#当传入：
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
#相当于：
args = (10, 5, 6, 7)
print(max(*args))
