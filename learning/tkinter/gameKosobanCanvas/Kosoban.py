# Информационный объект - это описание сущности в виде логически взаимосвязанных характеристик
# Существенные признаки - это параметры или характеристики, которые необходимы для текущей работы с объектами
#
# TODO:	Анимация ходьбы, Пол вне стен

from tkinter import *
from time import sleep
from winsound import Beep


def goCheat():
    """
	Чит. Установить ящики на цели и победить
	"""
    global moving
    print('Метод goCheat()')

    moving = True
    for i in range(len(boxes)):
        boxes[i][0] = finish[i][0]
        boxes[i][1] = finish[i][1]
        cnv.coords(boxes[i][2],
                   SQUARE_SIZE // 2 + boxes[i][1] * SQUARE_SIZE,
                   SQUARE_SIZE // 2 + boxes[i][0] * SQUARE_SIZE)
    cnv.update()
    sleep(2)
    checkBoxInFinish()


def nextLevelSet(btnNext: Button):
    """
	Кнопка "Continue"
	Активация следующего уровня
	"""
    global level

    level += 1
    cnv.focus_set()
    btnNext.destroy()
    btnCheat.place(x=10, y=590)
    btnReset.place(x=10, y=550)
    cnv.delete(ALL)
    reset()


def nextLevel():
    """
	Процедура смены уровня:
	- очистить экран от объектов
	- вывести таймер
	- вывести кнопку смены уровня
	"""
    print('Метод nextLevel()')

    # Очистить экран от всех canvas img
    cnv.delete(ALL)
    stopTimer()

    # Уводим кнопки за границы окна, чтобы они не мешали,
    btnCheat.place(x=-100, y=-100)  # пока на их месте будут другие
    btnReset.place(x=-100, y=-100)

    # Кнопка "Следующий уровень"
    btnNext = Button(text='Next Level',
                     font='Verdana, 19',
                     width=45)
    btnNext.place(x=300, y=550)
    btnNext.focus_set()
    btnNext['command'] = lambda b=btnNext: nextLevelSet(b)

    cnv.create_text(WIDTH * SQUARE_SIZE // 2,
                    200,
                    fill='#AAFFCC',
                    text=f'Mission complete! You solved it just for {getMinSec(second)}! Congratulations!',
                    font='Verdana, 25')


def checkBoxInFinish():
    """
	Проверка на победу. Все ящики на целях?
	"""
    global finish, win
    print('Метод checkBoxInFinish()')

    # Делаем все ящики "не на местах"
    for fin in finish:
        fin[3] = False

    win = True
    # Проверка каждой цели ящика с каждым ящиком
    fin = 0
    while fin < len(finish) and win:
        # Проверка каждого ящика с каждой целью ящика
        box = 0
        while box < len(boxes):
            # Если координаты цели ящиков и ящика совпадают
            if finish[fin][0:2] == boxes[box][0:2]:
                # То делаем этот ящик "на месте"
                finish[fin][3] = True
                # Прерывание внутреннего цикла
                box = len(boxes)
            # Если не совпали координаты, то далее проверяем следующий ящик
            box += 1
        # Если победа, то продолжаем, иначе не победа и прерывание цикла
        win = win and finish[fin][3]
        # Далее проверяем следующую цель ящиков
        fin += 1

    if win:
        Beep(750, 10)
        Beep(1750, 10)
        nextLevel()


def movePlayerBoxTo(x, y, count, numberBox):
    """
	Синхронная анимация движения игрока И ящика
	Принимает кол-во pxl (X,Y) в направлении движения
	и кол-во итераций (count)
	"""
    global moving

    count -= 1
    cnv.move(player[2], x, y)
    # Анимация движения ящика
    cnv.move(boxes[numberBox][2], x, y)

    if count > 0:
        moving = True
        root.after(20, lambda x=x,
                              y=y,
                              c=count,
                              n=numberBox:  # Номер передвигаемого ящика в boxes[[]]
        movePlayerBoxTo(x, y, c, n))
    else:
        print('Метод movePlayerBoxTo() выполнился')
        moving = False
        checkBoxInFinish()


def movePlayerTo(x, y, count):
    """
	Анимация движения игрока.
	Принимает кол-во pxl (X,Y) в направлении движения
	и кол-во итераций (count)
	"""
    global moving

    # Минус итерация
    count -= 1
    # Двигать canvas
    cnv.move(player[2], x, y)

    if count > 0:  # Если остались итерации
        moving = True  # Анимация движения происходит
        # TODO: Изучить lambda
        root.after(20,  # Цикл перемещения каждые 20 млс
                   lambda x=x,  # Смещение "за раз" по оси X
                          y=y,  # Смещение "за раз" по оси Y
                          c=count:  # Кол-во смещений
                   movePlayerTo(x, y, c))
    else:
        print(f'Метод movePlayerTo({x}, {y}, {count}) выполнился')
        # Анимация движения не происходит
        moving = False


def getBox(x, y):
    """
	Возвращает номер ящика (строку)
 	по координатам x,y в boxes[x][y].
	Если по x,y нет ящика, то None
	"""
    print('Метод getBox()')
    # i - Номер ящика в boxes[[]]
    for i in range(len(boxes)):
        if boxes[i][0] == x and boxes[i][1] == y:
            return i
    return None


def getNumber(x, y):
    """
	Возвращает информацию о наличии объекта
 	по координатам x,y в dataLevel[x][y]
	"""
    print('Метод getNumber()')

    # Есть ли ящик в dataLevel[x][y]?
    for box in boxes:
        if box[0] == x and box[1] == y:
            return 2
    # Если нет, то возвращаем 0 или 1
    if dataLevel[x][y] <= 1:
        return dataLevel[x][y]


def move(v):
    """
	Проверка пути. Движение игрока, ящика.
	"""
    print(f'Метод move({v})')

    # Если УЖЕ идёт анимация движения
    if moving:
        return 0

    # Удалить img предыдущего хода
    cnv.delete(player[2])  # [2] - ID canvas
    # Установить img игрока в сторону ходьбы (v)
    player[2] = cnv.create_image(SQUARE_SIZE // 2 + player[1] * SQUARE_SIZE,
                                 SQUARE_SIZE // 2 + player[0] * SQUARE_SIZE,
                                 image=img[4][v])

    x = player[0]  # Координата X img игрока в мат. модели
    y = player[1]  # Координата Y img игрока в мат. модели
    Beep(625, 10)  # Звук ходьбы

    if v == UPKEY:  # Если передано направление (v) движения ВВЕРХ
        # То проверить следующую координату вверх
        check = getNumber(x - 1, y)
        if check == 0:  # Если там пусто (0)
            # Движение img Player[2][v] 8 раз по 8 pxl вверх
            movePlayerTo(0, -8, 8)
            # Обновление координаты X в информационной модели игрока
            player[0] -= 1
        elif check == 2:  # Если там Ящик (2)
            # То проверить СЛЕДУЮЩУЮ ПОСЛЕ ЯЩИКА координату вверх
            nextCheck = getNumber(x - 2, y)
            if nextCheck == 0:  # Если там пусто (0)
                # Получить номер строки ящика (выше) в списке boxes[x][y]
                numberBox = getBox(x - 1, y)
                # Запуск анимации движения игрока и ящика вверх
                movePlayerBoxTo(0, -8, 8, numberBox)
                player[0] -= 1
                # Обновление координаты X в информационной модели ящика
                boxes[numberBox][0] -= 1
    elif v == DOWNKEY:  # Если передано направление (v) движения ВНИЗ
        check = getNumber(x + 1, y)
        if check == 0:
            movePlayerTo(0, 8, 8)
            player[0] += 1
        elif check == 2:
            nextCheck = getNumber(x + 2, y)
            if nextCheck == 0:
                numberBox = getBox(x + 1, y)
                movePlayerBoxTo(0, 8, 8, numberBox)
                player[0] += 1
                boxes[numberBox][0] += 1
    elif v == LEFTKEY:  # Если передано направление (v) движения ВЛЕВО
        check = getNumber(x, y - 1)
        if check == 0:
            movePlayerTo(-8, 0, 8)
            player[1] -= 1
        elif check == 2:
            nextCheck = getNumber(x, y - 2)
            if nextCheck == 0:
                numberBox = getBox(x, y - 1)
                movePlayerBoxTo(-8, 0, 8, numberBox)
                player[1] -= 1
                boxes[numberBox][1] -= 1
    elif v == RIGHTKEY:  # Если передано направление (v) движения ВПРАВО
        check = getNumber(x, y + 1)
        if check == 0:
            movePlayerTo(8, 0, 8)
            player[1] += 1
        elif check == 2:
            nextCheck = getNumber(x, y + 2)
            if nextCheck == 0:
                numberBox = getBox(x, y + 1)
                movePlayerBoxTo(8, 0, 8, numberBox)
                player[1] += 1
                boxes[numberBox][1] += 1


def getMinSec(s):
    """
	Возвращает строку в виде ММ:СС (мин:сек)
	"""

    intMin = s // 60
    intSec = s % 60
    textSecond = str(intSec)

    if intMin > 59:
        intMin %= 60
    if intSec < 10:
        textSecond = '0' + textSecond
    if intMin == 0:
        return f'{textSecond} sec.'
    else:
        textMin = str(intMin)
        if intMin < 10:
            textMin = '0' + textMin
        return f'{textMin} min. {textSecond} sec.'


def updateText():
    """
	Обновление полоски с текстом вверху
	"""
    global textTime, second, timeRun

    second += 1
    cnv.delete(textTime)
    txt = f'Level: {level}	Time: {getMinSec(second)}'
    textTime = cnv.create_text(10,  # X относительно canvas
                               10,  # Y относительно canvas
                               fill='#ffffff',  # Цвет текста
                               anchor='nw',  # Выравнивание по левому краю
                               text=txt,  # Текстовая надпись
                               font='Verdana, 15')  # Шрифт и размер
    timeRun = root.after(1000, updateText)


def createLevel():
    """
	Рисует в Canvas новый загруженный уровень,
	на основе математической модели из файла level??.dat
	"""
    global player, boxes, finish
    print('Метод createLevel()')

    # Создание списков для информационных моделей:
    player = []  # Игрока
    boxes = []  # Ящиков
    finish = []  # Целей ящиков

    # Координата X тайловой матрицы модели игры
    for i in range(len(dataLevel)):
        # Координата Y
        for j in range(len(dataLevel[i])):
            # Если по координатам будет 1 (-СТЕНА в математической модели),
            if dataLevel[i][j] == 1:  # то выведи img стены по координатам
                # (// 2 т.к Canvas устанавливается по координатам центра)
                cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                 SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                 # Установить img wall.png
                                 image=img[0])
            # Если по координатам будет 3 (-ЦЕЛЬ ЯЩИКОВ),
            elif dataLevel[i][j] == 3:  # то выведи img цели по координатам
                dataLevel[i][j] = 0  # Сделай эту область доступной для прохода,
                finish.append([i, j,  # Добавь в список координаты объекта
                               cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,  # X в canvas
                                                SQUARE_SIZE // 2 + i * SQUARE_SIZE,  # Y
                                                # Установить img finish.png
                                                image=img[2]),
                               # Ящик не там
                               False])

            if dataLevel[i][j] == 2:  # ЯЩИК в математической модели
                dataLevel[i][j] = 0
                boxes.append([i, j,
                              cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                               SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                               # Установить img box.png
                                               image=img[1])])
            elif dataLevel[i][j] == 4:  # ИГРОК
                dataLevel[i][j] = 0
                player = [i, j,
                          cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                           SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                           # Установить img player.png
                                           image=img[4][1])]
            elif dataLevel[i][j] == 5:  # ФОН
                cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                 SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                 # Установить img outside.png
                                 image=img[3])
    print(finish)


