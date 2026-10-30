import sys
from PyQt5.QtWidgets import QApplication
from classes.contact_management import Contacts  # Meine Klasse Contacts
from gui.contact_gui import ContactApp  # Meine GUI

def main():
    # Telefonbuch initialisieren
    phonebook = Contacts()

    # Standardkontakte zum Start der Anwendung für ein sehr simples MVP
    phonebook.add_contact("Jon Doe", "01431 84253")
    phonebook.add_contact("Max Mustermann", "01431 84253")
    phonebook.add_contact("Obi One", "08657 18657")
    phonebook.add_contact("Obi Two", "09875 49827")
    phonebook.add_contact("Monty Python", "02375 41127")

    # QApplication initialisieren
    app = QApplication(sys.argv)

    # Meine GUI ContactApp mit Parameter phonebook starten und anzeigen
    window = ContactApp(phonebook)
    window.show()

    # PyQT-Ereignisschleife starten
    app.exec()

if __name__ == "__main__":
    main()
