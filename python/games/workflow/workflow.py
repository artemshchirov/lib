from tkinter import *
from tkinter import ttk         # Для RadioButton
from tkinter import messagebox  # Для окон-сообщений
from random import randint
import pygame
# from tkinter.messagebox import *
from tkinter import filedialog
# from winsound import Beep       # Бипер (пищалка), генератор звука
from tkinter import ttk
import sys

def playMusic():
	'''
	При кнопке старт запускает музыку
	'''
	# TODO: Протестировать здесь всё

	pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

	pygame.init()

	pygame.mixer.init()

	pygame.mixer.music.load('playlist/music_01.ogg')

	pygame.mixer.music.play(-1)

	comboMusic['state'] = DISABLED

def blockTopScreen():
	'''
	Режим блокировки экрана и отключения бинда выхода (<q>).
	Включается в контекстном ПКМ меню
	'''
	print('Метод blockTopScreen()')
	if (valueScreenBlock.get() == 1):
		root.attributes('-topmost', True)
	else:
		root.attributes('-topmost', False)
def autoChangeImage():
	'''
	Режим автосмены изображений.
	Включается в контекстном ПКМ меню
	'''
	print('Метод autoAnimationImage()')
def autoAnimationSpeed():
	'''
	Режим автоизменения скорости анимации слайдов.
	Включается в контекстном ПКМ меню
	'''
	global reverse, scale
	print('Метод autoAnimationSpeed()')

	if (not reverse and scale < 40):
		scale += 1
	else:
		reverse = True

	if (reverse and scale > 10):
		scale -= 1
	else:
		reverse = False

	scaleAnimationSpeed.set(scale)
def popupMenu(event):
	'''
	Открывает контекстное меню по нажатию ПКМ
	'''

	menuRightClick.post(event.x_root, event.y_root)
def isCheckImage():
	'''
	Выбор заготовленных изображений для спрайтов
	'''
	# global imageBackground

	# if (image.get() == 0):      # Если в переменной image содержится 0
	#     imageBackground = imageBackground01
	#     Beep(1350, 50)
	# elif (image.get() == 1):      # Если в переменной image содержится 1
	#     imageBackground = imageBackground02
	#     Beep(1450, 50)
	# elif (image.get() == 2):      # Если в переменной image содержится 2
	#     imageBackground = imageBackground03
	#     Beep(1550, 50)
	print('Метод isCheckImage()')
def keyReciever(event):

	print(f'char: {event.char}, keysym: {event.keysym}')

	if (event.keysym == 'space'):
		if (pause == True):
			startMoving()
		else:
			pauseMoving()

	if (event.char == 'r' or event.char == 'к'):
		reset()
	elif (event.char == 'q' or event.char == 'й'):
		if (valueScreenBlock.get() == 1):
			pass
		else:
			endQuit()
def mouseCoords(event):
	'''
	Активирует и убирает нижнюю панель,
	в зависимости от координаты Y курсора мыши
	'''
	global startLine, hideMenu

	# Координата Y курсора
	yPoint = event.y

	# В каком случае активировать нижнюю панель
	if (yPoint > yLine):
		startLine = True	# 1й раз

		# print(f'hideMenu: {hideMenu}')

		butNum = 0
		for i in buttons:
			butNum += 30
			i.place(x=w/2+10, y=(h-heightPic)+heightPic/(len(buttons)+3)+butNum, anchor=CENTER)

			scaleAnimationSpeed.place(x=w/3.141, y=h-heightPic/1.92)

			comboMusicText.place(x=w/3.02, y=620)
			comboMusic.place(x=w/3.15, y=h-heightPic/1.52)

			radioImageText.place(x=w/1.67, y=623)
			radio01.place(x=w/1.67, y=h-heightPic/1.55)
			radio02.place(x=w/1.67, y=h-heightPic/1.88)
			radio03.place(x=w/1.67, y=h-heightPic/2.41)

		cnvBack.place(x=w/2, y=h-heightPic/1.9, anchor=CENTER)
	# TODO: сделать if чтобы проверять и не ставить повторно - экономить ресурсы
	elif (startLine):

		# print(f'hideMenu: {hideMenu}')

		for i in buttons:
			i.place(x=wMiddle, y=h+100)
		cnvBack.place(x=wMiddle, y=h+100)

		scaleAnimationSpeed.place(x=wMiddle, y=h+100)

		comboMusicText.place(x=wMiddle, y=h+100)
		comboMusic.place(x=wMiddle, y=h+100)

		radioImageText.place(x=wMiddle, y=h+100)
		radio01.place(x=wMiddle, y=h+100)
		radio02.place(x=wMiddle, y=h+100)
		radio03.place(x=wMiddle, y=h+100)
