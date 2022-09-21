from turtle import *
import turtle
t = Turtle()
turtle.tracer(0, 0)

bgcolor('white')
#colors = ['red', 'blue', 'green', 'yellow', 'white', 'purple']
colors = ['red', 'blue']
for i in range(360):
    t.color(colors[i % 2])
    #t.color('blue')
    t.forward(90)
    #t.right(30)
    #t.forward(20)
    #t.left(60)
    #t.forward(50)
    #t.right(30)

    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.right(1)
t.left(1)
t.penup()
t.setposition(0, -90)
t.color('black')
t.pendown()
t.circle(90, 360)
turtle.exitonclick()