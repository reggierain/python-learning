import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

loc = turtle.Turtle()
loc.hideturtle()
loc.penup()

score = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            score += 1
        state = data[data["state"] == answer_state]
        loc.goto(state.x.item(), state.y.item())
        loc.write(state.state.item())







screen.exitonclick()