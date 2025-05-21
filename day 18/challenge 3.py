from turtle import Turtle, Screen, colormode
import random
turtle = Turtle()
turtle.shape("circle")
turtle.pensize(10)
direction = [0,90,180,270]
turtle.speed(7)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

colormode(255)
screen = Screen()
while True:
    #a = random.randint(0, 7)
    color = random_color()
    print(color)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    c = random.choice(direction)
    turtle.forward(50)
    turtle.right(c)


screen.screensize(400,300)
screen.exitonclick()

