from turtle import Screen
from food import Food
from score import ScoreBoard
import time
from snake import Snake

# set up of the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('dark green')
screen.title("My snake game!!")
screen.tracer(0)

# set up the snake

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# access controls

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, 'Right')

# start moving

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inc_score()
        snake.extend()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        snake.new_game()

    for seg in snake.segs[1::]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            snake.new_game()

screen.exitonclick()
