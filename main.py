import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


count_states = []

while len(count_states) < 50:
    answer_state = screen.textinput(title=f"{len(count_states)}/50 States correct", prompt="What`s another state`s name`s").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in count_states:
        count_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

# Reviso los estados no adivinados y guarda en archivo csv
state_to_learn = []
for state in all_states:
    if state not in count_states:
        state_to_learn.append(state)

states_dict = {
    "States to learn": state_to_learn
}

pandas.DataFrame(states_dict).to_csv("States_to_learn.csv")
screen.exitonclick()






