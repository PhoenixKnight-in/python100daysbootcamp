import random
from turtle import Turtle, Screen, colormode
turtle = Turtle()
screen = Screen()
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]
colormode(255)

# posi = turtle.pos()
# turtle.setheading(225)
# turtle.forward(300)
# print(turtle.pos())
# turtle.setheading(0)
turtle.teleport(-212.13,-212.13)
origin_x = turtle.pos()[0]
origin_y = turtle.pos()[1]
x = origin_x
y = origin_y
for i in range(10):
    for j in range(11):
        turtle.dot(10,random.choice(color_list))
        turtle.teleport(x)
        x += 50
    y += 50
    x = origin_x
    turtle.teleport(origin_x,y)
screen.exitonclick()