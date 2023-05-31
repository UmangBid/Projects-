import random

roll_again = "Y"
while roll_again == "Y":
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    print(f"Dice1 = {Dice1}", f"\nDice2 = {Dice2}")
    roll_again = input("Roll the dice again? (Y/N)")