from turtle import Turtle,Screen,colormode
import random
turtle = Turtle()
screen = Screen()
colormode(255)
def color_random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


angle = 0
while angle < 360:
    angle += 3
    color = color_random()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.speed(0)
    turtle.circle(100)
    turtle.left(angle)
'''
turtle.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        color = color_random()
        turtle.color(color)
        turtle.circle(100)
        turtle.setheading(turtle.heading()+10)

draw_spirograph(5)'''
screen.exitonclick()