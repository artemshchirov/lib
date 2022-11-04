from tkinter import *
from random import randint
from time import sleep
from winsound import Beep

def nextLevel():
	'''
	Загрузка level+1 уровня
	'''
	global level, playGame

	cnv.delete(ALL)
	level += 1
	playGame = True
	reset()
def endLevel():
	'''
	Конец уровня
	'''
	global playGame

	playGame = False  # Конец игровой сессии
	cnv.delete(ALL)
	cnv.create_text(WIDTH // 2, HEIGHT // 2,
					fill = '#FFFFFF',
					font=f', 15',
					text=f'ПОБЕДА! ЗАГРУЖАЕМ СЛЕДУЮЩИЙ УРОВЕНЬ!')
	root.focus_set()
	root.update()

	Beep(randint(850, 1000), 400)
	Beep(randint(750, 1000), 200)
	Beep(randint(950, 1000), 600)
	Beep(randint(850, 1000), 500)

	root.after(2000, nextLevel)

def continueAfterPause():
	'''
	"Продолжение после паузы".
	Очистить всё и начать игру заново
	'''
	btnContinueAfterPause.destroy()
	saveScores(scores)
	cnv.delete(ALL)
	showMenu()
	restartGame()
def endTableScore(inputWindow, positionPlayer):
	'''
	Вызывается когда игрок нажал кнопку "Еще разок?".
	inputWindow - ссылка на Toplevel окно. Нужна для уничтожения окна после ввода ника.
	Аргумент positionPlayer - номер игрока в таблице рекордов. Нужен для исправления scores[x][y]
	'''
	global playerName, scores

	root.deiconify()  #  Теперь пользователь может взаимодействовать с главным окном
	inputWindow.destroy()  #  Уничтожить окно
	playerName = playerName.get()  # Присваивание значения из введенного пользователем

	filter = '_-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
	for i in playerName:  # Проверка на допустимость введенного знака
		if (i.upper() not in filter):
			playerName = playerName.replace(i, '')

	if (playerName == None):  # Если ник не введен, то установка дефолтного имени
		playerName = defaultName
	elif (len(playerName) > 20):  # Ограничение количества знаков в нике
		playerName = playerName[0:20]

	scores[positionPlayer][0] = playerName  #  Обновление списка рекордов

	# Очистить всё и начать игру заново
	continueAfterPause()
def hideScores():
	'''
	Удаляем таблицу очков
	'''
	global textScores

	for i in textScores:
		cnv.delete(i)
def inputNameFilter(event):
	'''
	Проверяет ведённое пользователем на корректность
	'''
	global playerName

	filter = '_-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
	pN = ''

	for i in playerName.get():  # Проверка на допустимость введенного знака
		if (i.upper() in filter):
			pN += i

	if (len(pN) > 20):  # Ограничение количества знаков в нике
		pN = pN[0:20]
	elif (pN == None):  # Если ник не введен, то установка дефолтного имени
		pN = defaultName
	# Установка новой, отфильтрованной строки в Entry
	playerName.set(pN)
def getPlayerName(positionPlayer):
	'''
	Формирует окно для ввода имени и
	проверяется корректность введённых значений.
	Вызывается если игрок еще не вводил свой ник
	'''
	global playerName

	inputWindow = Toplevel(root)  # Создание окна верхнего уровня (2е окно в приложении)

	# Переделка вторичного окна в модальное
	inputWindow.grab_set()  # .grab_set() устанавливает режим перехвата событий

	#Геометрия нового окна
	X_NEW = root.winfo_screenwidth() // 2 - 150
	Y_NEW = root.winfo_screenheight() // 2 - 260
	inputWindow.geometry(f'{300}x{120}+{X_NEW}+{Y_NEW}')
	inputWindow.overrideredirect(True)  # Если True, то вывод окна без рамки (окон управления)
	inputWindow.focus_set()  # Перенос бинда клавиш в новое окно

	Label(inputWindow, text='Вы - один из лучших! Введите ник:').place(x=13, y=10)

	playerName = StringVar()
	playerName.set(defaultName)
	newName = Entry(inputWindow, textvariable=playerName, width=45)  # Создание виджета Entry
	newName.place(x=13, y=40)
	newName.focus_set()
	newName.select_range(0, END)  # Выбор всего текста в окне
	newName.bind('<KeyRelease>', inputNameFilter)  # Перехват нажатия клавиш в новое окно

	btnGo = Button(inputWindow, text="Еще разок?", width=38)
	btnGo.place(x=13, y=70)
	btnGo['command'] = lambda iW=inputWindow, posP=positionPlayer: endTableScore(iW, posP)
