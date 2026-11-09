from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)

for x in range(36):
    timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    timmy.circle(100)
    timmy.right(10)

screen.exitonclick()