#字典的查看方法有：
dir_my = {'name':'linahan','age':'22','email':'1596695476@qq.com'}
print(dir_my.get('school'))         #没有key不会报错，输出None
print(dir_my['name'])               #没有key会报错
#判断是否存在key
print('school'in dir_my)


for k in dir_my:            #Iterable的默认object是keys
    print(k)
#迭代values
for v in dir_my.values():
    print(v)
#迭代keys and values
for d in dir_my.items():
    print(d)