def showScores(numberPlayer):
	'''
	Отображает таблицу очков.
	Принимает sortScoreTable(), номер позиции игрока
	'''
	global textScores

	textScores = []  # Пересоздание списка для хранения ссылок на объекты .create_text()

	for i in range(len(scores)):
		# Если позиция игрока == итерируемая позиция в списке, то зеленый цвет
		if (i == numberPlayer):
			colorText = "#00FF55"
		else:
			colorText = "#e2cb2f"
		# Создаём текст на экране и добавляем объект текста в список textScores
		textScores.append(cnv.create_text(210,
										  170 + i * 22,
										  fill=colorText,
										  font=", 14",
										  text=str(i + 1)))  # Номер строки
		textScores.append(cnv.create_text(240,
										  170 + i * 22,
										  fill=colorText,
										  anchor="w",
										  font=", 14",
										  text=scores[i][0]))  # Имя игрока
		textScores.append(cnv.create_text(590,
										  170 + i * 22,
										  fill=colorText,
										  anchor="e",
										  font=", 14",  # Заработанные очки
										  text=scores[i][1]))
def sortScoreTable(score):
	'''
	Определение позиции игрока в таблице рекордов
	посредством bubble sort
	'''
	global scores

	name = playerName
	if (playerName == None):
		name = "Вы"

	scores.append([name, score])

	positionPlayer = 10
	for i in range(len(scores) - 1, 0, -1):
		if (scores[i][1] > scores[i - 1][1]):
			scores[i][1], scores[i - 1][1] = scores[i-1][1], scores[i][1]
			scores[i][0], scores[i - 1][0] = scores[i-1][0], scores[i][0]
			positionPlayer -= 1
	del scores[10]

	if (positionPlayer < 10 and playerName == None):
		getPlayerName(positionPlayer)

	return positionPlayer
def endGame():
	'''
	Конец игры.
	Вызывается, когда пришельцы "раздавили"
	корабль игрока или когда жизней < 0
	'''
	global playGame, btnContinueAfterPause, score

	playGame = False  # Игра закончилась

	# Убираем фокус с Canvas на окно
	root.focus_set()  # Чтобы не работали Esc, <- и ->. Т.к конец игры

	cnv.delete(ALL)  # Очищаем поле от всех Canvas
	cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)  # Рисуем фон
	cnv.create_text(160,
					 80,
					 fill="#FFFFFF",
					 anchor="nw",
					 font=f", 22",
					 text=f"КОНЕЦ ИГРЫ. ЛУЧШИЕ ИГРОКИ:")

	score -= penalty  # Уменьшение кол-ва очков на заработанные штрафы во время игры

	showScores(sortScoreTable(int(score)))  # передавая во внутреннюю функцию приведённые к целому очки

	# Формирование и вывод кнопки "Продолжить" внизу окна
	btnContinueAfterPause = Button(root, text="Продолжить", width=70)
	btnContinueAfterPause.place(x=140, y=HEIGHT - 50)
	btnContinueAfterPause["command"] = continueAfterPause

