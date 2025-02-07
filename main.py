from encodings.punycode import segregate
from turtle import Screen
from snake import Snake
from food import Food
from scoredboard import  Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("the snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #DITICT COLLISION WITH FOOD
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #DITICT COLLISION WITH WALL
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.gameover()

    for  segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.gameover()








screen.exitonclick()