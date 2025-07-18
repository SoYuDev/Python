from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forwards():
    my_turtle.forward(10)

# Needed to start listening to events
screen.listen()
# When we press space, we will call the function move_forwards()
screen.onkey(key="space", fun = move_forwards)
screen.exitonclick()