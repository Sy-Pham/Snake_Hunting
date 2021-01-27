from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time




#init screen
screen = Screen()
width_ = 600
height_ = 600
screen.setup(width_, height_)
screen.bgcolor("black")
screen.title("Snake Hunting")
screen.tracer(0)




#init instance
snake = Snake()
food = Food()
score = Score()

#catch key event to control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#run game
speed = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect colission with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # dedect collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
           

#exit game
screen.exitonclick()