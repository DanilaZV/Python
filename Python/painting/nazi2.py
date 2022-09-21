from turtle import *
import turtle
import time
t = Turtle()
circ = turtle.Turtle()
t.hideturtle()
#t.speed(0)


turtle.setup(1000, 600)
circ.penup()
circ.setposition(0,-150)
circ.pendown()
bgcolor('red')
circ.pensize(10)
circ.color('white', 'white')

circ.begin_fill()
circ.circle(150, 360)
circ.end_fill()

t.color('black')
t.pensize(30)
t.penup()
t.setposition(0, 0)
t.pendown()
for i in range(1200):
    #turtle.delay(-200)
    #Рисование "крестика"
    turtle.tracer(12, 0)
    for i in range(4):
        #t.speed(0)
        #turtle.delay(-1)#Скорость поворота
        t.forward(90)
        t.right(90)
        t.forward(90)
        t.penup()
        t.setposition(0,0)
        t.pendown()
        t.right(180)

    time.sleep(0.1)       
    t.clear()#Очистка "крестика"
    t.right(1)#Поворот черепашки 
t.pensize(10)
t.penup()
t.color('red')
t.write("Пошли нахрен, хохлы",  True, align="center", font=('Arial', 100, 'normal'))

t.penup()
turtle.exitonclick()