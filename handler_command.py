
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Oops, an error occurred: {e}")
    return inner


@input_error
def add(name, phone, dict):
    if name != None and phone != None:
        dict.append(
                {"name": name, #.capitalize(),
                 "phone": phone
                }
            )
        print(f"Контакт {name} додано!")
        return dict
    else:
        raise ValueError("Give me name and phone please")


@input_error
def change(name, new_phone, dict):
    for contact in dict:
        if contact["name"] == name:
            contact["phone"] = new_phone
            print(f"Номер телефона контакта {name} змінено на {new_phone}")
            return dict
        else:
            raise KeyError ("Contact not found")


@input_error
def show(name, dict):
    for contact in dict:
        if contact["name"] == name:
            print(contact["name"], contact["phone"])
        else:
            raise KeyError ("Contact not found")


@input_error
def all(dict):
    if dict:
        print(dict)
    else:
        raise ValueError ("No contacts added")
