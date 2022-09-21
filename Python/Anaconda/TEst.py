import tkinter as tka
import math
from tkinter import *

#заголовок
tk=tka.Tk()
tk.title(" Sample ")
#кнопка
button=tka.Button(tk)
button["text"]="Закрыть"
button["command"]=tk.quit
button.pack()
#Окно(Высота, ширина, фон, хз)
canvas=tka.Canvas(tk)
canvas["height"]=360
canvas["width"]=480
canvas["background"]="#eeeeff"
canvas["borderwidth"]=2
canvas.pack()
#Цифры по углам
canvas.create_text(20, 10, text="20, 10")
canvas.create_text(460, 350, text="460, 350")
#Расчёт точек синусоиды
points=[]
ay=150
y0=150
x0=50
x1=470
dx=10
#
for n in range(x0, x1, dx):
	y=y0-ay*math.cos(n*dx)
	pp=(n, y)
	points.append(pp)
#Линия синусоиды(рисование линии синего цвета по получившимся в массиве точкам)
canvas.create_line(points, fill="blue", smooth=1)
#Линия по оси игрек
y_axe=[]
yy=(x0, 0)
y_axe.append(yy)
yy=(x0, y0+ay)
y_axe.append (yy)
canvas.create_line(y_axe, fill="red", width=2, arrow='last')
#canvas.create_text(37, 150, text = '0.0', fill = 'purple', font = ('Helvectica', '7'))
for i in range(-60, 300, 30):
	canvas.create_line(48, i, 52, i, width = 0.5, fill = 'black')
	
#amount = [30, 60, 90, 120]
#for i in range(120, 2, -30):
#	for k in range(i):
#		canvas.create_text(37, i, text = str(k), fill="purple", font=("Helvectica", "7"))
#for i in range(180, 302, 30):
	canvas.create_text(37, i, text = str(i), fill="purple", font=("Helvectica", "7"))
#Линия по оси икс
x_axe=[]
xx=(x0, y0)
x_axe.append(xx)
xx=(x1, y0)
x_axe.append(xx)
canvas.create_line(x_axe, fill="green", width=2, arrow='last')
for i in range(80, 470, 30):
	canvas.create_line(i, 148, i, 152, width = 0.5, fill = 'black')
	canvas.create_text(i, 142, text = str(i), fill="purple", font=("Helvectica", "7"))
#Окошечко
tk.mainloop()