#coding:gbk
print('请输入坐标（先输入x后按回车再输入y）')
x=int(input())
y=int(input())
if x>=0:
    if y>=0:
        print('(%d,%d)位于第一象限'%(x,y))
    else:
        print('(%d,%d)位于第四象限'%(x,y))
else:
    if y>=0:
        print('(%d,%d)位于第二象限'%(x,y))
    else:
        print('(%d,%d)位于第三象限'%(x,y))
