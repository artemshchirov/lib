# Справка: lesswrong.ru/458

to_do = []
results = []
utility = []
chances = []

choice_to_do = ''
while choice_to_do != '-':
    to_do.append(input('\nНапишите действие (Д)\n'
                       '>>> '))
    print('\nДобавленные действия')
    for i in range(len(to_do)):
        print(f'{i + 1}. {to_do[i]}')
    choice_to_do = input('\nДобавить еще действие? (+ / -)\n'
                         '>>> ')

choice_results = ''
choice_utility = ''
while choice_results != '-':
    results.append(input('\nНапишите возможный исход (И)\n'
                         '>>> '))

    utility_chances = ''
    within_range = False
    while not within_range:
        utility_chances = input(f'Оценка полезности (П) исхода {results[len(results) - 1]}? (от 0 до 1):\n'
                                '>>> ')
        try:
            utility_chances = float(utility_chances)
        except ValueError:
            print('Это не число от 0 до 1!')
            continue
        if 0 <= utility_chances <= 1:
            within_range = True
        else:
            within_range = False
            print('Это не число от 0 до 1!')

    utility.append(utility_chances)

    print('\nДобавленные Исход : Полезность')
    for i in range(len(results)):
        print(f'{i + 1}. {results[i]} : {utility[i]}')
    choice_results = input('\nДобавить еще возможный исход? (+ / -)\n>>> ')

print(f'\nКакая вероятность у Действие : Исход? (от 0 до 1)')
probability = 1
count = 0
for i in range(len(to_do)):
    for j in range(len(results)):
        count += 1
        choice_chances = ''
        within_range = False
        while not within_range:
            print(f'Осталось вероятности: {probability}')
            choice_chances = input(f'{count}. {to_do[i]}:{results[j]}.\n>>> ')
            try:
                choice_chances = float(choice_chances)
            except ValueError:
                print('Это не число от 0 до 1!')
                continue
            if 0 <= choice_chances <= 1:
                within_range = True
            else:
                within_range = False
                print('Это не число от 0 до 1!')

            probability -= choice_chances
            if probability < 0:
                probability += choice_chances
                check_probability = ''
                while check_probability != "ок" and check_probability != "-1":
                    print()
                    check_probability = input(
                                            'Внимание! Сумма всех вероятностей больше 1\n'
                                            'Введите "ок", чтобы продолжить или "-1", чтобы изменить вероятности\n'
                                            '>>> ')
                if check_probability == "-1":
                    print(*chances, sep='\n')
                    line_number = input('Введите номер строки, вероятность которой вы хотели бы изменить\n'
                                        '"ок" - Выйти и продолжить\n'
                                        '>>> ')
                    if line_number == "ок":
                        break
                    else:
                        count_probability = 0
                        for n in range(len(to_do)):
                            for m in range(len(results)):
                                count_probability += 1
                                print(f'{count_probability}. {to_do[n]}:{results[m]}')

                        choice_line = ''
                        while not choice_line.isdigit():
                            choice_line = input('Введите номер строки, вероятность которой вы хотели бы изменить\n'
                                                '"ок" - Выйти и продолжить\n'
                                                '>>> ')
                            if choice_line == 'ок':
                                break

                            if choice_line.isdigit():
                                choice_line = int(choice_line)
                                if choice_line in range(count_probability):
                                    new_value = ''
                                    while not new_value.isdigit():
                                        new_value = input(
                                            f'Введите новое значение для {choice_line} строки. (от 0 до 1)\n'
                                            f'Осталось вероятности: {probability}'
                                            '>>> ')
                                    print(chances)
                                    chances[choice_line] = int(new_value)
                                    print(chances)
                            else:
                                choice_line = ''

            chances.append(choice_chances)

print('\nДействие : Исход : Полезность : Вероятность>0  \
       \nОжидаемая полезность действия = сумма полезности исходов действия * вероятность исхода')

for i in range(len(to_do)):
    for j in range(len(results)):
        idx = i * len(to_do) + j
        def_utility = None
        print(f'{idx + 1}. Д({to_do[i]}) : И({results[j]}):П({utility[j]}) : В({chances[idx]})  \
              \nОП = ')
