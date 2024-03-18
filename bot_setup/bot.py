from classes import AddressBook, Record
from decorators import input_days_error,input_error
from notesbook import Notesbook
import pickle
import os

USER_FOLDER = os.path.expanduser("~")
NOTES_FOLDER = os.path.join(USER_FOLDER, "Notes")

def parse_input(user_input):
    """Function analyzes user input and splits the command and arguments"""
    if user_input == "":
        return '0'
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    """Function adds new contact with phone number or adds phone number to the existing contact"""
    name, phone = args
    if len(phone) < 10:
        return '\nKodi>> Phone number must consist of 10 digits'
    record = book.find(name.lower())
    if record is None:
        record = Record(name.lower())
        record.add_phone(phone)
        book.add_record(record)
        return "\nKodi>> Phone has been added to the contact"
    else:
        record.add_phone(phone)
        return "\nKodi>> Phone has been added to the contact"

@input_error  # add address function for bot
def add_address(args, book):
    """Function adds new contact with address or adds address to the existing contact"""
    name, street, house, city, postal_code = args
    full_address = f"{street} {house}, {city}, {postal_code}"  # the complete address
    record = book.find(name.lower())
    if record is None:
        record = Record(name.lower())
        record.add_address(full_address)
        book.add_record(record)
        return "\nKodi>> Address added successfully to the contact."
    else:
        record.add_address(full_address)
        return "\nKodi>> Address added successfully to the contact."

@input_error # show address when name is given
def show_address(args, book):
    """Function checks if a contact is in contacts and prints contact's address"""
    if len (args) == 0:
        return "\nKodi>> You didn't tell me your name. Please enter show-address <name>."
    name = args[0]
    record = book.find(name.lower())
    if record is None:
        raise KeyError #("No record found with this name")
    return f"\nKodi>> Address for contact {name}: {', '.join(record.addresses)}" if record.addresses else "\nKodi>> No address found for this contact."

@input_error
def change_contact(args, book):
    """Function checks if a contact is in contacts and substitutes the phone number"""
    name, old_phone, new_phone = args
    record = book.find(name.lower())
    return record.edit_phone(old_phone, new_phone)

@input_error
def show_phone(args, book):
    """Function checks if a contact is in contacts and prints contact's phone number(s)"""
    name = args[0]
    record = book.find(name.lower())
    if record is None:
        raise KeyError
    return record.show_phones()

@input_error
def add_birthday(args, book):
    """Function adds new contact with birthday or adds birthday to the existing contact"""
    name, birthday = args
    record = book.find(name.lower())
    if record is None:
        record = Record(name.lower())
        record.add_birthday(birthday)
        book.add_record(record)
        return "\nKodi>> Birthday has been successfully added"
    else:
        record.add_birthday(birthday)
        return "\nKodi>> Birthday has been successfully added"

@input_error
def show_birthday(args, book):
    """Function checks if a contact is in contacts and prints contact's birthday"""
    if len (args) == 0:
        raise ValueError
    name = args[0]
    record = book.find(name.lower())
    if record is None:
        raise KeyError
    return record.show_birthday()

@input_days_error
def show_week_birthday(args,book):
    """
    Function checks contacts' birthdays and 
    prints people to congratulate during the following # days
    """
    count = int(args[0])
    return book.get_birthdays_per_week(count)

def show_all(book):
    """Function prints all contacts from the book"""
    return book.__str__() # show address in str by AddressBook

@input_error
def add_email(args, book):
    """Function adds new contact with email or adds email to the existing contact"""
    name, email = args
    record = book.find(name.lower())
    if record is None:
        record = Record(name.lower())
        record.add_email(email)
        book.add_record(record)
        return "\nKodi>> Email has been successfully added"
    else:
        record.add_email(email)
        return "\nKodi>> Email has been successfully added"

@input_error
def show_email(args, book):
    """Function checks if a contact is in contacts and prints contact's email"""
    if len (args) == 0:
        return "\nKodi>> You didn't tell me your name. Please enter show-email <name>."
    name = args[0]
    record = book.find(name.lower())
    if record is None:
        raise KeyError
    elif record:
        return record.show_email() if record.email else "\nKodi>> No email found for this contact."

@input_error
def delete_record(args, book):
    """Function checks if a contact is in contacts and deletes it from the book"""
    if len (args) == 0:
        return "\nKodi>> Please enter <contact name>."
    name = args[0]
    record = book.find(name.lower())
    if record is None:
        raise KeyError
    elif record:
        book.delete(name)
        return "\nKodi>> Cool! Record has been successfully deleted."

@input_error
def new_note(args, notes):
    """Function adds a new note"""
    note = ' '.join(args)
    return notes.add_note(note)

@input_error
def edit_note(args, notes):
    """Function searches for notes and edits an existing note"""
    id, *note = args
    return notes.edit_note(id, ' '.join(note))

@input_error
def show_note(args, notes):
    """Function searches for notes"""
    note = ' '.join(args)
    return notes.find_note(note)

@input_error
def delete_note(args, notes):
    """Function searches for a note and deletes the existing note"""
    id = args[0]
    return notes.delete_note(id)

def all_notes(notes):
    """Function prints all notes in the notebook"""
    return notes

