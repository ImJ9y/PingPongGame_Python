import time
from turtle import Screen
from paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My PingPong Game")
screen.tracer(0)

# Create a player instance
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreBoard = Scoreboard()

# Bind the player movement methods to the keyboard
screen.listen()
screen.onkey(l_paddle.up, "q")
screen.onkey(l_paddle.down, "a")

screen.onkey(r_paddle.up, "]")
screen.onkey(r_paddle.down, "'")

# Main game loop
game_is_on = True
while game_is_on:
    #when ball is missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreBoard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreBoard.r_point()

    if scoreBoard.player1_score > 3 or scoreBoard.player2_score > 3:
        scoreBoard.game_over()
        game_is_on = False
        break

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()


screen.exitonclick()