def pauseMoving():
	'''
	Заканчивает движение слайда и ставит движение на паузу.
	Меняет кнопку PAUSE на кнопку START
	'''
	global pause

	startButton['text'] = 'START'
	startButton['command'] = startMoving

	pause = True
def endQuit():
	'''
	Нажатие на кнопку QUIT закрывает opera.exe и программу
	'''
	print('Метод quit()')

	# Закрывает процесс (браузер)
	# os.system("taskkill /im opera.exe /f")

	quit(0)
def reset():
	'''
	Возврат изображения к стартовому состоянию
	'''
	global dataImage, canvasImage, pause
	print('===== Метод reset() =====')

	startButton['text'] = 'START'
	startButton['command'] = startMoving

	# noDirection = None
	# moving = False
	pause = True
	# count = 64

	# Очистить поле, удалив все Canvas на экране
	cnv.delete(ALL)
	print('dataImage1: ', dataImage, 'blackImage: ', blackImage)

	# Очистка и создание нового экрана с Canvas imgs
	dataImage = []
	canvasImage = []
	print('dataImage2: ', dataImage, 'blackImage: ', blackImage)

	for i in range(n):
		dataImage.append([])
		canvasImage.append([])
		for j in range(m):
			dataImage[i].append(i * n + j)
			canvasImage[i].append(cnv.create_image(172 + j * widthPic,
												   95 + i * heightPic,
												   image=imageBackground01[i * n + j]))

	print('dataImage3: ', dataImage, 'blackImage: ', blackImage)

	root.bind("<space>", lambda e: startMoving())
	resetButton['state'] = DISABLED
def moveSlides(x1, y1, x2, y2, x, y):
	'''
	Цикл движения imgs.png для создания анимации
	'''
	global count, moving



	count -= 1
	moving = True		# Если убрать это, то будет эффект рандомных движений всех картинок

	if (not pause and dataImage[x1][y1] == blackImage):
		cnv.move(canvasImage[x1][y1], -x, -y)
		cnv.move(canvasImage[x2][y2], x, y)
	elif (dataImage[x2][y2] == blackImage):
		cnv.move(canvasImage[x1][y1], x, y)
		cnv.move(canvasImage[x2][y2], -x, -y)

	if (count > 0):
		root.after(50 // scaleAnimationSpeed.get(), 									# Цикл перемещения каждые 20 млс
					lambda x=x,							# Смещение "за раз" по оси X
					y=y,								# Смещение "за раз" по оси Y
					x1=x1, y1=y1, x2=x2, y2=y2:			# Кол-во смещений
					moveSlides(x1, y1, x2, y2, x, y))	# Рекурсия этого метода
	else:
		print('\n\nЦикл методов moveSlides() ЗАВЕРШЕН')
		print(f'Осталось count: {count}')
		count = 64*4
		print(f'Было count: {count}\n')

		moving = False

		generatorXY()
def exchangeImage(x1, y1, x2, y2, dir):
	'''
	Обмен мест изображений в математической
	и соответсвенно в графической моделях
	'''
	global dataImage, canvasImage

	# print(f'Метод exchangeImage({x1}, {y1}, {x2}, {y2}) начал выполнилнятся')
	# tmp = dataImage[x1][y1]

	# Изменяем математическую модель
	dataImage[x1][y1], dataImage[x2][y2] = dataImage[x2][y2], dataImage[x1][y1]

	# Изменяем графическую модель
	canvasImage[x1][y1], canvasImage[x2][y2] = canvasImage[x2][y2], canvasImage[x1][y1]
	print('dataImage[x1][y1] == blackImage:', dataImage[x1][y1])
	print('dataImage[x2][y2] == blackImage:', dataImage[x2][y2])

	# Если в ПКМ menu выбрана автоскорость
	if (valueAutoSpeed.get() == 1):
		autoAnimationSpeed()

	# Направление и расстояние перемещения слайдов
	if (dir == 0):		# ВНИЗ
		moveSlides(x1, y1, x2, y2, 0, -12/16)
	elif (dir == 1):	# ВВЕРХ
		moveSlides(x1, y1, x2, y2, 0, 12/16)
	elif (dir == 2):	# ВПРАВО
		moveSlides(x1, y1, x2, y2, -21.37/16, 0)
	elif (dir == 3):	# ВЛЕВО
		moveSlides(x1, y1, x2, y2, 21.37/16, 0)
