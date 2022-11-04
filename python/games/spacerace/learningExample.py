from tkinter import *
root = Tk()            # Объявление переменной для программы.
                       # Она отвечает за взаимодействие с элементами программы Tkinter
# Размеры окна программы
WIDTH = 640
HEIGHT = 480

# root.winfo_screenwidth()     # Найти ширину экрана
# root.winfo_screenheight()    # Найти высоту экрана

# Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Устанавливаем ширину, высоту и позицию
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Установка заголовка
root.title('Test window')

# Запрещаем изменение размеров
root.resizable(False, False)

button01 = Button()    # Объявление переменной для виджета-кнопки
# ----- Правильная последовательность при размещении кнопки:

# 1. Сначала создаем текст внутри виджета-кнопки
button01['text'] = 'Close'
# 2.Сначала получаем ширину для кнопки
X_BTN = WIDTH // 2 - button01.winfo_reqwidth() // 2
# 3.Получаем высоту для кнопки
Y_BTN = HEIGHT // 2 - button01.winfo_reqheight() // 2
# 4.Устанавливаем позицию кнопки
button01.place(x=X_BTN, y=Y_BTN)

# Добавление реакции на нажатие кнопки
button01['command'] = quit

root.mainloop()
