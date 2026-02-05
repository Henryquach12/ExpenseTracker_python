import Logic
from datetime import date
import calendar
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
        if month is not None:
            month = month[0]
        total = self.logic.calcSum(month)
        if total is None:
            print(f"No record found for month {month}")
        elif month is not None:
            month_name = calendar.month_name[month]
            print(f"Total expenses for {month_name}: ${total}")
        else:
            print(f"Total expenses: ${total}")

    def deleteExpense(self, id=id):
        self.logic.deleteRow(id)
        print("Expense deleted successfully")


    

        

