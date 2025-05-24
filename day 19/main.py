from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height = 400)
user_bet = screen.textinput(title = "Make your bet",prompt = "Which turtle will win the race? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
x_c = -230
y_c = -50
all_turtle = []
for turtle_index in range(0,6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= x_c,y = y_c)
    y_c += 25
    all_turtle.append(new_turtle)
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the bet The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost the bet The {winning_color} turtle is the winner!")

        rand_dist= random.randint(0,10)
        turtle.forward(rand_dist)



screen.exitonclick()