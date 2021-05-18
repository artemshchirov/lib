from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

# ----- МЕТОДЫ И ФУНКЦИИ -----
def setupHorse():
    global state01, state02, state03, state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    weather = randint(1, 5)
    timeDay = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    # Маркеры ситуаций
    reverse01 = False
    reverse01 = False
    reverse01 = False
    reverse01 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fastSpeed01 = False
    fastSpeed02 = False
    fastSpeed03 = False
    fastSpeed04 = False
def winRound(horse):
    global x01, x02, x03, x04
    global money

    res = "К финишу пришел гонщик "
    if (horse == 1):
        res += gandName
        win = summ01.get() * winCoeff01
    elif (horse == 2):
        res += rickName
        win = summ02.get() * winCoeff02
    elif (horse == 3):
        res += jesuName
        win = summ03.get() * winCoeff03
    elif (horse == 4):
        res += dartName
        win = summ04.get() * winCoeff04

    if (horse > 0):
        res += f"\nВы выиграли: {int(win)}{valuta}. "
        if (win > 0):
            res += "\nПоздравляем! Средства уже у вас в кармане!"
            insertText(f"Этот забег принёс вам {int(win)}{valuta}.")
        else:
            res += "\nК сожалению, гонщик на которого вы ставили не пришел первым."
            insertText("Делайте ставку! Увеличивайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    else:
        messagebox.showinfo("Всё плохо", "До финиша не дошел никто.\nЗабег признан несостоявшимся.\nСтавки на него возвращены")
        insertText("Гонка признана несостоявшейся.")
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))

    # Сброс переменных
    setupHorse()

    # Сбрасываем виджеты перед новой игрой
    startButton["state"] = "normal"
    stavka01["state"] = "readonly"
    stavka02["state"] = "readonly"
    stavka03["state"] = "readonly"
    stavka04["state"] = "readonly"
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceInWindow()

    # Обновляем интерфейс
    refreshCombo(eventObject="B")
    viewWeather()
    healthHorse()
    insertText(f"Ваши средства: {int(money)}{valuta}")

    if (money < 1):
        messagebox.showinfo("Стоп!", "Будут еще деньги - будут еще гонки.")
        quit(0)
# Определение и установка шанса на разворот участника
def problemHorse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global state01, state02, state03, state04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

# Определение № участника, у которого будет СОБЫТИЕ
    player = randint(1, 4)
# Чем выше число, тем ниже вероятность события
# используется в условиях, в выражении с randint
    maxRand = 8000   # Чем больше значение, тем меньше шанс на проблемные события

    if (player == 1 and play01 == True and x01 > 0):
        if (randint(0, maxRand) < state01 * 5):
# Смена маркера движения
            reverse01 = not reverse01
