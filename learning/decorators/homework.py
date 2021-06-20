from functools import wraps
from time import sleep


def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print('args: ', args)
        print('kwargs: ', kwargs)
    return wrapper


@print_args
def my_args():
    print('Where is my args?')


my_args('Tommy', 'Alice', dog1='Jack', dog2='Fly')


def print_args(func):
    def wrapper(*args, **kwargs):
        print('*args:', args)
        print('**kwargs', kwargs)
        return func(*args, **kwargs)
    return wrapper


@print_args
def shop_list(*args, **kwargs):
    print('I bought {} {}'.format(args[1], kwargs['fruit']))


shop_list('one', 'two', 'three', fruit='banana', vegetable='carrot')


def hello_from_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        code = func()
        print('Hello from decorator! ' + code)
    return wrapper


@hello_from_decorator
def some_func():
    return 'Some code'


some_func()


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            raise ValueError("Function must have less than 3 arguments!")
        else:
            return func(*args, **kwargs)
    return wrapper


@prohibit_more_than_2_args
def less_2_args(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)


less_2_args('cat', 'bird')


def wait(n):
    def inner_deck(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(n)
            print(f"There was a pause {n} seconds "
                  f"before execution {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return inner_deck


@wait(3)
def say_meow():
    print('Meow!')


say_meow()
