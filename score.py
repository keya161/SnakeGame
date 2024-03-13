from turtle import Turtle
FONT = ('Arial', 12, 'normal')
# TODO:5 scoreboard


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt')as high:
            self.high_score = int(high.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(0, 280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}  High score : {self.high_score}", move=False, align='center', font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', mode='w') as high:
                high.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def inc_score(self):
        self.score += 1
        self.update()
