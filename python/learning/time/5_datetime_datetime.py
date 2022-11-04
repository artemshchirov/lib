from datetime import datetime

today = datetime(2021, 6, 30)
print(today)
today_now = today.now()
print(today_now)

timestamp = datetime.timestamp(today)
print(timestamp)  # 1625000400.0
timestamp_now = datetime.timestamp(today_now)
print(timestamp_now)

today_from_timestamp = datetime.fromtimestamp(timestamp)
print(today_from_timestamp)  # 2021-06-30 00:00:00

today_format = today.strftime('%d %B %y')
print(f'Today is {today_format}')
print(f'Today is {today.strftime("%A")}')

today = datetime.today()
print(today)
utc_today = today.utcnow()
print(utc_today)
print(today.date())
print(today.time())
print(today.isocalendar())  # (year, week number, weekday)
print(today.isoformat())



