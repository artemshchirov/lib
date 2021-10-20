# 1) Ищем индексы чисел с начала и конца, меньше и больше (соответсвенно) среднего числа и меняем местами
# 2) Повторяем пока перебираемые числа с обоих сторон не станут равны или первый индекс не станет больше
# 3) Рекурсивно отправляем списки, 1й до и 2й после итогового индекса в п.2
# 4) п.2
# 5) Соединяем возвращенные отсортированные списки в один

listStart = [5, 8, 1, 99, 3, 5, 2, 0, 2, 5, 2]
print(f'Start: {listStart}')
countRec = 0

def methodQsort(list, startElement, endElement):
    '''
    Сортировка методом
    '''
    global countRec
    countRec += 1
    # Если левая граница больше правой, то прерываем метод с помощью return
    if (startElement >= endElement):
        print(f'\nreturn: startElement {startElement} >= {endElement} endElement')
        return
    # В качестве опрного значения число из середины списка
    average = list[startElement + (endElement - startElement) // 2]
    # Границы входящего списка в пределах которых происходит обработка
    first = startElement
    last = endElement
    print('Start while (first <= last):')
    # Нахождение элемента
    while (first <= last):
        print(f'\ncountRec: {countRec}')
        print(f'average: {average}')
        print(f'first=startElement: {first}')
        print(f'last=endElement: {last}')
        print(f'list: {list[startElement:endElement+1]}\n')
        # Нахождение левого элемента, у которого index >= average
        print('first:', first, end=' ')
        while (list[first] < average):
            first += 1
            print(first, end=' ')
        # Нахождение правого элемента, у которого index <= average
        print('\nlast:', last, end=' ')
        while (list[last] > average):
            last -= 1
            print(last, end=' ')
        print(f'\nlist[first]: {list[first]}, list[last]: {list[last]}')
        if (first <= last):
            list[first], list[last] = list[last], list[first]
            first += 1
            last -= 1
        print(f'\nEdited: {list[startElement:endElement+1]}\n', '=' * 20)
    print('End while (first <= last):\n', '=' * 40)
    print('\n===== START methodQsort(list, first, endElement): =====')
    methodQsort(list, startElement, last)
    print(f'FINISH methodQsort(list, first, endElement): {list}')
    print('START  methodQsort(list, first, endElement):')
    methodQsort(list, first, endElement)
    print(f'FINISH methodQsort(list, first, endElement): {list}')

def qsort(list, startElement, endElement):
    '''
    Сортировка методом.
    Тренировочное поле:
    '''

    # ======================================

    if (startElement >= endElement):
        return

    average = list[startElement + (endElement - startElement) // 2]

    first = startElement
    last = endElement

    while (first <= last):

        while (list[first] < average):
            first += 1

        while (list[last] > average):
            last -= 1

        if (first <= last):
            list[first], list[last] = list[last], list[first]
            first += 1
            last -= 1

    qsort(list, startElement, last)
    qsort(list, first, endElement)



    # ======================================

qsort(listStart, 0, len(listStart) - 1)
# methodQsort(listStart, 0, len(listStart) - 1)
print(f'\n!!!Sorted: {listStart}')
