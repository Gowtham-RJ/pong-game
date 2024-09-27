from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("White")
        self.penup()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.new_cor = 0

    def move_up(self):
        self.new_cor = self.ycor()
        if self.new_cor <= 240:
            self.new_cor += 20
        self.goto(self.x, self.new_cor)

    def move_down(self):
        self.new_cor = self.ycor()
        if self.new_cor > -240:
            self.new_cor -= 20
        self.goto(self.x, self.new_cor)



