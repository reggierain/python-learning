from turtle import Turtle
import random

MOVEMENTS = [1, -1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 0
        self.move_y = 0
        self.ball_reset()


    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def bounce_paddle(self):
        self.move_x *= -1

    def ball_reset(self):
        self.move_x = random.choice(MOVEMENTS)
        self.move_y = random.choice(MOVEMENTS)
        self.goto(0, 0)
