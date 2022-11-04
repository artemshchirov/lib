# ЗАМЕТКИ
# Сделать версию на весь экран и бОльшим колчеством спрайтов
# Сделать запоминание темы и прогресса
# Добавить глобальные переменные для отслеживания пустого поля
# Потестить root.update()
# Добавить анимацию смены изображений методом в exchangeImage(). Посмотреть про объекты Canvas и библ. puGames

from tkinter import *
from tkinter import ttk  # Для RadioButton
from tkinter import messagebox  # Для окон-сообщений
from random import randint
from winsound import Beep  # Бипер (пищалка), генератор звука
from time import sleep  # Для пауз


def music():
    """
    Imperial March Beep мелодия
    """
    # Beep - метод генерации звука
    # Beep(x - Частота звука (от 37 до 32767 Герц), y - Продолжительность)
    Beep(440, 500)
    Beep(440, 500)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)
    Beep(659, 500)
    Beep(659, 500)
    Beep(659, 500)
    Beep(698, 350)
    Beep(523, 150)
    Beep(415, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)


def refreshText():
    """
    Обновляет текст меток статистики
    """
    textSteps['text'] = f'Сделано ходов: {steps[diffCombobox.current()]}'
    textRecord['text'] = f'Рекорд ходов: {record[diffCombobox.current()]}'


def saveRecords():
    """
    Сохраняет в файл steps.dat рекорды установленные игроком
    """
    global record

    try:
        f = open('steps.dat', 'w', encoding='utf-8')
        for i in range(len(steps)):
            # Проверка на "был ли уже записанный рекорд побит?".
            # Сравнение списков
            if steps[i] > 0 and steps[i] < record[i]:
                record[i] = steps[i]
            f.write(str(record[i]) + '\n')
        f.close()
    except:
        messagebox.showinfo('Ошибка', 'Возникла проблема с файлом при сохранении очков')
        record[i] = steps[i]


def getRecordSteps():
    """
    Возвращает список рекордов из save файла
    в переменную record
    """
    # Список заполняется значениями из файла для списка records[]
    m = []
    try:
        f = open('steps.dat', 'r', encoding='utf-8')
        for line in f.readlines():
            m.append(int(line))
        f.close()
    except:
        print('Файл рекордов не найден. Проверьте путь и имя файла')
        print('Создаю файл... Рекорды обнулены')

    # Список должен быть не меньше уровней сложностей (6). Проверка:
    if len(m) != 6:
        for i in range(6):
            m.append(1000 + 500 * i)

    return m


def seeEnd(event):
    """
    Возвращение спрайтов на поле как было
        до нажатия кнопки "Посмотреть, как..."
    """
    global dataImage

    Beep(1082, 50)

    for i in range(n):
        for j in range(m):
            dataImage[i][j] = copyData[i][j]

    # Обновление изображений в окне
    updatePictures()


def seeStart(event):
    """
    Показывает собранное изображение,
        когда ЛКМ зажата кнопка "Посмотреть, как..."
    """
    global copyData, dataImage

    Beep(1632, 50)

    for i in range(n):
        for j in range(m):
            # Сохраняем позиции спрайтов текущей игры
            copyData[i][j] = dataImage[i][j]
            # Формируем новое, упорядоченное поле от 0 до 15
            dataImage[i][j] = i * n + j

    # Обновление изображений
    updatePictures()


def isCheckImage():
    """
    Выбор заготовленных изображений для спрайтов
    """
    global imageBackground

    if image.get() == 0:  # Если в переменной image содержится 0
        imageBackground = imageBackground01
        Beep(1350, 50)
    elif image.get() == 1:  # Если в переменной image содержится 1
        imageBackground = imageBackground02
        Beep(1450, 50)
    elif image.get() == 2:  # Если в переменной image содержится 2
        imageBackground = imageBackground03
        Beep(1550, 50)

    updatePictures()


def updatePictures():
    """
    Обновление всех изображений в labelImage на основе dataImage
    """
    # Циклом проходим все labelImage[][], устанавливая необходимые изображения
    for i in range(n):
        for j in range(m):
            labelImage[i][j]['image'] = imageBackground[dataImage[i][j]]

    # Обновление экрана
    root.update()


