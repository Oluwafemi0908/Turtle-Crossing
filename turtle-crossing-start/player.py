from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280
        self.penup()
        self.shape('turtle')
        self.restart()
        self.setheading(90)

    def move(self):
        self.forward(self.MOVE_DISTANCE)

    def restart(self):
        self.goto(self.STARTING_POSITION)
