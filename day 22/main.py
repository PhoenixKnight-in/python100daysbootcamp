from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width= 800,height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.go_up,"Up")
screen.onkeypress(paddle_r.go_down,"Down")
screen.onkeypress(paddle_l.go_up,"w")
screen.onkeypress(paddle_l.go_down,"s")

game_is_on = True
n = 1

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh(n)
    # detecting collision with left and right walls
    if ball.xcor() > 390 :
        ball.reset_position()
        n *= -1
        scoreboard.l_point()
    if ball.xcor()< -390:
        ball.reset_position()
        n *= -1
        scoreboard.r_point()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detection with the right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() >320:
        ball.bounce_p()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_p()
screen.update()
screen.exitonclick()