import random
import turtle
import numpy

# list of possible colors and shapes
colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
shapes = ["triangle", "square"]

# array where ball objects will be placed
balls = []


class Ball(turtle.Turtle):
    def __init__(self):
        # initializing object
        self = turtle.Turtle()
        # self.penup()
        self.speed(0)

        #position & velocity
        x = random.randint(-300, -290)
        y = -200
        self.goto(x, y)
        self.dy = random.randint(0, 1)
        self.dx = -3
        self.da = random.randint(-5, 5)

        #shape & color
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))

        # Bounce coefficient, magnus (spin) force, and drag force
        # clay = 0.7, hard = 0.6, grass = 0.5 (estimates)
        self.bounce = .7

        # need to update fM equation properly
        # fM = dP * A (https://en.wikipedia.org/wiki/Magnus_effect)
        self.fM = self.da

        # need to also update fD
        #fD = 1/2*p*numpy.pow(u, 2)*cD*A
        # https://en.wikipedia.org/wiki/Drag_equation
        self.fD = .005

        # add self to balls list
        balls.append(self)
