# *args and **kwargs

# *args
def func_with_args(*args):
    print(args)


func_with_args(1, 2, 3)


def ten_percent_of_product(x, y, z):
    return (x * y * z) * 0.1


print(ten_percent_of_product(10, 20, 7))


def ten_percent_of_product_with_args(*args):
    product = 1
    for number in args:
        product = product * number
    return product * 0.1


print(ten_percent_of_product_with_args(10, 20, 2, 1, 4, 345))


def percent_of_product_with_args(percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent


print(percent_of_product_with_args(20, 10, 20, 2, 1, 4, 345))


# **kwargs
def func_with_kwargs(**kwargs):
    print(kwargs)


func_with_kwargs(first=1, second=2, third=3)


def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello! Nice to meet you, {}'.format(kwargs['name']))
    else:
        print('Hello! What is your name?')


hello_with_kwargs(gender='male', age=24, name='Jack')
hello_with_kwargs(gender='male', age=24)


def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
    else:
        print('{}! What is your name?'.format(greeting))


hello_with_greeting_and_kwargs('Good morning', gender='male', age=24, name='Jack')


# hello_with_greeting_and_kwargs(gender='male', age=24)

def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')
