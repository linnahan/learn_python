#第一种，麻烦
a ='abcde'
b =''
for i in a:
    b =i+b
print(b)
#第二种，切割字符串
print(a[::-1])