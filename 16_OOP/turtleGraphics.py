# Python external library - Option A
import turtle

# Only import Turtle and Screen classes - Option B
from turtle import Turtle, Screen

# Instantiation of objects
# mi_turtle = turtle.Turtle()

mi_turtle2 = Turtle()
mi_turtle2.shape("turtle")
mi_turtle2.color("red", "green")
mi_turtle2.forward(100)

my_screen = Screen()

print(my_screen.canvheight)
my_screen.exitonclick()

# Imported Python Package
from prettytable import PrettyTable
table = PrettyTable()
table.align = "l"
table.add_column("Pokemon Name", ["Pikachu", "Giratina", "Blastoise"])
table.add_column("Type", ["Electric", "Ghost", "Water"])
print(table)





