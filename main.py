from turtle import Turtle, Screen

cosmos = Turtle()
screen = Screen()

def move_forward():
    cosmos.fd(10)

def move_backward():
    cosmos.back(10)

def counter_clockwise():
    cosmos.lt(10)

def clockwise():
    cosmos.rt(10)

def clear():
    cosmos.clear()
    cosmos.penup()
    cosmos.home()
    cosmos.pendown()

screen.listen()
screen.onkeypress(key= "w", fun= move_forward)
screen.onkeypress(key= "s", fun= move_backward)
screen.onkeypress(key= "a", fun= counter_clockwise)
screen.onkeypress(key= "d", fun= clockwise)
screen.onkey(key= "c", fun= clear)
screen.exitonclick()