@input_error
def add_tags(args, notes):
    """Function adds a tag to the existing note"""
    id, *tags = args
    if len(tags) == 0:
        return '\nKodi>> Ooops... I wait for some tags'
    return notes.add_tags(id, tags)

@input_error    
def delete_tag(args, notes):
    """Function deletes a tag from the existing note"""
    id, tag = args
    if len(tag) == 0:
        return '\nKodi>> Ooops... I wait for some tag'
    return notes.delete_tag(id, tag)

@input_error
def save_all(args, book, notes):
    """Function saves both contacts and notes"""
    save_contacts(book)
    save_notes(notes)
    return "\nKodi>> Contacts and notes saved successfully."


def find_note_by_tags(args, notes):
    """Function searches and prints notes by a provided tag"""
    if len(args) == 0:
        return '\nKodi>> Ooops... I wait for some tags'
    return notes.find_note_by_tags(args)

def save_contacts(book):
    """Function saves the contact book"""
    with open("contacts.pkl", "wb") as f:
        pickle.dump(book.data, f)
    print("\nKodi>> Contacts saved successfully.")

def save_notes(notes):
    """Function saves the notes"""
    notes.save_notes()
    print("\nKodi>> Notes saved successfully.")

def load_notes():
    """Function loads the notes"""
    notes_path = os.path.join(NOTES_FOLDER, "notes.pkl")
    if os.path.exists(notes_path):
        return Notesbook(notes_path)
    else:
        return Notesbook()

def main():
    notes_path = os.path.join(NOTES_FOLDER, "notes.pkl")
    notes = load_notes()
    book = AddressBook({'path': "contacts.pkl"})
    book.load()
    notes = Notesbook(notes_path)
    print("\nHi! I'm a your's personal assistant bot. My name is Kodi!\nType 'help' to see the list of commands.\n")
    while True:
        user_input = input("\nKodi>> Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye"]:
            if len(book)!=0:
                print("\nKodi>> Do you want to save your data?")
                answer = input("Yes/No\nYou: ")
                if answer.lower()=="yes":
                    save_contacts(book)
            save_notes_command(notes)
            print("\nKodi>> Good bye! See you soon!")
            break
        elif command == "hello":
            print("\nHow can I help you?")
        elif command == "help":
            print("{:3}{:<15}{:<}".format("", "add", "to add contact name and phone number"))
            print("{:3}{:<15}{:<}".format("", "phone", "to show contact phone number"))
            print("{:3}{:<15}{:<}".format("", "change", "to change contact phone number"))
            print("{:3}{:<15}{:<}".format("", "add-address", "to add contact address"))
            print("{:3}{:<15}{:<}".format("", "show-address", "to show contact address"))
            print("{:3}{:<15}{:<}".format("", "add-birthday", "to add contact birthday"))
            print("{:3}{:<15}{:<}".format("", "show-birthday", "to show contact birthday"))
            print("{:3}{:<15}{:<}".format("", "birthdays", "to show contacts' birthdays in # days"))
            print("{:3}{:<15}{:<}".format("", "add-email", "to add contact email"))
            print("{:3}{:<15}{:<}".format("", "show-email", "to show contact email"))
            print("{:3}{:<15}{:<}".format("", "delete", "to delete contact"))
            print("{:3}{:<15}{:<}".format("", "new-note", "to create a new note"))
            print("{:3}{:<15}{:<}".format("", "edit-note", "to edit an existing note"))
            print("{:3}{:<15}{:<}".format("", "show-note", "to show an existing note"))
            print("{:3}{:<15}{:<}".format("", "all-notes", "to show all the notebook"))
            print("{:3}{:<15}{:<}".format("", "delete-note", "to delete an existing note"))
            print("{:3}{:<15}{:<}".format("", "add-tags", "to add a tag to notes"))
            print("{:3}{:<15}{:<}".format("", "find-note", "to search in notes by tags"))
            print("{:3}{:<15}{:<}".format("", "delete-tag", "to delete an existing tag"))
            print("{:3}{:<15}{:<}".format("", "all", "to show all the address book"))
            print("{:3}{:<15}{:<}".format("", "save", "to save the address book"))
            print("{:3}{:<15}{:<}".format("", "exit/close/bye", "to close the address book"))
        elif command == "add":
            print(add_contact(args, book))
        elif command == "add-address":
            print (add_address (args, book)) # command for adding the address
        elif command == "show-address":
            print (show_address (args, book)) # command for showing
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "show-email":
            print (show_email (args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_week_birthday(args,book))
        elif command == "all":
            print(show_all(book))
        elif command == "delete":
            print(delete_record(args, book))
        elif command == "new-note":
            print(new_note(args, notes))
        elif command == "all-notes":
            print(all_notes(notes))
        elif command == "edit-note":
            print(edit_note(args, notes))
        elif command == "show-note":
            print(show_note(args, notes))
        elif command == "delete-note":
            print(delete_note(args, notes))
        elif command == "add-tags":
            print(add_tags(args, notes))
        elif command == "delete-tag":
            print(delete_tag(args, notes))
        elif command == "find-note":
            print(find_note_by_tags(args, notes))
        elif command == "save":
            save_contacts(book)
        elif command == "save-notes":
            save_notes(notes)
        elif command == "save-all":
            print(save_all(args, book, notes))
        else:
            print("\nKodi>> I don't know such command. Please, type 'help' to see the list of commands.")

if __name__ == "__main__":
    main()