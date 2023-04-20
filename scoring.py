from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.result = ""
        self.score = 0
        self.color("black")

    def update_score(self):
        self.score +=1
        self.result = f"{self.score}/ 50"
        return self.result

    def score_board(self):
        self.result = f"{self.score}/ 50 states correct"
        return self.result
