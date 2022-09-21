#import turtle

#turtle.circle(40,45) 
#turtle.color('green')
#turtle.circle(50,275)
#turtle.mainloop()
import turtle as t
 
#t.tracer(False)
 
# Значения для параболы.
a = 0.01
b = 0
c = 0
min_x = -100
max_x = 100
y = [a*x*x + b*x + c for x in range(min_x, max_x)]
 
# Построение разметки.
t.pencolor('lightgray')
for i in range(-700, 701, 50):
    t.dot(5)
    t.goto(i, 0)
t.goto(0, 0)
for i in range(-400, 401, 50):
    t.dot(5)
    t.goto(0, i)
 
# Построение параболы.
t.pencolor('black')
t.up()
t.goto(min_x, y[0])
t.down()
t.width(3)
for i in range(min_x, max_x):
    t.goto(i, y[i+max_x])
 
# Закрытие по клику.
t.exitonclick()