#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools
from itertools import chain
from lib2to3.pgen2.tokenize import group

natuals = itertools.count(1)
'''for n in natuals:
    print(n)'''
    
#cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('abc')
'''for c in cs:
    print(c)'''

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('a',2)
for r in ns:
    print(r)

'''无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：'''
natw = itertools.takewhile(lambda x : x <= 5,natuals)
print(list(natw))


#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ab','yz'):
    print(c)
    
#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
