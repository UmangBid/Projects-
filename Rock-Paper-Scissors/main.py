import random

while True:
    choose = "rock", "paper", "scissors"
    user_choice = input("Enter a choice (rock, paper, scissors): ")

    comp_choice = random.choice(choose)
    print(f"\nYou chose {user_choice}, computer chose {comp_choice}.")

    if user_choice == comp_choice:
        print("It's a tie!")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper covers rock! You lose.")
        else:
            print("Rock breaks scissors! You win.")

    elif user_choice == "paper":
        if comp_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("Rock breaks scissors! You lose.")
        else:
            print("Scissors cuts paper! You win.")
    play_again = input("\nPlay again (Y/N)? ")
    if play_again != "Y":
        break
