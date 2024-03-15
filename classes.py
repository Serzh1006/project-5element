from collections import UserDict
from datetime import datetime
from collections import defaultdict
import re
import os
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if not (len(phone) == 10 and phone.isdigit()):
            raise ValueError("Must be 10 numbers")
        super().__init__(phone)

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(e)
        self.phones = []
        self.birthday = ''
        self.email = ''
        self.addresses = [] # new address list

    def add_address (self, address): # add-address function
        self.addresses.append (address)
        return self.addresses   # show the address list
        

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                try:
                    self.phones[index] = Phone(new_phone)
                except ValueError as e:
                    print(e)
                return 'Contact updated'
        return 'Phone is not found'

    def find_phone(self, searched_phone):
        for phone in self.phones:
            if str(phone) == searched_phone:
                return str(phone)
            
    def add_birthday(self, birthday):
        try:
            self.birthday = datetime.strptime(birthday, "%d.%m.%Y")
            return 'Birthday added'
        except ValueError:
            return "Birthday should be in format DD.MM.YYYY"
        
    def show_birthday(self):
        try:
            return self.birthday.strftime('%d.%m.%Y')
        except:
            return 'Not found'
    
    def show_phones(self):
        return f"{'; '.join(p.value for p in self.phones)}"
    
    def add_email(self, email):
        try:
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                self.email = email
                return "Email added"
            else:
                raise TypeError
        except ValueError as e:
            return e
    
    def show_email(self):
        return self.email

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.file_path = args[0]['path']
        # self.file_path = os.path.join(os.path.expanduser("~"), "contacts.pkl")
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "rb") as f:
                    self.data = pickle.load(f)
            except:
                print("Load error")

    def save(self):
        with open(self.file_path, "wb") as f:
            pickle.dump(self.data, f)
    
    def add_record(self, record):
        self.data[record.name.value] = record
        self.save()
        return 'Contact added'

    def delete(self, name):
        del self.data[name]
        self.save()

    def find(self,name):
        for key, record in self.data.items():
            if key == name:
                return record
            
    def get_birthdays_per_week(self,count_days):
        current_date = datetime.today().date()
        birth_dates = defaultdict(list)
        result = ''
        for name, date in self.items():
            if not date.birthday:
                continue
            birthday_this_year = date.birthday.replace(year=current_date.year).date()
            if birthday_this_year < current_date:
                birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
            delta_days = (birthday_this_year - current_date).days
            if delta_days < count_days:
                birth_dates[birthday_this_year].append(name)
        if len(birth_dates)==0:
            return "\nBirthday not found!\n"
        else:
            for birthday, name in birth_dates.items():
                result += f"{birthday}: {', '.join(name)}\n"
            return result
    
    def __str__(self):
        result = ''
        for key, value in self.data.items():
            result += f"""Contact name: {key}, phones: {'; '.join(p.value for p in value.phones)}{', birthday: ' 
            + value.birthday.strftime('%d.%m.%Y') if value.birthday else ''}{', email: ' + value.email if value.email else ''}{', addresses: ' + ', '.join(value.addresses) if value.addresses else ''}\n"""
        return result