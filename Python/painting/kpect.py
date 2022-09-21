from turtle import *
import turtle
import time
t = Turtle()

#t.hideturtle()

t.color('blue')
t.pensize(5)
for i in range(3600):
    #turtle.delay(-200)
    #Рисование "крестика"
    for i in range(4):
        #t.speed(0)
        
        turtle.delay(0)#Скорость поворота
        t.forward(90)
        t.penup()
        t.setposition(0,0)
        t.pendown()
        t.right(90)
        
    
    for i in range(2):
        t.color('red')
        t.pu()
        t.fd(90)
        t.pd()
        t.right(90)
        t.forward(90)
        t.penup()
        t.setposition(0,0)
        t.pendown()
        t.right(90)
        
    
    t.left(90)
    for i in range(2):
        t.color('green')
        t.pu()
        t.fd(90)
        t.pd()
        t.right(90)
        t.forward(90)
        t.penup()
        t.setposition(0,0)
        t.pendown()
        t.right(90)
    t.color('blue')   
    #time.sleep(1)
    t.clear()
    t.right(1)
turtle.exitonclick()

