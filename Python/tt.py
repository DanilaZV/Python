from turtle import *
import turtle
t = Turtle()
bgcolor('yellow')
t.hideturtle()
turtle.setup(1000, 600)
t.color('blue')
t.write("NIKITA GEY",  False, align="left", font=('Arial', 50, 'normal'))
t.write("NIKITA GEY",  False, align="center", font=('Arial', 60, 'normal'))
t.write("NIKITA GEY",  True, align="right", font=('Arial', 50, 'normal'))
turtle.exitonclick()
