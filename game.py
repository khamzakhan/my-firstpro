import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it within 10 attempts?")

    while attempts < 5:
        guess = int(input("Enter your guess: "))

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    print(f"Game over! The number was {number}.")

guess_the_number()
