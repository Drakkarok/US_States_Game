import pandas
import csv
import turtle
# from turtle import Turtle, Screen

screen = turtle.Screen()
screen.title("U.S. - States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
wanna_be_over = 1


while [x for x in all_states if x not in guessed_states] is not None and wanna_be_over != 0:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(state_data.state.item())
    elif answer_state == '0':
        wanna_be_over = 0

never_guessed_states = [x for x in all_states if x not in guessed_states]
new_data = pandas.DataFrame(never_guessed_states)
new_data.to_csv("states_to_learn.csv")
screen.exitonclick()