def resetPictures():
    """
    Сброс игрового поля в исходное, упорядоченное состояние
    """
    global dataImage, steps, playGame

    # Игра началась
    steps[diffCombobox.current()] = 0
    # Обнуление количества шагов для текущего уровня сложности
    playGame = False

    # Настраиваем состояние виджетов
    startButton['state'] = NORMAL
    resetButton['state'] = DISABLED
    diffCombobox['state'] = 'readonly'
    radio01['state'] = NORMAL
    radio02['state'] = NORMAL
    radio03['state'] = NORMAL

    # Заполнение списка первоначальными значениями
    # (от 0 до 15 включительно), чтобы вывести правильное изображение
    for i in range(n):
        for j in range(m):
            dataImage[i][j] = i * n + j
    # Задаём пустое поле
    dataImage[n - 1][m - 1] = blackImg

    # Победные сигналы
    # ПРОТЕСТИРОВАТЬ
    Beep(1750, 50)

    # Обновление экрана
    updatePictures()

    # Обновление текста меток статистики
    refreshText()


def exchangeImage(x1, y1, x2, y2):
    """
    Обмен мест изображений в математической
        и соответсвенно в графической моделях
    """
    global dataImage, labelImage

    # Изменяем математическую модель
    dataImage[x1][y1], dataImage[x2][y2] = dataImage[x2][y2], dataImage[x1][y1]

    # Получаем изобаржение по номеру из dataImage и устанавливаем его в labelImage
    labelImage[x1][y1]['image'] = imageBackground[dataImage[x1][y1]]
    labelImage[x2][y2]['image'] = imageBackground[dataImage[x2][y2]]

    root.update()

    # Пауза между перемещением спрайтов при перемешивании
    numSleep = diffCombobox.current()
    if numSleep == 0:
        sleep(0.1)
    else:
        sleep(numSleep / (10 ** numSleep * numSleep))


def shufflePictures(x, y):
    """
    На основе сложности запускаем цикл,
        в котором 'играем' наоборот: перемешиваем
        спрайты игрового поля, начиная
        с финальной позиции
    Если выбран уровень сложности "Donate!",
        то просто меняем местами 14 и 15 фишки
    """
    # .current() возвращает номер текущего выбранного значения списка
    # внутри Combobox['values']

    if 0 < diffCombobox.current() < 5:
        # Количество перемешиваний в зависимости от уровня сложности
        count = (1 + diffCombobox.current()) ** 4
        # Запрет направления
        noDirection = 0
        # Повторение перемешиваний
        # countBlackImgMoves = 0              # ТЕСТ
        # countSpareShuffles = 0              # ТЕСТ
        while count > 0:
            # countBlackImgMoves += 1         # ТЕСТ
            # print(countBlackImgMoves)       # ТЕСТ
            # for l in range(len(dataImage)): # ТЕСТ
            #     print(dataImage[l])         # ТЕСТ
            # print()                         # ТЕСТ
            # Задаём заведомо истинную комбинацию для while
            direction = noDirection
            # Получаем число, ТОЧНО не повторяющее предыдущее
            while direction == noDirection:  # Пока НовоеНаправление == Запрещённому
                direction = randint(0, 3)  # Генерируем НовоеНаправление
            # ВНИЗ
            if direction == 0 and x + 1 < n:
                # Обмениваем текущее "пустое" поле и спрайт ниже
                exchangeImage(x, y, x + 1, y)
                # Увеличиваем x, т.к пустое поле перместилось в новую позицию
                x += 1
                # Запрещаем направление. То есть следующее direction не должно
                # равняться числу 1, которое символизирует обмен с верхним спрайтом
                noDirection = 1
                count -= 1
            # ВВЕРХ
            elif direction == 1 and x - 1 >= 0:
                exchangeImage(x, y, x - 1, y)
                x -= 1
                noDirection = 0
                count -= 1
            # ВПРАВО
            elif direction == 2 and y + 1 < m:
                exchangeImage(x, y, x, y + 1)
                y += 1
                noDirection = 3
                count -= 1
            # ВЛЕВО
            elif direction == 3 and y - 1 >= 0:
                exchangeImage(x, y, x, y - 1)
                y -= 1
                noDirection = 2
                count -= 1
            # else:
            #     countSpareShuffles += 1     # ТЕСТ
            # print(countSpareShuffles)   # ТЕСТ
    # Начальные позиции спрайтов на сложности Donate!
    elif diffCombobox.current() == 0:
        exchangeImage(n - 1, m - 1, n - 1, m - 2)
        exchangeImage(n - 1, m - 2, n - 1, m - 3)
    # Начальные позиции спрайтов на сложности Impossible
    else:
        exchangeImage(n - 1, m - 3, n - 1, m - 2)

    Beep(1300, 50)

    resetButton['state'] = NORMAL


