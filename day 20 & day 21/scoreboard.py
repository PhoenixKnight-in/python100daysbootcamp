from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_text()
    def write_text(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg = f"Score = {self.score}",move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def scoring(self):
        self.clear()
        self.score += 1
        self.write_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False, align=ALIGNMENT, font=FONT)