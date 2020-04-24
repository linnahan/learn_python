import re

a = open('this.txt','rt',encoding='utf-8').read()
print(a)
string = '<p>(.*?)</p>'
corvent = re.compile(string).findall(a)
print(type(corvent))
try:
    bb = '\n'.join(corvent)
    print(bb)
except:
    print('hh')