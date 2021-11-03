import turtle as t
import time
import snake
import food
import scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Yalmeida ")
screen.tracer(0)


snake = snake.Snake()
screen.listen()

food = food.Food()
score = scoreboard.Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.west, "a")
    screen.onkey(snake.east, "d")
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.clear()
        score.update_score()
        print(f" score: {score.points}")
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()