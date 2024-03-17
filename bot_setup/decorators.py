def input_days_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "\nKodi>> Oh no! The quantity must be a digit and an integer!"
        except IndexError:
            return "\nKodi>> Hmm...Please provide <count days> in format birthdays <count days>"
    return inner


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_email" or func.__name__ == "show_email":
                return "\nKodi>> Please provide contact name and email"
            elif func.__name__ == "add_address" or func.__name__ == "show_address":
                return "\nKodi>> Enter contact name and address in format <name> <street> <house> <city> <postal_code>."
            elif func.__name__ == "add_birthday" or func.__name__ == "show_birthday":
                return "\nKodi>> Please provide contact name and birthday in format DD.MM.YYYY." 
            elif func.__name__ == "new_note":
                return "\nKodi>> Expected command new-note Text."
            elif func.__name__ == "edit_note":
                return "\nKodi>> Expected command edit-note ID New-text."
            elif func.__name__ == "delete_note":
                return "\nKodi>> Expected command delete-note ID."
            elif func.__name__ == "show_note":
                return "\nKodi>> Expected command show-note KeyWords."  
            elif func.__name__ == "delete_tag":
                return "\nKodi>> Expected command delete-tag ID Tag(one tag)."
            elif func.__name__ == "add_tags":
                return "\nKodi>> Expected command add-tags ID Tags."
            elif func.__name__ == "find_note_by_tags":
                return "\nKodi>> Expected command find-note Tags."         
            return "\nKodi>> Give me name and phone please."
        except KeyError:
            if func.__name__ == "edit_note":
                return "\nKodi>> Note with this ID doesn`t exist."
            elif func.__name__ == "delete_note":
                return "\nKodi>> Note with this ID doesn`t exist."
            elif func.__name__ == "delete_tag":
                return "\nKodi>> Note with this ID doesn`t exist."
            elif func.__name__ == "add_tags":
                return "\nKodi>> Note with this ID doesn`t exist."
            return '\nKodi>> Sorry! No record found with this name'
        except TypeError:
            if func.__name__ == "add_birthday" or func.__name__ == "show_birthday":
                return "\nKodi>> Birthday should be in format DD.MM.YYYY."
            elif func.__name__ == "new_note":
                return "\nKodi>> Expected command new-note Text."
            return '\nKodi>> Please provide full info'
        except AttributeError:
            return '\nKodi>> Contact not found'
        except IndexError:
            if func.__name__ == "delete_note":
                return "\nKodi>> Expected command delete-note ID."
            return '\nKodi>> Please provide full info'

    return inner