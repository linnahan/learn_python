#查看函数

def fn():
    pass

print(type(fn))
print(type(print))
print(type(''.format))
print(type(123))
print(type('aaa'))

#判断一个对象是否是函数可以使用types模块中定义的常量：

import types

print('\n',type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#要更好的判断class的类型，可以使用isinstance()函数。

print('\n',isinstance('ggg',str))
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print('\n',dir('hh'))
'''类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：'''
print(len('aaaaa'))
print('aaaaa'.__len__())
#我们自己写的类，如果也想用len()的话，就自己写一个__len__()方法：
'''class mydog():
    def __len__(self):
        print(10)
dog = mydog()
len(dog)'''

#测试对象的属性、方法
class wahh(object):
    def __init__(self):
        self.x = 666
aa = wahh()
print(hasattr(aa,'x'))      #aa对象有x属性吗？
setattr(aa,'y',99)          #设置aa对象y属性为99
print(getattr(aa,'y',404))      #获取aa对象的y属性,不存在返回404