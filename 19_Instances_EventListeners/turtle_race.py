import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# If user_bet exists...
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Checks if the evaluated turtle has reached the end.
        if turtle.xcor() > 230:
            is_race_on = False
            # pencolor returns the color of the turtle
            winning_color = turtle.pencolor
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # If the evaluated turtle has not reached the end...
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
