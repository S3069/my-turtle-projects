from turtle import *
import random

# Made by lvxq37-2
# I intentionally kept functions beside their calls so it is clear where the code is used

# Setting up: Background
t = Turtle()
title("Race mini-game")
t.screen.setup(800, 600)
t.screen.bgpic('grassy background.png')

# Setting up: Finish line
t.speed(10000)
t.hideturtle()
t.color('red')
t.pensize(5)
t.penup()
t.goto(220, 180)
t.right(90)
t.pendown()
t.forward(360)

# Setting up: Players
p1 = Turtle()
p1.shape('turtle')
p1.color('yellow')
p1.penup()
p1.goto(-250, 100)

p2 = Turtle()
p2.shape('turtle')
p2.color('blue')
p2.penup()
p2.goto(-250, -100)

# Dice
dice = [1, 2, 3, 4, 5, 6]

done()