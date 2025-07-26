from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Creation of the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.up()
        new_turtle.color("white")
        self.segments.append(new_turtle)
        new_turtle.setpos(position)

    def extend(self):
        # Adds a new segment within the last segment of the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # For loop which starts at the end of the list (start, end, step)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # If the current heading is down, it can't go up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)
