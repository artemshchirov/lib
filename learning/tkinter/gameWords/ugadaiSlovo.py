# ЗАМЕТКИ 
# Добавить английский язык и переключение между языками
# Добавить уровень сложности "Провидец" - 0 открытых букв

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

def cheat(event):
    wordLabel['text'] = wordComp

def pressKey(event):
    '''
    Тех. параметры можно отслеживать с помощью event.
    event.keycode возвращает код нажатой КЛАВИШИ
    event.char возвращает СИМВОЛ, расположенный на клавише
    '''
    print(f'Код клавиши: {event.keycode}, Символ: {event.char.upper()}')

    # Открытие загадонного слова по нажатию CTRL
    # (пример обработки event)
    # if (event.keycode == 17):
        # wordLabel['text'] = wordComp

    # Получаем символ с клавиши
    ch = event.char.upper()
    if (len(ch) == 0):
        return 0

    # Определяем порядковый номер нажатого символа в русском алфавите
    codeBtn = ord(ch) - st
    if (0 <= codeBtn <= 32 or codeBtn == -15):
        pressLetter(codeBtn)

def updateInfo():
    '''
    Обновление информации об очках
    '''
    scoreLabel['text'] = f'Ваши очки: {score}'
    topScoreLabel['text'] = f'Лучший результат: {topScore}'
    userTryLabel['text'] = f'Осталось попыток: {userTry}'

def saveTopScore():
    '''
    Сохраняет в файл очки пользователя
    '''
    global topScore

    # Изменение
    topScore = score

    # Запись в файл для последующего использования
    try:
        f = open('topchik.dat', 'w', encoding='utf-8')
        f.write(str(topScore))
        f.close()
    except:
        messagebox.showinfo('Ошибка', 'Возникла проблема с файлом\nСохранение рекорда невозможно')

def getTopScore():
    '''
    Загрузка рекорда из файла
    '''
    try:
        f = open('topchik.dat', 'r', encoding='utf-8')
        m = int(f.readline())
        f.close()
    except:
        m = 0

    return m

def getWordsFromFile():
    '''
    Загружает слова в список
    '''
    # Переменная-список для хранения слов из файла
    ret = []

    # Блок проверки ошибок (вдруг файла нет):
    try:
        f = open('words_ru.dat', 'r', encoding='utf-8')
        # Чтение построчно
        for l in f.readlines():
            # Убираем символ переноса строки из файла
            l = l.replace('\n', '')
            # Добавление слова в список
            ret.append(l)
        f.close()
    except:
        print('Проблема с файлом. Программа прекращает работу')
        quit(0)

    # Возвращаем список
    return ret

def getLevel(eventObject):
    '''
    Возвращает выбранный игроком уровень сложности
    '''
    global level, bonusScore

    if bonus.get() == 'Ветеран':
        level = 3
        bonusScore = 0.15
        printScore = '15%'
    elif bonus.get() == 'Бог':
        level = 4
        bonusScore = 0.25
        printScore = '25%'
    else:
        level = 2
        bonusScore = 0.5
        printScore = '5%'

    # Модификатор бонуса сложности для отображения в метке
    levelLabel['text'] = f'Бонус: +{printScore}'

    # Стартуем новый раунд!
    startNewRound()

def startNewRound():
    '''
    Начало нового раунда
    '''
    global wordStar, wordComp, userTry, dictionary

    if (len(dictionary) > 0):
        # Загадываем слово
        wordComp = dictionary[randint(0, len(dictionary) - 1)]
        # Удаление загаданного слова из списка в этой игре (чтобы не было повторов)
        dictionary.remove(wordComp)
    else:
        # Иначе подгружаем словарь еще раз
        messagebox.showinfo('Вот это да!', 'В словаре закончились слова.\nЗагружаю словарь заново...')
        dictionary = getWordsFromFile()

    # Формируем строку из '*'
    wordStar = '*' * len(wordComp)

    for i in range(0, len(wordComp), level):
        wordStar = getWordStar(wordComp[i])

    # Сбрасываем кнопки и отключаем кнопки уже открытых букв
    for i in range(33):
        letter = st + i

        if (i == 6):
            letter = 1025
        elif (i > 6):
            letter -= 1

        if chr(letter) in wordStar:
            btn[i]['text'] = '.'
            btn[i]['state'] = 'disabled'
        else:
            btn[i]['text'] = chr(letter)
            btn[i]['state'] = 'normal'

    # Устанавливаем текст в метку
    wordLabel['text'] = wordStar
    # Устанавливаем метку по центру для вывода слова
    # winfo_reqwidth()  - функция возвращающая размер объекта в пикселях
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)


    # сбрасываем попытки
    userTry = 10
    # Обновление информации в окне
    updateInfo()

def compareWord(s1, s2):
    '''
    Возвращение количества несовпадений до нажатия буквы и после
    '''

    # Возвращаемый результат, количество разных символов
    res = 0

    # Сравнение каждого символа по очереди
    for i in range(len(wordStar)):
        # Если символы разные
        if (s1[i] != s2[i]):
            # То увеличиваем результат
            res += 1

    # print(f'Совпадений найдено: {res}')
    return res

def getWordStar(ch):
    '''
    Возвращение слова с открытыми символами вместо звездочек
    '''
    # Переменная для результата
    ret = ''
    # print('ch ', ch )
    for i in range(len(wordComp)):
        if (wordComp[i] == ch):
            ret += ch
        else:
            ret += wordStar[i]
    return ret

