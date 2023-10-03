import datetime
import os
import csv

# Variablen definieren
now = datetime.datetime.now()
# Datum und Uhrzeit im folgenden Format "2023-09-26 15:47"
formated = now.strftime("%Y-%m-%d")
pfad = r'D:/Dokumente/GitHub/simpleExpenseTracker/'
filename = "ausgaben.csv"
csvdelimiter = ";"

if os.path.exists(pfad + filename):
    with open(pfad + filename, 'r') as file:
        lines = file.readlines()
        konto = int(''.join([char for char in lines[0] if char.isdigit()])) # extract number out of String
    print(konto)
else:
    konto = int(input("Was ist ihr aktueller Kontostand: "))
    data = [
        ["Kontostand:", konto],
        ["Type", "Amount", "Reason", "Date"],
        ]
    with open(pfad + filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csvdelimiter)
        writer.writerows(data)
    print("CSV file has been created!")


def writebalance(newbalance):
    with open(pfad + filename, 'r') as file:
        lines = file.readlines()
    lines[0] = f"Kontostand:;{newbalance}\n"
    with open(pfad + filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csvdelimiter)
        # Hier konvertieren wir jede Zeile in eine Liste von Zeichenketten,
        # indem wir sie bei den Semikolons teilen, bevor wir sie schreiben.
        writer.writerows([line.strip().split(';') for line in lines])


def currentBalance():
    message = "Ihr Kontostand liegt nun bei: " + str(konto) + "€." + " | " + formated
    print(message)


def newExpense(betrag, zweck):
    global formated
    global konto
    konto = konto - betrag
    writebalance(konto)
    new_data = ["Expense", betrag, zweck, formated]
    with open(pfad + filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=csvdelimiter)
        writer.writerow(new_data)
    message = "Sie haben " + str(betrag) + '€ für "' + zweck + '" ausgegeben.' + " | " + formated
    print(message)


def newIncome(betrag, quelle):
    global formated
    global konto
    konto = konto + betrag
    writebalance(konto)
    new_data = ["Income", str(betrag), quelle, formated]
    with open(pfad + filename, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=csvdelimiter)  # Hier wird der Delimiter gesetzt
        writer.writerow(new_data)
    message = "Sie haben " + str(betrag) + '€ durch "' + quelle + '" erhalten.' + " | " + formated
    print(message)


while True:
    print("\nWählen sie von 1 bis 3:\n")
    print("1: Neue Ausgabe")
    print("2: Neues Einkommen")
    print("3: Kontostand Einsehen")
    useraction = int(input("\nWelche Aktion wollen Sie durchführen: "))
    if (useraction == 1):
        print()
        amount = int(input("Betrag: "))
        purpose = input("Zweck: ")
        newExpense(amount, purpose)
    elif (useraction == 2):
        print()
        amount = int(input("Betrag: "))
        source = input("Quelle: ")
        newIncome(amount, source)
    elif (useraction == 3):
        print()
        currentBalance()
    else:
        print("\nBitte geben sie eine gültige Eingabe an.")
