# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions

# def my_function(x):
#     return x
#
#
# print(my_function(4))


def count_up_to(x):
    count = 1
    while count <= x:
        yield count  # return iterator and remember number of "count" in this func
        count += 1


print(count_up_to(4), '\n')

print(list(count_up_to(7)))

counter = count_up_to(10)

counter.__next__()
counter.__next__()
next(counter)
next(counter)


for number in counter:
    print(number)
