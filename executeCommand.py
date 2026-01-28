import os
import csv
from datetime import date
class expenseTracker:
    def __init__(self, fileName="trackerFile.csv"):
        self.fileName = fileName
        self.checkFile()
    #Check if CSV file does exist
    def checkFile(self):
        if not os.path.exists(self.fileName):
            with open(self.fileName, 'w', newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID','Date','Description','Amount'])
    #Create unique ID 
    def takeIndex(self):
        with open(self.fileName, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)-1 #ID counted, except header  
    #Write new expense to CSV file
    def newExpense(self, data, amount):
        today = date.today().isoformat()
        ID = self.takeIndex()
        with open(self.fileName, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([ID, today, data, amount])


        

