def decorator_function(original_func):
    def wrap_function():
        print('Some code before the old code')
        original_func()
        print('Some code after the old code')
    return wrap_function


@decorator_function
def simple_function():
    print('Simple function code')


# simple_function()


def make_compliment(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet you')
        func(*args, **kwargs)
        print('You look great!')
    return wrapper


@make_compliment
def ask_name():
    print('What is your name?')


ask_name()


@make_compliment
def say_name(name):
    print('My name is ' + name)


say_name('Jack')


@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')


order('chips', drink='cola')  # *args, **kwargs