def clear_setGrass():
    """
	Замостить grass.png всю область окна
	"""
    print('Метод clear_setGrass()')

    # Удалить все с полотна Canvas
    cnv.delete(ALL)
    # alg Вывода изображений на Canvas по координатам
    for i in range(WIDTH):  # 20
        for j in range(HEIGHT):  # 10
            # // 2 т.к Canvas устанавливается по координатам центра
            cnv.create_image(SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                             SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                             # Установить img outside.png
                             image=background)


def getLevel(lvl):
    """
	Загрузка данных уровня
	"""
    global dataLevel
    print('Метод getLevel()')

    # Математическая модель
    dataLevel = []
    # Временный список
    tmp = []
    # Для запуска следующего уровня,
    nextLevel = lvl + 1  # в случае ошибки.

    # Для работы с именами файлов
    idx = str(lvl)
    if lvl < 10:
        idx = f'0{lvl}'

    try:  # Открытие файла уровня level в папке levels
        f = open(f'levels/level{idx}.dat', 'r', encoding='utf-8')
        for i in f.readlines():
            tmp.append(i.replace('\n', ''))
        f.close()
        for i in range(len(tmp)):
            dataLevel.append([])
            for j in tmp[i]:
                dataLevel[i].append(int(j))
    except:
        print('Не найден файл с данными.')
        print(f'Включаю уровень {lvl + 1}')
        # TODO: Обработать исключения
        getLevel(lvl + 1)


