def fun(arg1,arg2):
    print(arg1,arg2)
fun(3,7)
fun(arg2=3,arg1=7)      #一般的

def fun_1(a=3,b=5,c=7):
    print(a,b,c)
fun_1()
fun_1(9,6)              #提供的参数会按顺序先匹配前面位置的参数，后面未匹配到的参数使用默认值
fun_1(8,c=0)
fun_1(b=0)

def calcsum(*ages):    #可以接受任意数量的参数      较灵活
    sum=0              #*ages为元件tuple，有序！！！
    for i in ages:
        sum+=i
    print(sum)
calcsum(599,144,333)
calcsum()

def printALL(**kages):          #把参数以键值对字典的形式传入     最灵活
    for k in kages:             #字典是无序的
        print(k,':',kages[k])
        #print(type(k))
    #print(type(kages))
printALL(a=6,b=8,c=4,d=9)

def func(x, y=5, *a, **b):              #几种参数调用方式，可以混合在一起使用
    print(x, y, a, b)
func(1, 2, 3)
func(1, 2, 3, 4)
func(x=1, y=1, a=1)
func(x=1, y=1, a=1, b=1)                 #将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
func(1, y=1)                             #将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。
func(1, 2, 3, 4, a=1)
func(1, 2, 3, 4, k=1, t=2, o=3)
'''在混合使用时，首先要注意函数的写法，必须遵守：
带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
元组参数(*args)须在带有默认值的形参(arg=)之后；
字典参数(**kargs)须在元组参数(*args)之后。'''