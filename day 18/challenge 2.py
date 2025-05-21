from turtle import Turtle, Screen
import random
turtle = Turtle()
side = 3
a = 0
color = ["CornflowerBlue","powder blue","aquamarine","dark khaki","gold","sienna",
         "violet","indigo"]
def draw_shape(side):
    global a
    turtle.pencolor(color[a])
    turtle.fillcolor(color[a])
    for i in range(side):
        turtle.forward(100)
        turtle.right(360/side)
    a += 1

while side <= 10:
    draw_shape(side)
    side += 1




screen = Screen()
screen.exitonclick()
