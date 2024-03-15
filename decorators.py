def input_days_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Please enter digits!"
        except IndexError:
            return "Please enter count days!"
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
            return "Give me name and phone please."
        except KeyError:
            return 'No record found with this name'
        except TypeError:
            if func.__name__ == "add_birthday" or func.__name__ == "show_birthday":
                return "Birthday should be in format DD.MM.YYYY."
            return 'Please provide full info'
        except AttributeError:
            return 'Contact not found'

    return inner