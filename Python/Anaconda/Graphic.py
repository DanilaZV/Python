from asyncore import write
import turtle # 

#t = turtle.Turtle()
turtle.setup(500, 400)
turtle.reset() 
turtle.tracer(1)
turtle.speed(0)

#КВАДРАТ
turtle.up()
turtle.goto(200, -120)
turtle.width(2)
turtle.down()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(400)
turtle.up()
# Надпись

turtle.goto(-190, 135)
turtle.color('Black')
turtle.write('Система координат', font=('Times New Roman', 15, 'bold'))
#

turtle.goto(0, 0)
turtle.color('blue')
turtle.width(1)
turtle.write('0,0') #Задание начала координат
#* Установка левого нижнего угла

x=-170
y=-120
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
#*
#% Установка верхнего правого угла
x=130 
y=100 
coords=str(x)+","+str(y) 
turtle.goto(x,y) 
turtle.write(coords)
#%
#$Верхняя линия
x=0 
y=100
turtle.goto(x,y)
coords=str(x)+","+str(y)
turtle.write(coords)
turtle.down()
turtle.right(90)
turtle.forward(100)
turtle.up()
#$
#@Нижняя линия
x=0 
y=-100 
coords=str(x)+","+str(y)
turtle.down()
turtle.goto(x,y)
turtle.write(coords) # 
turtle.up()
turtle.goto(0, 0)
#@
#!Правая линия
x=150 
y=0 
coords=str(x)+","+str(y) 
turtle.down()
turtle.goto(x,y) 
turtle.write(coords) # 
turtle.up()
#!
#&Левая линия
x=-150
y=0 
coords=str(x)+","+str(y) 
turtle.down()
turtle.goto(x,y) 
turtle.write(coords)
turtle.up()
#&
#
turtle.goto(0,0)
turtle.color('black')
turtle.down()
turtle.right(90)
turtle.circle(110, 90)
#
#t.screen.exitonclick()
turtle.mainloop()