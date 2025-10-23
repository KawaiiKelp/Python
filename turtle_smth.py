import turtle
turtle.bgcolor("black")
turtle.pensize(5)

def curve():
    for i in range(10):
        turtle.right(20)
        turtle.forward(20)

turtle.speed(0)
turtle.color("red", "pink")
turtle.begin_fill()
curve()
curve()
curve()
turtle.left(140)
turtle.forward(200)
curve()
turtle.left(20)
turtle.forward(200)
turtle.left(140)
curve()
curve()
curve()
turtle.right(6)
turtle.forward(200)