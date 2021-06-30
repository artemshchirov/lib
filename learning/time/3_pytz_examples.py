import pytz
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

kiev = 'Europe/Kiev'
tz_kiev = pytz.timezone(kiev)
print(tz_kiev)
kiev_time = datetime.datetime.now(tz_kiev)
print(kiev_time)  # 2021-06-30 02:42:27.585079+03:00

jerusalem = 'Asia/Jerusalem'
tz_jerusalem = pytz.timezone(jerusalem)
jerusalem_time = datetime.datetime.now(tz_jerusalem)
print(jerusalem_time)

for tz in pytz.all_timezones:
    print(tz)

for country in pytz.country_names:  # all timezones
    print(country, pytz.country_names[country], pytz.country_timezones.get(country))

