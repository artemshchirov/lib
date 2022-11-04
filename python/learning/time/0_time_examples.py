import time

print(time.gmtime(0))
print(time.gmtime())  # seconds from time.time() since epoch start
print(time.time())
print(time.localtime())  # your zone time

epoch_start_time = time.gmtime(0)
print(epoch_start_time)
print(f"Year: {epoch_start_time[0]}")
print(f"Month: {epoch_start_time[1]}")
print(f"Day: {epoch_start_time[2]}")

print(f"Year: {epoch_start_time.tm_year}")  # namedtuple
print(f"Month: {epoch_start_time.tm_mon}")
print(f"Day: {epoch_start_time.tm_mday}")
print(f"Week day: {epoch_start_time.tm_wday}")

print(time.ctime(time.time()))  # Wed Jun 30 00:44:14 2021
print(time.ctime(1111111111))

print("Text before delay")
# time.sleep(3.2)
print("Text after 3.2 seconds")

local_time = time.localtime(time.time())
print(local_time)
mk_time = time.mktime(local_time)
print(time.asctime(local_time))
print(time.localtime(mk_time))

print(time.strftime('%x %X'))  # directives as argument
print(time.strftime('%m/%d/%Y, %H:%M:%S', local_time))

time_string = '30 June, 2021'

struct_time = time.strptime(time_string, '%d %B, %Y')
print(struct_time)
