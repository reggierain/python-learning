from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    def create_segments(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.segments.append(new)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[pos - 1].xcor()
            new_y = self.segments[pos - 1].ycor()
            self.segments[pos].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.goto(100000, 1000000)
        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]