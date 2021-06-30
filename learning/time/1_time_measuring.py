import time

input('Press Enter to start ')

# start_time = time.time()  # DEPRECATED
start_time = time.perf_counter()
for i in range(10000000):
    x = i * i
end_time = time.perf_counter()
# end_time = time.time()  # # DEPRECATED

print(end_time - start_time)
