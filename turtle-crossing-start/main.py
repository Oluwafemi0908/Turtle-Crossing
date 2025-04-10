import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True


def play_game():
    global game_is_on
    screen = Screen()
    scoreboard = Scoreboard()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()

    player = Player()

    screen.onkey(fun=player.move, key='Up')

    cars = CarManager()
    loop = 5
    car_passed = 0

    while game_is_on:
        loop += 1
        time.sleep(0.05)
        screen.update()

        for car in cars.cars:
            if car.xcor() < player.xcor() - 10 and car.ycor() < player.ycor():
                car_passed += 1
            if car.xcor() < -350:
                cars.cars.remove(car)
        score = car_passed * scoreboard.level * 0.5
        scoreboard.clear()
        scoreboard.display(score)

        if loop == 6:
            cars.create_car()
            loop = 0

        cars.move()

        for car in cars.cars:
            if car.distance(player) <= 19.5:
                game_is_on = False
                scoreboard.game_over(score)

        if player.ycor() >= player.FINISH_LINE_Y:
            player.restart()
            scoreboard.add_score(score)
            cars.increase_speed()
    if not game_is_on:
        restart = screen.textinput('restart', "Restart")
        if restart.lower() == 'r':
            screen.clearscreen()
            game_is_on = True
            play_game()

    screen.exitonclick()


play_game()
