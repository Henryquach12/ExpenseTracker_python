from datetime import datetime
from Database import dataBase

#Main function
class spendingTracker():
    #Execute choosen function
    def trigger(self):
        db = dataBase()
        while True:
            try:
                command = int(input("(1) add new expense (2) Show current expense (3) Finish tracking: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
            if command == 1:
                data = self.newExpense()
                db.newRecord(data)
            elif command == 2:
                db.displayRecord()
            elif command == 3:
                print("good bye!")
                break
            else:
                print("Invalid choice! Try again...")

    #Add new expense
    def newExpense(self):
        date = datetime.now().strftime("%Y-%m-%d")
        while True:
            try:
                amount = float(input(f"Please enter the amount of spending money in {date}: $"))
                break
            except ValueError:
                print("The amount must be a number! Please try again...")
        category = input("Please enter type of spending: ")
        while not category.replace(" ","").isalpha():
            print("Category must contain letters only! Please try again...")
            category = input("Please enter type of spending: ")
        new_note = input("Do you want to make a note (y/n): ").strip().lower()
        if new_note == "y" or new_note == "yes":
            note = input("Please leave your note here: ")
        else:
            note = None
        return (date, amount, category, note)

tracker = spendingTracker()
tracker.trigger()