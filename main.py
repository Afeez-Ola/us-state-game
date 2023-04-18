import turtle
import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=720, height=460)
screen.addshape(image)

turtle.shape(image)


def get_mouse_coor(x, y):
    print(x, y)


screen.onclick(get_mouse_coor)
turtle.mainloop()
