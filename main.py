import turtle
import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=720, height=460)
screen.addshape(image)

turtle.shape(image)

answer_text = screen.textinput(title="Guess the State", prompt="What's another state's name? ")
states = pandas.read_csv("50_states.csv")

if states["state"]  == answer_text:
    print(states.state)






turtle.mainloop()