def shufflePictures(x, y):
	'''

	'''
	global noDirection	# Для теста print() в конце def moveSlides()
	print(f'!!! Метод shufflePictures({x}, {y}) начат !!!')
	countShuffle = 1
	print(f'before while. noDirection: {noDirection}')

	while (countShuffle > 0):
		direction = noDirection
		print(f'1st while. direction: {direction}, noDirection: {noDirection}')
		while (direction == noDirection):   # Пока НовоеНаправление == Запрещённому
			direction = randint(0, 3)       #   Генерируем НовоеНаправление
			print(f'2th while. direction: {direction}, noDirection: {noDirection}')

		# ВНИЗ
		if (direction == 0 and x + 1 < n):
			print(f'\n=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x + 1}, y2: {y}, dir: {direction}) НАЧАТ')
			exchangeImage(x, y, x + 1, y, direction)
			x += 1
			noDirection = 1
			countShuffle -= 1
			print(f'=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x + 1}, y2: {y}, dir: {direction}) ЗАВЕРШЕН')

		# ВВЕРХ
		elif (direction == 1 and x - 1 >= 0):
			print(f'\n=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x - 1}, y2: {y}, dir: {direction}) НАЧАТ')
			exchangeImage(x, y, x - 1, y, direction)
			x -= 1
			noDirection = 0
			countShuffle -= 1
			print(f'=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x - 1}, y2: {y}, dir: {direction}) ЗАВЕРШЕН')

		# ВПРАВО
		elif (direction == 2 and y + 1 < m):
			print(f'\n=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x}, y2: {y + 1}, dir: {direction}) НАЧАТ')
			exchangeImage(x, y, x, y + 1, direction)
			y += 1
			noDirection = 3
			countShuffle -= 1
			print(f'=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x}, y2: {y + 1}, dir: {direction}) ЗАВЕРШЕН')

		# ВЛЕВО
		elif (direction == 3 and y - 1 >= 0):
			print(f'\n=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x}, y2: {y - 1}, dir: {direction}) НАЧАТ')
			exchangeImage(x, y, x, y - 1, direction)
			y -= 1
			noDirection = 2
			countShuffle -= 1
			print(f'=== Метод exchangeImage(x1: {x}, y1: {y}, x2: {x}, y2: {y - 1}, dir: {direction}) ЗАВЕРШЕН')
def generatorXY():
	'''
	Генерация x,y для dataImage[[]],
	чтобы двигать images.png
	'''
	print('===== Метод generatorXY() =====')

	if (not pause):
		if (not moving):
			x = 0
			y = 0
			while (dataImage[x][y] != blackImage):
				y += 1
				if y >= m:
					x += 1
					y = 0
			shufflePictures(x, y)
def startMoving():
	'''
	Запуск потока анимаций слайдов
	'''
	global pause

	print('===== Метод startMoving() =====')

	playMusic()

	startButton['text'] = ' PAUSE'
	startButton['command'] = pauseMoving
	resetButton['state'] = NORMAL

	pause = False

	generatorXY()

# =============== НАЧАЛО ПРОГРАММЫ
# Создание окна
root = Tk()
root.attributes('-fullscreen', True)  # Полный экран
# root.attributes('-topmost', False)  # Поверх других окон
# ФОКУС ОКНА
root.resizable(False, False)

