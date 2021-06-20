from random import choice
# Higher order functions which accept another function as arguments


def product(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


def cube(x):
    return x * x * x


print(product(4, square))
# 1 2 3
# 1 4 9

print(product(4, cube))
# 1 2 3
# 1 8 27


def my_function(a, b, func):
    result = func([a, b])
    return result


print(my_function(7, 3, sum))


# Using nested function


def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    result = get_color() + ' ' + thing
    return result


print(colorize('apple'))


# Higher order functions which return another function as argument


def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    return get_color


first_color = make_color()
print(first_color())

second_color = make_color()
print(second_color())

third_color = make_color()
print(third_color())


# Inner function can access outer function scope


def colorize1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color


print(colorize1('orange')())
colorized_cat = colorize1('cat')
print(colorized_cat())
