from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, lives):
        super().__init__()
        with open("highscore.txt") as file:
            self.highscore = file.read()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(125, 270)
        self.lives = lives
        self.write(f"Lives: {lives} Score: {self.score} Highscore: {self.highscore}", align="center", font=('Ariel', 15, 'normal'))
        self.hideturtle()

    def update_score(self, brick, lives):
        self.clear()
        if brick.color() == ('red', 'red'):
            self.score += 10
        if lives < self.lives:
            self.lives = lives
        else:
            self.score += 1
        self.write(f"Lives: {lives} Score: {self.score} Highscore: {self.highscore}", align="center", font=('Ariel', 15, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.score > int(self.highscore):
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))
            self.write(f" Game Over!\nNEW HIGHSCORE: {self.score}",
                   align="center", font=("Ariel", 30, "bold"))
        else:
            self.write(f" Game Over!\nFinal Score: {self.score}\nHigh Score: {self.highscore}",
                   align="center", font=("Ariel", 30, "bold"))
