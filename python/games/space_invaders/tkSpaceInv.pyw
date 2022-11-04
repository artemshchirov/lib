# TODO: Добавить анимацию фона

from tkinter import *
from random import randint
from time import sleep
from winsound import Beep


# Очистить всё и начать игру заново
def continueAfterPause():
    btnContinueAfterPause.destroy()
    saveScores(scores)
    cnv.delete(ALL)
    showMenu()
    restartGame()

# Запись очков в файл
def endTableScore(inputWindow, positionPlayer):
    global playerName, scores
    root.deiconify()
    inputWindow.destroy()
    playerName = playerName.get()
    if (playerName == ""):
        playerName = defaultName
    scores[positionPlayer][0] = playerName
    continueAfterPause()


# Фильтрация вводимых знаков
def inputNameFilter(event):
    global playerName
    filter = "_-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    pN = ""
    for i in playerName.get():
        if (i.upper() in filter):
            pN += i
    if (len(pN) > 20):
        pN = pN[0:20]
    elif (pN == ""):
        pN = defaultName
    playerName.set(pN)


# Окно для ввода имени
def getPlayerName(positionPlayer):
    global playerName

    inputWindow = Toplevel(root)      # Окно верхнего уровня
    inputWindow.grab_set()            # Запрещаем изменять root

    # Настраиваем окно
    X_NEW = root.winfo_screenwidth() // 2 - 150
    Y_NEW = root.winfo_screenheight() // 2 - 260
    inputWindow.geometry(f"{300}x{120}+{X_NEW}+{Y_NEW}")
    inputWindow.overrideredirect(True)
    inputWindow.focus_set()

    Label(inputWindow, text="Вы - один из лучших! Введите ник:").place(x=13, y=10)

    playerName = StringVar()
    playerName.set(defaultName)
    newName = Entry(inputWindow, textvariable=playerName, width=45)
    newName.place(x=13, y=40)
    newName.focus_set()
    newName.select_range(0, END)
    newName.bind("<KeyRelease>", inputNameFilter)

    btnGo = Button(inputWindow, text="Продолжить...", width=38)
    btnGo.place(x=13, y=70)
    btnGo["command"] = lambda iW=inputWindow, posP=positionPlayer: endTableScore(iW, posP)


# Находим номер игрока в списке лучших
def sortScoreTable(score):
    global scores

    name = playerName
    if (playerName == None):
        name = "Вы"

    scores.append([name, score])

    positionPlayer = 10
    # Переносим игрока как можно выше в таблице
    # в зависимости от очков (принцип "пузырьковой сортировки",
    # попарное сравнение и обмен)
    for i in range(len(scores) - 1, 0, -1):
        if (scores[i][1] > scores[i - 1][1]):
            scores[i][0], scores[i - 1][0] = \
                scores[i - 1][0], scores[i][0]
            scores[i][1], scores[i - 1][1] = \
                scores[i - 1][1], scores[i][1]
            positionPlayer -= 1

    # Удаляем последний элемент
    del scores[10]

    if (positionPlayer < 10 and
            playerName == None):
        getPlayerName(positionPlayer)
    return positionPlayer


# Конец игры
def endGame():
    global playGame, btnContinueAfterPause, score
    playGame = False
    root.focus_set()
    cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)
    cnv.create_text(160, 80,
                    fill="#FFFFFF",
                    anchor="nw",
                    font=f", 22",
                    text=f"КОНЕЦ ИГРЫ. ЛУЧШИЕ ИГРОКИ:")
    score -= penalty
    showScores(sortScoreTable(int(score)))
    btnContinueAfterPause = Button(root, text="Продолжить", width=70)
    btnContinueAfterPause.place(x=140, y=HEIGHT - 50)
    btnContinueAfterPause["command"] = continueAfterPause


# Геттер - координата X инопланетянина obj
def getInvadersX(obj):
    return cnv.coords(obj[0])[0]


# Геттер - координата Y инопланетянина obj
def getInvadersY(obj):
    return cnv.coords(obj[0])[1]


# Геттер - координата X игрока
def getPlayerX():
    return cnv.coords(player[0])[0]


# Геттер - координата Y игрока
def getPlayerY():
    return cnv.coords(player[0])[1]


# Геттер - координата X ракеты
def getRocketX():
    return cnv.coords(rocketObject)[0]


