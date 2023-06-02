FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.write(f"Level = {self.level}",align = "left", font = FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over!!!",align = "center", font = FONT)