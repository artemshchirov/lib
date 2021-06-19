# If we have an error - except fires and else doesn't fire
# If we haven't an error - else fires and except doesn't fire
# Finally block fires anyway

while True:
    try:
        number = int(input('Enter some number '))
        print(number / 2)
    except:
        print('You have to enter a number!')
    else:
        print('Good job! This is a number')
        break
    finally:
        print('Finally block')
print('Code after error handling')


def divide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print('You can`t divide the zero')
        print('e:', e)
    except TypeError as err:
        print('x and y must be numbers')
        print('e:', err)
    else:
        print('x was divided by y')
    finally:
        print('finally block\n')


print(divide(4, 'w'))
print(divide(4, 0))
print(divide(9, 3))
