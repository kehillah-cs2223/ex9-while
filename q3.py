"""
Question 3

tl;dr Play rock-paper-scissors until the user decides to exit.

Here's an answer to a question from Quiz 2, plus some code to ask for input from
the user.

Write a while loop that:

1. gets a computer choice and user choice
2. prints out both choices
    (You DON'T have to say who won, but you can add that logic if you want!)
3. asks the user if they want to play again
4. stops only when the user says "no"

"""

import random

def get_computer_choice():
    """ Randomly choose either "rock", "paper", or "scissors" """

    choice = random.randint(0, 2)
    if choice == 0:
        return "rock"
    elif choice == 1:
        return "paper"
    elif choice == 2:
        return "scissors"

####### EDIT THIS WHILE LOOP! #######
# Play rock-paper-scissors until the user decides to exit.
while True:
    computer_choice = get_computer_choice()
    user_choice = input("Choose 'rock', 'paper', or 'scissors': ")

