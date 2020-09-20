# Name: David Lee
# Purpose: The purpose of this program is to create a
# a number guessing game that allows the user to continue
# to guess until they correctly guess the actual value of
# a randomly generated number between 1 and 100.

from random import randint

rand_num = randint(1, 100)
print("Welcome to the number guessing game! You may exit the game at any time by entering in EXIT during any of the input phases.")
user_guess = input("Please guess a number between 1 and 100: ")
guess_count = 1
correct = False
while not correct:
    # If user inputs the exit command
    if user_guess == "EXIT":
        print("Thank you for playing the number guessing game. Please join us again soon!")
        correct = True

    # Do not accept any non positive integer values
    elif user_guess.isnumeric() == False:
        print("Incorrect input. Please only enter in an integer value between 1 and 100. ")
        user_guess = input("Please guess a number between 1 and 100:  ")

    # Only accept numbers in the range 1-100
    elif int(user_guess) < 1 or int(user_guess) > 100:
        user_guess = input("Please only enter a number between 1 and 100. Please guess another number: ")

    # If user guesses too low
    elif int(user_guess) < rand_num:
        user_guess = input("Guess is too low. Please guess again: ")
        guess_count += 1

    # If user guesses too high
    elif int(user_guess) > rand_num:
        user_guess = input("Guess is too high. Please guess again: ")
        guess_count += 1

    # If user guesses correctly
    else:
        print("That is correct. Good job!")
        print(f"It took {guess_count} guesses to reach the correct number.")
        print("Thank you for playing the guessing game! See you again next time!")
        correct = True
