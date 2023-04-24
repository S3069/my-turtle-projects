from turtle import *
import math
import pygame

# Made by lvxq37-2
# I intentionally kept functions beside their calls so it is clear where the code is used

# Setting up: Background
t = Turtle()
title("Race mini-game")
t.screen.setup(800, 600)
t.screen.bgpic('race-game-files/grassy background.png')

# Setting up: Background Music
# Please run 'python3 -m pip install -U pygame --user' in the terminal if you are experiencing issues with Pygame, or consult the Pygame wiki: https://www.pygame.org/wiki/GettingStarted
pygame.mixer.init()
pygame.mixer.music.load("race-game-files/Wallpaper.mp3") 
pygame.mixer.music.play(-1,0.0)                             # Music is looped until the game is closed

# Setting up: Finish line
finish_l = 220
t.speed(10000)
t.hideturtle()
t.color('red')
t.pensize(5)
t.penup()
t.goto(finish_l, 180)
t.right(90)
t.pendown()
t.forward(360)

# Setting up: Players at Start Line
start_l = -260
p1 = Turtle()
p1.shape('turtle')
p1.color('yellow')
p1.penup()
p1.goto(start_l, 100)

p2 = Turtle()
p2.shape('turtle')
p2.color('blue')
p2.penup()
p2.goto(start_l, -100)

# Dice
dice_val = [1, 2, 3, 4, 5, 6]

# In a standard game, players need to move 480 pixels to win.
# A score of 1 will move the player forward by 22 pixels 
# This amounts to a maximum of 20 moves (or minimum of 4) in order for a player to win

# This calculates the maximum number of turns per player. This may change from 20 if the starting or finish lines are changed
max_turns = math.ceil((finish_l - start_l)/22)

def reset():
    p1.right(180)
    p1.goto(start_l, 100)
    p1.left(180)
    
    p2.right(180)
    p2.goto(start_l, -100)
    p2.left(180)

def check(position):
    if p1.pos() >= (finish_l, 100):
        return True
    elif p2.pos() >= (finish_l, -100):
        return True

def game():
    for i in range(max_turns): # Maximum limit is standard 20 moves (valid or invalid) per player
        p1_roll = int(input("Player 1, please enter the number you rolled on your die: "))
        if p1_roll in dice_val:
            print("Player 1 moves forward", p1_roll, "steps")
            p1.forward(22*p1_roll)
            if check(position) == True:
                print("Player 1 wins! Well done")
                break
        else:
            print("Nope! Skip!")

        p2_roll = int(input("Player 2, please enter the number you rolled on your die: "))
        if p2_roll in dice_val:
            print("Player 2 moves forward", p2_roll, "steps")
            p2.forward(22*p2_roll)
            if check(position) == True:
                print("Player 2 wins! Well done")
                break
        else:
            print("Nope! Skip!")


def main():
    print("\nPlease have 1 die ready before you start the game.\nRemember: entering an invalid dice roll will result in a penalty - You'll miss your turn!\n")
    game()
    rematch = input("Would you like a rematch? y/n: ")
    if rematch.upper() == "Y":
        reset()
        main()
    else:
        print("Thanks for playing, goodbye :)")
        bye()

main()