# Сообщение об этом пользователю из окнах
            messagebox.showinfo("Аааа!", f"{rickName} начинает палить по {gandName}у из бластера!\n{gandName} убегает")
        elif (randint(0, maxRand) < state01 * 5):
        # Участнкк остановился
            play01 = False
        # Сообщение, что участник остановился
            messagebox.showinfo("Никогда такого не было и вот опять!", f"{gandName} оглушен темной силой {dartName}а")
        elif (randint(0, maxRand) < state01 * 5 and not fastSpeed01):
            # Задаем множитель ускорения
            fastSpeed01 = True
            # Сообщение, что участник ускорился
            messagebox.showinfo("На ускорении", f'{gandName} использует заклинание "Ускорение"')
    elif (player == 2 and play02 == True and x02 > 0):
        if (randint(0, maxRand) < state02 * 5):
            reverse02 = not reverse02
            messagebox.showinfo("Аааа!", f"{jesuName} превращает всё вино Рика в воду.\n{rickName} возвращается пополнить запасы")
        elif (randint(0, maxRand) < state02 * 5):
            play02 = False
            messagebox.showinfo("Никогда такого не было и вот опять!", f"{rickName} остановился перекусить семенами мегадеревьев")
        elif (randint(0, maxRand) < state02 * 5 and not fastSpeed02):
            fastSpeed02 = True
            messagebox.showinfo("Механизация", f"{rickName} включает экзоскелет и ускоряется")
    elif (player == 3 and play03 == True and x03 > 0):
        if (randint(0, maxRand) < state03 * 5):
            reverse03 = not reverse03
            messagebox.showinfo("Аааа!", f"{dartName} темной силой сводит с ума {jesuName}а.\n{jesuName} разворачивается")
        elif (randint(0, maxRand) < state03 * 5):
            play03 = False
            messagebox.showinfo("Никогда такого не было и вот опять!", f"{jesuName} остановился переговорить с Отцом")
        elif (randint(0, maxRand) < state03 * 5 and not fastSpeed03):
            fastSpeed03 = True
            messagebox.showinfo("Чудеса да и только", f"{jesuName} решает сократить путь по воде")
    elif (player == 4 and play04 == True and x04 > 0):
        if (randint(0, maxRand) < state04 * 5):
            reverse04 = not reverse04
            messagebox.showinfo("Аааа!", f'{gandName} применяет заклинание "Страх" на {dartName}а.\n{dartName} в страхе разворачивается')
        elif (randint(0, maxRand) < state04 * 5):
            play04 = False
            messagebox.showinfo("Никогда такого не было и вот опять!", f"{dartName} оглушен заклинанием {gandName}а")
        elif (randint(0, maxRand) < state04 * 5 and not fastSpeed04):
            fastSpeed04 = True
            messagebox.showinfo("Прилив темных сил", f"У {dartName}а открывается второе тяжелое дыхание")
# Принимает имя, состояние(здоровья), коэффициент победы
# и возвращает строку, которая с помощью healthHorse() выводится в чат
def getHealth(name, state, win):
    s = f"{name} "

    if (state == 5):
        s += "плохо спал. Подёргивается веко."
    elif (state == 4):
        s += "негативно вибрирует."
    elif (state == 3):
        s += "разминается перед гонкой."
    elif (state == 2):
        s += "в отличном настроении, покушал хорошо."
    elif (state == 1):
        s += "закинул кислоты на удачу!"

    s += f" ({win}:1)"
    return s
# Отображение состояния участников в чате
# Вывод строк из getHealth(name, state, win) в чат
def healthHorse():
    insertText(getHealth(gandName, state01, winCoeff01))
    insertText(getHealth(rickName, state02, winCoeff02))
    insertText(getHealth(jesuName, state03, winCoeff03))
    insertText(getHealth(dartName, state04, winCoeff04))
# Формирует строку о времени и выводит её в чат
# использует переменную timeDay = randint(1, 5)
def viewWeather():
    s = "Сейчас на трассе  "
    if (timeDay == 1):
        s += 'ночь, '
    elif (timeDay == 2):
        s += 'утро, '
    elif (timeDay == 3):
        s += 'день, '
    elif (timeDay == 4):
        s += 'вечер, '
# Формирует строку о погоде и выводит её в чат
# использует переменную weather = randint(1, 5)
    if (weather == 1):
        s += 'льёт сильный дождь.'
    elif (weather == 2):
        s += 'моросит дождик'
    elif (weather == 3):
        s += 'облачно, на горизонте тучи.'
    elif (weather == 4):
        s += 'облачно, ветер.'
    elif (weather == 5):
        s += 'безоблачно, прекрасная погода!'
    insertText(s)
# Определение скорости перемещения и направления участников
def moveHorse():
    global x01, x02, x03, x04
# X%(20) шанс на разворот лошади обратно:
    if (randint(0, 100) < 20):
        problemHorse()
