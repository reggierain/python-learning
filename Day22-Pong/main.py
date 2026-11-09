from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(350)
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

left_paddle = Paddle(-350)
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.005)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_paddle()

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

screen.exitonclick()