#列表
a = [56,496,21,48,16]
b = [12,8,923,78,5,1]
#第一种
c = a + b
print(c)
#第二种----a会被改变
a.extend(b)
print(a)
#第三种
a = [56,496,21,48,16]
print([*a,*b])


#字典
dic1 = {'name':'linnahan','phone':15219726974}
dic2 = {'school':'gdsyhgxy','qqnumber':1596695476}

print({**dic1,**dic2})