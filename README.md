# Expense Tracker (CSV)

## Overview
This project is a simple expense tracking application implemented in Python and the idea was provided by roadmap.sh (https://roadmap.sh/projects/expense-tracker). 
It takes input from commandlines (CLI) and stores expense records in a CSV file and provides basic CRUD-like functionality such as inserting, showing, deleting records, and calculating total expenses.

The purpose of this project is to practice:
- File handling with CSV
- Basic data processing
- Object-Oriented Programming (OOP) concepts in Python

---

## Features
- Automatically creates a CSV file if it does not exist
- Insert new expense records
- Display all stored expenses in a formatted table
- Delete an expense by its ID
- Calculate total expenses
- Calculate total expenses by month

---

## Example intput:
$ expense-tracker add --description "Lunch" --amount 20
- Expense added successfully (ID: 1)
  
$ expense-tracker add --description "Dinner" --amount 10
- Expense added successfully (ID: 2)
  
$ expense-tracker list
- ID  Date       Description  Amount
- 1   2024-08-06  Lunch        $20
- 2   2024-08-06  Dinner       $10

$ expense-tracker summary
- Total expenses: $30
  
$ expense-tracker delete --id 2
- Expense deleted successfully
  
$ expense-tracker summary
- Total expenses: $20
  
$ expense-tracker summary --month 8
-  Total expenses for August: $20

