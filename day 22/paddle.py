from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.goto(self.pos_x,self.pos_y)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.pos_x, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.pos_x, new_y)
