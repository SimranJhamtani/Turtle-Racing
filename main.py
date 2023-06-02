import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
screen = Screen()
car = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.up ,'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for cars in car.all_cars:
        if player.distance(cars) < 18 :
            game_is_on = False
            scoreboard.gameover()

    if player.ycor() >= 280 :
        player.level_up()
        scoreboard.increase_level()
        car.increasespeed()


screen.exitonclick()