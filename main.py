import turtle
import random
import time
from ball import Ball
from ball import balls

from typing_extensions import runtime
import sys
import os
import subprocess

# window operations
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Ball Bouncing Simulation")
wn.tracer(0)  # for updating frames better

# constants/timers
WAIT_TIME = 0.005
BALL_COUNT = 10
runtime = 0
spawn_time = .5
gravity = 0.1

# ball spawning
for _ in range(5):
    Ball()
    time.sleep(.005)

# frame update loop
while True:
    wn.update()
    # ball physics & collision operations
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.dy -= ball.da*.01
        if ball.dx >= 0:
            ball.dx -= ball.fD
        else:
            ball.dx += ball.fD
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)

        # Wall collisions
        if ball.xcor() > 300:
            ball.dx *= -1
            #ball.da *= -1

        if ball.xcor() < -300:
            ball.dx *= -1
            #ball.da *= -1

        # Bounce check
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -ball.bounce
            ball.da *= -ball.bounce * 0.2  # ball.bounce
            print(str(ball.color()) + ": " + str(ball.da))

    # Ball collision check
    # for i in range(0, len(balls)):
    #     for j in range(i+1, len(balls)):
    #         if balls[i].distance(balls[j]) < 20:
    #             balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
    #             balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy

    # wait/runtime timer to manage update speed
    time.sleep(WAIT_TIME)
    runtime += WAIT_TIME
    print(runtime)
    if(runtime >= 2):
        #subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        sys.exit()
