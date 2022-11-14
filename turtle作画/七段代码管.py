from turtle import *
from time import gmtime,strftime


def start():
    penup()
    goto(-150, 0)

def dr():
    penup()
    fd(5)

def drawst(tool):
    dr()
    pendown() if tool else penup()
    fd(40)
    dr()
    right(90)

def drawdigit(digit):
    for i in str(digit):
        if i.isdigit():
            drawst(True) if eval(i) in [2,3,4,5,6,8,9] else drawst(False)
            drawst(True) if eval(i) in [0,1,3,4,5,6,7,8,9] else drawst(False)
            drawst(True) if eval(i) in [0,2,3,5,6,8,9] else drawst(False)
            drawst(True) if eval(i) in [0,2,6,8] else drawst(False)
            left(90)
            drawst(True) if eval(i) in [0,4,5,6,8,9] else drawst(False)
            drawst(True) if eval(i) in [0,2,3,5,6,7,8,9] else drawst(False)
            drawst(True) if eval(i) in [0,1,2,3,4,7,8,9] else drawst(False)
            right(180)
            penup()
            fd(20)
        else:
            penup()
            right(90)
            fd(20)
            write(i,font=('微软雅黑',30,'normal'))
            left(180)
            fd(20)
            right(90)
            fd(40)



def timege():
    nowtime = strftime('%H:%M',gmtime())
    print(nowtime)
    return nowtime

def main():
    speed(11)
    setup(400, 300)
    screensize(0,0,'black')
    pencolor('red')
    start()
    drawdigit(digit=timege())
    hideturtle()
    done()

if __name__ == '__main__':
    main()