def startExplosion(n):
	'''
	Старт анимации взрыва.
	n - номер пораженного пришельца
	'''
	global invadersObject

	if (not playGame):
		return 0

	Beep(650, 20)
	animationExplosion(7,  # Старт анимации взрыва с 7 кадра до 0
					   getInvadersX(invadersObject[n]),
					   getInvadersY(invadersObject[n]))
	invadersObject[n][1] -= 1  # Уменьшение ранга пришельца (хранится по адресу invadersObject[n][у]) при попадании

	if (invadersObject[n][1] < 0):
		cnv.delete(invadersObject[n][0])

		del invadersObject[n]
def animationShoot(frame):
	'''
	Анимация ракеты игрока
	'''
	global rocketObject, \
		rocketSpeedY, \
		penalty, \
		score, \
		player

	if (not playGame):
		rocketObject = None
		rocketSpeedY = rocketSpeedYDefault
		return 0

	# Смена положения изображения ракеты игрока
	cnv.move(rocketObject, 0, -rocketSpeedY)
	rocketSpeedY *= rocketScale

	x = getRocketX()
	y = getRocketY()
	frame += 1  # Счетчик кадров анимации ракеты
	if (frame > len(rocketTexture) - 1):
		frame = 0

	cnv.delete(rocketObject)

	rocketObject = cnv.create_image(x,
									y,
									image=rocketTexture[frame])
	rocketX = getRocketX()
	rocketY = getRocketY()
	if (rocketY < (maxY) and  # Если ракета игрока в зоне "прямоугольника инопланетян"
		(leftInvadersBorder - SQUARE_SIZE) < rocketX < (rightInvadersBorder + SQUARE_SIZE)):
		find = 0  # Создание переменной для хранения номера уничтоженного инопланетянина
		while (find < len(invadersObject)):
			invadersX = getInvadersX(invadersObject[find])
			invadersY = getInvadersY(invadersObject[find])
			if (abs(invadersX - rocketX) < SQUARE_SIZE * 0.4 and   # Расстояние X между ракетой и пришельцем
					abs(invadersY - rocketY) < SQUARE_SIZE * 0.8): # Расстояние Y
				score += 50 * (level + 1)
				startExplosion(find)  # Старт взрыва инопланетянина, в которого попали
				y = -1  # Y ракеты вышло за поле и она должна пропасть в else дальше
				penalty -= 5  # Компенсация штрафа за промах т.к было попадание
				find = len(invadersObject) - 1  # Остановить цикл, если было попадание
			find += 1  # Если не было попадания, ищем в цикле дальше следующего инопланетянина
	if (y > 0):  # Если Y ракеты игрока НЕ вышло за поле, то продолжаем анимацию ракеты
		root.after(23, lambda frame=frame: animationShoot(frame))
	else:  # Если Y ракеты игрока вышло за поле, то
		Beep(700, 20)
		cnv.delete(rocketObject)  # Удаляем изображение ракеты
		penalty += 5  # Начисление штрафа за непопадание
		player[1] += 1  # Возвращаем запас ракет
		rocketSpeedY = rocketSpeedYDefault  # Убираем ускорение следующей ракеты
def getRocketY():
	'''
	Возвращает Y координату ракеты игрока
	'''
	return cnv.coords(rocketObject)[1]
def getRocketX():
	'''
	Возвращает Х координату ракеты игрока
	'''
	return cnv.coords(rocketObject)[0]
def shoot():
	'''
	Запуск ракеты игрока
	'''
	global player, rocketObject

	if (not playGame or onMenu):
		return 0

	if (player[1] == 0):  # Если не осталось ракет у игрока
		return 0

	player[1] -= 1  # Уменьшение количества ракет игрока
	# Создание изображения ракеты игрока
	rocketObject = cnv.create_image(getPlayerX(),
									getPlayerY(),
									image=rocketTexture[0])
	# Запуск функции запуска анимации ракеты игрока
	root.after(10, lambda frame=0: animationShoot(frame))
def getPlayerX():
	return cnv.coords(player[0])[0]
def getPlayerY():
	return cnv.coords(player[0])[1]

