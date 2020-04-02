#返回函数
def alzy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

print(alzy_sum(2,6,9,7,3)())
#返回数值
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs

f1,f2,f3 = count()
print(f2)
