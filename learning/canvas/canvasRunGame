from tkinter import *

def move(vector):
    '''
    Принимает направление c клавиш и двигает cnv
    vector - направление движения
    '''
    if (vector == UPKEY):
        cnv.move(player, 0, -playerSpeed)
    elif (vector == DOWNKEY):
        cnv.move(player, 0, playerSpeed)
    elif (vector == LEFTKEY):
        cnv.move(player, -playerSpeed, 0)
    elif (vector == RIGHTKEY):
        cnv.move(player, playerSpeed, 0)

def evilMove():
    global evilAfter, vectorX, vectorY

    # Передвижение вражеского круга
    cnv.move(evil, vectorX, vectorY)

    # Получение координат в список
    # Так легче считать и читать код
    # cnv.coords возвращает список
    # В нем [0] - координата X, [1] - Y
    x = cnv.coords(evil)[0]
    y = cnv.coords(evil)[1]

    # Проверка на касание красным границ окна
    if (x > WIDTH - 32 or x < 32):
        vectorX = -vectorX
    if (y > HEIGHT - 32 or y < 32):
        vectorY = -vectorY

    # Получение координат игрока
    xP = cnv.coords(player)[0]
    yP = cnv.coords(player)[1]

    # Теорема Пифагора. Если расстояние меньше
    # диаметра круга, то значит есть касание
    distance = (abs(x - xP) ** 2 + abs(y - yP) ** 2) ** 0.5

    if (distance < 64):     # Если соприкосновение
        root.after_cancel(evilAfter)
    else:
        evilAfter = root.after(30, evilMove)    # 17=60FPS, 30=33FPS

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
evilCircle = PhotoImage(file='canvasImageMoves/circle.png')
playerSquare = PhotoImage(file='canvasImageMoves/square.png')

# Картинка фона устанавливается нижним слоем, первая
# Для Canvas начало координат в центре
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Смещение красного дъявола
vectorX = 5
vectorY = 5

# Скорость движения квадрата
playerSpeed = 3

# Создание и получение ссылок на объекты Canvas
evil = cnv.create_image(32, 32, image=evilCircle)
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

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

# Запуск движения красного дъявола
evilAfter = root.after(30, evilMove)

root.mainloop()
