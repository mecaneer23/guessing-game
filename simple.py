import random

won = False
num = random.randint(1, 100)
while won == False:
    print("Guess a number: ")
    answer = int(input())
    if answer > num:
        print("Too high")
    elif answer < num:
        print("Too low")
    else:
        won = True
        print("You won!")