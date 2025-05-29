from turtle import Turtle,Screen

screen = Screen()
screen.setup(width =600,height= 600)
screen.bgcolor("black")
screen.title("SNAKE RUNNER")
# To create a snake body
turtle = Turtle()
turtle.shape("square")
turtle.color("white")
turtle.resizemode("user")
turtle.shapesize(1,3,1)
screen.listen()
def move_forward():
    turtle.forward(10)
screen.onkeypress(key = "w",fun= move_forward)



screen.exitonclick()