import random
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1:  ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    
    2:  ("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    
    3:  ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),

    4:  ("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),
    
    5:  ("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),

    6:  ("┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘"),
}
dice = []
total = 0

number_of_dice = int(input("Enter the number of dice you want: "))

for die in range (number_of_dice):
    dice.append(random.randint(1,6))

#PRINT VERTICALLY 
for die in range(number_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

#PRINT HORIZONTALLY 
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print (f"total: {total}")
