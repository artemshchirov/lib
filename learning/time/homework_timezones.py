import pytz
import datetime
from random import randint as rnd

count = 7
for idx, country in enumerate(pytz.country_names):  # all timezones'
    print(country, pytz.country_names[country], pytz.common_timezones[idx])
    count -= 1
    if count <= 0:
        print()
        break

user_choice = ''
while user_choice != 'q':
    user_choose = input('Please enter a two-letters code of the country to choose the timezone or "q" to quite:\n')
    print(f'Local time is {datetime.datetime.now(pytz.country_names[user_choice])}')


# kiev = 'Europe/Kiev'
# tz_kiev = pytz.timezone(kiev)
# kiev_time = datetime.datetime.now(tz_kiev)
# print(kiev_time)  # 2021-06-30 02:42:27.585079+03:00