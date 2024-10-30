from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class Engine:

    def __init__(self, _player):
        self.blocks = []
        self.racket = _player
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")

    def createblocks(self, n_rows):
        for i in range(0, n_rows):
            for r in range(0, 17):
                t = Turtle()
                t.shape("square")
                t.shapesize(1, 2)
                t.fillcolor(COLORS[i])
                t.penup()
                t.goto(-380 + (r * 50), 50 + (25 * i))
                self.blocks.append(t)

    def verify_contact(self, ball):
        for block in self.blocks:
            if ball.distance(block) < 25:
                self.blocks.remove(block)
                block.clear()
                block.hideturtle()
                del block
                ball.bounce_x()
                ball.bounce_y()

        if ball.xcor() > 380:
            ball.bounce_x("R")

        if ball.xcor() < -380:
            ball.bounce_x("L")

        if ball.ycor() > 290:
            ball.bounce_y("T")

        x_pos = ball.xcor() - (self.racket.xcor() + 10)
        x_neg = ball.xcor() - (self.racket.xcor() - 10)
        if ((0 <= x_pos <= 20) or (-20 <= x_neg <= 0)) and (ball.ycor() <= -240):
            ball.bounce_x()
            ball.bounce_y("B")

        if ball.ycor() <= -290:
            return False

        return True

    def verify_blocks(self):
        if len(self.blocks) <= 0:
            return False
        return True

    def game_over(self, text):
        self.writer.goto(0, -50)
        self.writer.write(text, move=False, align="center", font=("Courier", 25, "normal"))