# Расчитываем скорость для каждой лошади
# в формуле скорости учитываются: время, погода, состояние здоровья, рандом
    speed01 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, timeDay + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    multiple = 1.5
    speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

    print(f"Гендальф X: {int(x01 * 100) / 100}, Sp :{int(speed01 * 100) / 100}, Рик X: {int(x02 * 100) / 100}, Sp :{int(speed02 * 100) / 100}, Иисус X: {int(x03 * 100) / 100}, Sp :{int(speed03 * 100) / 100}, Дарт X: {int(x04 * 100) / 100}, Sp :{int(speed04 * 100) / 100}")

    # Вправо или влево бежит лошадь?
    if (play01):
        if (not reverse01):
            x01 += speed01
        else:
            x01 -= speed01
    if (play02):
        if (not reverse02):
            x02 += speed02
        else:
            x02 -= speed02
    if (play03):
        if (not reverse03):
            x03 += speed03
        else:
            x03 -= speed03
    if (play04):
        if (not reverse04):
            x04 += speed04
        else:
            x04 -= speed04

# Окно с сообщением, где гонщик - его значение X
    horsePlaceInWindow()

    allPlay = play01 or play02 or play03 or play04
    allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    allReverse = reverse01 and reverse02 and reverse03 and reverse04

    if (not allPlay or allX or allReverse):
        winRound(0)
        return 0

# Если ось Х гощика < 952, то вызывай moveHorse() каждые 5 милисекунд
# root - определение в каком всё окне
    if (x01 < 952 and
        x02 < 952 and
        x03 < 952 and
        x04 < 952):
        root.after(5, moveHorse)
    else:
        if (x01 >= 952):
            winRound(1)
        elif (x02 >= 952):
            winRound(2)
        elif (x03 >= 952):
            winRound(3)
        elif (x04 >= 952):
            winRound(4)
# Функция запускается при нажатии на кнопку СТАРТ
# Отвечает за перемещение картинок участников по оси X
def runHorse():
    global money
# Отключение СТАРТ и Comboboxов во время гонки
    startButton["state"] = "disabled"
    stavka01["state"] = "disabled"
    stavka02["state"] = "disabled"
    stavka03["state"] = "disabled"
    stavka04["state"] = "disabled"
