import csv
from datetime import datetime
import os

file_name = "spending.csv"
def init_file():
    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Note"])
init_file()

class ExpenseTracker:
    def __init__(self, ex_amount, category, date, note=None):
        self.ex_amount = ex_amount
        self.category = category
        self.note = note
        self.date = date
    def add_expense(self):
        with open(file_name, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.date, self.ex_amount, self.category, self.note])

def show_expense():
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def running():
    while True:
        try:
            command = int(input("(1) add new expense (2) Show current expense (3) Finish tracking: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if command == 1:
            date = datetime.now().strftime("%d-%m-%Y")
            while True:
                try:
                    ex_amount = float(input(f"Please enter the amount of spending money in {date}: $"))
                    break
                except ValueError:
                    print("The amount must be a number! Please try again...")
            category = input("Please enter type of spending: ")
            new_note = input("Do you want to make a note (y/n): ").strip().lower()
            if new_note == "y" or new_note == "yes":
                note = input("Please leave your note here: ")
            else:
                note = None
            tracking = ExpenseTracker(ex_amount=ex_amount, note=note, category=category, date=date)
            tracking.add_expense()
        elif command == 2:
            show_expense()
        elif command == 3:
            print("good bye!")
            break
        else:
            print("Invalid choice! Try again...")
running()