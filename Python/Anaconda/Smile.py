import turtle

turtle.speed(0)
turtle.up()
turtle.goto(0, -100)  # center circle around origin
turtle.down()

turtle.begin_fill()
turtle.fillcolor("orange")  # draw head

turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.width(5)
turtle.backward(50)
turtle.forward(100)
turtle.right(50)
turtle.pendown()

turtle.up()
turtle.goto(-67, -40)
turtle.setheading(-60)
turtle.width(5)
turtle.down()
turtle.color('red')
turtle.circle(80, 120)  # draw smile
turtle.color('black')

turtle.fillcolor("blue")

for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)  # draw eyes
    turtle.end_fill()

turtle.hideturtle()
turtle.done()