#!/usr/bin/py
" write a program that tells the user to guess a random number from 1 to 5,if thhe user guess the number correct tell him congratulation you just won yourself 1000000, other wise tell them to try again, a user has three trials until gameover "

import random 

number = random.randint(1,5)
trials = 3

while trials > 0:
    guess = int(input("Guess a number between 1 and 5: "))
    if guess == number:
        print("congratualtion! you just won yourself 1,000,000!")
        break 
    else:
        trials-=1
        if trials> 0:
            print("wrong guess. Try again.")
        else:
            print("Game over! you have used up all your trails ")
            print("the correct answer was:", number )

