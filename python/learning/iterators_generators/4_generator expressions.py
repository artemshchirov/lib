import time


def get_number_from_range():
    for number in range(10):
        yield number


counter = get_number_from_range()
print(counter, '\n')

print(next(counter))
print(next(counter))


# Generator expression
counter1 = (number for number in range(10))
print(counter1)

print(next(counter1))
print(next(counter1))

# Comparing generators and lists
list_start_time = time.time()
print(sum([number for number in range(10000000)]))  # full memory because of list creation
list_processing_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum((number for number in range(10000000))))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')
print(f'Processing with list is {gen_processing_time}')




