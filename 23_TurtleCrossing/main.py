import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            print("Squish!")
            scoreboard.game_over()
            game_is_on = False

    # Detect if player has reached the other side.
    if player.ycor() > player.finish_line_value:
        player.refresh()
        print("You've reached the other side!")
        print("Lvl up!")
        scoreboard.increase_lvl()

screen.exitonclick()
