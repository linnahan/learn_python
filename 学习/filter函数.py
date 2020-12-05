def not_empty(s):
    return s and s.strip()
print(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))           #filter返回值为Iterator，是一个惰性序列!!
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))     #实现一个“筛选”函数

#exp:
def isodd(n):
    return n%2 == 1
print(list(filter(isodd,[18,23,56,49])))

#素数生成器:埃氏筛法
def zrsscq():                               #自然数生成器
    n = 1
    while True:
        n+=1
        yield n
def shaixuan(n):                            #筛选函数
    return lambda x: x%n >0
def sushu():                                #素数生成器
    it = zrsscq()       #初始序列！！！
    while True:
        n = next(it)
        it = filter(shaixuan(n), it)    #过滤自然数
        yield n

list1 = []
for i in sushu():
    if i<100:
        list1.append(i)
    else:
        break
print(list1)

#回数
def _not_divisible(n):
    return n == int(str(n)[::-1])
def is_palindrome(num):
    output = filter(_not_divisible, range(10, num))
    #print(type(output))
    return list(output)
print(is_palindrome(1000))