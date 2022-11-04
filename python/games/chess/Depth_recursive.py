import random

def do(is_me, depth):
    if (depth == 5):
        print('Макс. глубина')
        return
    if (is_me):
        print('Мой ход')
    else:
        print('Ход противника')
    do(not is_me, depth + 1)

# do(True, 0)

def do2(is_me, depth):
    if (depth == 4):
        return
    for i in ('Ход 1', 'Ход 2'):
        if (is_me):
            print(' ' * depth * 2 + 'Мой' + ' ' + i)
        else:
            print(' ' * depth * 2 + 'Противника' + ' ' + i)
        do2(not is_me, depth + 1)

# do2(True, 0

def ppp(depth, message):
    print(' ' * depth * 3 + message)

def do3(is_me, depth):
    if depth == 3:
        return random.randint(0, 100)

    rates = []
    for i in ('Ход 1', 'Ход 2'):
        if (is_me):
            ppp(depth, ('Мой' + ' ' + i))
        else:
            ppp(depth, ('Противника' + ' ' + i))
    
        rate = do3(not is_me, depth + 1)
        ppp(depth, f'Позиция оценена: {rate}%')
        rates.append(rate)

    if (is_me):
        ppp(depth, f'Из оценок {rates} выбираем лучшую')
    else:
        ppp(depth, f'Из оценок {rates} выбираем худшую')

    if (is_me):
        return max(rates)
    else:
        return min(rates)

do3(True, 0)
