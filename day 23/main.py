import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

cars = []



screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


scoreboard.update()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_goal():
        player.start()
        car_manager.increase_speed()
        scoreboard.update()





screen.exitonclick()