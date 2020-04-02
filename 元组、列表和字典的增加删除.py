#列表
a = [1,2,3,4,5]
b = [5,6,7,8,9]
a.insert(3,'aa')    #index增加
print(a)
b.append('bb')      #在后面直接加上object
print(b)
a.pop(0)            #index删除
print(a)
b.remove(9)         #直接把object删除
print(b)
a[0]='a'            #index赋予，不常用
print(a)

#字典
dir_my = {'name':'linahan','age':'22','email':'1596695476@qq.com'}
dir_my['age']=21                        #可用于修改、增加
print(dir_my)
dir_my['school']='gdsyhgxy'
print(dir_my)
dir_my.pop('email')                     #删除的两种方法
print(dir_my)
del dir_my['name']
print(dir_my)

#元组：元素值不能修改，但可以对元组进行连接组合和复制！！！
tuple_1=(5,6,9,2,3,4)
tuple_2=(77,)*5
tuple_1=tuple_1+tuple_2
print(tuple_1)

