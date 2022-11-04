from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

date_1 = date(2021, 6, 30)
date_2 = date(2019, 12, 25)
diff = date_1 - date_2
print(diff)
print(type(date_1), type(date_2), type(diff))

today = date.today()
print(today)

my_birthday = date(today.year, 5, 17)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)

print(my_birthday)
days_until_birthday = my_birthday - today
print(f'You will celebrate your birthday in {days_until_birthday.days} days!')

week_day = today.weekday()
print(week_day)
week_day_today = today.isoweekday()
print(week_day_today)

