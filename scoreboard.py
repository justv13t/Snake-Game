from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Read highscore from 'data.txt' file
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # If new high score, then update data.txt file
        if self.score > self.high_score:
            self.high_score = self.score
            # Write highscore to data.txt file
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        # Reset current score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

