import random
from tkinter import Tk, Label
from turtle import Turtle, Screen

def error():
    root = Tk()
    root.title("Error Popup")
    label = Label(root, text= "Error! Wrong Input!", font= ("Arial", 10), fg= "red")
    label.pack(pady = 20)

screen = Screen()
screen.setup(600, 600)
is_race_on = False
user_bet = screen.textinput(title= "Make your bet",
                            prompt="Which turtle will win the race? Enter a color:"
                                   " \nred\norange\nyellow\ngreen\nblue\npurple\n").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["joseph", "june", "cosmos", "chidera", "ayo", "leon"]
turtle_list = []
x = -280
y = -150

for name in range(0, len(names)):
    names[name] = Turtle("turtle")
    names[name].color(colors[name])
    names[name].penup()
    names[name].goto(x, y)
    turtle_list.append(names[name])
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    if user_bet not in colors:
        error()
        user_bet = screen.textinput(title="Make your bet",
                                    prompt="Which turtle will win the race? Enter a color:"
                                           " \nred\norange\nyellow\ngreen\nblue\npurple\n").lower()
    else:
        for turtle in turtle_list:
            winner = turtle.xcor()
            move = random.randint(0, 10)
            turtle.forward(move)
            if winner >= 300:
                is_race_on = False
                champ = int(turtle_list.index(turtle))
                if user_bet == colors[champ]:
                    print("You won the bet! Congratulations.")
                else:
                    print("You didn't win the bet.")
                    print(f"The winner was {colors[champ]}")

screen.exitonclick()