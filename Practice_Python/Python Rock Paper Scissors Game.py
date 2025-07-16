import random
options = ("rock", "paper", "scissors")
running = True
print("--------Welcome to rock, paper, scissors game--------")
while running:
    machine = random.choice(options)
    human = None
    while human not in options:
        human = input("Enter a choice(rock, paper, scissors): ").lower()
    if human == machine:
        print("It's a tie!")
        print()
    elif human == "rock" and machine == "scissors":
        print("You are a winner!")
    elif human == "rock" and machine == "paper":
        print("Machine are a winner!")
    elif human == "paper" and machine == "rock":
        print("Human are a winner!")
    elif human == "paper" and machine == "scissors":
        print("Machine are a winner!")
    elif human == "scissors" and machine == "paper":
        print("Human are a winner!")
    else:
        print("Machine are a winner!")
    answer = input("Do you want to play again? (y/n): ").lower()
    if not answer == "y":
        running = False
print("Thanks for your playing!")


    
    
    