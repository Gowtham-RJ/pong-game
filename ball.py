from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.025

    def move(self):
        position_x = self.xcor() + self.x_move
        position_y = self.ycor() + self.y_move
        self.goto(position_x, position_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.025

    def increase_speed(self):
        if self.move_speed > 0.004169295424916645:
            self.move_speed *= 0.9
