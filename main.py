import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()
guessed_state = []
# date_xcon = data["x"].to_list()
# date_ycon = data["y"].to_list()
# print(all_state)

while len(guessed_state) < 50:
    answer_state = turtle.textinput(f"{len(guessed_state)}/50 States Correct", "What's another state name ?")
    title_answer_state = answer_state.title()

    if title_answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        missing_state_data = pandas.DataFrame(missing_state)
        missing_state_data.to_csv("Missing_State.csv")
        break

    if title_answer_state in all_state:
        guessed_state.append(title_answer_state)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        data_state = data[data.state == title_answer_state]
        print(data_state)
        tim.goto(int(data_state.x), int(data_state.y))
        # tim.write(data_state.state.item(), align="center", font=("Arial", 10, "normal"))
        tim.write(title_answer_state)

# states to learn.csv

# My style too complicate
# def state_position(x_con, y_con, state):
#     turtle.penup()
#     turtle.write(state, align="center", font=("Arial", 8, "normal"))
#     turtle.goto(x_con, y_con)

# i = 0
# if answer_state have answer in the csv
# if they got it right
# create a turtle to write a name of the state at the state's x and y position
# for d_state in data_state:
#     i += 1
#     if d_state == title_answer_state:
#         print(d_state, i)
#         print(date_xcon[i-1], date_ycon[i-1])
#         state_position(date_xcon[i-1], date_ycon[i-1], d_state)
#
# guess_cont = True

# while guess_cont:
#     for data_state in d:
#         if data_state == da:
#             print(da)


screen.exitonclick()
