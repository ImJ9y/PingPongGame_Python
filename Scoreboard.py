from turtle import Turtle, Screen
from Ball import Ball

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))
    def l_point(self):
        self.player1_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.player2_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGMENT, font=FONT)