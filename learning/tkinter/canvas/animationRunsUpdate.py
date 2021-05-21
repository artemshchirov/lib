from tkinter import *

def playerMove():
    global vectorXp, vectorYp, playerAfter

    cnv.move(player, vectorXp, vectorYp)
    cnv.move(playerHit1_12, vectorXp, vectorYp)
    cnv.move(playerHit2_12, vectorXp, vectorYp)
    cnv.move(playerHit3_12, vectorXp, vectorYp)
    cnv.move(playerHit4_12, vectorXp, vectorYp)
    cnv.move(playerHit1_6, vectorXp, vectorYp)
    cnv.move(playerHit2_6, vectorXp, vectorYp)
    cnv.move(playerHit3_6, vectorXp, vectorYp)
    cnv.move(playerHit4_6, vectorXp, vectorYp)
    cnv.move(playerHit5_6, vectorXp, vectorYp)
    cnv.move(playerHit6_6, vectorXp, vectorYp)
    cnv.move(playerHit7_6, vectorXp, vectorYp)
    cnv.move(playerHit8_6, vectorXp, vectorYp)

    xP = cnv.coords(player)[0]
    yP = cnv.coords(player)[1]

    if (xP > WIDTH - 32 or xP < 32):
        vectorXp = -vectorXp
    if (yP > HEIGHT - 32 or yP < 32):
        vectorYp = -vectorYp

    playerAfter = root.after(30, playerMove)

def move(vector):
    '''
    Принимает направление c клавиш и двигает cnv
    vector - направление движения
    '''
    global vectorXp, vectorYp

    print(f'move({vector})')

    if (vector == UPKEY):
        vectorXp = 0
        vectorYp = -playerSpeed
    elif (vector == DOWNKEY):
        vectorXp = 0
        vectorYp = playerSpeed
    elif (vector == LEFTKEY):
        vectorXp = -playerSpeed
        vectorYp = 0
    elif (vector == RIGHTKEY):
        vectorXp = playerSpeed
        vectorYp = 0

def evilMove():
    global evilAfter, vectorXs, vectorYs,   \
    vectorXm, vectorYm, vectorXl, vectorYl

    # Передвижение вражеского круга
    cnv.move(evilSmall, vectorXs, vectorYs)
    cnv.move(evilMiddle, vectorXm, vectorYm)
    cnv.move(evilLarge, vectorXl, vectorYl)

    # Получение координат в список. Легче считать и читать код
    # cnv.coords возвращает список. [0] - координата X, [1] - Y
    xS = cnv.coords(evilSmall)[0]
    yS = cnv.coords(evilSmall)[1]
    xM = cnv.coords(evilMiddle)[0]
    yM = cnv.coords(evilMiddle)[1]
    xL = cnv.coords(evilLarge)[0]
    yL = cnv.coords(evilLarge)[1]

    # Получение координат игрока
    xP = cnv.coords(player)[0]
    yP = cnv.coords(player)[1]

    xCircleHit1_12 = cnv.coords(playerHit1_12)[0]
    yCircleHit1_12 = cnv.coords(playerHit1_12)[1]
    xCircleHit2_12 = cnv.coords(playerHit2_12)[0]
    yCircleHit2_12 = cnv.coords(playerHit2_12)[1]
    xCircleHit3_12 = cnv.coords(playerHit3_12)[0]
    yCircleHit3_12 = cnv.coords(playerHit3_12)[1]
    xCircleHit4_12 = cnv.coords(playerHit4_12)[0]
    yCircleHit4_12 = cnv.coords(playerHit4_12)[1]

    # Проверка на касание красными границ окна
    if (xS > WIDTH - 8 or xS < 8):
        vectorXs = -vectorXs
    if (yS > HEIGHT - 8 or yS < 8):
        vectorYs = -vectorYs
    if (xM > WIDTH - 16 or xM < 16):
        vectorXm = -vectorXm
    if (yM > HEIGHT - 16 or yM < 16):
        vectorYm = -vectorYm
    if (xL > WIDTH - 32 or xL < 32):
        vectorXl = -vectorXl
    if (yL > HEIGHT - 32 or yL < 32):
        vectorYl = -vectorYl

    # Теорема Пифагора. Если расстояние меньше
    # диаметра круга то значит есть касание
    # TODO: Прописать маленькие кружки
    distanceS = (abs(xS - xP) ** 2 + abs(yS - yP) ** 2) ** 0.5
    distanceS1 = (abs(xS - xCircleHit1_12) ** 2 + abs(yS - yCircleHit1_12) ** 2) ** 0.5
    distanceS2 = (abs(xS - xCircleHit2_12) ** 2 + abs(yS - yCircleHit2_12) ** 2) ** 0.5
    distanceS3 = (abs(xS - xCircleHit3_12) ** 2 + abs(yS - yCircleHit3_12) ** 2) ** 0.5
    distanceS4 = (abs(xS - xCircleHit4_12) ** 2 + abs(yS - yCircleHit4_12) ** 2) ** 0.5

    distanceM = (abs(xM - xP) ** 2 + abs(yM - yP) ** 2) ** 0.5
    distanceM1 = (abs(xM - xCircleHit1_12) ** 2 + abs(yM - yCircleHit1_12) ** 2) ** 0.5
    distanceM2 = (abs(xM - xCircleHit2_12) ** 2 + abs(yM - yCircleHit2_12) ** 2) ** 0.5
    distanceM3 = (abs(xM - xCircleHit3_12) ** 2 + abs(yM - yCircleHit3_12) ** 2) ** 0.5
    distanceM4 = (abs(xM - xCircleHit4_12) ** 2 + abs(yM - yCircleHit4_12) ** 2) ** 0.5

    distanceL = (abs(xL - xP) ** 2 + abs(yL - yP) ** 2) ** 0.5
    distanceL1 = (abs(xL - xCircleHit1_12) ** 2 + abs(yL - yCircleHit1_12) ** 2) ** 0.5
    distanceL2 = (abs(xL - xCircleHit2_12) ** 2 + abs(yL - yCircleHit2_12) ** 2) ** 0.5
    distanceL3 = (abs(xL - xCircleHit3_12) ** 2 + abs(yL - yCircleHit3_12) ** 2) ** 0.5
    distanceL4 = (abs(xL - xCircleHit4_12) ** 2 + abs(yL - yCircleHit4_12) ** 2) ** 0.5

    # Если соприкосновение
    # TODO: Прописать маленькие кружки
    if (distanceS < 40 or distanceM < 48 or distanceL < 64
    or distanceS1 < 14 or distanceM1 < 22 or distanceL1 < 38
    or distanceS2 < 14 or distanceM2 < 22 or distanceL2 < 38
    or distanceS3 < 14 or distanceM3 < 22 or distanceL3 < 38
    or distanceS4 < 14 or distanceM4 < 22 or distanceL4 < 38):
        root.after_cancel(playerAfter)
        root.after_cancel(evilAfter)
    else:   # 17=60FPS, 30=33FPS
        evilAfter = root.after(30, evilMove)

