from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")

    def update_score(self):
        self.score +=1
        self.write(f"{self.score} / 50",align="left", font=('Arial', 14, 'normal'))
