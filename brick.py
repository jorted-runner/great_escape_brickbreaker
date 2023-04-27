from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class BrickManager:

    def __init__(self):
        self.all_bricks = []
        self.brick_lives = {}
        self.levels = {
            1: {
                "starting_x": -275,
                "starting_y": 120,
                "starting_speed": .02
            },
            2: {
                "starting_x": -275,
                "starting_y": 80,
                "starting_speed": .015
            },
            3: {
                "starting_x": -275,
                "starting_y": 40,
                "starting_speed": .0125
            },
            4: {
                "starting_x": -275,
                "starting_y": 0,
                "starting_speed": .01
            },
            5: {
                "starting_x": -275,
                "starting_y": -20,
                "starting_speed": .0095
            },
            6: {
                "starting_x": -275,
                "starting_y": -30,
                "starting_speed": .009
            },
            7: {
                "starting_x": -275,
                "starting_y": -40,
                "starting_speed": .0085
            },
            8: {
                "starting_x": -275,
                "starting_y": -50,
                "starting_speed": .008
            },
            9: {
                "starting_x": -275,
                "starting_y": -100,
                "starting_speed": .0075
            },
            10: {
                "starting_x": -275,
                "starting_y": -120,
                "starting_speed": .007
            }
        }

    def set_level(self, level):
        starting_x = self.levels[level]["starting_x"]
        starting_y = self.levels[level]["starting_y"]
        while starting_y < 265:
            self.create_brick(starting_x, starting_y, color=random.choice(COLORS))
            starting_x += 55
            if starting_x > 300:
                starting_x = -275
                starting_y += 30


    def create_brick(self, x, y, color):
        new_brick = Turtle("square")
        new_brick.shapesize(stretch_wid=1, stretch_len=2.5)
        new_brick.penup()
        new_brick.color(color)
        new_brick.goto(x, y)
        if color == "red":
            hits_needed = 3
        elif color == "yellow":
            hits_needed = 2
        else:
            hits_needed = 1
        self.all_bricks.append(new_brick)
        self.brick_lives[new_brick] = hits_needed
    
    def destroy_brick(self, brick):
        self.all_bricks.remove(brick)
        brick.goto(1000,1000)

