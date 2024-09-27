
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
board = Scoreboard()
over = t.Turtle()
over.hideturtle()
over.penup()
over.goto(0, 0)
over.color("white")

splitter = t.Turtle()
splitter.penup()
splitter.hideturtle()
splitter.goto(0, -290)
splitter.color("white")
splitter.pencolor("white")
splitter.setheading(90)

for i in range(30):
    if i % 2 == 0:
        splitter.pendown()
        splitter.forward(20)
    else:
        splitter.penup()
        splitter.forward(20)

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        board.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        board.increase_r_score()

    if board.l_score >= 5:
        game_is_on = False
        over.goto(-(12 * 20) / 2, 0)
        over.write("Left Player wins", font=("Courier", 20, "normal"))
    elif board.r_score >= 5:
        game_is_on = False
        over.goto(-(12 * 20) / 2, 0)
        over.write("Right Player wins", font=("Courier", 20, "normal"))
t.exitonclick()
