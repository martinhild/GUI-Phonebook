
class Person:
    """
    Person mit Name, Telefonnummer und eindeutiger ID.
    """
    _id_counter = 0

    def __init__(self, name: str = "", phone_number: str = ""):
        Person._id_counter += 1
        self.id = Person._id_counter
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.name} - {self.phone_number}"

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class Contacts:
    """
    Liste von Person-Objekten. Methoden zum Hinzufügen,
    Entfernen und Suchen von Kontakten.
    """
    def __init__(self, contacts: list[Person] = None):
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def add_contact(self, name, number):
        new_person = Person(name, number)
        self.contacts.append(new_person)

    def remove_contact(self, name):
        for contact in self.contacts:
            if name == contact.name:
                self.contacts.remove(contact)
                return True
        return False

    def search_by_name(self, name: str):
        result = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        return result

    def __str__(self):
        if not self.contacts:
            return "Keine Kontakte vorhanden."
        return "\n".join(str(contact) for contact in self.contacts)

