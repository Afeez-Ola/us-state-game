import turtle
import pandas
from scoring import Scoreboard

scoreboard = Scoreboard()

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=720, height=460)
screen.addshape(image)

turtle.shape(image)

text_turtle = turtle.Turtle()
text_turtle.penup()
game_on = True
attempts = 50
while game_on:

    answer_text = screen.textinput(title=scoreboard, prompt="What's another state's name? ").lower()
    states_dict = pandas.read_csv("50_states.csv").to_dict()

    states = states_dict["state"]
    x_coor = states_dict["x"]
    y_coor = states_dict["y"]
    found_state_index = 0
    for state in states:
        if (states[state]).lower() == answer_text:
            found_state_index = state
            attempts -=1
            print(attempts)
    if attempts == 0:
        game_on = False

    text_turtle.hideturtle()
    text_turtle.setposition(x_coor[found_state_index], y_coor[found_state_index])
    text_turtle.write(answer_text)
    print(f"{x_coor[found_state_index]} , {y_coor[found_state_index]}")


turtle.mainloop()
