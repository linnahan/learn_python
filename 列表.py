#列表
a = [1,2,3,4,5]
b = [5,6,7,8,9]
a.insert(3,'aa')    #index增加
print(a)
b.append('bb')      #在后面直接加上object
print(b)
a.pop(0)            #index删除
print(a)
#或del a[0]
b.remove(9)         #直接把object删除
print(b)
a[0]='a'            #index修改
print(a)

#注意区别
ls = ['cat','dog','tiger',1024]
ls[1:2] = [1,2,3,4]
#ls[1] = [1,2,3,4]
print(ls)

line_1=[1,5,2,9,4,7,8,6]
line_2=[]
for i in line_1:
    if i%2==0:
        line_2.append(i)
print(line_2)
line_3=[i for i in line_1 if i%3==0]
print(line_3)
print([i for i in range(1,101) if i%2==0 and i%3==0])    #要记得加[]号
line_1[4]='gdf'
print(line_1)