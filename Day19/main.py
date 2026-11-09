from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

start_x = -230
start_y = -125

if user_bet:
    is_race_on = True

for x in colors:
    tim = Turtle(shape="turtle")
    tim.color(x)
    tim.penup()
    tim.goto(start_x, start_y)
    start_y += 50
    turtles.append(tim)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle wins!")
            else:
                print(f"You've lost! {winning_color} turtle wins!")
            break

        move_distance = random.randint(0, 10)
        turtle.forward(move_distance)

screen.exitonclick()