import mysql.connector
from tabulate import tabulate
class dataBase:
    #Create database
    def __init__(self):
        self.dataBase = mysql.connector.connect(
            host="localhost",
            user="root",
            password="HH@oqu@ch1209@",
            database="mydatabase"
        )
        #Preparing a cursor object
        self.cursorObject = self.dataBase.cursor()
        #Creating tracking table 
        self.spendingRecord = """CREATE TABLE IF NOT EXISTS SPENDING (
                            expense_id INT AUTO_INCREMENT PRIMARY KEY,
                            date DATE NOT NULL,
                            amount DECIMAL(10,2) NOT NULL,
                            category VARCHAR(50) NOT NULL,
                            note TEXT NULL
                            )"""
        self.cursorObject.execute(self.spendingRecord)

    #New record function
    def newRecord(self, data):
        date, amount, category, note = data 
        sql = "INSERT INTO SPENDING (date, amount, category, note) VALUES (%s, %s, %s, %s)"
        value = (date, amount, category, note)
        self.cursorObject.execute(sql, value)
        self.dataBase.commit()
        print("_______________________________________")
        print("New record has been added successfully!")
        print()

    #display function
    def displayRecord(self):
        query = """SELECT expense_id, date, CONCAT('$', FORMAT(amount,2)) AS amount, category, IFNULL(note,'-') FROM SPENDING"""
        self.cursorObject.execute(query)
        records = self.cursorObject.fetchall()
        if not records:
            print("No records found!")
            return
        print(tabulate(records, headers=["ID", "Date", "Amount", "Category", "Note"], tablefmt="grid"))

