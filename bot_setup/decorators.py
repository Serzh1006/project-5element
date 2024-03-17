def input_days_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "The quantity must be a digit and an integer!"
        except IndexError:
            return "Please provide <count days> in format birthdays <count days>"
    return inner


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_email" or func.__name__ == "show_email":
                return "Please provide contact name and email"
            elif func.__name__ == "add_address" or func.__name__ == "show_address":
                return "Enter contact name and address in format <name> <street> <house> <city> <postal_code>."
            elif func.__name__ == "add_birthday" or func.__name__ == "show_birthday":
                return "Please provide contact name and birthday in format DD.MM.YYYY." 
            elif func.__name__ == "new_note":
                return "Expected command new-note Text."
            elif func.__name__ == "edit_note":
                return "Expected command edit-note ID New-text."
            elif func.__name__ == "delete_note":
                return "Expected command delete-note ID."
            elif func.__name__ == "show_note":
                return "Expected command show-note KeyWords."  
            elif func.__name__ == "delete_tag":
                return "Expected command delete-tag ID Tag(one tag)."
            elif func.__name__ == "add_tags":
                return "Expected command add-tags ID Tags."
            elif func.__name__ == "find_note_by_tags":
                return "Expected command find-note Tags."         
            return "Give me name and phone please."
        except KeyError:
            if func.__name__ == "edit_note":
                return "Note with this ID doesn`t exist."
            elif func.__name__ == "delete_note":
                return "Note with this ID doesn`t exist."
            elif func.__name__ == "delete_tag":
                return "Note with this ID doesn`t exist."
            elif func.__name__ == "add_tags":
                return "Note with this ID doesn`t exist."
            return 'No record found with this name'
        except TypeError:
            if func.__name__ == "add_birthday" or func.__name__ == "show_birthday":
                return "Birthday should be in format DD.MM.YYYY."
            elif func.__name__ == "new_note":
                return "Expected command new-note Text."
            return 'Please provide full info'
        except AttributeError:
            return 'Contact not found'
        except IndexError:
            if func.__name__ == "delete_note":
                return "Expected command delete-note ID."
            return 'Please provide full info'

    return inner