import turtle
import pandas
from scoring import Score

scoreboard = Score()
score = scoreboard.score_board()

image = "blank_states_img.gif"
attempts = 50
guessed_state = []
missing_states = []

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=720, height=460)
screen.addshape(image)
turtle.shape(image)

states_dict = pandas.read_csv("50_states.csv").to_dict()

states = states_dict["state"]
x_coor = states_dict["x"]
y_coor = states_dict["y"]
state_list = list(states.values())

x_list = list(x_coor.values())
y_list = list(y_coor.values())

while len(guessed_state) < attempts:
    answer_text = (screen.textinput(title=score, prompt="What's another state's name? ")).title()
    if answer_text == "Exit":
        for item in state_list:
            if item not in guessed_state:
                missing_states.append(item)
        remaining_states = pandas.DataFrame({"state": missing_states})
        remaining_states.to_csv("remaining_states.csv")
        break
    if answer_text in state_list:
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        index = state_list.index(answer_text)
        text_turtle.goto(x_list[index], y_list[index])
        text_turtle.write(answer_text)
        guessed_state.append(answer_text)
        score = scoreboard.update_score()
    else:
        print("nope" + answer_text)


