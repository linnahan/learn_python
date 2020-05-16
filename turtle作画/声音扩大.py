from turtle import *


screensize(600,400)
speed(11)
penup()
backward(100)
pendown()
for i in range(30):
    forward(10)
    circle(5*i)
hideturtle()
done()