def stopTimer():
    """
	Остановка таймера
	"""
    global timeRun

    if timeRun != None:
        root.after_cancel(timeRun)
        timerRun = None


def reset():
    """
	Рестарт. Сброс текущей и начало новой игры, с новыми параметрами.
	Активация при запуске, сбрасывания поля, загрузке следующего уровня
	"""
    global moving, second, timeRun
    print('Метод reset()')

    # Анимация просиходит в данный моменит?
    moving = False
    # Обнуление таймера
    second = -1  # TODO: Переделать, чтобы было second = 0

    stopTimer()
    # Загрузка из файла следующего уровня
    getLevel(level)
    # Установить начальную фоновую текстуру
    clear_setGrass()
    # Создание новоего уровня
    createLevel()
    # Обновление метки и запуск таймера
    updateText()


# === === === === === НАЧАЛО ПРОГРАММЫ === === === === ===
root = Tk()
root.resizable(False, False)
root.title('Оригинальная игра про двигание ящиков v. 3.3672 alpha beta super')
root.iconbitmap('icon/icon.ico')

# 20х10 спрайтов - площадь открываемого окна
WIDTH = 20
HEIGHT = 10
# 1 спрайт == 64x64 pxl
SQUARE_SIZE = 64

POS_X = root.winfo_screenwidth() // 2 - (WIDTH * SQUARE_SIZE) // 2
POS_Y = root.winfo_screenheight() // 2 - (HEIGHT * SQUARE_SIZE) // 2
root.geometry(f'{WIDTH * SQUARE_SIZE + 0}x{HEIGHT * SQUARE_SIZE + 0}+{POS_X}+{POS_Y}')

