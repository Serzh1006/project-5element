from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):

    birth_dates = defaultdict(list)
    current_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)
        
        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            week_day = birthday_this_year.strftime('%A')
            if day_of_week in [5,6]:
                week_day = 'Monday'
                       
            birth_dates[week_day].append(name)
        

    return birth_dates

users = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 6)},
        {"name": "Max Tylor", "birthday": datetime(1987, 3, 7)},
        {"name": "Bill Morten", "birthday": datetime(1993, 3, 8)},
        {"name": "Dan Gates", "birthday": datetime(1977, 3, 9)}]

print(get_birthdays_per_week(users))




