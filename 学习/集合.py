a = {1,2,3,4}
b = {4,5,6,7}
#集合的并集
print(a | b)
#print(a.union(b))

#集合的交集
print(a & b)
#print(a.intersection(b))

#集合的补集
print(a ^ b)

#集合的差集
print(a - b)
#print(a.difference(b))

a.add('linnahan')       #增加元素
print(a)
a.remove(4)             #删除元素
print(a)
print(a.pop())          #随机取出一个元素，返回元素，没有元素了会报错
print(a)
a.discard(2)            #取出固定元素，没有不会报错
print(a)


#集合应用场景：去除重复项
ss = [7,9,5,1,8,4,6,7,5,2,7,6,2,4]
ss = list(set(ss))
print(ss)