def pressLetter(n):
    '''
    Действия при нажатии мышкой на кнопку с буквой
    '''
    global wordStar, score, userTry

    # print(f'Вы нажали на букву {chr(st + n)} (n: {n})')

    # Сохраняем слово до ввода буквы, чтобы сравнить потом с новым
    # и узнать есть ли результат (новые открытые буквы)
    oldWordStar = wordStar
    wordStar = getWordStar(chr(st + n))
    # Получаем количество совпадений - отгаданных пользователем букв
    count = compareWord(wordStar, oldWordStar)

    if (n == -15):      # Если код буквы Ё
        n = 6
    elif (n >= 6):      # Если код после буквы Ё в списке кнопок
        n += 1

    # Проверяем, если эта буква уже была была выбрана, то прерываем метод
    if (btn[n]['text'] == '.'):
        return 0

    btn[n]['text'] = '.'
    btn[n]['state'] = 'disabled'

    wordLabel['text'] = wordStar

    # Считаем очки
    if (count > 0):
        score += count * 5
    else:
        score -= 10
        # Проверка, чтобы очки не свалились в отрицательные значения
        if (score < 0):
            score = 0
        # Уменьшение количества оставшихся попыток
        userTry -= 1

    updateInfo()

    # Сравниваем загаданное слово с содержимым wordStar
    if (wordComp == wordStar):
        # Добавляем 20% от имеющихся очков + модификатор уровня сложности
        score += (score // 5) + (score * bonusScore)
        score = int(score)
        # Обновление меток с очками на экране
        updateInfo()

        # Если заработано больше, чем рекорд, то сообщаем и записываем
        if (score > topScore):
            messagebox.showinfo('Поздравляем!', f'Вы - топчик!\nУгадано слово: {wordComp}\nНажмите ОК для продолжения игры')
            # Метод, который записывает рекорд в файл
            saveTopScore()
        else:
            messagebox.showinfo('Отлично', f'Слово угадано: {wordComp}\nПродолжаем играть!')
        startNewRound()
    elif (userTry <= 0):
        messagebox.showinfo('Бу!', 'Отведенное количество попыток закончено...\nВозвращайтесь скорей!')
        quit(0)

# Создание окна
root = Tk()
root.resizable(False, False)
root.title('Угадай слово и радуйся')

# Настройка геометрии окна
WIDTH = 810     # Ширина
HEIGHT = 320    # Высота
SCR_WIDTH = root.winfo_screenwidth()    # Программное получение ширины экрана пользователя
SCR_HEIGHT = root.winfo_screenheight()  # Программное получение высоты экрана пользователя
POS_X = SCR_WIDTH // 2 - WIDTH // 2     # Координата по оси X
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2   # Координата по оси Y
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# Метка для вывода слова, которое человек угадывает в текущем раунде
wordLabel = Label(font='Consolas 35')

# Метки для отображения текущих очков и рекорда
scoreLabel = Label(font=', 12')
topScoreLabel = Label(font=', 12')

# Метка оставшихся попыток
userTryLabel = Label(font=', 12')

# Устанавливаем метки в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

# Метка выбора сложности Combobox
levelLabel = Label(font=', 10')
levelLabel.place(x=660, y=170)

# Переменные для хранения значений
score = 0                    # Текущие очки
topScore = getTopScore()     # Рекорд игры
userTry = 10                 # Количество оставшихся попыток

st = ord('А')       # Для определения символа на кнопке по коду
btn = []            # Список кнопок

# Работаем с кнопками
for i in range(33):
    if (i < 6):
        btn.append(Button(text=chr(st + i), width=2, font='Consolas 15'))
        btn[i]['command'] = lambda x=i: pressLetter(x)
    elif (i == 6):
        btn.append(Button(text=chr(1025), width=2, font='Consolas 15'))
        btn[i]['command'] = lambda x=-15: pressLetter(x)
    else:
        btn.append(Button(text=chr(st + i-1), width=2, font='Consolas 15'))
        btn[i]['command'] = lambda x=i-1: pressLetter(x)

    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)

# Определяем глобально: 'загаданное слово'
wordComp = ''
# Определяем глобально: 'слово со звездочкой'
wordStar= ''

# Словарь
dictionary = getWordsFromFile()

# Combobox выбора уровня сложности
getLevelBox = ttk.Combobox(root)
getLevelBox['state'] = 'readonly'
getLevelBox.place(x=625, y=195)
bonus = StringVar()
levels = ['Легко', 'Ветеран', 'Бог']
getLevelBox["values"] = levels
getLevelBox['textvariable'] = bonus
getLevelBox.bind("<<ComboboxSelected>>", getLevel)
getLevel("")
getLevelBox.current(0)

# Стартуем новый раунд! (Вызывается из getLevel())
# startNewRound()

# Устанавливаем обработчик клавиш
root.bind('<Key>', pressKey)
# 'CTRL + /' вызывает cheat(). Для изменения горячих клавиш надо дописать
# клавишу X к '<Control-X>' и следом вызываемую функцию
# список возможных клавиш: https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm
# https://stackoverflow.com/questions/16082243/how-to-bind-ctrl-in-python-tkinter
# для рус раскладки
root.bind("<Control-.>", cheat)
# для англ раскладки
root.bind("<Control-slash>", cheat)

root.mainloop()
