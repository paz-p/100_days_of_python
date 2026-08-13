from turtle import Screen,Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

segments = []
screen = Screen()
turtle = Turtle()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        print("Nom Nom Nom")
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False

    for segment in snake.segments[1:]:
         if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



scoreboard.game_over()
screen.exitonclick()
