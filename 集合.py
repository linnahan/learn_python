a = {1,2,3,4}
b = {4,5,6,7}
#集合的并集
print(a | b)
print(a.union(b))

#集合的交集
print(a & b)
print(a.intersection(b))

#包含a去除b
print(a.difference(b))

a.add('linnahan')       #增加
print(a)
a.remove(4)             #删除
print(a)