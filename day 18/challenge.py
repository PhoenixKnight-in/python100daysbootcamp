from turtle import Turtle, Screen
tim = Turtle()

def dash_line():
    print(tim.pos())
    tim.forward(5)
    tim.color("white")
    tim.forward(5)
    tim.color("black")
def dash_line2():
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()
for i in range(20):
    dash_line()

screen = Screen()
screen.exitonclick()