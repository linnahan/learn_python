a="I'm a student!"
b=a.split()              #分割a后的序列是一个新的定义，不再是a
print(a)
print(b)
for i in b:
    print(i)
c='hi.I\'m a student.hello'
print(c.split('.'))