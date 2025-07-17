import turtle as t
from turtle import Turtle, Screen
import random

# Set the color mode to RGB
t.colormode(255)


# 1.
def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


# 2.
def draw_dashed_line(turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)
        turtle.down()


# 3.
def draw_triangle(turtle):
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)


def draw_shape(num_sides, turtle):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.left(angle)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours_tuple = (r, g, b)
    return colours_tuple

def random_walk(turtle, steps):
    angles = [0, 90, 180, 270]
    turtle.pensize(10)
    turtle.speed("fast")
    for _ in range(steps):
        # Choose a random color from the color list
        #turtle.color(random.choice(colours))

        turtle.color(random_color())
        turtle.forward(50)
        # setheading is the same as .left(random.choice(angles)
        turtle.setheading(random.choice(angles))

def draw_spirograph(turtle, size_of_gap):
    turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size_of_gap)



colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red", "green")

# draw_square(my_turtle)

# draw_dashed_line(my_turtle)

# for shape in range(3, 11):
#     my_turtle.color(random.choice(colours))
#     draw_shape(shape, my_turtle)

# random_walk(my_turtle, 100)

draw_spirograph(my_turtle, 5)

screen = Screen()
# The window won't disappear until you click.
screen.exitonclick()