def updateInfoLine():
	'''
	Обновление инфостроки
	'''
	global informationLine


	if (informationLine != None):  # Проверка есть ли что-нибудь и удаление, если есть
		for i in informationLine:
			cnv.delete(i)

	informationLine = []  # Обнуление списка и создание обновленных элементов заново
	informationLine.append(cnv.create_text(20,
										   440,
										   fill='#ABCDEF',
										   anchor='nw',
										   font=f', 12',
										   text=f'ОЧКИ: {int(score)}'))
	informationLine.append(cnv.create_text(170,
										   440,
										   fill='#ABCDEF',
										   anchor='nw',
										   font=f', 12',
										   text=f'ВРАГИ: {len(invadersObject)}'))
	informationLine.append(cnv.create_text(320,
										   440,
										   fill='#ABCDEF',
										   anchor='nw',
										   font=f', 12',
										   text=f'ЖИЗНИ: {lives}'))
	informationLine.append(cnv.create_text(480,
										   440,
										   fill='#ABCDEF',
										   anchor='nw',
										   font=f', 12',
										   text=f'УРОВЕНЬ: {level}'))
	informationLine.append(cnv.create_text(650,
										   440,
										   fill='#ABCDEF',
										   anchor='nw',
										   font=f', 12',
										   text=f'ШТРАФЫ: -{penalty}'))
def hideMenu():
	'''
	Скрывает меню
	'''
	global menu1, menu2, onMenu

	if (onMenu):
		menu1.place(x=-100, y=-100)
		menu2.place(x=-100, y=-100)
		onMenu = False
		hideScores()  # Скрываем таблицу очков
	else:
		showMenu()
def showMenu():
	'''
	Показываем кнопки меню
	'''
	global menu1, menu2, onMenu

	if (not onMenu):
		menu1.place(x=235, y=37)
		menu2.place(x=235, y=97)
		showScores(-1)  # Показываем кнопки меню
		onMenu = True
	else:
		hideMenu()

def animationExplosion(frame, x, y):
	'''
	Анимация взрыва
	'''

	if (not playGame):
		return 0

	# Создание нового кадра начиная с позиции frame до 0 в explosionTexture[frame]
	templExpl = cnv.create_image(x, y, image=explosionTexture[frame])
	if (frame > -1):  # Если кадры не закончились в explosionTexture[]
		# Запускаем новый кадр (по адресу explosionTexture[frame - 1]) через 10 милисекунд
		root.after(10, lambda frame=frame - 1,
							  x=x,
							  y=y: animationExplosion(frame, x, y))
	cnv.update()
	sleep(0.01 + frame / 1000)  # пауза, чтобы успеть увидеть анимацию
	# Удаление предыдущей анимации
	cnv.delete(templExpl)
