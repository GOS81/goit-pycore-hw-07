from handler_command import add, change, show, all, input_error

contact_dictionary = []

@input_error
def parse_input(input_command):
    cmd, *arg = input_command.split()
    cmd = cmd.lower()
    contact_name = arg[0].capitalize() if len(arg) > 0 else None
    contact_phone = arg[1] if len(arg) > 1 else None
    if cmd == "hello":
        print("Чим я можу вам допомогти?")

    elif cmd == "help":
        print("Введіть одну з команд: hello, add, change, show, all, exit or close")
    
    elif cmd == "close" or cmd == "exit":
        print("Ви залишаєте додаток! \nГарного дня!")
        return exit()

    elif cmd == "add":
        add(contact_name, contact_phone, contact_dictionary)

    elif cmd == "change":
        if contact_name != None and contact_phone != None:
            change(contact_name, contact_phone, contact_dictionary)
        else:
            raise ValueError ("Give me name and phone please")
    
    elif cmd == "show":
        show(contact_name, contact_dictionary)
    
    elif cmd == "all":
        all(contact_dictionary)

    else:
        raise ValueError("Command not found! Try one of these: hello, add, change, show, all, exit or close")

    return contact_dictionary