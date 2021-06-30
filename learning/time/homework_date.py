from datetime import date

year = int(input('Please enter a year: '))
month = int(input('Please enter a month: '))
day = int(input('Please enter a day: '))

week_day = date(year, month, day).weekday()

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(f'{year}-{month}-{day} is {week[week_day]}')
