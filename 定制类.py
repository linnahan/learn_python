print('hukhu'.__class__)
print(type('hukhu'))
class hh(object):
    def __init__(self):     # 初始化两个计数器a，b
        self.a, self.b = 0, 1
    def __iter__(self):     # 实例本身就是迭代对象，故返回自己
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 30:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __str__(self):      #字符串
        return 'hhhh'

    def __getitem__(self, item):    #索引
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

    def __getattr__(self, attr):    #获取属性，只有在没有找到属性的情况下，才调用！！！
        if attr == 'score':
            return 99

    def __call__(self, *args, **kwargs):     #调用实例
        print('wc   nbaaaa!!!')


a = hh()
for i in a:
    print(i,end='')
print(a)
print(a[5])
print(a.score)
a()

'''怎么判断一个变量是对象还是函数呢？
我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例
通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。'''
print(callable(a))

