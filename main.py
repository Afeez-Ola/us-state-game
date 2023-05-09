import turtle
import pandas
from scoring import Score

# Initialize Score class
scoreboard = Score()
score = scoreboard.score_board()

# Set up screen
screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=720, height=460)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# Load states data from CSV
states_dict = pandas.read_csv("50_states.csv").to_dict()
states = states_dict["state"]
x_coor = states_dict["x"]
y_coor = states_dict["y"]
state_list = list(states.values())
x_list = list(x_coor.values())
y_list = list(y_coor.values())

# Initialize game variables
attempts = 50
guessed_state = []

# Game loop
while len(guessed_state) < attempts:
    answer_text = (screen.textinput(title=score, prompt="What's another state's name? ")).title()

    if answer_text == "Exit":
        missing_states = [item for item in state_list if item not in guessed_state]
        remaining_states = pandas.DataFrame({"state": missing_states})
        remaining_states.to_csv("remaining_states.csv")

        break
    if answer_text in state_list:
        # Update turtle with guessed state name
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        index = state_list.index(answer_text)
        text_turtle.goto(x_list[index], y_list[index])
        text_turtle.write(answer_text)
        guessed_state.append(answer_text)
        score = scoreboard.update_score()
    else:
        print("Nope: " + answer_text)
