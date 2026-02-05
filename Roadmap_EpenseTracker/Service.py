import Logic
from datetime import date

# Handle commands and call logic 
class serviceOperation:
    def __init__(self):
        self.logic = Logic.expenseLogic()

    # Write new expense to CSV file
    def newExpense(self, note, amount):
        today = date.today().isoformat()
        ID = self.logic.takeIndex()
        data = [ID, today, note.lower(), amount]
        self.logic.insertData(data)
        print(f"Expense added successfully (ID:{ID})")

    # Show expense record
    def showExpense(self):
        self.logic.readData()

    # Return total expense 
    def sumExpense(self, month=None):
        month = month[0]
        total = self.logic.calcSum(month)
        print(f"Total expenses: ${total}")

    def deleteExpense(self, id=id):
        pass


    

        