def startNewRound():
    """
    Сбрасываем состояния элементов интерфейса,
        чтобы их нельзя было нажать или выбрать
    Проигрываем звуковой сигнал
    Находим координаты пустого поля
    Запускаем метод shufflePictures(x, y),
        который перемешивает изображения
    """
    global steps, playGame
    # Игра началась
    playGame = True
    # Обнуление количества шагов для текущего уровня сложности
    steps[diffCombobox.current()] = 0

    diffCombobox['state'] = DISABLED
    startButton['state'] = DISABLED
    radio01['state'] = DISABLED
    radio02['state'] = DISABLED
    radio03['state'] = DISABLED

    # Проиграем звуковой сигнал. МОЖНО МЕНЯТЬ
    Beep(1200, 50)

    # ========== ВАРИАНТ ПО ГЛАВЕ
    # Находим координаты пустого поля простым перебором каждого элемента
    # двумерного списка dataImage[][]
    # Переборный алгоритм
    # x = 0
    # y = 0
    # for i in range(n):
    #     for j in range(m):
    #         # При совпадении числа в dataImage[][] с номером "пустого поля"
    #         # x и y счётчики циклов, ведь их значения и будут искомыми координатами
    #         if (dataImage[i][j] == blackImg):
    #             x = i
    #             y = j

    # ========== МОЙ ВАРИАНТ WHILE
    x = 0
    y = 0
    while dataImage[x][y] != blackImg:
        y += 1
        if y >= m:
            x += 1
            y = 0

    # ========== МОЙ ВАРИАНТ global
    #

    shufflePictures(x, y)

    # Обновление текста меток статистики
    refreshText()


def go(x, y):
    """
    Реакция при ЛКМ на спрайт
    Меняет местами пусто поле с изображением,
    если возможно
    """
    global steps, playGame

    # print(f'go: {x}, {y}')    # Отображение индекса изображения в dataImage
    if x + 1 < n and dataImage[x + 1][y] == blackImg:
        exchangeImage(x, y, x + 1, y)
    elif x - 1 >= 0 and dataImage[x - 1][y] == blackImg:
        exchangeImage(x, y, x - 1, y)
    elif y - 1 >= 0 and dataImage[x][y - 1] == blackImg:
        exchangeImage(x, y, x, y - 1)
    elif y + 1 < m and dataImage[x][y + 1] == blackImg:
        exchangeImage(x, y, x, y + 1)
    else:
        Beep(50, 100)
        return 0

    Beep(1400, 50)

    # Если спрайты были перемещены, то +1 к статистике ходов
    if playGame:
        steps[diffCombobox.current()] += 1
        # Обновление текста меток статистики
        refreshText()
        # Если не собрано, то win = True
        win = True
        for i in range(n):
            for j in range(m):
                # В dataImage[3][3] должно быть blackImg
                if i == n - 1 and j == m - 1:
                    # Если хоть одно из выражений = False
                    win = win and dataImage[i][j] == blackImg  # то win = False
                else:  # иначе сравниваем с dataImage[от 0 до 14]
                    win = win and dataImage[i][j] == i * n + j

        if win:
            # Установка спрайта картинки вместо пустого поля (для красоты)
            dataImage[n - 1][m - 1] = blackImg - 1
            updatePictures()

            messagebox.showinfo('Красота!', 'Это победа!\nДостойно уважения')

            music()
            saveRecords()
            playGame = False
            refreshText()


# =============== НАЧАЛО ПРОГРАММЫ
# Создание окна
root = Tk()
root.resizable(False, False)
root.title('Головоломка для самых умных')
# Иконка. Путь указывается от файла с кодом до объекта (иконки)
root.iconbitmap('favicon/favicon.ico')

# Цвета. Код - только шестнадцатеричная запись
back = '#373737'  # Фон: Черный
fore = '#AFAFAF'  # Шрифт: Серый

# Настройка геометрии окна
WIDTH = 422
HEIGHT = 730
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
# Устанавливаем фоновый цвет
root['bg'] = back

# Кнопка ПОСМОТРЕТЬ СОБРАННОЕ
seeButton = Button(root, text='See, how it should be', width=56)
seeButton.place(x=10, y=620)
seeButton.bind('<Button-1>', seeStart)  # нажатие ЛКМ по виджету вызывается метод seeStart
seeButton.bind('<ButtonRelease>', seeEnd)  # отпуск ЛКМ возвращает как было до нажатия виджета

# Кнопка СТАРТ
startButton = Button(text='START', width=56)
startButton.place(x=10, y=650)
startButton['command'] = startNewRound

# Кнопка СБРОС
resetButton = Button(text='Reset', width=56)
resetButton.place(x=10, y=680)
resetButton['command'] = resetPictures

# Метка для вывода текста с количестом
# Сделанных ходов
textSteps = Label(root, bg=back, fg=fore)
textSteps.place(x=10, y=550)
# и Рекордом текущего уровня
textRecord = Label(root, bg=back, fg=fore)
textRecord.place(x=10, y=570)

