from turtle import *
import turtle
t = Turtle()
t.speed(10)

bgcolor('white')
t.color('black')
t.pensize(10)


for i in range(4):
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.right(180)
t.penup()

turtle.exitonclick()