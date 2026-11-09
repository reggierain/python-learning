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
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

cars = CarManager()

scoreboard = Scoreboard()

increment_counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    increment_counter += 1

    if increment_counter == 6:
        increment_counter = 0
        cars.generate_car()

    for car in cars.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.player_is_at_finish_line():
        player.move_to_starting_position()
        cars.level_up()
        scoreboard.increase_level()

    cars.move_cars()

screen.exitonclick()