# Геттер - координата Y ракеты
def getRocketY():
    return cnv.coords(rocketObject)[1]


# Обновляем инфостроку
def updateInfoLine():
    global informationLine
    if (informationLine != None):
        for i in informationLine:
            cnv.delete(i)

    informationLine = []
    informationLine.append(cnv.create_text(20,
                                           440,
                                           fill="#ABCDEF",
                                           anchor="nw",
                                           font=f", 12",
                                           text=f"ОЧКИ: {int(score)}"))

    informationLine.append(cnv.create_text(170,
                                           440,
                                           fill="#ABCDEF",
                                           anchor="nw",
                                           font=f", 12",
                                           text=f"ВРАГИ: {len(invadersObject)}"))

    informationLine.append(cnv.create_text(320,
                                           440,
                                           fill="#ABCDEF",
                                           anchor="nw",
                                           font=f", 12",
                                           text=f"ЖИЗНИ: {lives}"))

    informationLine.append(cnv.create_text(480,
                                           440,
                                           fill="#ABCDEF",
                                           anchor="nw",
                                           font=f", 12",
                                           text=f"УРОВЕНЬ: {level}"))

    informationLine.append(cnv.create_text(650,
                                           440,
                                           fill="#ABCDEF",
                                           anchor="nw",
                                           font=f", 12",
                                           text=f"ШТРАФЫ: -{penalty}"))


# Запись очков в файл
def saveScores(scoresToFile):
    # Данные нужны в формате: [str: Ник, int: Очки]
    try:
        f = open("scores.dat", "w", encoding="utf-8")
        for sc in scoresToFile:
            f.write(f"{sc[0]} {sc[1]}\n")
        f.close()
    except:
        print("Что-то пошло не так.")


# Загрузка очков из scores.dat
def loadScores():
    ret = []
    try:
        f = open("scores.dat", "r", encoding="utf-8")
        for sc in f.readlines():
            s = sc.replace("\n", "")
            # Преобразовываем в список
            s = s.split(" ")

            # Проверяем. Защита от дурака на длину ника
            if (len(s[0]) > 20):
                s[0] = s[0][0:20]
            elif (s[0] == ""):
                s[0] = defaultName

            # Проверяем. Защита от дурака на очки
            s[1] = int(s[1])
            if (s[1] > 1000000):
                s[1] = 1000000
            elif (s[1] < 0):
                s[1] = 0
            ret.append(s)
        f.close()
    except:
        print("Файла не существует.")

    if (len(ret) != 10):
        ret = []
        for i in range(10):
            ret.append([defaultName, 0])
        saveScores(ret)
    return ret


# Удаляем таблицу очков
def hideScores():
    global textScores
    for i in textScores:
        cnv.delete(i)


# Рисуем таблицу очков
def showScores(numberPlayer):
    global textScores
    textScores = []
    for i in range(len(scores)):
        if (i == numberPlayer):
            colorText = "#00FF55"
        else:
            colorText = "#AA9922"
        textScores.append(cnv.create_text(210,
                                          170 + i * 22,
                                          fill=colorText,
                                          font=", 14",
                                          text=str(i + 1)))  # Номер
        textScores.append(cnv.create_text(240,
                                          170 + i * 22,
                                          fill=colorText,
                                          anchor="w",
                                          font=", 14",
                                          text=scores[i][0]))  # Ник
        textScores.append(cnv.create_text(590,
                                          170 + i * 22,
                                          fill=colorText,
                                          anchor="e",
                                          font=", 14",
                                          text=scores[i][1]))  # Очки


# Показываем кнопки меню
def showMenu():
    global menu1, menu2, onMenu
    if (not onMenu):
        menu1.place(x=235, y=37)
        menu2.place(x=235, y=97)
        # Показываем таблицу очков
        showScores(-1)
        onMenu = True
    else:
        hideMenu()


# Скрываем кнопки меню, меняя их координаты
def hideMenu():
    global menu1, menu2, onMenu
    if (onMenu):
        menu1.place(x=-100, y=-100)
        menu2.place(x=-100, y=-100)
        onMenu = False
        # Скрываем таблицу очков
        hideScores()
    else:
        showMenu()


