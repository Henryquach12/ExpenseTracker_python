import random
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("-----Python Number Guessing Game!-----")
print(f"Please guess a number between {lowest_number}-{highest_number}")
while is_running:
    guess = input("Enter your number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        pass
        if guess < lowest_number or guess > highest_number:
            print("Your number is out of range!")
            print(f"Please guess a number between {lowest_number}-{highest_number}")
            print()
        elif guess < answer:
            print("Your number is too low!")
            print()
        elif guess > answer: 
            print("Your number is too high!")
            print()
        else:
            print("Your number is correct!")
            print()
            break
    else: 
        print("Invalid!")
        print(f"Please guess a number between {lowest_number}-{highest_number}")
print()
print("------------RESULT!------------")
print(f"The correct number is {answer}")
print(f"You have guessed {guesses} times")
print("Good job!")     