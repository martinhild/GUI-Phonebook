from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLineEdit,
                             QLabel, QListWidget, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
from classes.contact_management import Contacts, Person


class ContactApp(QWidget):
    """
    ContactApp erbt von QWidget und ist eine GUI für die Kontaktverwaltung.
    Arbeitet mit phonebook, von der importierten Klasse Contacts.
    """
    def __init__(self, phonebook: Contacts):
        super().__init__()

        # GUI bekommt phonebook der Klasse Contacts
        self.phonebook = phonebook

        # Fenster Setup
        self.setWindowTitle('Kontaktverwaltung')
        self.setGeometry(100, 100, 400, 400)

        # Erzeuge ein QVBoxLayout namens main_layout
        self.main_layout = QVBoxLayout()
        # Setze main_layout als Layout für das ContactApp-Fenster
        self.setLayout(self.main_layout)

        # Eingabefelder (Diese Widgets sind Kinder des Hauptfensters)
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Name eingeben...")
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Telefonnummer eingeben...")

        # Buttons (Ebenfalls Erben des Hauptfensters)
        self.show_button = QPushButton('Alle anzeigen', self)
        self.add_button = QPushButton('Kontakt hinzufügen', self)
        self.search_button = QPushButton('Kontakt suchen', self)
        self.delete_button = QPushButton('Kontakt löschen', self)

        # Listen-Widget für Anzeige der Kontakte (wieder Kind vom Hauptfenster)
        self.contact_list = QListWidget(self)

        # Layout anpassen: Alle Widgets hinzufügen
        self.main_layout.addWidget(self.name_input)
        self.main_layout.addWidget(self.phone_input)
        self.main_layout.addWidget(self.show_button)
        self.main_layout.addWidget(self.add_button)
        self.main_layout.addWidget(self.search_button)
        self.main_layout.addWidget(self.delete_button)
        self.main_layout.addWidget(self.contact_list)

        # Buttons mit Methoden verbinden
        self.show_button.clicked.connect(self.update_contact_list)
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)
        self.delete_button.clicked.connect(self.delete_contact)

    def update_contact_list(self):
        """
        # Hilfsmethode um nach Aktionen den Aktuellen inhalt von phonebook in
        contact_list (das Listen-Widget) zu laden.
        """
        self.contact_list.clear()  # Bisheriges löschen
        for contact in self.phonebook.contacts:  # phonebook lesen
            self.contact_list.addItem(str(contact))  # contact_list neu füllen

    def add_contact(self):
        """
        Speichert Inhalte der Eingabefelder in phonebook und aktualisiert Anzeige.
        """
        name = self.name_input.text()  # .text(): Methode von QLineEdit. Liest Eingabefeld.
        phone = self.phone_input.text()
        if name and phone:
            self.phonebook.add_contact(name, phone)  # speichern
            self.update_contact_list()  # Anzeige updaten
            self.name_input.clear()  # Eingabefelder wieder leeren
            self.phone_input.clear()

    def search_contact(self):
        """
        Leert die Anzeige, durchsucht phonebook und fügt Suchergebnisse der Anzeige hinzu.
        """
        name = self.name_input.text()  # Methode von QLineEdit
        if name:
            results = self.phonebook.search_by_name(name)
            self.contact_list.clear()
            for contact in results:
                self.contact_list.addItem(str(contact))  # contact_list mit Ergebnissen füllen


    def delete_contact(self):
        """
        Löscht den ausgewählten Kontakt aus phonebook und aus der Anzeige.
        """
        contact = self.contact_list.currentItem()  # Methode von QListWidget: Markiertes Listenelement
        if contact:  # Absicherung, dass wirklich ein Kontakt ausgewählt ist
            name = contact.text().split(' - ')[0]  # Extrahiert name aus "Name - Telefonnummer"

            # Best#tigung für Löschung
            question = QMessageBox.question(self, "Bestätigung",f"Kontakt {name} wirklich löschen?",
            QMessageBox.Yes | QMessageBox.No,  # Optionen
            QMessageBox.No)  # Standardantwort

            if question == QMessageBox.Yes:
                self.phonebook.remove_contact(name)
                self.update_contact_list()


