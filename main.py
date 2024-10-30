import time
from turtle import Screen
from game_engine import Engine
from racket import Racket
from ball import Ball

GAME_ON = True


def end_game():
    global GAME_ON
    GAME_ON = False


def restart_game():
    global GAME_ON
    if GAME_ON:
        pass
    GAME_ON = True


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

while GAME_ON:
    player = Racket()
    ball = Ball()
    engine = Engine(player)

    engine.createblocks(7)

    screen.onkey(player.move_left, "a")
    screen.onkey(player.move_right, "d")
    screen.onkey(end_game, "b")
    screen.onkey(restart_game, "y")

    screen.listen()

    while GAME_ON:
        time.sleep(0.05)
        screen.update()
        ball.move_ball()

        GAME_ON = engine.verify_contact(ball)

        if GAME_ON:
            GAME_ON = engine.verify_blocks()
            if not GAME_ON:
                engine.game_over("You Win")
        else:
            engine.game_over("GAME OVER")

    answer = screen.textinput("Try Again", "Do you wanna try again? (y/n)")

    if answer is None:
        screen.exitonclick()
    else:
        answer = str.lower(answer)

    if answer == 'y':
        for block in engine.blocks:
            engine.blocks.remove(block)
            block.clear()
            block.hideturtle()
            del block
        engine.writer.clear()
        player.clear()
        player.hideturtle()
        ball.clear()
        ball.hideturtle()
        del player
        del ball
        del engine

        GAME_ON = True

        screen.update()

screen.exitonclick()