# Обновление показываемой суммы в кармане игрока
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()
# Вызывается при выборе значения во всплывающих окнах Combobox.
# Задает в список Combobox 10 значений с шагом 1/10 от всей суммы игрока
def refreshCombo(eventObject):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney["text"] = f"У вас в кармане: {int(money - summ)} {valuta}"
# Динамическое обновление списков Comboboxов (10 чисел с шагом 1/10 от всей суммы игрока)
# после каждого выбора в Combobox
    stavka01["values"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02["values"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03["values"] = getValues(int(money - summ01.get() - summ02.get() - summ04.get()))
    stavka04["values"] = getValues(int(money - summ01.get() - summ02.get() - summ03.get()))
# Отключение кнопки СТАРТ, если денег == 0
    if (summ > 0):
        startButton["state"] = "normal"
    else:
        startButton["state"] = "disabled"
# В чекбоксах ставится галочка, если значения (суммы) Comboboxa больше 0
    if (summ01.get() > 0):
        gandGame.set(True)
    else:
        gandGame.set(False)
    if (summ02.get() > 0):
        rickGame.set(True)
    else:
        rickGame.set(False)
    if (summ03.get() > 0):
        jesuGame.set(True)
    else:
        jesuGame.set(False)
    if (summ04.get() > 0):
        dartGame.set(True)
    else:
        dartGame.set(False)
# Чтение из файла оставшейся суммы
def loadMoney():
  try:
    f = open('raceMoney.dat', 'r')
    m = int(f.readline())
    f.close()
  except FileNotFoundError:
    print(f'Файла не существует. Задано значение {defaultMoney}{valuta}')
    m = defaultMoney
  return m
# Запись суммы в файл
def saveMoney(moneyToSave):
  try:
    f = open('raceMoney.dat', 'w')
    f.write(str(moneyToSave))
    f.close()
  except:
    print('Ошибка создания файла. Гонка закрывается!')
    quit(0)
# Добавление строки в текстовый блок
def insertText(s):
    textDiary.insert(INSERT, s + '\n')
    textDiary.see(END)
# Расположение лошадей на экране
def horsePlaceInWindow():
    gand.place(x=int(x01), y=20)
    rick.place(x=int(x02), y=100)
    jesu.place(x=int(x03), y=175)
    dart.place(x=int(x04), y=260)
# Создание динамичного списка значений для вывода возможных сумм ставок в Combobox
# Список изменяется в зависимости от выбранных игроком ставок
# Содержит в себе  i * (int(summa) // 10 in range(10)
def getValues(summa):
    value = []
    if (summa > 9):
        for i in range(10):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if (summa > 0):
            value.append(summa)

    return value

root = Tk()    # Объявление переменной для программы.
               # Она отвечает за взаимодействие с элементами программы Tkinter

# ----- ОПРЕДЕЛЕНИЕ ЗНАЧЕНИЙ ПЕРЕМЕННЫХ -----

# Размеры окна программы
WIDTH = 1024
HEIGHT = 600

# Стартовые X -позиции участников
x01 = 20    # позиция Гендальфа
x02 = 20    # Рика
x03 = 20    # Иисуса
x04 = 20    # Гендальфа

# Имена участников гонки:
gandName = 'Гендальф'
rickName = 'Рик!'
jesuName = 'Иисус'
dartName = 'Дарт'

# Логические переменные
# Маркеры ситуаций, проверка на:
# Бежит ли участник назад?
reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False
# Перемещается ли участник?
play01 = True
play02 = True
play03 = True
play04 = True
# Высокая ли скорость?
fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False

# Для loadMoney() и saveMoney()
defaultMoney = 10000
money = 0
valuta = '$'
#Погода. 1 - ливень, ураган 5 - безоблачное небо
weather = randint(1, 5)
# Время суток. 1 - ночь, 2 - утро, 3 - день, 4 - вечер
timeDay = randint(1, 5)

# ----- ФОРМИРОВАНИЕ ЭЛЕМЕНТОВ В ОКНЕ -----

# Состояние лощадей
# 1 - великолепно!
# 5 - ужасно больна
state01 = randint(1,5)
state02 = randint(1,5)
state03 = randint(1,5)
state04 = randint(1,5)

# Определение коэффициентов ставок каждой лошади.
# Зависит от её здоровья в этот раунд и показывает шансы на победу
winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

# Создаем главное окно
# Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH //2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Настраиваем заголовок окна
root.title('Космическая гонка')

# Запрещаем пользователю менять размер окна
root.resizable(False, False)

# Устанавливаем ширину, высоту и позицию
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# Фон: дорожки и финиш
road_image = PhotoImage(file='road.png')    # Загружаем изображение фона
road = Label(root, image=road_image)        # Устанавливаем изображение в Label
road.place(x=0, y=17)                       # Выводим изображение в окно

# Определение переменных с картинками участников:
# 1. Гендальф (horse01)
gand_image = PhotoImage(file='gandalf.png')
gand = Label(root, image=gand_image)

# 2. Рик (horse02)
rick_image = PhotoImage(file='rick.png')
rick = Label(root, image=rick_image)

# 3. Иисус (horse03)
jesu_image = PhotoImage(file='jesus.png')
jesu = Label(root, image=jesu_image)

# 4. Дарт (horse04)
dart_image = PhotoImage(file='dart.png')
dart = Label(root, image=dart_image)

horsePlaceInWindow()    # Функция вывода участников в окно

# Кнопка "СТАРТ"
startButton = Button(text='СТАРТ', font='arial 20', width=61, background='#37AA37')
startButton.place(x=20, y=370)
startButton["state"] = "disabled"

# Чат с информацией:
# 1.a Настройка размера и переноса строк (по слову). Text - это виджет
textDiary = Text(width=62, height=8, wrap=WORD)
# 1.b Позиционирование чата в окне
textDiary.place(x=430, y=440)

# 2. Создание виджета скролл-полосы
scroll = Scrollbar(command=textDiary.yview, width=20)    # 'textDiary.yview' - привязка к Y-оси textDiary
# 2.b Позиционирование скролла в окне, в чате
scroll.place(x=990, y=440, height=142)
# 2.c Связь скролла с текстовым полем
textDiary['yscrollcommand'] = scroll.set

money = loadMoney()    # Загрузка счета из файла raceMoney.dat

if (money <= 0):
    messagebox.showinfo('Стоп!', 'Нет алмазов - нет гонок!')
    quit(0)

# Виджет отображения оставшихся денег:
labelAllMoney = Label(text=f'В твоём кармане: {money} {valuta}.', font='Arial 12')
labelAllMoney.place(x=20, y=565)

# Текст слева от чекбоксов:
# 1 строка Гендальф
labelGand = Label(text='Ставка на гонщика №1')
labelGand.place(x=20, y=440)
# 2 строка Рик
labelRick = Label(text='Ставка на гонщика №2')
labelRick.place(x=20, y=470)
# 3 строка Иисус
labelJesu = Label(text='Ставка на гонщика №3')
labelJesu.place(x=20, y=500)
# 4 строка Дарт
labelDart = Label(text='Ставка на гонщика №4')
labelDart.place(x=20, y=530)

# Определение логических переменных со значениями только 0/1 (BooleanVar())
gandGame = BooleanVar()
# Установка начального значения логической переменной (0)
gandGame.set(0)
# Привязка логической переменной к галочке чекбокса.
# переменная будет 1 когда галочка есть, 0 - если галочки нет
gandCheck = Checkbutton(text=gandName, variable=gandGame, onvalue=1, offvalue=0)
# Позиция в графическом окне 1 чекбокса Гендальфа
gandCheck.place(x=162, y=437)

rickGame = BooleanVar()
rickGame.set(0)
rickCheck = Checkbutton(text=rickName, variable=rickGame, onvalue=1, offvalue=0)
# Позиция в графическом окне 2 чекбокса Рика
rickCheck.place(x=162, y=467)

jesuGame = BooleanVar()
jesuGame.set(0)
jesuCheck = Checkbutton(text=jesuName, variable=jesuGame, onvalue=1, offvalue=0)
# Позиция в графическом окне 3 чекбокса Иисуса
jesuCheck.place(x=162, y=497)

dartGame = BooleanVar()
dartGame.set(0)
dartCheck = Checkbutton(text=dartName, variable=dartGame, onvalue=1, offvalue=0)
# Позиция в графическом окне 4 чекбокса Дарта
dartCheck.place(x=162, y=527)

# Запрет пользователю на ставить галочки в чекбоксах
gandCheck["state"] = "disable"
rickCheck["state"] = "disable"
jesuCheck["state"] = "disable"
dartCheck["state"] = "disable"

# Создание переменной для отображения и настройки всплывающего окна выбора
# № stavka так же определяет № строки всплывающего окна
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

# Запрет пользователю вводить данные во всплывающие окна
# № stavka так же определяет № строки всплывающего окна
stavka01['state'] = 'readonly'
stavka01.place(x=255, y=440)
stavka02['state'] = 'readonly'
stavka02.place(x=255, y=470)
stavka03['state'] = 'readonly'
stavka03.place(x=255, y=500)
stavka04['state'] = 'readonly'
stavka04.place(x=255, y=530)

# Задаем переменным тип число - int
summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

# Привязываем переменную к Combobox
stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

# При выборе значения во всплывающих окнах Combobox,
# произойдет метод refreshCombo
stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

# Обновляем значения Combobox
refreshCombo("")

# Значения Combobox по умолчанию.
# Цифра - позиция в списке Combobox
stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

# При нажатии на кнопку СТАРТ выполняется метод def runHorse():
startButton["command"] = runHorse

viewWeather()
healthHorse()
##############################################
root.mainloop()
##############################################
