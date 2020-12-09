a = "I'm a student!"
b = a.split()              #分割a后的序列是一个新的定义，不再是a
print(b)
c = 'hi.I\'m a student.hello'
print(c.split('.'))

#或者用正则
import re
d = re.split(r' ',a)
print(d)