WIDTH = 640
HEIGHT = 480

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')

# Создание виджета - Canvas
cnv = Canvas(root, width=WIDTH, height=HEIGHT)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

# Загрузка изображения
back = PhotoImage(file='canvasImageMoves/background.png')
circleSmall = PhotoImage(file='canvasImageMoves/circleSmall.png')
circleMiddle = PhotoImage(file='canvasImageMoves/circleMiddle.png')
circleLarge = PhotoImage(file='canvasImageMoves/circleLarge.png')
playerSquare = PhotoImage(file='canvasImageMoves/square.png')
circleHit12 = PhotoImage(file='canvasImageMoves/circle12.png')
circleHit6 = PhotoImage(file='canvasImageMoves/circle6.png')
# Картинка фона устанавливается нижним слоем, первая
# Для Canvas начало координат в центре
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Смещение красного дъявола
vectorXs = 2
vectorYs = 10
vectorXm = 10
vectorYm = 2
vectorXl = 5
vectorYl = 5

# Скорость движения квадрата
playerSpeed = 5
vectorXp = 0
vectorYp = 0

# Создание и получение ссылок на объекты Canvas
evilSmall = cnv.create_image(32, 32, image=circleSmall)
evilMiddle = cnv.create_image(32, 32, image=circleMiddle)
evilLarge = cnv.create_image(32, 32, image=circleLarge)
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

playerHit1_12 = cnv.create_image(WIDTH // 2 - 26, HEIGHT // 2 + 26, image=circleHit12)
playerHit2_12 = cnv.create_image(WIDTH // 2 + 26, HEIGHT // 2 + 26, image=circleHit12)
playerHit3_12 = cnv.create_image(WIDTH // 2 - 26, HEIGHT // 2 - 26, image=circleHit12)
playerHit4_12 = cnv.create_image(WIDTH // 2 + 26, HEIGHT // 2 - 26, image=circleHit12)

playerHit1_6 = cnv.create_image(WIDTH // 2 - 29, HEIGHT // 2 - 17, image=circleHit6)
playerHit2_6 = cnv.create_image(WIDTH // 2 - 17, HEIGHT // 2 - 29, image=circleHit6)
playerHit3_6 = cnv.create_image(WIDTH // 2 + 29, HEIGHT // 2 + 17, image=circleHit6)
playerHit4_6 = cnv.create_image(WIDTH // 2 + 17, HEIGHT // 2 + 29, image=circleHit6)
playerHit5_6 = cnv.create_image(WIDTH // 2 - 29, HEIGHT // 2 + 17, image=circleHit6)
playerHit6_6 = cnv.create_image(WIDTH // 2 - 17, HEIGHT // 2 + 29, image=circleHit6)
playerHit7_6 = cnv.create_image(WIDTH // 2 + 29, HEIGHT // 2 - 17, image=circleHit6)
playerHit8_6 = cnv.create_image(WIDTH // 2 + 17, HEIGHT // 2 - 29, image=circleHit6)


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

# Запуск отложенного цикла движения
evilAfter = root.after(30, evilMove)
playerAfter = root.after(30, playerMove)

root.mainloop()
