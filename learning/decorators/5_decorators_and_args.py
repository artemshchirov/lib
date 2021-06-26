from functools import wraps


def check_if_first_arg_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@check_if_first_arg_is('red')
def print_rainbow_colors(*args):
    print(args)


print_rainbow_colors('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')


@check_if_first_arg_is(7)
def multiply_7(a, b):
    return a * b


print(multiply_7(6, 4))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', '4')

# *args = ('Hi!', '3')
# *types = (str, int)
# zip(args, types) - ('Hi!', str) ('3', int)


@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))
print(divide('4', '2'))
