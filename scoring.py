from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.result = "0/50 states correct"
        self.color("black")

    def update_score(self):
        self.result = f"{int(self.result.split('/')[0]) + 1}/50 states correct"
        return self.result

    def score_board(self):
        return self.result
