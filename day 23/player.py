from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.color("Black")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
    def move_r(self):
        new_r = self.xcor()+5
        self.goto(new_r,self.ycor())

    def move_l(self):
        new_r = self.xcor()-5
        self.goto(new_r,self.ycor())
    def reset_p(self):
        self.goto(STARTING_POSITION)