# Анимация вражеской ракеты
def animationInvadersRocket():
    global invadersRocket, \
        invadersRocketSpeed, \
        lives

    if (not playGame):
        invadersRocket = None
        invadersRocketSpeed = invadersRocketSpeedDefault
        return 0

    cnv.move(invadersRocket, invadersSpeed / 2, int(invadersRocketSpeed))

    invadersRocketSpeed *= invadersRocketSpeedScale

    x = cnv.coords(invadersRocket)[0]
    y = cnv.coords(invadersRocket)[1]

    # Рассчитываем попадание в игрока
    if (y > getPlayerY() - SQUARE_SIZE // 2):
        if (x > getPlayerX() - SQUARE_SIZE and
                x < getPlayerX() + SQUARE_SIZE):
            animationExplosion(7,
                               getPlayerX(),
                               getPlayerY())
            Beep(400, 2)
            Beep(550, 2)
            Beep(570, 3)
            y = HEIGHT
            lives -= 1
            cnv.coords(player[0], WIDTH // 2, getPlayerY())

    if (y < HEIGHT):
        root.after(20, animationInvadersRocket)
    else:
        cnv.delete(invadersRocket)
        invadersRocket = None
        invadersRocketSpeed = invadersRocketSpeedDefault


# Стартуем ракету врага
def startInvadersRocket():
    global invadersRocket
    if (not playGame):
        return 0

    if (len(invadersObject) > 0):
        n = randint(0, len(invadersObject) - 1)
        Beep(1200, 40)
        invadersRocket = cnv.create_image(getInvadersX(invadersObject[n]),
                                          getInvadersY(invadersObject[n]),
                                          image=invadersRocketTexture)
        root.after(20, animationInvadersRocket)


# Анимация взрыва
def animationExplosion(frame, x, y):
    if (not playGame):
        return 0

    tempExpl = cnv.create_image(x, y, image=explosionTexture[frame])
    if (frame > -1):
        root.after(10, lambda frame=frame - 1,
                              x=x,
                              y=y: animationExplosion(frame, x, y))
    cnv.update()
    sleep(0.01 + frame / 1000)
    cnv.delete(tempExpl)


# Старт анимации взрыва
def startExplosion(n):
    global invadersObject
    if (not playGame):
        return 0
    Beep(650, 20)
    animationExplosion(7,
                       getInvadersX(invadersObject[n]),
                       getInvadersY(invadersObject[n]))
    invadersObject[n][1] -= 1
    if (invadersObject[n][1] < 0):
        cnv.delete(invadersObject[n][0])
        # Уничтожаем объект - инопланетятина,
        # удаляя его из списка
        del invadersObject[n]


# Анимация ракеты
def animationShoot(frame):
    global rocketObject, \
        rocketSpeedY, \
        penalty, \
        score, \
        player

    if (not playGame):
        rocketObject = None
        rocketSpeedY = rocketSpeedYDefault
        return 0

    cnv.move(rocketObject, 5, -rocketSpeedY)
    rocketSpeedY *= rocketScale

    x = getRocketX()
    y = getRocketY()
    frame += 1
    if (frame > len(rocketTexture) - 1):
        frame = 0
    sleep(0.02)
    # Удаляем объект и создаём с новой текстурой
    cnv.delete(rocketObject)
    rocketObject = cnv.create_image(x,
                                    y,
                                    image=rocketTexture[frame])

    if (cnv.coords(rocketObject)[1] < maxY + SQUARE_SIZE):
        rocketX = getRocketX()
        rocketY = getRocketY()
        find = 0
        while (find < len(invadersObject)):
            invadersX = getInvadersX(invadersObject[find])
            invadersY = getInvadersY(invadersObject[find])
            # Коэффициент 0.4 - чем меньше, тем точнее надо попасть
            if (abs(invadersX - rocketX) < SQUARE_SIZE * 0.4 and
                    abs(invadersY - rocketY) < SQUARE_SIZE * 0.8):
                score += 50 * (level + 1)
                startExplosion(find)
                y = -1
                find = len(invadersObject)
                penalty -= 5
            find += 1
    if (y > 0):
        # Рекурсивно вызываем анимацию
        root.after(3, lambda frame=frame: animationShoot(frame))
    else:
        Beep(700, 20)
        # Удаляем ракету по окончании анимации
        cnv.delete(rocketObject)
        # Увеличиваем штраф, независимо от попадания
        # P.S. Уменьшаем на 5, когда ракета поразила цель
        penalty += 5
        # Устанавливаем 1 "заряд" для игрока
        player[1] += 1
        rocketSpeedY = rocketSpeedYDefault


# При нажатии на пробел - выстрел
def shoot():
    global player, rocketObject
    if (not playGame or
            onMenu):
        return 0
    if (player[1] == 0):
        return 0
    player[1] -= 1

    rocketObject = cnv.create_image(getPlayerX(),
                                    getPlayerY(),
                                    image=rocketTexture[0])
    root.after(10, lambda frame=0: animationShoot(frame))


# Перемещение игрока
def move(x):
    if (not playGame or
            onMenu):
        return 0
    if (x == LEFTKEY):
        cnv.move(player[0], -playerSpeed, 0)
    elif (x == RIGHTKEY):
        cnv.move(player[0], playerSpeed, 0)

    if (getPlayerX() < SQUARE_SIZE):
        cnv.move(player[0], playerSpeed, 0)
    elif (getPlayerX() > WIDTH - SQUARE_SIZE):
        cnv.move(player[0], -playerSpeed, 0)

# Переключение на следующий уровень
def next():
    global level, \
        playGame
    cnv.delete(ALL)
    level += 1
    playGame = True
    reset()

# Конец уровня
def endLevel():
    global playGame
    playGame = False
    cnv.delete(ALL)
    cnv.create_text(WIDTH // 2, HEIGHT // 2,
                    fill="#FFFFFF",
                    font=f", 15",
                    text=f"ПОБЕДА! ЗАГРУЖАЕМ СЛЕДУЮЩИЙ УРОВЕНЬ!")
    # Забираем фокус с Canvas чтобы не работали кнопки
    root.focus_set()
    root.update()
    Beep(randint(850, 1000), 400)
    sleep(0.01)
    Beep(randint(750, 1000), 200)
    sleep(0.03)
    Beep(randint(950, 1000), 600)
    sleep(0.07)
    Beep(randint(850, 1000), 500)
    sleep(0.5)
    root.after(300, nextLevel)

# Главный цикл игры
def mainloop():
    global invadersObject, \
        leftInvadersBorder, \
        rightInvadersBorder, \
        invadersSpeed, \
        playGame, \
        score, \
        maxY, \
        frame

    # Если список врагов пуст, то есть они все уничтожены
    if (len(invadersObject) == 0):
        endLevel()

    # Не выполняем mainloop(), если нет игры
    if (not playGame):
        return 0

    # Перерисовываем текстуры
    for obj in invadersObject:
        cnv.move(obj[0], int(invadersSpeed), 0)
        xPos = getInvadersX(obj)
        yPos = getInvadersY(obj)
        cnv.delete(obj[0])
        obj[0] = cnv.create_image(xPos,
                                  yPos,
                                  image=invadersTexture[obj[1] * 2 + frame])
    # Меняем кадр
    frame += 1
    if (frame > 1):
        frame = 0

    # Изменяем левую и правую границу
    # инопланетного массива
    leftInvadersBorder += int(invadersSpeed)
    rightInvadersBorder += int(invadersSpeed)

    # Запуск ракеты инопланетян
    if (randint(0, 150) < abs(invadersSpeed) and
            invadersRocket == None):
        startInvadersRocket()

    # Проверяем для изменения направления движения
    # самую левую точку X и самую правую точку X
    # прямоугольного блока с инопланетянами
    if (rightInvadersBorder > WIDTH - SQUARE_SIZE or
            leftInvadersBorder < SQUARE_SIZE):
        invadersSpeed *= 1.1
        invadersSpeed = -invadersSpeed
        maxY = 0
        # Перебираем все элементы, т.к. нижние линии в какой-то
        # момент могут быть уничтожены. Поэтому недостаточно взять координату
        # "нижних" элементов математически, умножив размер спрайта
        # на количество линий инопланетных кораблей
        for obj in invadersObject:
            cnv.move(obj[0], 0, SQUARE_SIZE)
            # Находим максимальную "нижнюю" точку блока инопланетян
            if (cnv.coords(obj[0])[1] + SQUARE_SIZE // 2 > maxY):
                maxY = cnv.coords(obj[0])[1] + SQUARE_SIZE // 2

    # Скорость обновления главного цикла: 100 миллисекунд,
    # то есть 10 (десять) кадров в секунду
    root.after(100, mainloop)
    score -= .1
    updateInfoLine()

    # Если инопланетяне придавили игрока или
    # жизней не осталось совсем
    if (maxY > getPlayerY() or lives < 0):
        endGame()

# Нажатие на кнопку "Старт"
def startGame():
    global playGame
    if (playGame):
        hideMenu()
        return 0
    playGame = True
    hideMenu()
    mainloop()


# Сброс всего подчистую с установкой первого уровня
def globalReset():
    global level, \
        score, \
        penalty, \
        playGame, \
        playerSpeed, \
        lives
    playGame = False
    playerSpeed = 5
    level = 11
    score = 0
    penalty = 0
    lives = 3


# Перезапуск игры полностью
def restartGame():
    globalReset()
    reset()
    showScores(-1)


# Сброс и формирование объектов игрового мира
def reset():
    global invadersObject, \
        invadersWidth, \
        invadersHeight, \
        invadersSpeed, \
        leftInvadersBorder, \
        rightInvadersBorder, \
        player, \
        maxY, \
        rocketObject, \
        invadersRocket

    cnv.delete(ALL)  # Очищаем канвас
    cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)  # Создаём фон (нижний слой)
    cnv.focus_set()  # Устанавливаем фокус для перехвата нажатий клавиш на клавиатуре

    rocketObject = None  # Игрок "не пустил" ракету
    invadersRocket = None  # Инопланетяне "не пустили" ракету
    invadersSpeed = 3 + level // 5  # Рассчитываем скорость движения инопланетян

    # Рассчитываем количество инопланетян по ширине и высоте
    invadersWidth = (1 + int(level // 3)) * 2
    invadersHeight = 2 + (level // 4)
    if (invadersWidth > 14):
        invadersWidth = 14
    if (invadersHeight > 8):
        invadersHeight = 8

    # Рассчитываем максимальную точку Y (нижняя линия
    # блока инопланетян). Необходимо, потому что последующие
    # расчёты происходят по мере смещения инопланетян по Y
    maxY = (invadersHeight - 1) * 10 + SQUARE_SIZE * invadersHeight + SQUARE_SIZE // 2

    invadersObject = []
    for i in range(invadersWidth):
        for j in range(invadersHeight):
            # Уровень врага: 0 - слабый, 2 - сильный
            rang = randint(0, level // 8)
            if (rang > 2):
                rang = 2
            posX = SQUARE_SIZE // 2 + \
                   (WIDTH // 2 - (invadersWidth * (SQUARE_SIZE + 10)) // 2) + \
                   i * SQUARE_SIZE + i * 10
            posY = 20 + j * 10 + j * SQUARE_SIZE
            # rang умножаем на 2 потому что каждая вторая текстура - текстура для анимации,
            # то есть нужны только изображения по индексам 0, 2, 4
            invadersObject.append([cnv.create_image(posX, posY, image=invadersTexture[rang * 2]),
                                   rang])

    # Вычисляем левую и правую границы блока инопланетян:
    # левая граница - координаты объекта в списке с индексом [0] (левый верхний инопланетянин)
    # правая граница - координаты последнего объекта (правый нижний инопланетянин)
    leftInvadersBorder = cnv.coords(invadersObject[0][0])[0]
    rightInvadersBorder = cnv.coords(invadersObject[len(invadersObject) - 1][0])[0]

    # Космический корабль игрока на Canvas и количество выстрелов
    player = [cnv.create_image(WIDTH // 2, HEIGHT - SQUARE_SIZE * 2, image=playerTexture), 1]

    updateInfoLine()  # Обновляем информационный текст внизу экрана
    mainloop()  # Запускаем игру


# Создание окна
root = Tk()
root.resizable(False, False)
root.title("Вторжение инопланетян")
# Иконка, изготовлено на сайте https://www.favicon.by/
root.iconbitmap("icon/icon.ico")

# Ширина и выота окна
WIDTH = 800
HEIGHT = 480

# Размер одного спрайта
SQUARE_SIZE = 32

# Настраиваем окно
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Канвас
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)

# Текстура фона
backGround = PhotoImage(file="image/background.png")

# ============== ИНОПЛАНЕТЯНЕ ==================
# Имена файлов с текстурами инопланетян
invadersFile = ["inv01.png", "inv01_move.png",
                "inv02.png", "inv02_move.png",
                "inv03.png", "inv03_move.png"]

# Загружаем текстуры
invadersTexture = []
for fileName in invadersFile:
    invadersTexture.append(PhotoImage(file=f"image/{fileName}"))

# Список для информационных объектов:
# Индекс [0] - Текстура
# Индекс [1] - Уровень
invadersObject = None
invadersSpeed = None  # Скорость перемещения инопланетян

leftInvadersBorder = None   # Левая и
rightInvadersBorder = None  # правая границы блока инопланетян в пикселях
                            # Необходимы для смены движения

maxY = None  # Самая нижняя точка Y расположения текстур инопланетян
invadersWidth = None  # Количество "столбцов" инопланетян
invadersHeight = None  # Количество "строк" инопланетян

# ============== ИГРОК =====================
playerTexture = PhotoImage(file="image/player.png")  # Текстура корабля игрока
player = None  # Объект для игрока на Canvas
playerSpeed = None  # Скорость смещения при нажатии на клавишу управления курсором

# Константы-коды для направления движения
LEFTKEY = 0
RIGHTKEY = 1

# Назначаем клавиши управления курсором
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))
cnv.bind("<space>", lambda e: shoot())
cnv.bind("<Escape>", lambda e: showMenu())

# Спрайты ракеты, выпускаемой инопланетянами
invadersRocketTexture = PhotoImage(file="image/rocket/rocket_invaders.png")
invadersRocket = None  # Объект на Canvas инопланетной ракеты
invadersRocketSpeedScale = 1.05  # Увеличение скорости с каждым "кадром"
invadersRocketSpeedDefault = 1  # Скорость по умолчанию
invadersRocketSpeed = invadersRocketSpeedDefault  # Скорость ракеты. Больше - быстрей

# Загружаем текстуры боевой ракеты (изменяется лишь пламя из сопла)
rocketFiles = ["rocket01.png", "rocket02.png", "rocket03.png", "rocket04.png"]
rocketTexture = []
for fileName in rocketFiles:
    rocketTexture.append(PhotoImage(file=f"image/rocket/{fileName}"))

rocketObject = None  # Боевая ракета, которой стреляет игрок: объект на Canvas
rocketSpeedYDefault = 8  # Скорость ракеты по умолчанию. Больше - быстрей
rocketSpeedY = rocketSpeedYDefault  # Cкорость ракеты по Y
rocketScale = 1.05  # Коэффициент ускорения выпущенной игроком ракеты

# ============= ТЕКСТУРЫ ВЗРЫВА ===============
explosionFiles = ["expl01.png", "expl02.png", "expl03.png", "expl04.png",
                  "expl05.png", "expl06.png", "expl07.png", "expl08.png"]
explosionTexture = []
for fileName in explosionFiles:
    explosionTexture.append(PhotoImage(file=f"image/expl/{fileName}"))

level = None  # Текущий уровень игры, задаётся в globalReset()
frame = 0  # Кадр анимации для инопланетян

# =============== НАСТРОЙКИ ИГРОКА ============
score = 0  # Очки игрока
penalty = 0  # Штрафы за промахи
lives = 3  # Жизни
playGame = False  # Игра "Нет игры" или True - "Игра началась"
defaultName = "Anonymous"

# ============= МЕНЮ ИГРЫ ==============
# Кнопка "Старт"
menu1 = Button(root, text="Старт", font=", 20", width=20)
menu1.place(x=-100, y=-100)
menu1["command"] = startGame

# Кнопка "Сброс"
menu2 = Button(root, text="Сброс", font=", 20", width=20)
menu2.place(x=-100, y=-100)
menu2["command"] = restartGame

# Кнопка для продолжения после вывода таблицы рекордов
btnContinueAfterPause = None

# Ниже кнопок расположена таблица рекордов
onMenu = False  # Меню "Выключено"
playerName = None  # Имя игрока
scores = loadScores()  # Список с никами и очками
textScores = None  # Список .create_text для отображения таблицы очков на Canvas

informationLine = None  # "Информационная строка" внизу окна

# ============= НАЧИНАЕМ ==============
globalReset()  # Сбрасываем очки и прочее
reset()  # Создаём игровой мир
playGame = True
mainloop()

# Бам! Всё!
root.mainloop()
