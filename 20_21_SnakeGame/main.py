from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turns off the animation
screen.tracer(0)

# Instance of the snake
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")

game_is_on = True
while game_is_on:
    # Once we move all the segments of the snake, we update their positions
    screen.update()
    # Execution delay, this controls the speed of the snake
    time.sleep(.1)
    my_snake.move()

    # Detect collision with food (units in px)
    if my_snake.head.distance(food) < 15:
        print("Yum yum yum")
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.

    # Without Slicing

    # for segment in my_snake.segments:
    #     # If my snake's head is touching any of the snake segments...
    #     if segment == my_snake.head:
    #         pass
    #     elif my_snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    # With Slicing, ignoring the first position of the list
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
