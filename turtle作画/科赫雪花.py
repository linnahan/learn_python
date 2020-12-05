from turtle import *


def oneline(n,size):
    if n == 0:
        fd(size)
    else:
        for i in [0,60,-120,60]:
            left(i)
            oneline(n-1,size/3)

def fill(n,size):
    for i in range(3):
        oneline(n,size)
        right(120)

def main():
    setup(600,600)
    screensize(0,0,'black')
    penup()
    speed(12)
    goto(-200,100)
    pendown()
    pencolor('white')
    begin_fill()
    fillcolor('white')
    fill(5,400)
    end_fill()
    hideturtle()
    done()

if __name__ == '__main__':
    main()