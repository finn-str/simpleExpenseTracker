import datetime
import os
import csv

# Define variables
now = datetime.datetime.now()
# Date and time in the following format "2023-09-26 15:47"
formatted = now.strftime("%Y-%m-%d")
path = r'D:/Documents/GitHub/simpleExpenseTracker/'
filename = "expenses.csv"
csv_delimiter = ";"

if os.path.exists(path + filename):
    with open(path + filename, 'r') as file:
        lines = file.readlines()
        account = int(''.join([char for char in lines[0] if char.isdigit()])) # extract number out of string
    print(account)
else:
    account = int(input("What is your current account balance: "))
    data = [
        ["Account Balance:", account],
        ["Type", "Amount", "Reason", "Date"],
        ]
    with open(path + filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csv_delimiter)
        writer.writerows(data)
    print("CSV file has been created!")


def write_balance(new_balance):
    with open(path + filename, 'r') as file:
        lines = file.readlines()
    lines[0] = f"Account Balance:;{new_balance}\n"
    with open(path + filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csv_delimiter)
        # Here, we convert each line into a list of strings by splitting them at semicolons before writing them.
        writer.writerows([line.strip().split(';') for line in lines])


def current_balance():
    message = "Your account balance is now: " + str(account) + "€." + " | " + formatted
    print(message)


def new_expense(amount, purpose):
    global formatted
    global account
    account = account - amount
    write_balance(account)
    new_data = ["Expense", amount, purpose, formatted]
    with open(path + filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=csv_delimiter)
        writer.writerow(new_data)
    message = "You spent " + str(amount) + '€ on "' + purpose + '".' + " | " + formatted
    print(message)


def new_income(amount, source):
    global formatted
    global account
    account = account + amount
    write_balance(account)
    new_data = ["Income", str(amount), source, formatted]
    with open(path + filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=csv_delimiter)  # Here, the delimiter is set
        writer.writerow(new_data)
    message = "You received " + str(amount) + '€ from "' + source + '".' + " | " + formatted
    print(message)


while True:
    print("\nSelect from 1 to 3:\n")
    print("1: New Expense")
    print("2: New Income")
    print("3: Check Account Balance")
    user_action = int(input("\nWhich action do you want to perform: "))
    if user_action == 1:
        print()
        amount = int(input("Amount: "))
        purpose = input("Purpose: ")
        new_expense(amount, purpose)
    elif user_action == 2:
        print()
        amount = int(input("Amount: "))
        source = input("Source: ")
        new_income(amount, source)
    elif user_action == 3:
        print()
        current_balance()
    else:
        print("\nPlease enter a valid input.")
