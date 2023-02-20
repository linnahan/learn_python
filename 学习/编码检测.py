import chardet

#demo：
b = chardet.detect(b'hello word')
print(b)
print(b'hello word')

g = chardet.detect('离离原上草，一岁一枯荣'.encode('gbk'))
print(g)
print('离离原上草，一岁一枯荣abc'.encode('gbk'))
u = chardet.detect('离离原上草，一岁一枯荣'.encode('utf-8'))
print(u)
print('离离原上草，一岁一枯荣abc'.encode('utf-8'))
