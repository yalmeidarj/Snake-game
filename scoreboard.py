from turtle import Turtle
style = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.write(arg=f"Score: {self.points} ", align='center', font=style)

    def update_score(self):
        self.points += 1
        self.write(arg=f"Score: {self.points} ", align='center', font=style)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align='center', font=style)