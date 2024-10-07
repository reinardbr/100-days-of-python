import random

rock = "rock"
paper = "paper"
scissors = "scissors"

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if player_choice == 0:
    print(f"You choose: {rock}")
    if computer_choice == 0:
        print(f"Computer choose: {rock}")
        print("Draw!")
    elif computer_choice == 1:
        print(f"Computer choose: {paper}")
        print("You lose!")
    else:
        print(f"Computer choose: {scissors}")
        print("You win!")
elif player_choice == 1:
    print(f"You choose: {paper}")
    if computer_choice == 0:
        print(f"Computer choose: {rock}")
        print("You win!")
    elif computer_choice == 1:
        print(f"Computer choose: {paper}")
        print("Draw!")
    else:
        print(f"Computer choose: {scissors}")
        print("You lose!")
elif player_choice == 2:
    print(f"You choose: {scissors}")
    if computer_choice == 0:
        print(f"Computer choose: {rock}")
        print("You lose!")
    elif computer_choice == 1:
        print(f"Computer choose: {paper}")
        print("You win!")
    else:
        print(f"Computer choose: {scissors}")
        print("Draw!")
else:
    print("You choose an invalid number. You lose!")