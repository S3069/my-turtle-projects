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
p1.goto(-260, 100)

p2 = Turtle()
p2.shape('turtle')
p2.color('blue')
p2.penup()
p2.goto(-260, -100)

# Dice
dice_val = [1, 2, 3, 4, 5, 6]

# Overall, players need to move 480 pixels to win.
# A score of 1 will move the player forward by 22 pixels 
# This amounts to a maximum of 20 moves or minimum of 4 in order for a player to win

for i in range(20):
    if p1.pos() > (220, 100):
        pass
    elif p2.pos() > (220, -100):
        pass
    else:
        p1_roll = int(input("Please enter the number you rolled on your die: "))
        if p1_roll in dice_val:
            print("Player 1 moves forward", p1_roll, "steps")
            p1.forward(22*p1_roll)
        p2_roll = int(input("Please enter the number you rolled on your die: "))
        if p2_roll in dice_val:
            print("Player 2 moves forward", p2_roll, "steps")
            p2.forward(22*p2_roll)
        

done()