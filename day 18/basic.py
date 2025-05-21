from turtle import Turtle ,Screen

tim = Turtle()

tim.shape("turtle")
tim.color("ForestGreen")

def move_turn_right():
    tim.forward(100)
    tim.right(90)
move_turn_right()
move_turn_right()
move_turn_right()
move_turn_right()


screen = Screen()
screen.exitonclick()