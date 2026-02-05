import os
import csv

# Main logic of program
class expenseLogic:
    def __init__(self, file_name="trackerFile.csv"):
        self.file_name = file_name
        self.checkFile()

    # Check if CSV file does exist
    def checkFile(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w', newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID','Date','Description','Amount'])
                
    # Create unique ID for each input
    def takeIndex(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file) #ID counted, except header    

    # Insert new record into databse
    def insertData(self, data):
        with open(self.file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    # Show current database data
    def readData(self):
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for index, r in enumerate(reader):
                if index >= 1:
                    print(f"{r[0]:<4} {r[1]:<12} {r[2]:<15} ${r[3]:>7}")
                else:
                    print(f"{r[0]:<4} {r[1]:<12} {r[2]:<15} {r[3]:>7}")

    # Calculate total expense
    def calcSum(self, month):
        total = 0
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            if month is None:
                for row in reader:
                    total = total + int(row[3])
            else:
                for row in reader:
                        date = row[1]
                        _, months, _ = date.split('-')
                        if int(months) == month:
                            total = total + int(row[3])
                        else:
                            return None
            return total
    
    # Delete specific row according to ID
    def deleteRow(self, id):
        rows = []
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] != str(id):
                    if int(row[0]) > id:
                        row[0] = str(int(row[0])-1)
                    rows.append(row)
        with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)




