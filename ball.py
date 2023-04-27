from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.goto(0, -210)
        self.x_move = 0
        self.y_move = 0
        self.move_speed = 0.018
        self.bounces = 0

    def movement(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_x(self):
        self.bounces += 1
        self.x_move *= -1
        if self.bounces != 0:
            if self.bounces % 5 == 0:
                self.move_speed *= .95
    
    def bounce_y(self):
        self.bounces += 1
        self.y_move *= -1
        if self.bounces != 0:
            if self.bounces % 5 == 0:
                self.move_speed *= .95
                  
    def start_movement(self):
        self.x_move = 3
        self.y_move = 3

    def reset_position(self, position):
        self.goto(position)
        self.x_move = 0
        self.y_move = 0
        