# Создание виджета Canvas
cnv = Canvas(root, width=WIDTH * SQUARE_SIZE, height=HEIGHT * SQUARE_SIZE, bg='#373737')
# Убрать автоматическую рамку вокруг Canvas
cnv.config(highlightthickness=0)
# Установка в область окна
cnv.place(x=0, y=0)
# Привязывание событий к canvas
cnv.focus_set()

# Кодировка кнопок константами
# для повышения читаемости кода
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Назначение клавиш управления курсором
cnv.bind('<Up>', lambda e, x=UPKEY: move(x))
cnv.bind('<Down>', lambda e, x=DOWNKEY: move(x))
cnv.bind('<Left>', lambda e, x=LEFTKEY: move(x))
cnv.bind('<Right>', lambda e, x=RIGHTKEY: move(x))

# Есть ли движение?
moving = True

# Загрузка из файлов изображений
background = PhotoImage(file='image/ground.png')  # Земля
img = []  # Список с изображениями:
img.append(PhotoImage(file='image/wall.png'))  # Стена
img.append(PhotoImage(file='image/box.png'))  # Ящик
img.append(PhotoImage(file='image/finish.png'))  # Цель ящиков
img.append(PhotoImage(file='image/back.png'))  # Фон
IMAGE_PLAYER = 4  # Константа для удобства
img.append([])  # Игрок смотрит:
img[IMAGE_PLAYER].append(PhotoImage(file='image/kosoban_up.png'))  # Вверх
img[IMAGE_PLAYER].append(PhotoImage(file='image/kosoban_down.png'))  # Вниз
img[IMAGE_PLAYER].append(PhotoImage(file='image/kosoban_left.png'))  # Влево
img[IMAGE_PLAYER].append(PhotoImage(file='image/kosoban_right.png'))  # Вправо

# список с информационной моделью игрока
# [0] == X, [1] == Y, [2] == img
player = None
# 2D список с инф. моделью ящика
# [0] == X, [1] == Y, [2] == img
boxes = None
# 2D список с инф. моделью цели для ящика
# [0] == X, [1] == Y, [2] == img,
# [3] == True/False (Установлен ли ящик?)
finish = None
# Выиграл ли игрок?
win = False
# Отображение таймера
textTime = None
second = None
# Начальный уровень
level = 5
# Математическая модель уровня
dataLevel = []
# Объект для хранения вызова .after()
timeRun = None

# Кнопка "Сбросить поле"
btnReset = Button(text='Restart'.upper(),
                  font=('Consolas', '15'),
                  width=20)
btnReset.place(x=10, y=550)
btnReset['command'] = reset
# Кнопка-чит "Установить ящики"
btnCheat = Button(text='Win'.upper(),
                  font=('Consolas', '15'),
                  width=20)
btnCheat.place(x=10, y=590)
btnCheat['command'] = goCheat

reset()
# === === === === === КОНЕЦ ПРОГРАММЫ === === === === ===
root.mainloop()
