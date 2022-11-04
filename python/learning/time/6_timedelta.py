from datetime import timedelta, datetime

year = timedelta(days=365)
print(year)

today = datetime.now()

print(f'Today is {today}')
print(f'23 days from today will be {today + timedelta(days=23)}')
print(f'1 days from today will be {today + timedelta(days=1)}')
print(f'999 days from today will be {today + timedelta(days=999)}')
print(f'230000 seconds from today will be {today + timedelta(seconds=230000)}')

last_birthday = datetime(2021, 5, 17)
print(f'My last birthday was {(today - last_birthday).days} days ago')

leap_year = timedelta(days=366)
print(f'There are {year.total_seconds()} seconds in year and '
      f'{leap_year.total_seconds()} seconds in a leap year')

print(f'There are {(year * 7).days} days in 7 years and '
      f'{(leap_year * 7).days} days in a 7 leap year')
