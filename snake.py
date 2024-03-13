from turtle import Turtle

START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segs = []
        self.snake_struc()
        self.head = self.segs[0]

# TODO:1 Create a snake body(3squares lined up)
    def snake_struc(self):
        for i in START:
            self.add_seg(i)

# TODO:2 Move snake

    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            self.segs[i].goto(self.segs[i - 1].pos())
        self.segs[0].forward(MOVE_DIST)

# TODO:3 Control the snake

    def up(self):
        if self.segs[0].heading() != DOWN:
            self.segs[0].setheading(UP)

    def down(self):
        if self.segs[0].heading() != UP:
            self.segs[0].setheading(DOWN)

    def right(self):
        if self.segs[0].heading() != LEFT:
            self.segs[0].setheading(RIGHT)

    def left(self):
        if self.segs[0].heading() != RIGHT:
            self.segs[0].setheading(LEFT)

# TODO:7 detect collision with tail

    def add_seg(self, position):
        seg = Turtle(shape='square')
        seg.color('light green')
        seg.penup()
        seg.goto(position)
        self.segs.append(seg)

    def extend(self):
        self.add_seg(self.segs[-1].position())

    def new_game(self):
        for i in self.segs:
            i.goto(1000, 1000)
        self.segs.clear()
        self.snake_struc()
        self.head = self.segs[0]
