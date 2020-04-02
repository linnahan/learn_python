line_1=[1,9,8,5,4,3]
def double_func(x):
    return x*2
line_2=map(double_func,line_1)
print(list(line_2))

lst_1=[1,2,3,4,5]           #列表解析
lst_2=[i*2 for i in lst_1]
print(lst_2)

lst_3=map(lambda x:x*2,lst_1)
print(list(lst_3))
lst_1_1=(1,2,3,4,6)
lst_3_1=map(lambda x:x*2,lst_1_1)
print(tuple(lst_3_1))

lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]

lst_3=[]                                    #自己想的：两列表相加
num=len(lst_1)
for i in range(num):
    a=lst_1[i]+lst_2[i]
    lst_3.append(a)
print(lst_3)

lst_map=map(lambda x,y:x+y,lst_1,lst_2)     #map函数做法
print(list(lst_map))