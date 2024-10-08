import turtle

turtle.title("Shapes on a Canvas")

screen= turtle.Screen()
screen.bgcolor("Light green")

t = turtle.Turtle()
t.shape('turtle')
t.color('white')
t.pensize(5)
t.speed(1)
t.fillcolor('white')



t.pendown()
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.left(60)
    
t.penup()
t.end_fill()
t.forward(-300)

t.begin_fill()
t.pendown()

t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.forward(120)

t.penup()
t.end_fill()
t.left(30)
t.forward(100)

t.begin_fill()
t.pendown()

t.forward(130)
t.left(90)
t.forward(250)
t.left(90)
t.forward(130)
t.left(90)
t.forward(250)

t.penup()
t.end_fill()

turtle.done()

