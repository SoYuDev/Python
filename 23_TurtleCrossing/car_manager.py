from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_SPAWN_POS = (-250, 250)


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT

    def generate_car(self):
        # Random number to control the spawn frequency
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.up()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.setpos(300, random.randint(*Y_SPAWN_POS))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT
