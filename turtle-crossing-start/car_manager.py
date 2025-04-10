import random
from turtle import Turtle

class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 5


    def create_car(self):
        car = Turtle()
        car.color(random.choice(self.COLORS))
        car.y_pos = random.randint(-12, 13)
        car.penup()
        car.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, car.y_pos * 20)
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for x in self.cars:
            x.forward(self.STARTING_MOVE_DISTANCE)


    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT


