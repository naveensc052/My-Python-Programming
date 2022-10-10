import random
my_choice = input("WELCOME___TO___THE___GAME\nEnter your choice(stone,paper,scissor):")
a = ["stone", "paper", "scissor"]
computer_choice = random.choice(a)

if my_choice == "stone":
    print(f"Computer choise is {computer_choice}\nYour choice is {my_choice}")
    if computer_choice == "stone":
        print("Game Draw")
    elif computer_choice == "paper":
        print("You Lose")
    else:
        print("You won")
elif my_choice == "paper":
    print(f"Computer choise is {computer_choice}\nYour choice is {my_choice}")
    if computer_choice == "stone":
        print("You won")
    elif computer_choice == "paper":
        print("Game Draw")
    else:
        print("You Lose")
elif my_choice == "scissor":
    print(f"Computer choise is {computer_choice}\nYour choice is {my_choice}")
    if computer_choice == "paper":
        print("You Won")
    elif computer_choice == "stone":
        print("You Lose")
    else:
        print("Game Draw")
else:
    print("Invalid input!")