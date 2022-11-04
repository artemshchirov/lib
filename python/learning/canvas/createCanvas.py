from tkinter import *

root = Tk()
root['bg'] = '#000010'
root.geometry('480x360')

# Создание виджета Canvas
cnv = Canvas(root, width=240, height=180, bg='#AAAAAA')

# Убрать автоматическую рамку вокруг Canvas
cnv.config(highlightthickness=0)

# Установка в область окна
cnv.place(x=50, y=50)




root.mainloop()
