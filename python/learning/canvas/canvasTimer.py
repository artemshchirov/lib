from tkinter import *

def plusSecond():
    global second, timerLink
    second += 1
    label['text'] = f'Прошло секунд: {second}'

    # Вызов через 1 секунду = 1000 милисекунд
    timerLink = root.after(1000, plusSecond)

def startTimer():
    global timerLink
    timerLink = root.after(1000, plusSecond)

def stopTimer():
    global timerLink
    if (timerLink != None):
        # after_cancel() прекращает работу
        root.after_cancel(timerLink)
        timerLink = None

root = Tk()
root.geometry(f'{130}x{100}')

label = Label(root)
label.place(x=10, y=10)

startBtn = Button(root, text='Старт')
startBtn.place(x=10, y=50)
startBtn['command'] = startTimer

stopBtn = Button(root, text='Пауза')
stopBtn.place(x=70, y=50)
stopBtn['command'] = stopTimer

second = 0

timerLink = None

plusSecond()
root.mainloop()
