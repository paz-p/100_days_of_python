from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 200)


    def update(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.home()
        self.write(f"Game Over!", align="center", font=FONT)