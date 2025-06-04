import sys
from PyQt5.QtWidgets import QApplication
from classes.contact_management import Contacts  # Meine Klasse Contacts
from gui.contact_gui import ContactApp  # Meine GUI

def main():
    # Telefonbuch initialisieren
    phonebook = Contacts()

    # Standardkontakte zum Start der Anwendung
    phonebook.add_contact("Joachim Schiller", "01472 548545")
    phonebook.add_contact("Beathe Kramp", "01431 245315")
    phonebook.add_contact("Rudi Knaller", "02433 12251")
    phonebook.add_contact("Jon Doe", "01431 84253")
    phonebook.add_contact("Sarah Maier", "08657 18657")
    phonebook.add_contact("Sascha Müller", "09875 49827")

    # QApplication initialisieren
    app = QApplication(sys.argv)

    # Meine GUI ContactApp mit Parameter phonebook starten und anzeigen
    window = ContactApp(phonebook)
    window.show()

    # PyQT-Ereignisschleife starten
    app.exec()

if __name__ == "__main__":
    main()
