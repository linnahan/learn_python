#coding:gbk
print('���������꣨������x�󰴻س�������y��')
x=int(input())
y=int(input())
if x>=0:
    if y>=0:
        print('(%d,%d)λ�ڵ�һ����'%(x,y))
    else:
        print('(%d,%d)λ�ڵ�������'%(x,y))
else:
    if y>=0:
        print('(%d,%d)λ�ڵڶ�����'%(x,y))
    else:
        print('(%d,%d)λ�ڵ�������'%(x,y))
