import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move,"Up")
screen.onkeypress(player.move_r,"Right")
screen.onkeypress(player.move_l,"Left")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    #Detect the collision with car
    for car in car_manager.all_cars:
        if player.distance(car)< 25:
            game_is_on = False
            scoreboard.game_over()

    #Detect reaches other side
    if player.ycor() > 300:
        player.reset_p()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