# Метка сложности
# НЕТ своей переменной т.к не будет использоваться. Экономия памяти на переменной
Label(root, bg=back, fg=fore, text='Сложность:').place(x=267, y=550)

# Названия степеней сложности перемешивания
itemDiff = ['Donate!', 'Easy', 'Gamer', 'King', 'God', 'Impossible']

# Выпадающий список
# values='X', где X - это значения показывающиеся в выпадающем окне
diffCombobox = ttk.Combobox(root, width=17, values=itemDiff, state='readonly')
diffCombobox.place(x=270, y=575)
# Менять рекорды для разных уровней сложности
diffCombobox.bind('<<ComboboxSelected>>', lambda e: refreshText())
# Сложность по-умолчанию при открытии программы
diffCombobox.current(1)

# Радиопереключатели (RadioButton)
# Создание переменной
image = IntVar()
# Устанавливаем значение
image.set(0)

# Создание RadioButton и привязка к ней переменной
radio01 = Radiobutton(root, text='Cyberpunk', variable=image, value=0, activebackground=back, bg=back, fg=fore)
radio02 = Radiobutton(root, text='Nature', variable=image, value=1, activebackground=back, bg=back, fg=fore)
radio03 = Radiobutton(root, text='Space', variable=image, value=2, activebackground=back, bg=back, fg=fore)
radio01['command'] = isCheckImage
radio02['command'] = isCheckImage
radio03['command'] = isCheckImage
radio01.place(x=150, y=548)
radio02.place(x=150, y=568)
radio03.place(x=150, y=588)

# =============== ИЗОБРАЖЕНИЯ
# Размер поля
n = 4  # Ширина
m = 4  # Высота
# Размер "полного" изображения в пикселях
pictureWidth = 400
pictureHeight = 532

# Ширина и высота одного спрайта в пикселях
widthPic = pictureWidth / n
heightPic = pictureHeight / n

# Имена файлов без указания каталога
fileName = ['img01.png', 'img02.png', 'img03.png', 'img04.png',
            'img05.png', 'img06.png', 'img07.png', 'img08.png',
            'img09.png', 'img10.png', 'img11.png', 'img12.png',
            'img13.png', 'img14.png', 'img15.png', 'img16.png', 'black.png']

# Каталоги для изображений
imageBackground = []  # Активное изображение
imageBackground01 = []  # Киберпанк
imageBackground02 = []  # Природа
imageBackground03 = []  # Космос

# Добавляем в списки элементы и загружаем в них объекты PhotoImage
for name in fileName:
    imageBackground01.append(PhotoImage(file='image01/' + name))
    imageBackground02.append(PhotoImage(file='image02/' + name))
    imageBackground03.append(PhotoImage(file='image03/' + name))

# Номер изображения "пустого" поля
blackImg = 16
# Устанавливаем набор спрайтов "Киберпанк"
imageBackground = imageBackground01

# Метки Label
labelImage = []
# Математическая модель игрового поля
dataImage = []
# Копия модели поля для просмотра "Как должно быть"
copyData = []

for i in range(n):
    # Начинаем заполнять списки
    labelImage.append([])
    dataImage.append([])
    copyData.append([])

    for j in range(m):
        # Формула i * n + j сгенерирует ряд чисел
        # 0, 1, 2, 3, 4 и так далее
        # Это и есть номера "собранной версии изображения"
        dataImage[i].append(i * n + j)
        copyData[i].append(i * n + j)
        # Создаём и настраиваем Label,
        # в который будем выводить PhotoImage из imageBackground
        labelImage[i].append(Label(root, bg=back))
        labelImage[i][j]['bd'] = 1  # ['bd'] - опция размера контура вокруг изображения
        labelImage[i][j].place(x=10 + j * widthPic, y=10 + i * heightPic)

        # Что произойдёт при нажатии на Label
        labelImage[i][j].bind('<Button-1>',
                              lambda e, x=i, y=j: go(x, y))  # e чтобы перехватить event (но без обработки)
        # Устанавливаем изображение
        # ['image'] - отвечает за привязку (установку) изображения
        # (в нашем случае это объект PhotoImage) к Label
        labelImage[i][j]['image'] = imageBackground[dataImage[i][j]]

# ===== ХОДЫ

# Рекорды. Индекс == уровень сложности
steps = [0, 0, 0, 0, 0, 0]
# Началась ли игра?
playGame = False
# Список рекордов (наименьшее количество шагов для сбора)
record = getRecordSteps()

# Обновление текста меток статистики
refreshText()

# Обновляем изображения
resetPictures()
# =============== КОНЕЦ ПРОГРАММЫ
root.mainloop()
