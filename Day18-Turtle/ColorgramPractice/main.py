from colors import colors
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()

x_start = -500
y_start = -500

tim.teleport(x_start, y_start)

for x in range(10):
    for y in range(10):
        tim.dot(50, random.choice(colors))
        tim.forward(100)
    y_start += 100
    tim.teleport(x_start, y_start)

screen.exitonclick()