from functools import wraps


def print_function_data(func):
    """
    This is decorator function
    """
    @wraps(func)  # save metadata of source func docs
    def wrapper(*args, **kwargs):
        print(f'You are using {func.__name__}')
        print(f'Function documentation {func.__doc__}')
        return func(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    """
    :param a: first number
    :param b: second number
    :return: sum of squares first and second number (a * a + b * b)
    """
    return a * a + b * b


print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
help(squares_sum)
