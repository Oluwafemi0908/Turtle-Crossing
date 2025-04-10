from turtle import Turtle
with open('highscore.txt') as file:
    highscore = file.read()
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

    def display(self, score):
        self.write(arg=f"Level: {self.level},   Score: {score}   HighScore: {highscore}", align='center', font=FONT)

    def add_score(self, score):
        self.level += 1
        self.display(score)

    def game_over(self, score):
        global highscore
        self.goto(0, 100)
        if score > float(highscore):
            highscore = score
        with open('highscore.txt', mode='w') as new_file:
            new_file.write(str(highscore))
        self.write(arg="Game Over!!!", align='center', font=('Arial', 40, 'bold'))
        self.hideturtle()
        self.goto(0, 75)
        self.write(arg=f"Final Score: {score}  HighScore: {highscore}", align='center', font=('Arial', 25, 'bold'))
        self.goto(0, 50)
        self.write(arg=f"Press R to restart", align='center', font=('Arial', 15, 'bold'))
