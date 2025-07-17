import colorgram
import turtle as t
import random

# Getting colors using the colorgram library, once we have it, we do not need to compute all this code.

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)

my_turtle = t.Turtle()
my_turtle.speed("fastest")
# We can comment this line to see the path of the turtle.
my_turtle.up()
my_turtle.hideturtle()
number_of_dots = 101

# Sets the turtle position at a specific position on the canvas.
my_turtle.setheading(225)
my_turtle.forward(250)
my_turtle.setheading(0)

for dot_count in range(1, number_of_dots):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)

    # Each 10 dots the turtle will go up in the canvas to draw another line of dots.
    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)




screen = t.Screen()
# The window won't disappear until you click.
screen.exitonclick()
