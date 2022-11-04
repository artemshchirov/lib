# ВЫХОД: ALT+F4

from tkinter import *
from random import randint


# Что происходит когда курсор мыши оказывается над кнопкой
def motionMouse(event):
    btn.place(x=randint(0, w - btn.winfo_reqwidth()), y=randint(0, h))


# Событие при нажатии на копку:
def pressMouse(event):
    quit(0)


# Создаем окно и разворачиваем на весь экран
root = Tk()
root.attributes('-fullscreen', True)
root.resizable(False, False)

# Устанавливаем чёрный цвет фона
root.configure(bg="#000000")

# Получаем ширину и высоту экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Формируем и распологаем кнопку
btn = Button(text="Чтобы продолжить работу, нажмите на эту кнопку.", font="Arial 20")
btn.place(x=w // 2 - btn.winfo_reqwidth() // 2, y=h // 2)

# Определяем, что произойдет, когда курсор мыши окажется НАД виджетом
btn.bind("<Enter>", motionMouse)

# Расскоментируйте строку, чтобы было честно, иначе нажать на кнопку нельзя совсем
btn.bind("<Button>-1", pressMouse)

root.mainloop()
