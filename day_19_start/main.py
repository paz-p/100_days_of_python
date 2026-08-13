from turtle import Turtle,Screen
import random


#TODO: I need to somehow make is to we can have as many turtles in the race class??


def setup_turtles(turtles,colors, amount_of_turtles):

    for i in range(amount_of_turtles):
        new_turtle = Turtle(shape = "turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        turtles.append(new_turtle)
    y = -300
    for turtle in turtles:
        turtle.goto(-350,y)
        y = y + 100


def move_turtles(turtles):
    for turtle in turtles:
        turtle.forward(random.randint(1,20))
        if turtle.xcor() > 350:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The winner is {turtle.pencolor()}, you win!")
                return False
            else:
                print(f"The winner is {turtle.pencolor()}, you lose!")
                return False
    return True




colors = ["red","blue","green","yellow","purple","black"]
turtles = []
race_is_on = False
screen = Screen()
screen.setup(750,700)
amount_of_turtles =  int(screen.textinput(title = "The great turtle race", prompt = "How many turtles does it have?"))
user_bet = screen.textinput(title = "Make your bet", prompt = "Pick your colored Turtle!" )
setup_turtles(turtles, colors, amount_of_turtles)
if user_bet:
    race_is_on = True
while race_is_on:
    race_is_on = move_turtles(turtles)

































screen.exitonclick()