#!/usr/bin/env python3
"""Solve the guessing game using a binary search algorithm"""


def main() -> None:
    """Guess a number the user is thinking of"""
    tries = 0
    lower_bound = 1
    upper_bound = 100
    print("Think of a number between 1 and 100...")
    while True:
        guess = (lower_bound + upper_bound) // 2
        response = input(
            f"Is your number {guess}?\nEnter (-, +, 0), "
            "corresponding to too low, too high, or correct:\n"
        )
        tries += 1
        if response == "-":
            upper_bound = guess - 1
        elif response == "+":
            lower_bound = guess + 1
        elif response == "0":
            print(f"Got it! It took {tries} tries.")
            break
        else:
            print("That's not a vaild response!")
            tries -= 1
            continue


if __name__ == "__main__":
    main()
