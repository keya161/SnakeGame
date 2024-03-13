from turtle import Turtle
from random import randint
# TODO:4 Detect collision with food(new should appear)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(randint(-250, 250), randint(-250, 250))