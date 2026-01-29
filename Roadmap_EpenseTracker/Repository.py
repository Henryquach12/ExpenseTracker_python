import os
import csv
class expenseRepo:
    def __init__(self, file_name="trackerFile.csv"):
        self.file_name = file_name
        self.checkFile()
    #Check if CSV file does exist
    def checkFile(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w', newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID','Date','Description','Amount'])
    #Create unique ID 
    def takeIndex(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file) #ID counted, except header    

    #Insert new record
    def insert(self, data):
            with open(self.file_name, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(data)
