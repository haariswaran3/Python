#!/usr/bin/env python

import random

def main():
 """Start a music guessing game."""
print("guess the music!")

music = [
        "do",
        "re",
        "mi",
        "fa",
        "so" 
        ]

x = random.choice(music)
max_trials = 2
trials = 0
print (x)
guess = None

while x != guess:

    guess = str(input("What music am i thinking of? "))
    trials += 1

    guess = str(input("What music am i thinking of? This is your last try !Answer correctly! "))

    if "do" == guess:
        print ("You guessed {}. Congratulation you got it right!".format(guess))
    else:
        print ("You guessed {}. Unfortunately you got the wrong answer. Please try again !". format(guess))
        break
main()