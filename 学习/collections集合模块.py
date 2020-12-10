#namedtuple类
#demo：定义坐标
from collections import namedtuple
from itertools import count
Point = namedtuple('Point', ['x','y'])
p = Point(5,9)
print(p.x)
print(p.y)

#deque类
'''使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：'''
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict类
'''使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['key1'])

#OrderedDict类
'''使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：'''
from collections import OrderedDict
od = OrderedDict([('a',1),('b',2),('c',3)])

#ChainMap类
'''ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，
但是查找的时候，会按照顺序在内部的dict依次查找。'''
from collections import ChainMap
#combined = ChainMap(command_line_args, os.environ, defaults) #命令行>环境变量>默认

#Counter类
'''Counter是一个简单的计数器，例如，统计字符出现的个数：'''
from collections import Counter
test = Counter()
for t in 'ahtsbtshbdaergrnytjs':
    test[t] = test[t]+1
print(test)