def animationInvadersRocket():
	'''
	Полёт и проверка попадания
	инопланетной запущенной ракеты
	'''
	global invadersRocket, \
		invadersRocketSpeed, \
		lives

	if (not playGame):
		invadersRocket = None
		invadersRocketSpeed = invadersRocketSpeedDefault
		return 0

	cnv.move(invadersRocket, invadersSpeed / 2, int(invadersRocketSpeed))  # Смещение ракеты пришельцев

	invadersRocketSpeed *= invadersRocketSpeedScale  # Ускорение ракеты

	x = cnv.coords(invadersRocket)[0]  # x = X координата ракеты пришельцев
	y = cnv.coords(invadersRocket)[1]  # y = Y координата ракеты пришельцев

	# Рассчитывание попадания в игрока
	if (y > getPlayerY() - SQUARE_SIZE // 2):  # Если Y ракеты пришельцев приблизилось к (Y - 1/2 текстуры) корабля игрока
		# Если X Ракеты пришельцев между левой и правой границей корабля игрока
		if (getPlayerX() - SQUARE_SIZE < x < getPlayerX() + SQUARE_SIZE):
			animationExplosion(7,			  # С какого кадра начинать анимацию
							   getPlayerX(),  # Где начинать анимацию
							   getPlayerY())
			Beep(400, 2)
			Beep(550, 2)
			Beep(570, 3)
			y = HEIGHT  # Установка высоты границы окна для проверки в следующем if, чтобы сработало else
			lives -= 1  # Вычитание жизни
			cnv.coords(player[0], WIDTH // 2, getPlayerY())  # Установка координат корабля игрока в центр

	if (y < HEIGHT):
		root.after(20, animationInvadersRocket)
	else:
		cnv.delete(invadersRocket)
		invadersRocket = None
		invadersRocketSpeed = invadersRocketSpeedDefault
def startInvadersRocket():
	'''
	Запуск ракеты инопланетянинами.
	Выбор, если возможно, случайного инопланетянина
	и создание на его координатах ракеты.
	Далее включается animationInvadersRocket()
	'''
	global invadersRocket

	if (not playGame or onMenu):
		return 0


	if (len(invadersObject) > 0):  # Если в окне есть хоть 1 инопланетянин
		n = randint(0, len(invadersObject) - 1)  # Выбираем случайного из них
		Beep(1200, 40)  # Создаём изображение ракеты инопланетян
		invadersRocket = cnv.create_image(getInvadersX(invadersObject[n]),  # X вылета ракеты
										  getInvadersY(invadersObject[n]),	# Y вылета ракеты
										  image=invadersRocketTexture)  # Загрузили при инициализации
		root.after(20, animationInvadersRocket)
def getInvadersX(obj):
	'''
	Возвращает координату X obj.
	Создана для сокращения записи
	'''
	return cnv.coords(obj[0])[0]
def getInvadersY(obj):
	'''
	Возвращает координату Y obj.
	Создана для сокращения записи
	'''
	return cnv.coords(obj[0])[1]

def move(x):
	'''
	Перемещение игрока
	'''
	# Если не идет игра или отображается меню
	if (not playGame or onMenu):
		return 0

	# Обработка нажатия клавиши
	if (x == LEFTKEY):
		cnv.move(player[0], -playerSpeed, 0)
	elif (x == RIGHTKEY):
		cnv.move(player[0], playerSpeed, 0)

	# Чтобы не выйти за пределы экрана
	if (getPlayerX() < SQUARE_SIZE):
		cnv.move(player[0], playerSpeed, 0)
	elif (getPlayerX() > WIDTH - SQUARE_SIZE):
		cnv.move(player[0], -playerSpeed, 0)

def mainloop():
	global invadersObject, \
		leftInvadersBorder, \
		rightInvadersBorder, \
		invadersSpeed, \
		playGame, \
		score, \
		maxY, \
		frame

	# Если все инопланетяне уничтожены
	if (len(invadersObject) == 0):
		endLevel()  # Следующий уровень

	if (not playGame):
		return 0

	# Перерисовываем текстуры
	for obj in invadersObject:
		# obj[0] - Canvas инопланетянина, obj[1] - ранг инопланетянина
		cnv.move(obj[0], int(invadersSpeed), 0)  # int() т.к скорость увеличивается на дробное число, а pxl дискретны
		# Сохранение X,Y Canvas перед его удалением, чтобы потом создать новый на этих координатах
		xPos = getInvadersX(obj)
		yPos = getInvadersY(obj)

		# Удаление Canvas для последующего создания нового кадра (анимация)
		cnv.delete(obj[0])

		obj[0] = cnv.create_image(xPos,  # Формула нижу для получения текстуры актуального кадра нужному рангу
								  yPos,  # Например (1й кадр пришельца 2го ранга) 2 * 2 + 1 = 5
								  image=invadersTexture[obj[1] * 2 + frame])
	frame += 1
	if (frame > 1):  # Предел кадра зависит от их количества (сейчас: 2)
		frame = 0

	leftInvadersBorder += int(invadersSpeed)  # Смещение левой границы "прямоугольника инопланетян"
	rightInvadersBorder += int(invadersSpeed)  # Смещение правой границы

	# Шанс и возможность запуска ракеты инопланетянами
	if (randint(0, 150) < abs(invadersSpeed) and
			invadersRocket == None):  # Если ракеты на экране нет, то invadersRocket == None
		startInvadersRocket()

	# Если "прямугольник инопланетян" дошел до границ игрового поля
	if (rightInvadersBorder > WIDTH - SQUARE_SIZE or
			leftInvadersBorder < SQUARE_SIZE):
		invadersSpeed = -invadersSpeed
		if (not onMenu):
			invadersSpeed *= 1.1
			maxY = 0  # Для работы в алгоритме нахождения нового значения maxY
			# Алгоритм нахождения максимального значения maxY и перемещения вниз изображений инопланетян
			for obj in invadersObject:  # Сдвиг на блок вниз картинок линий инопланетян
				cnv.move(obj[0], 0, SQUARE_SIZE)
				# Если сдвигаемый инопланетянин ближе к низу, чем точка maxY,
				if (cnv.coords(obj[0])[1] + SQUARE_SIZE // 2 > maxY):
					# то maxY = Y координата этого инопланетянина
					maxY = cnv.coords(obj[0])[1] + SQUARE_SIZE // 2

	score -= .1  # -1 очко за 10 вызовов (.1 = 1/10)
	updateInfoLine()

	if (maxY > getPlayerY() or lives < 0):
		endGame()

	root.after(100, mainloop)
def startGame():
	'''
	Нажатие на кнопку "Старт"
	'''
	global playGame

	if (playGame):
		hideMenu()
		return 0

	playGame = True
	hideMenu()
	mainloop()

def reset():
	'''
	Очистка Canvas от всех объектов, создание фона,
	получения фокуса для отслеживания нажатия клавиш,
	создание армады инопланетян и корабля игрока
	'''
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

	cnv.delete(ALL)
	cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)
	cnv.focus_set()  # Фокус на новом cnv для детекции биндов клавиш

	rocketObject = None  # Сброс значения ракеты игрока
	invadersRocket = None  #  Сброс значения ракеты инопланетян
	# Вычисление горизонтальной скорости инопланетян:
	invadersSpeed = 3 + level // 5  # 3 pxl за кадр + (level // 5) pxl

	# Вычисление "прямугольника инопланетян"
	invadersWidth = (1 + (level // 3)) * 2
	invadersHeight = 2 + (level // 4)
	# Проверка на разумное количество линий "прямоугольника"
	if (invadersWidth > 14):
		invadersWidth = 14
	if (invadersHeight > 8):
		invadersHeight = 8

	# Вычисление макс. координаты Y "прямоугольника инопланетян":
	# Умножение высоты текстуры на количество инопланетян с компенсацией половины высоты текстуры
	# и 10 pxl между между инопланетными "линиями"
	# Например (2 линии): maxY = 1 * 10 + 32 * 2 + 32 // 2 = 10 + 64 + 16 = 90
	maxY = (invadersHeight - 1)  * 10 + SQUARE_SIZE * invadersHeight + SQUARE_SIZE // 2

	# Создание 2D списка инопланетян и его заполнение
	invadersObject = []
	for i in range(invadersWidth):
		for j in range(invadersHeight):
			rang = randint(0, level // 8)  # Определение ранга инопланетянина
			if (rang > 2):
				rang = 2
			# Суть расчёта posX в нахождении ширины генерируемого блока пришельцев,
			# компенсация половины ширины от центральной точки X
			# с учётом расстояния между  пришельцами в 10 pxl
			posX = SQUARE_SIZE // 2 + \
				   (WIDTH // 2 - (invadersWidth * SQUARE_SIZE + 10)) // 2 + \
				   i * SQUARE_SIZE + i * 10
			# posY = 20 pxl от верха плюс равномерное распределение текстур
			# с расстоянием в 10 pxl между линиями
			posY = 20 + j * 10 + j * SQUARE_SIZE
			# invadersObject[x][0] - объект на Canvas
			# invadersObject[x][1] - ранг пришельца
			invadersObject.append([cnv.create_image(posX, posY, image=invadersTexture[rang * 2]), rang])
	# maxY = getInvadersY(invadersObject[len(invadersObject) - 1]) + SQUARE_SIZE // 2
	# Обозначение левой и правой границ "прямоугольника инопланетян"
	# invadersObject[x][y] x - номер инопланетянина. Индекс 0 - пришелец в левом верхнем углу
	leftInvadersBorder = cnv.coords(invadersObject[0][0])[0]  # [0] в конце это возвращаемая координата (x)
	rightInvadersBorder = cnv.coords(invadersObject[len(invadersObject) - 1][0])[0]

	# Создание игрока внизу окна
	player = [cnv.create_image(WIDTH // 2, HEIGHT - SQUARE_SIZE * 2, image=playerTexture), 1]  # 1 - количество ракет

	updateInfoLine()
	mainloop()
def globalReset():
	'''
	Сброс всего с установкой 1 уровня.
	Вызывается при создании игры и кнопкой "Сброс".
	# NOTE: Эксперименты с настройками - здесь
	'''
	global level, \
		score, \
		penalty, \
		playGame, \
		playerSpeed, \
		lives

	playGame = False
	playerSpeed = 5
	level = 8
	score = 0
	penalty = 0
	lives = 3

def restartGame():
	'''
	Служебный метод перезапуска игры
	1. Обнулить все значения
	2. Создать объекты и вывести на экран
	3. Отобразить рекорды игры
	'''

	globalReset()
	reset()
	showScores(-1)

def saveScores(scoresToFile):
	'''
	Запись очков в файл
	'''

	try:
		f = open('scores.dat', 'w', encoding='utf-8')
		for sc in scoresToFile:
			f.write(f'{sc[0]} {sc[1]}\n')
		f.close()
	except:
		print('Во время записи в scores.dat что- то пошло не так.')
def loadScores():
	'''
	Загрузка очков из scores.dat
	'''

	ret = []
	try:
		f = open('scores.dat', 'r', encoding='utf-8')
		for sc in f.readlines():
			s = sc.replace('\n', '')
			s = s.split(' ')
			# Если имя модифицировано в файле и его длина > 20 символов
			if (len(s[0]) > 20):
				s[0] = s[0][0:20]  # Обрезаем имя до 20 символов
			elif (s[0] == ''):
				s[0] = defaultName
			s[1] = int(s[1])
			# Если очки модифицированы в файле
			if (s[1] > 1000000):
				s[1] = 1000000
			elif (s[1] < 0):
				s[1] = 0
			ret.append(s)
		f.close()
	except:
		print('Файла score.dat не существует.')

	# TODO: Организовать проверку на подлинность (+10 к уму и +20 к алгоритмизации)
	# Если файл модифицирован и в нём больше 10 строк
	if (len(ret) != 10):
		ret = []
		for i in range(10):  # Устанавливаем дефолтные значения
			ret.append([defaultName, 0])
		saveScores(ret)

	return ret

# === СОЗДАНИЕ ОКНА ===
root = Tk()
root.resizable(False, False)
root.title("Вторжение Инопланетян")
root.iconbitmap("icon/icon.ico")

WIDTH = 800
HEIGHT = 480
SQUARE_SIZE = 32

POS_X = root.winfo_screenwidth() // 2  - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)

# === ЗАГРУЗКА ИЗОБРАЖЕНИЙ ===
backGround = PhotoImage(file='image/backGround.png')

# == ИЗОБРАЖЕНИЯ ИНОПЛАНЕТЯН ==
invadersFile = ['inv01.png', 'inv01_move.png',
				'inv02.png', 'inv02_move.png',
				'inv03.png', 'inv03_move.png']
invadersTexture = []
for fileName in invadersFile:  # Загрузка объектов-текстур инопланетян в список
	invadersTexture.append(PhotoImage(file=f'image/{fileName}'))  # для Canvas

level = None  # Уровень инопланетян
frame = 0  # Текущий кадр отображения текстур инопланетян

# === ИНИЦИАЛИЗАЦИЯ ПЕРЕМЕННЫХ ===
# чтобы знать с чем работать дальше в global области
invadersObject = None
invadersSpeed = None  # Скорость инопланетян. Вычисляется в reset()

leftInvadersBorder = None
rightInvadersBorder = None

maxY = None
invadersWidth = None
invadersHeight = None

# === ИГРОК ===
playerTexture = PhotoImage(file='image/player.png')
player = None
playerSpeed = None  # Скорость игрока
LEFTKEY = 0  # Для удобства
RIGHTKEY = 1  # бинда и обработки

# === БИНД КЛАВИШ ===
cnv.bind('<Left>', lambda e, x=LEFTKEY: move(x))
cnv.bind('<Right>', lambda e, x=RIGHTKEY: move(x))
cnv.bind('<space>', lambda e: shoot())
cnv.bind('<Escape>', lambda e: showMenu())

# === РАКЕТА ИНОПЛАНЕТЯН ===
invadersRocketTexture = PhotoImage(file='image/rocket/rocket_invaders.png')
invadersRocket = None
invadersRocketSpeedScale = 1.05  # Ускорение ракеты. Вычисляется в animationInvadersRocket()
invadersRocketSpeedDefault = 1
invadersRocketSpeed = invadersRocketSpeedDefault  # Сброс скорости до дефолтного значения

# === РАКЕТА ИГРОКА ===
rocketFiles = ['rocket01.png', 'rocket02.png', 'rocket03.png', 'rocket04.png']
rocketTexture = []
for fileName in rocketFiles:
	rocketTexture.append(PhotoImage(file=f'image/rocket/{fileName}'))

rocketObject = None
rocketSpeedYDefault = 8
rocketSpeedY = rocketSpeedYDefault
rocketScale = 1.05

# === ТЕКСТУРЫ ВЗРЫВА ===
explosionFiles = ['expl01.png', 'expl02.png', 'expl03.png', 'expl04.png',
				  'expl05.png', 'expl06.png', 'expl07.png', 'expl08.png']
explosionTexture = []
for fileName in explosionFiles:
	explosionTexture.append(PhotoImage(file=f'image/expl/{fileName}'))

# === НАСТРОЙКИ ИГРОКА ===
score = 0    # Очки
penalty = 0  # Штрафы за промахи
lives = 3    # Жизни
playGame = False
defaultName = "ПродаетсяПодРекламу"  # Имя игрока по-умолчанию

# === МЕНЮ ИГРЫ ===
menu1 = Button(root, text='Старт', font=', 20', width=20)
menu1.place(x=-100, y=-100)
menu1['command'] = startGame

menu2 = Button(root, text='Сброс', font=', 20', width=20)
menu2.place(x=-100, y=-100)
menu2['command'] = restartGame

# Переменная содержит ссылку на кнопку Button с надписью продолжить
btnContinueAfterPause = None

# === СЛУЖЕБНЫЕ ПЕРМЕННЫЕ ===
onMenu = False  # Игра на паузе?
playerName = None  # Имя игрока в отдельной сессии
scores = loadScores()  # загружаемый 2D список[x(позиция в таблице)][y], где [x][0] - имя игрока, а [x][1] - очки
textScores = None  # Список для create_image вывода из scores[x][y]

informationLine = None

# === НАЧИНАЕМ ===
globalReset()  # Сброс всех переменных на начальные
reset()  # Формирование расположения объектов в окне
playGame = True
mainloop()
# TODO: Исправить МЕГАБАГ
root.mainloop()
