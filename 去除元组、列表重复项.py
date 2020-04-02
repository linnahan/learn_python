a = (1,1,2,5,4,6,4)
b = [9,5,6,2,6,4,2]
print(a)
print(b)
print(tuple(set(a)))
print(list(set(b)))
#思路：把元组、列表转换为集合set（因集合没有重复元素），再转换回来
