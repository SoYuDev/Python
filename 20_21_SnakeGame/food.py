from turtle import Turtle
import random

POSITION_RANGE = (-280, 280)

# Inherits the Turtle class.
class Food(Turtle):

    def __init__(self):
        # Superclass constructor call
        super().__init__()
        self.shape("circle")
        self.penup()
        # Set the size of the food to 10x10px
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # * Unpacks the tuple
        random_x = random.randint(*POSITION_RANGE)
        random_y = random.randint(*POSITION_RANGE)
        self.goto(random_x, random_y)




