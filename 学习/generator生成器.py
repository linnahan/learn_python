#生成器
#第一种
g = (x*x for x in range(1,11))
for i in g:
    print(i)

#第二种
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b                #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a,b=b,a+b
        n=n+1
    return 'done'
for i in fib(6):
    print(i)                   #拿不到返回值‘done’

g = fib(6)
while True:
    try:
        print('g:',next(g))
    except StopIteration as e:
        print('Generation return value:',e.value)
        break