# Получаем ширину и высоту экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
wMiddle = (w - (w // 4)) // 2
hDown = (h - (h // 5))
print(f'h: {h}, hDown: {hDown}, w: {w}, wMiddle: {wMiddle}')
back = '#00021f'    # Фон
fore = 'white'    # Шрифт

# Размер поля
n = 4   # Ширина
m = 4   # Высота
# Ширина и высота одного спрайта в пикселях
widthPic = w / n
heightPic = h / n

# Создание виджета Canvas
cnv = Canvas(root, width=w, height=h, bg=back)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
# При движении курсора по Canvas активация mouseCoords()
cnv.bind('<Motion>', mouseCoords)

# Создание виджета Canvas для фона кнопок
# TODO: попробовать на Lenovo heightPic/len(buttons)
cnvBack = Canvas(root, width=widthPic*1.5, height=heightPic-heightPic/2, bg=back)
cnvBack.config(highlightthickness=1)
cnvBack.place(x=w/2, y=h-heightPic/1.9, anchor=CENTER)

# Создание кнопок
startButton = Button(text='START', width=29)	# Кнопка START
resetButton = Button(text='RESET', width=29)	# Кнопка RESET
quitButton = Button(text='QUIT', width=29)		# Кнопка QUIT
# Установка кнопок для отображения в окне
buttons = [startButton, resetButton, quitButton]
butNum = 0
for i in buttons:
	butNum += 30
	i.place(x=w/2+10, y=h-heightPic/1.2+butNum, anchor=CENTER)

# Бинд функций к кнопкам
startButton['command'] = startMoving
resetButton['command'] = reset
quitButton['command'] = endQuit
# Отключение кнопки Reset при запуске
resetButton['state'] = DISABLED

# Combobobx выбора плейлиста
# Текст над Combobox
comboMusicText = Label(text='Choose playlist:', font='Arial 10', background=back, fg=fore)
comboMusicText.place(x=w/3.02, y=620)
# Combobox
comboMusic = ttk.Combobox(root,
							values=["January",
									"February",
									"March"],
							width=19)
comboMusic['state'] = 'readonly'
comboMusic.place(x=w/3.15, y=h-heightPic/1.52)

# TODO: Окно ПКМ для включения автосмены картинок и скорости анимации
# Ползунок управления скоростью анимации
scaleAnimationSpeed = Scale(root, from_=1, to=50, length=130, orient=HORIZONTAL)
scaleAnimationSpeed.set(25)
scaleAnimationSpeed.place(x=w/3.141, y=h-heightPic/1.92)

# Радиопереключатели (RadioButton)
# Текст над переключателями
radioImageText = Label(text='Choose Image:', font='Arial 10', background=back, fg=fore)
radioImageText.place(x=w/1.67, y=623)
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
radio01.place(x=w/1.67, y=h-heightPic/1.55)
radio02.place(x=w/1.67, y=h-heightPic/1.88)
radio03.place(x=w/1.67, y=h-heightPic/2.41)

# Перехват нажатия клавиш для keyReciever
root.bind("<Key>", keyReciever)

# =============== ИЗОБРАЖЕНИЯ
# Имена файлов без указания каталога
fileName = ['image01.png', 'image02.png', 'image03.png', 'image04.png',
			'image05.png', 'image06.png', 'image07.png', 'image08.png',
			'image09.png', 'image10.png', 'image11.png', 'image12.png',
			'image13.png', 'image14.png', 'image15.png', 'black.png']

# Каталоги для изображений
imageBackground = []    # Активное изображение
imageBackground01 = []	# "Синий космос"

# Загрузка изображений в список по-умолчанию
# TODO: Запоминание открытого ранее списка
for name in fileName:
	imageBackground01.append(PhotoImage(file='image01/' + name))
# Устанавливаем набор спрайтов в активный сейчас
imageBackground = imageBackground01

# Математическая модель игрового поля
dataImage = []
# Графическая Canvas модель игрового поля
canvasImage = []
# Координата X тайловой матрицы модели игры
for i in range(n):
	dataImage.append([])
	canvasImage.append([])
	for j in range(m):
		dataImage[i].append(i * n + j)
		canvasImage[i].append(cnv.create_image(172 + j * widthPic,
											   95 + i * heightPic,
											   image=imageBackground01[i * n + j]))

# Контекстное меню по нажатию ПКМ
root.bind("<Button-3>", popupMenu)
menuRightClick = Menu(tearoff=0)

valueAutoSpeed = BooleanVar()
valueAutoSpeed.set(0)
menuRightClick.add_checkbutton(label="Авто скорость анимации",
 								onvalue=1, offvalue=0,
								variable=valueAutoSpeed,
								command=autoAnimationSpeed)

valueAutoImage = BooleanVar()
valueAutoImage.set(0)
menuRightClick.add_checkbutton(label="Авто смена изображения",
								onvalue=1, offvalue=0,
								variable=valueAutoImage,
								command=autoChangeImage)

valueScreenBlock = BooleanVar()
valueScreenBlock.set(0)
menuRightClick.add_checkbutton(label="Блокировка окна",
								onvalue=1, offvalue=0,
								variable=valueScreenBlock,
								command=blockTopScreen)

# Позиция пустого слайда в dataImage[][]
blackImage = 15

# Направление движения слайда
noDirection = None

# Происходит ли анимация?
moving = None
# Количество шагов анимации в 1 перемещении слайда
count = 64*4

# Скорость анимации слайдов
scale = scaleAnimationSpeed.get()
# Замедление анимации
reverse = None

# Активирована ли пауза?
pause = True

# Координата Y курсора
yPoint = None
# Линия активации нижней панели курсором
yLine = h - (h / 4)
# Хоть 1 раз курсор опускался ниже yLine?
startLine = None
# Скрыта ли панель?
hideMenu = True

#
playlist = []

# =============== КОНЕЦ ПРОГРАММЫ
root.mainloop()
