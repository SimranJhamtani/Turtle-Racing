COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 30
STARTING_POSITION = (0, -280)
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE


    def create_car(self):
        r_choice = random.randint(1,6)
        if r_choice == 1:
            new_car=Turtle()
            choice = random.choice(COLORS)
            new_car.penup()
            new_car.shape("square")
            new_car.color(choice)
            new_car.shapesize(0.5, 2)
            rand_y = random.randint(-250, 250)
            new_car.goto(300,rand_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def increasespeed(self):
        self.carspeed += MOVE_INCREMENT