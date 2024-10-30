from turtle import Turtle
from random import choice

ANGLES = [-10, -8, 8, 10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = choice(ANGLES)
        self.y_move = choice(ANGLES)
        self.move_speed = 1
        self.setheading(270)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self, racket_bounce=""):
        if racket_bounce == "B":
            self.y_move = abs(choice(ANGLES))
        elif racket_bounce == "T":
            self.y_move = abs(choice(ANGLES)) * -1
        else:
            self.y_move = choice(ANGLES)

    def bounce_x(self, racket_bounce=""):
        if racket_bounce == "L":
            self.x_move = abs(choice(ANGLES))
        elif racket_bounce == "R":
            self.x_move = abs(choice(ANGLES)) * -1
        else:
            self.x_move = choice(ANGLES)

    def increase_speed(self):
        self.move_speed *= 1

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
