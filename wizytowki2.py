from faker import Faker
fake = Faker("pl_PL")

class BaseContact():                                                    #def klasy BaseContact
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}, {self.email}"     
    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])
    @property
    def contact_number(self):
        return self.phone
    def contact(self):
        return f"Wybieram numer: {self.contact_number} i dzwonię do {self.first_name} {self.last_name}"
