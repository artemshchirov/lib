import time

print(f'UTC time: {time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime())}')
print(f'Local time: {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())}')

print(time.altzone/60/60)
print(time.daylight)
print(time.localtime())
print(time.timezone/60/60)

print(time.tzname)
print(time.tzname[0])
if time.daylight != 0:
    print(time.tzname[1])

print(time.localtime().tm_zone)
print(time.localtime().tm_gmtoff/60/60)
