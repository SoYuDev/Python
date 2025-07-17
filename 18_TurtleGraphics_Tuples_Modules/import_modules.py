# Different ways to import modules

# 1.
import turtle
my_turtle = turtle.Turtle()

# 2.
from turtle import Turtle
my_turtle2 = Turtle()

# 3.
# This is generally a bad practice when it comes to import modules.
from turtle import *

# 4.
# We can give an alias name to a module, useful when the module name is really long.
import turtle as t
my_turtle3 = t.Turtle

#----------------------------------------------------------------------------------------------------------------------#
# 5. Some modules need to be installed because they are not included in Python's standard library.
import heroes
print(heroes.gen())