#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(10))

#尾随递归
def dig(n):
    return dig_iter(n,1)
def dig_iter(n,project):
    if n==1:
        return project
    return dig_iter(n-1,n*project)

print(dig(10))

#一般的用循环实现，跟尾随递归相似
sum = 1
for i in range(1,11):
    sum = sum*i
print(sum)