import turtle
import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
# screen.setup(width=720, height=460)
screen.addshape(image)

turtle.shape(image)

text_turtle = turtle.Turtle()
game_on = True

while game_on:

    answer_text = screen.textinput(title="Guess the State", prompt="What's another state's name? ")
    states_dict = pandas.read_csv("50_states.csv").to_dict()

    states = states_dict["state"]
    x_coor = states_dict["x"]
    y_coor = states_dict["y"]
    found_state_index = 0
    for state in states:
        if states[state] == answer_text:
            found_state_index = state
    text_turtle.penup()
    text_turtle.write(answer_text)
    text_turtle.goto(x_coor[found_state_index], y_coor[found_state_index])

turtle.mainloop()
