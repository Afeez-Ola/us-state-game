import turtle
import pandas
from scoring import Score

scoreboard = Score()
score = scoreboard.score_board()

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=720, height=460)
screen.addshape(image)

turtle.shape(image)

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
game_on = True
attempts = 50
correct_guess = []

states_dict = pandas.read_csv("50_states.csv").to_dict()

states = states_dict["state"]
x_coor = states_dict["x"]
y_coor = states_dict["y"]
state_list = list(states.values())
state_list = [state.lower() for state in state_list]

x_list = list(x_coor.values())
y_list = list(y_coor.values())

while game_on:
    answer_text = screen.textinput(title=score, prompt="What's another state's name? ")
    answer_text = answer_text.lower()

    if answer_text in state_list:
        index = state_list.index(answer_text)
        text_turtle.goto(x_list[index], y_list[index])
        text_turtle.write(answer_text)
        correct_guess.append(answer_text)
        score = scoreboard.update_score()
    else:
        print("nope" + answer_text)

    print(correct_guess)
turtle.mainloop()
