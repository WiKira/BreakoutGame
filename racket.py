from turtle import Turtle

START_POSITIONS = [(-350, 0), (350, 0)]


class Racket(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.goto(0, -250)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_left(self):
        x_pos = self.xcor() - 40 if self.xcor() - 40 > -360 else -360
        self.goto(x_pos, -250)

    def move_right(self):
        x_pos = self.xcor() + 40 if self.xcor() + 40 < 360 else 360
        self.goto(x_pos, -250)
