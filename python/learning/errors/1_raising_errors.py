# raise ValueError('My invalid value')
# raise ValueError()


def get_rainbow_color(color_number):
    """
    :param color_number: Color number must be integer type
    and must be in range of integer from 1 to 7
    :return: color name
    """
    color_number_list = [1, 2, 3, 4, 5, 6, 7]

    if type(color_number) is not int:
        raise TypeError('Color number must be integer')

    if color_number not in color_number_list:
        raise ValueError('color number must be in range of integer from 1 to 7')

    if color_number == 1:
        return 'red'
    elif color_number == 2:
        return 'orange'
    elif color_number == 3:
        return 'yellow'
    elif color_number == 4:
        return 'green'
    elif color_number == 5:
        return 'blue'
    elif color_number == 6:
        return 'indigo'
    elif color_number == 7:
        return 'violet'


color = get_rainbow_color(7)
print(color)


def colorize_text(color_number, text):
    """
    :param color_number: Color number must be integer type
    and must be in range of integer from 1 to 7
    :param text: text must be string type
    """
    color_number_list = [1, 2, 3, 4, 5, 6, 7]

    if type(color_number) is not int:
        raise TypeError('Color number must be integer')

    if color_number not in color_number_list:
        raise ValueError('color number must be in range of integer from 1 to 7')

    if type(text) is not str:
        raise TypeError('Parameter text must be string type')

    if color_number == 1:
        print('red ' + text)
    elif color_number == 2:
        print('orange ' + text)
    elif color_number == 3:
        print('yellow ' + text)
    elif color_number == 4:
        print('green ' + text)
    elif color_number == 5:
        print('blue ' + text)
    elif color_number == 6:
        print('indigo ' + text)
    elif color_number == 7:
        print('violet ' + text)


colorize_text(1, 'True')
