import turtle as t
import time

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        new_segment.speed("slowest")
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        game_is_on = True
        for p in range(len(self.body) - 1, 0, -1):
            new_x = self.body[p - 1].xcor()
            new_y = self.body[p - 1].ycor()
            self.body[p].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)