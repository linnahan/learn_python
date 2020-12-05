from turtle import *
from random import randint,random
from math import sin,cos


setup(800,600)
screensize(400,300,'gray')

#五角星
def fivestar(r):
    for j in range(5):
        fd(r)
        right(144)

#星星天空
def star_sky():
    pencolor('yellow')
    speed(12)
    for i in range(30):
        penup()
        goto(randint(-400,400),randint(100,300))
        pendown()
        begin_fill()
        fillcolor('yellow')
        fivestar(8)
        end_fill()

#花
def flower(r):
    speed(12)
    for i in range(5):
        seth(72*i)
        begin_fill()
        fillcolor(random(),random(),random())
        circle(r,360)
        end_fill()
    fd(1.6*r)
    begin_fill()
    fillcolor('white')
    left(90)
    circle(1.6*r,360)
    end_fill()

#奥运五环
def aywh():
    pensize(5)
    pencolor('blue')
    left(90)
    circle(-20,360)
    penup()
    seth(0)
    fd(50)
    pendown()
    pencolor('black')
    left(90)
    circle(-20, 360)
    penup()
    seth(0)
    fd(50)
    pendown()
    pencolor('red')
    left(90)
    circle(-20, 360)
    seth(180)
    penup()
    fd(5)
    pendown()
    pencolor('green')
    circle(20,360)
    penup()
    fd(50)
    pendown()
    pencolor('yellow')
    circle(20,360)


aywh()
fivestar(50)
flower(50)
hideturtle()
done()