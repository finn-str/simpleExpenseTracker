import datetime
import os

#Variablen definieren
jetzt = datetime.datetime.now()
formatiert = jetzt.strftime("%Y-%m-%d %H:%M") # Datum und Uhrzeit im folgenden Format "2023-09-26 15:47"
pfad = "/workspaces/python-beginner-projects/projects/expense_tracker/"
filename = "ausgaben.txt"

if os.path.exists("/workspaces/python-beginner-projects/projects/expense_tracker/ausgaben.txt"):
    with open(pfad + filename, 'r') as datei:
        erste_zeile = datei.readline()
        print(erste_zeile.strip())  # strip() entfernt führende und abschließende Leerzeichen, einschließlich Zeilenumbrüchen
        konto = int(erste_zeile.strip())
else:
    konto = int(input("Was ist ihr aktueller Kontostand: "))
    print("Ihr aktueller Kontostand wurde auf " + str(konto) + " geupdatet.")
    with open(pfad + filename, 'w') as datei:
            datei.writelines(str(konto) + "\n")

def schreibeKonto(kontoneu):
    erstezeile = str(kontoneu)
    # Die Datei öffnen und den Inhalt einlesen
    with open(pfad + filename, 'r') as datei:
        zeilen = datei.readlines()
        # Änderungen an der ersten Zeile vornehmen
        zeilen[0] = str(erstezeile) + "\n"
        # Den aktualisierten Inhalt zurück in die Datei schreiben
    with open(pfad + filename, 'w') as datei:
            datei.writelines(zeilen)

def kontostand():
    message = "Ihr Kontostand liegt nun bei " + str(konto) + "€." + " | " + formatiert
    print(message)
    return message

def neueAusgabe(betrag, zweck):
    global konto
    konto = konto - betrag
    schreibeKonto(konto)
    message = "Sie haben " + str(betrag) + '€ für "' + zweck + '" ausgegeben.' + " | " + formatiert
    print(message)
    return message

def neuesEinkommen(betrag, quelle):
    global formatiert
    global konto
    konto = konto + betrag
    schreibeKonto(konto)
    message = "Sie haben " + str(betrag) + '€ durch "' + quelle + '" erhalten.' + " | " + formatiert
    print(message)
    return message

while True:
    print("\nWählen sie von 1 bis 10:\n")
    print("1: Neue Ausgabe")
    print("2: Neues Einkommen")
    print("3: Kontostand Einsehen")
    eingabe = int(input("\nWelche Aktion wollen Sie durchführen: "))
    if (eingabe == 1):
        print()
        betrag = int(input("Betrag: "))
        zweck = input("Zweck: ")
        with open(pfad + filename, 'a') as datei:
            datei.write(neueAusgabe(betrag, zweck) + "\n")
    elif (eingabe == 2):
        print()
        betrag = int(input("Betrag: "))
        quelle = input("Quelle: ")
        with open(pfad + filename, 'a') as datei:
            datei.write(neuesEinkommen(betrag, quelle) + "\n")
    elif (eingabe == 3):
        print()
        with open(pfad + filename, 'a') as datei:
            datei.write(kontostand() + "\n")
    else:
        print("\nBitte geben sie eine gültige Eingabe an.")
