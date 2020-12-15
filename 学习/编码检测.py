import chardet

#demo：
b = chardet.detect(b'hello word')
print(b)

g = chardet.detect('离离原上草，一岁一枯荣'.encode('gbk'))
print(g)

u = chardet.detect('离离原上草，一岁一枯荣'.encode('utf-8'))
print(u)