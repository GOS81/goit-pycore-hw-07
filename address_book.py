from collections import UserDict
from datetime import datetime, timedelta, date

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Phone number must be a string.")
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits.")
        if len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Birthday must be a string in format DD.MM.YYYY")
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        if parsed_date > date.today():
            raise ValueError("Birthday can't be in the future.")
        super().__init__(parsed_date)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [phn for phn in self.phones if phn.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phn in enumerate(self.phones):
            if phn.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        for phn in self.phones:
            if phn.value == phone:
                return phn
        return None
    
    def add_birthday(self, contact_birthday):
        self.birthday = Birthday(contact_birthday)

    def __str__(self):
        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(phn.value for phn in self.phones)}{birthday_str}"


class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = date.today()
        end_date = today + timedelta(days=7)
        result = []

        for record in self.data.values():
            if not record.birthday:
                continue
            birthday_this_year = record.birthday.value.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if today <= birthday_this_year <= end_date:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)
                result.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })
        return result



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("14.07.1990")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9176543210")
jane_record.add_birthday("15.07.2020")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")
# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
# book.delete("Jane")
# for name, record in book.data.items():
#     print(record)

print("\nХто має день народження наступного тижня:")
for item in book.get_upcoming_birthdays():
    print(item)