import Repository
from datetime import date

class expenseTracker:
    def __init__(self):
        self.repo = Repository.expenseRepo()
    #Write new expense to CSV file
    def newExpense(self, note, amount):
        today = date.today().isoformat()
        ID = self.repo.takeIndex()
        data = [ID, today, note, amount]
        self.repo.insert(data)


        

