from classes import AddressBook, Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return 'No record found with this name'
        except TypeError:
            return 'Please provide full info'
        except AttributeError:
            return 'Contact not found'

    return inner


@input_error
def add_contact(args, book):
    name, phone = args
    if len(phone) != 10:
        return 'Must be 10 numbers'
    record = Record(name)
    record.add_phone(phone)
    return book.add_record(record)

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    return record.edit_phone(old_phone, new_phone)

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    return record.show_phones()

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    return record.add_birthday(birthday)

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    return record.show_birthday()

def show_week_birthday(book):
    return book.get_birthdays_per_week()


def show_all(book):
    return book.__str__()


def main():
    # contacts = {}
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)


        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_week_birthday(book))
        elif command == "all":
            print(show_all(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()