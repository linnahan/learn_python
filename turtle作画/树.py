from turtle import *
import random



def drawTree(length):
    if length > 1:
        if length < 30 and length > 14:
            pensize(4)
        elif length < 15 and length > 5:
            color('#04B486')
            pensize(3)
        elif length < 5 and length > 1:
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')
            pensize(5)
        #随机角度和长度
        randangle = 2*random.random()
        randlen = 2*random.random()
        #每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20*randangle)
        drawTree(length - 10 * randlen)
        #这里是向右的角度转动
        left(40*randangle)
        drawTree(length - 10*randlen)
        #为什么需要再向右转20度？那是因为 我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)

        up()
        backward(length)
        down()


tracer(False)
setworldcoordinates(-1000,-750,1000,750)
speed(12)
color('#5E5E5E')
pensize(5)

up()
goto(0,-700)    #跳到绘制起始点
down()

left(80)
fd(140)

drawTree(120)

done()