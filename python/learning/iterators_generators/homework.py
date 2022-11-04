def get_week_day():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in week:
        yield day


current_day = get_week_day()

print(current_day.__next__())  # 'Sunday'
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())  # 'Saturday'


def even_odd():
    words = ['even', 'odd']
    while True:
        for word in words:
            yield word


even_odd_generator = even_odd()

print(next(even_odd_generator))  # 'even'
print(next(even_odd_generator))  # 'odd'
print(next(even_odd_generator))  # 'even'
print(next(even_odd_generator))  # 'odd'


def get_infinite_square_generator():
    i = 1
    while True:
        yield i ** 2
        i += 1


infinite_square_generator = get_infinite_square_generator()

print(next(infinite_square_generator))  # 1
print(next(infinite_square_generator))  # 4
print(next(infinite_square_generator))  # 9
print(next(infinite_square_generator))  # 16
