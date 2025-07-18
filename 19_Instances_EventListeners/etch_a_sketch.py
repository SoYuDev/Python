import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def rotate_left():
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading + 10)

def rotate_right():
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading - 10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_left, "a")
screen.onkey(rotate_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()