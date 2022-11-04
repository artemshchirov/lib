from tkinter import *

def go(vector):
    '''
    Принимает направление c клавиш и двигает cnv
    '''
    if (vector == UPKEY):
        cnv.move(player, 0, -2)
        cnv.move(evil, 0, 2)
    elif (vector == DOWNKEY):
        cnv.move(player, 0, 2)
        cnv.move(evil, 0, -2)
    elif (vector == LEFTKEY):
        cnv.move(player, -2, 0)
        cnv.move(evil, 2, 0)
    elif (vector == RIGHTKEY):
        cnv.move(player, 2, 0)
        cnv.move(evil, -2, 0)

WIDTH = 640
HEIGHT = 480

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')

cnv = Canvas(root, width=WIDTH, height=HEIGHT)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
# Перехват нажатия клавиш
cnv.focus_set()

# Загрузка изображения
back = PhotoImage(file='canvasImageMoves/background.png')
# Установка изображения name.create_image(X, Y, PhotoImage)
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

evilCircle = PhotoImage(file='canvasImageMoves/circle.png')
evil = cnv.create_image(32, 32, image=evilCircle)

playerSquare = PhotoImage(file='canvasImageMoves/square.png')
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

# Кодировка кнопок константами
# для повышения читаемости кода
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Назначение клавиш управления курсором
cnv.bind('<Up>', lambda e, x=UPKEY: go(x))
cnv.bind('<Down>', lambda e, x=DOWNKEY: go(x))
cnv.bind('<Left>', lambda e, x=LEFTKEY: go(x))
cnv.bind('<Right>', lambda e, x=RIGHTKEY: go(x))

root.mainloop()
