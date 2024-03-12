from collections import UserDict
from datetime import datetime
from collections import defaultdict 



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
            return "Format DD.MM.YYYY"
        
    def show_birthday(self):
        try:
            return self.birthday.strftime('%d.%m.%Y')
        except:
            return 'Not found'
    
    def show_phones(self):
        return f"{'; '.join(p.value for p in self.phones)}"
    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):

    def __init__(self):
        self.data = {}
    
    def add_record(self, record):
        self.data[record.name.value] = record
        return 'Contact added'

    def delete(self, name):
        del self.data[name]

    def find(self,name):
        for key, record in self.data.items():
            if key == name:
                return record
            
    def get_birthdays_per_week(self):
        current_date = datetime.today().date()
        birth_dates = defaultdict(list)
        result = ''

        for name, date in self.items():
        
            birthday_this_year = date.birthday.replace(year=current_date.year).date()

            if birthday_this_year < current_date:
                birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

            delta_days = (birthday_this_year - current_date).days

            week_day = birthday_this_year.strftime('%A')
            if delta_days < 7:
                week_day = birthday_this_year.weekday()

                week_day = birthday_this_year.strftime('%A')
                if week_day in [5,6]:
                    week_day = 'Monday'
                    
                birth_dates[week_day].append(name)
      
        for birthday, name in birth_dates.items():
            result += f"{birthday}: {', '.join(name)}\n"
        return result
    
    
    def __str__(self):
     
        result = ''
        for key, value in self.data.items():
            
            result += f"Contact name: {key}, phones: {'; '.join(p.value for p in value.phones)}{', birthday: ' + value.birthday.strftime('%d.%m.%Y') if value.birthday else ''}\n"

        return result
