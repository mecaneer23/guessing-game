#!/usr/bin/env python3

from random import randrange

number = randrange(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"You got it in {tries} tries!")
        break