from functools import wraps


def prohibit_int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('KeyWord arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


@prohibit_int_args
def print_hello(name):
    print('Hello ' + name)


print_hello('Jack')
print_hello(3)
