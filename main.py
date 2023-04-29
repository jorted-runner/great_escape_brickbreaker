from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import BrickManager
from scoreboard import ScoreBoard
import time

level = 1
lives = 3

def start_ball():
    ball.bounces = 0
    ball.move_speed = brick_manager.levels[level]["starting_speed"]
    ball.start_movement()

def start_ball_trace():
    ball.pendown()

def end_ball_trace():
    ball.penup()

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("Black")
game_screen.title("The Great Escape - Brick Breaker")
game_screen.tracer(0)

paddle = Paddle((0, -225))
ball = Ball()
score_keeper = ScoreBoard(lives)
brick_manager = BrickManager()
brick_manager.set_level(level)
ball.move_speed = brick_manager.levels[level]["starting_speed"]

game_screen.onkeypress(fun=paddle.right, key="Right")
game_screen.onkeypress(fun=paddle.left, key="Left")
game_screen.onkeyrelease(fun=paddle.stop, key="Right")
game_screen.onkeyrelease(fun=paddle.stop, key="Left")

game_screen.onkey(fun=start_ball, key="space")
game_screen.onkey(fun=start_ball_trace, key="t")
game_screen.onkey(fun=end_ball_trace, key="u")
game_screen.listen()

game_is_on = True 
while game_is_on:
    time.sleep(ball.move_speed)
    game_screen.update()
    ball.movement()
    paddle.move()
    if len(brick_manager.all_bricks) > 0:
        for brick in brick_manager.all_bricks:
            distance = ((ball.xcor() - brick.xcor())**2 + (ball.ycor() - brick.ycor())**2)**0.5
            if distance < 32:
                if brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10:
                    if ((ball.xcor() >= brick.xcor() - 25 and ball.x_move < 0)
                        or (ball.xcor() <= brick.xcor() + 25 and ball.y_move > 0)):
                        ball.bounce_x()
                        brick_manager.brick_lives[brick] -= 1
                        if brick_manager.brick_lives[brick] < 1:
                            brick_manager.destroy_brick(brick)
                            score_keeper.update_score(brick, lives)
                            break
                        if brick.color() == ('red', 'red'):
                            brick.color("yellow")
                            score_keeper.update_score(brick, lives)
                            break
                        elif brick.color() == ('yellow', 'yellow'):
                            brick.color("green")
                            score_keeper.update_score(brick, lives)
                            break
                        break
                elif ((ball.ycor() >= brick.ycor() + 12 and ball.y_move < 0)
                or (ball.ycor() <= brick.ycor() - 12 and ball.y_move > 0)) \
                    and brick.xcor() - 25 < ball.xcor() < brick.xcor() + 25:
                    ball.bounce_y()
                    brick_manager.brick_lives[brick] -= 1
                    if brick_manager.brick_lives[brick] < 1:
                        brick_manager.destroy_brick(brick)
                        score_keeper.update_score(brick, lives)
                        break
                    if brick.color() == ('red', 'red'):
                        brick.color("yellow")
                        score_keeper.update_score(brick, lives)
                        break
                    elif brick.color() == ('yellow', 'yellow'):
                        brick.color("green")
                        score_keeper.update_score(brick, lives)
                        break
                    break

    else:
        level += 1
        x = paddle.xcor()
        y = -210
        ball.reset_position((x, y))
        brick_manager.set_level(level)
    
    if ball.ycor() < -600/2 + 5:
        lives -= 1
        score_keeper.update_score(brick, lives)
        if lives < 1:
            x = paddle.xcor()
            y = -210
            ball.reset_position((x, y))
            for brick in brick_manager.all_bricks:
                brick.goto(1000, 1000)
            game_screen.update()
            score_keeper.game_over()
        else:
            x = paddle.xcor()
            y = -210
            ball.reset_position((x, y))
    elif paddle.distance(310, -225) < 50:
        paddle.left()
    elif paddle.distance(-310, -225) < 50:
        paddle.right()
    if ball.ycor() == -210 and ball.distance(paddle) < 60:
        ball.bounce_y()
    if ball.xcor() > 290 or ball.xcor() < -295:
        ball.bounce_x()
    elif ball.ycor() > 290:
        ball.bounce_y()
        
game_screen.exitonclick()